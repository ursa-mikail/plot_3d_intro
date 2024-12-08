import numpy as np
import plotly.graph_objects as go

# Define the heart equation function
def heart_equation(x, y, z):
    return (x**2 + (9/4)*y**2 + z**2 - 1)**3 - x**2*z**3 - (9/200)*y**2*z**3

# Create a grid of points
x = np.linspace(-1.5, 1.5, 100)
y = np.linspace(-1.5, 1.5, 100)
z = np.linspace(-1.5, 1.5, 100)
x, y, z = np.meshgrid(x, y, z)

# Compute the values of the heart equation
values = heart_equation(x, y, z)

# Create a mask for the surface plot (values close to zero)
surface_mask = np.abs(values) < 0.05

# Extract the coordinates where the mask is True
x_surface = x[surface_mask]
y_surface = y[surface_mask]
z_surface = z[surface_mask]

# Create the scatter plot
fig = go.Figure(data=[go.Scatter3d(
    x=x_surface,
    y=y_surface,
    z=z_surface,
    mode='markers',
    marker=dict(
        size=2,
        color='red',
        opacity=0.8
    )
)])

# Update layout for better visuals
fig.update_layout(
    title='3D Heart Shape',
    scene=dict(
        xaxis_title='X axis',
        yaxis_title='Y axis',
        zaxis_title='Z axis'
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# Show the plot
fig.show()

