import matplotlib.pyplot as plt

from pkg.models.first_order.terminal_velocity import TerminalVelocity
from pkg.utils.plot_utils import plot_solution

def terminal_velocity_dynamics(m=1, g=9.81, k=0.1, tn=10, dt=0.1):
    model = TerminalVelocity()

    dxdt = lambda vt: model.rhs(vt, m, g, k)
    title = f"Terminal Velocity Dynamics (m={m} kg, g={g} m/s^2, k={k})"

    # Plot with multiple initial conditions
    x0 = [0.0, 10.0, 20.0, 30.0, 40.0]
    ax = plot_solution(dxdt, x0=x0, tn=tn, dt=dt, n_slope=20, slope_length=0.2, show=True, title=title)
    
    plt.show()

if __name__ == "__main__":
    terminal_velocity_dynamics()