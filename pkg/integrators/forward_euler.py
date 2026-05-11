import numpy as np
def forward_euler(x0, dxdt,tn, dt=0.1):
    t = 0
    xi = x0
    data = [[t,xi]]
    n_steps = tn/dt
    for step in range(int(n_steps)):
        k1 = xi + dxdt(xi)*dt

        xi = k1
        t= t+dt

        data.append([t,xi])

    return np.array(data)