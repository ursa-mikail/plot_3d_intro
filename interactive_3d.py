
import numpy as np
import plotly.graph_objects as go

# Define the parameters
a, b = 2, 2

# Create a meshgrid for x and y
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Compute the function z = (x^2 / a^2) + (y^2 / b^2)
z = (x**2 / a**2) + (y**2 / b**2)

# Create the surface plot
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y, colorscale='Viridis')])

# Update layout for better visuals
fig.update_layout(
    title='Interactive 3D Surface Plot',
    scene=dict(
        xaxis_title='X axis',
        yaxis_title='Y axis',
        zaxis_title='Z axis'
    ),
    margin=dict(l=0, r=0, b=0, t=40)
)

# Show the plot
fig.show()

