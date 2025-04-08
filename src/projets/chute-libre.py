
import matplotlib.pyplot as plt



def rk4_solver(f, y0, t0, t_max, dt):
    """Solve an ODE using Runge-Kutta 4th order."""
    t, y = t0, y0
    while t <= t_max:
        yield t, y
        k1 = dt * f(t, y)
        k2 = dt * f(t + dt / 2, y + k1 / 2)
        k3 = dt * f(t + dt / 2, y + k2 / 2)
        k4 = dt * f(t + dt, y + k3)
        y += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += dt

def free_fall_friction(t, v):
    g, c, m = 9.81, 0.25, 47
    return g - (c / m) * v**2

trajectory = rk4_solver(free_fall_friction, y0=0, t0=0, t_max=10, dt=0.1)
times, velocities = zip(*trajectory)

plt.plot(times, velocities, label="Vitesse (RK4)", color="r")
plt.xlabel("Temps (s)")
plt.ylabel("Vitesse (m/s)")
plt.title("Chute libre avec frottement (Méthode RK4)")
plt.legend()
plt.grid()
plt.show()
