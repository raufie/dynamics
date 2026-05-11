import matplotlib.pyplot as plt

from pkg.models.first_order.capactor import CapacitorModel
from pkg.utils.plot_utils import plot_solution


def capacitor_dynamics(C=1, V0=5, R=1, model_type="charge", k=1, tn=10, dt=0.1):
    linear_resistor_model = CapacitorModel(C=C, V0=V0, R=R, k=k)

    if model_type == "charge":
        dxdt = linear_resistor_model.charge_model_rhs
        title="Capacitor Charging Dynamics"
    elif model_type == "discharge":
        dxdt = linear_resistor_model.discharge_model_rhs
        title="Capacitor Discharging Dynamics"
    else:
        raise ValueError("model_type must be 'charge' or 'discharge'")

    if k== 1:
        title += " (Linear)"
    else:
        title += f" (Nonlinear, k={k})"
    # Plot with multiple initial conditions
    x0 = [0.0, 2.5, 5.0, 7.5, 10.0]
    ax = plot_solution(dxdt, x0=x0, tn=tn, dt=dt, n_slope=20, slope_length=0.2, show=True, title=title)
    
    plt.show()
if __name__ == "__main__":
    # charge-linear
    capacitor_dynamics(model_type="charge", k=1)
    # # discharge-linear
    capacitor_dynamics(model_type="discharge", k=1)
    # charge-nonlinear
    capacitor_dynamics(model_type="charge", k=5, R=15.5)
    # discharge-nonlinear
    capacitor_dynamics(model_type="discharge", k=3)

