import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters for scaling
a = 1
b = 1

# Create a grid of x and y values
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Compute z based on the given equation
# z = (x / a) ** 2 + (y / b) ** 2
z = (x / a) ** 2 - (y / b) ** 2


# Create the plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(x, y, z, cmap='viridis')

# Labels and title
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
# ax.set_title(r'$z = \left(\frac{x}{a}\right)^2 + \left(\frac{y}{b}\right)^2$')
ax.set_title(r'$z = \left(\frac{x}{a}\right)^2 - \left(\frac{y}{b}\right)^2$' + ': 3D Saddle (Hyperbolic Paraboloid)')

# Show the plot
plt.show()

R = 3  # Major radius
r = 1  # Minor radius

u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z, cmap='cividis')

ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
ax.set_title('3D Donut (Torus)')

plt.show()

