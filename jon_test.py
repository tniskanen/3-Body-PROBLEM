import math

mass_1 = 3
planet_1_x = 1
planet_1_y = 2

mass_2 = 3
planet_2_x = 2
planet_2_y = 4

G = 6.67 * 10**-11


x_abs = abs(planet_1_x - planet_2_x)
y_abs = abs(planet_1_y - planet_2_y)
r_squared = x_abs**2 + y_abs**2
force_1 = (G * mass_1 * mass_2) / r_squared

