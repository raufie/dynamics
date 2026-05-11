import numpy as np
import matplotlib.pyplot as plt
from pkg.integrators.forward_euler import forward_euler


def plot_slope_field(dxdt, t_span=(0.0, 1.0), x_span=(0.0, 1.0), n=25, length=0.2, ax=None, color="grey", linewidth=1.0):
    """Plot a slope field for dx/dt = f(x) in the (t, x) plane.

    Parameters
    ----------
    dxdt : callable
        Derivative function f(x) returning dx/dt.
    t_span : tuple[float, float]
        Time interval for the slope field.
    x_span : tuple[float, float]
        State interval for the slope field.
    n : int
        Number of grid points in each dimension.
    length : float
        Approximate length of each line segment.
    ax : matplotlib.axes.Axes | None
        Axes to draw on. A new one is created if None.
    color : str
        Color of the slope field segments.
    linewidth : float
        Width of the slope field segments.
    """
    if ax is None:
        _, ax = plt.subplots()

    t_values = np.linspace(t_span[0], t_span[1], n)
    x_values = np.linspace(x_span[0], x_span[1], n)
    T, X = np.meshgrid(t_values, x_values)
    slopes = np.vectorize(dxdt)(X)

    scaled_dt = length / np.sqrt(1.0 + slopes**2)
    T_end = T + scaled_dt
    X_end = X + slopes * scaled_dt

    for i in range(T.shape[0]):
        for j in range(T.shape[1]):
            ax.plot([T[i, j], T_end[i, j]], [X[i, j], X_end[i, j]], color=color, linewidth=linewidth)

    ax.set_xlim(t_span)
    ax.set_ylim(x_span)
    ax.set_xlabel("t")
    ax.set_ylabel("x")
    ax.set_title("Slope Field")
    ax.grid(True, linestyle="--", alpha=0.4)
    return ax


def _compute_state_space(x0, dxdt, tn, dt, margin=0.05):
    x0_list = np.atleast_1d(x0)
    trajectories = [forward_euler(float(x_init), dxdt, tn, dt) for x_init in x0_list]
    
    # Filter out trajectories with NaN or Inf
    valid_traj = [traj for traj in trajectories if np.all(np.isfinite(traj))]
    if not valid_traj:
        raise ValueError("No valid (finite) trajectories found. Check your ODE or initial conditions.")
    
    all_x = np.concatenate([traj[:, 1] for traj in valid_traj])
    all_x = all_x[np.isfinite(all_x)]
    if all_x.size == 0:
        raise ValueError("No finite state values found in trajectories.")
    x_min, x_max = float(all_x.min()), float(all_x.max())
    delta = max(0.1, (x_max - x_min) * margin)
    return (0.0, tn), (x_min - delta, x_max + delta), valid_traj


def plot_solution(dxdt, x0, tn, dt=0.1, t_span=None, x_span=None, n_slope=25, slope_length=0.2, ax=None, show=True, interactive=False, title="Solution Curves with Slope Field"):
    """Plot solution curves together with a full state-space slope field.

    If t_span or x_span are not provided, the function estimates the domain from the trajectories.
    """
    if t_span is None or x_span is None:
        t_span, x_span, trajectories = _compute_state_space(x0, dxdt, tn, dt)
    else:
        x0_list = np.atleast_1d(x0)
        trajectories = [forward_euler(float(x_init), dxdt, tn, dt) for x_init in x0_list]

    if ax is None:
        fig, ax = plt.subplots()
    else:
        fig = ax.figure

    plot_slope_field(dxdt, t_span=t_span, x_span=x_span, n=n_slope, length=slope_length, ax=ax)

    for x_init, trajectory in zip(np.atleast_1d(x0), trajectories):
        ax.plot(trajectory[:, 0], trajectory[:, 1], linewidth=2.0, label=f"x₀={x_init}")

    ax.set_title(title)
    ax.legend(loc="best")

    if interactive:
        plt.ion()
        if fig.canvas.manager is not None:
            fig.canvas.manager.set_window_title("ODE Solution")
        if show:
            plt.show()
    elif show:
        import warnings
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=UserWarning)
            plt.show()

    return ax
