import numpy as np


def rk4_step(f, t, X, U, D, dt):

    k1 = f(t, X, U, D)
    k2 = f(t + dt/2, X + dt/2 * k1, U, D)
    k3 = f(t + dt/2, X + dt/2 * k2, U, D)
    k4 = f(t + dt, X + dt * k3, U, D)

    X_next = X + (dt/6) * (k1 + 2*k2 + 2*k3 + k4)

    # -------- PHYSICAL CONSTRAINTS --------
    X_next[0] = np.clip(X_next[0], 0.0, 1.0)       # SOC bounded
    X_next[7] = np.clip(X_next[7], 0.0, 1.0)       # Battery health bounded

    return X_next