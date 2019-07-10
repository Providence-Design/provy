#!usr/bin/python
import math
PI =22/7
radius = float(input('enter radius of the sphere: '))
sa = 4 * PI * (radius *radius)
volume = (4/3) * PI * (radius * radius )* radius
print("\n the surface area of the sphere =%.2f" %sa)
print("\n volume of the sphere = %.2f" %volume)
