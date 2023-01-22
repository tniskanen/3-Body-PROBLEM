import math

mass_1 = 50
planet_1_x = -200
planet_1_y = -150

mass_2 = 75
planet_2_x = 200
planet_2_y = -150

mass_3 = 100
planet_3_x = 0
planet_3_y = 196.4101615



t = 1/60
G = 6.67 * 10**-11

x_abs = abs(planet_1_x - planet_2_x)
y_abs = abs(planet_1_y - planet_2_y)
r_squared = x_abs**2 + y_abs**2
force_1 = (G * mass_1 * mass_2) / r_squared

x = planet_1_x - planet_2_x
y = planet_1_y - planet_2_y

if x < 0:
    if y > 0:
        angle_1 = math.degrees(math.atan(y/x))
        angle_1 = 180 - angle_1
        f1_x = force_1 * math.cos(angle_1)
        f1_y = force_1 * math.sin(angle_1)
    if y < 0:
        angle_1 = math.degrees(math.atan(y/x))
        angle_1 = 270 - angle_1
        f1_x = force_1 * math.cos(angle_1)
        f1_y = force_1 * math.sin(angle_1)        
if x > 0:
    if y < 0:
        angle_1 = math.degrees(math.atan(y/x))
        angle_1 = 360 - angle_1
        f1_x = force_1 * math.cos(angle_1)
        f1_y = force_1 * math.sin(angle_1)
    if y > 0:
        angle_1 = math.degrees(math.atan(y/x))
        f1_x = force_1 * math.cos(angle_1)
        f1_y = force_1 * math.sin(angle_1)
if x == 0:
    if y > 0:
        angle_1 = 90
        f1_x = 0
        f1_y = force_1
    if y < 0:
        angle_1 = 270 
        f1_x = 0
        f1_y = force_1 * -1
if y == 0:
    if x > 0:
        angle_1 = 0
        f1_x = force_1
        f1_y = 0
    if x < 0:
        angle_1 = 180
        f1_x = force_1 * -1
        f1_y = 0                     

x_abs = abs(planet_3_x - planet_2_x)
y_abs = abs(planet_3_y - planet_2_y)
r_squared = x_abs**2 + y_abs**2
force_2 = (G * mass_3 * mass_2) / r_squared

x = planet_3_x - planet_2_x
y = planet_3_y - planet_2_y

if x < 0:
    if y > 0:
        angle_2 = math.degrees(math.atan(y/x))
        angle_2 = 180 - angle_2
        f2_x = force_2 * math.cos(angle_2)
        f2_y = force_2 * math.sin(angle_2)
    if y < 0:
        angle_2 = math.degrees(math.atan(y/x))
        angle_2 = 270 - angle_2
        f2_x = force_2 * math.cos(angle_2)
        f2_y = force_2 * math.sin(angle_2)       
if x > 0:
    if y < 0:
        angle_2 = math.degrees(math.atan(y/x))
        angle_2 = 360 - angle_2
        f2_x = force_2 * math.cos(angle_2)
        f2_y = force_2 * math.sin(angle_2)
    if y > 0:
        angle_2 = math.degrees(math.atan(y/x))
        f2_x = force_2 * math.cos(angle_2)
        f2_y = force_2 * math.sin(angle_2)
if x == 0:
    if y > 0:
        angle_2 = 90
        f2_x = 0
        f2_y = force_2
    if y < 0:
        angle_2 = 270
        f2_x = 0
        f2_y = force_2 * -1
if y == 0:
    if x > 0:
        angle_2 = 0
        f2_x = force_2
        f2_y = 0
    if x < 0:
        angle_2 = 0
        f2_x = force_2 * -1
        f2_y = 0

f_x = f1_x + f2_x
f_y = f1_y + f2_y
fr = math.sqrt(f_x**2 + f_y**2)
theta = math.degrees(math.atan(f_y/f_x))
if f_x < 0:
    if f_y > 0:
        theta = 180 - theta
    if f_y < 0:
        theta = 270 - theta
if f_y < 0:
    if f_x > 0:
        theta = 360 - theta 

displacement = (fr/mass_2) * t * t

delta_x = displacement * math.sin(theta) 
delta_y = displacement * math.cos(theta)


    

if __name__ == '__main__':
    print(delta_x)
    print(delta_y)