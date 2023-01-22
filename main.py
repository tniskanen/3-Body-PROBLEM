import arcade
import math

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1600
SCREEN_TITLE = "3 Body Model"
PIXEL_CONSTANT = 100000

mass_1 = 5.972 * 10**33
planet_1x = 700 * 100000
planet_1y = 700 * 100000
fy1 = 1000000000000000000000000000000
fx1 = 1000000000000000000000000000000

mass_2 = 5.972 * 10**33
planet_2x = 840 * 100000
planet_2y = 800 * 100000
fy2 = 1000000000000000000000000000000
fx2 = 1000000000000000000000000000000

mass_3 = 5.972 * 10**33
planet_3x = 900 * 100000
planet_3y = 900 * 100000 
fy3 = 1000000000000000000000000000000
fx3 = 1000000000000000000000000000000

class planet:
    # represents each planet in the system
    def __init__(self, mass, x, y, fx, fy):
        self.mass = mass
        self.x = x #m
        self.y = y
        self.fx = fx
        self.fy = fy
        #mass vs size ratio
        self.radius = 7


    def update_pos(self, mass1, x1, y1, mass2, x2, y2):
        mass_1 = mass1
        planet_1_x = x1
        planet_1_y = y1

        mass_2 = self.mass
        planet_2_x = self.x
        planet_2_y = self.y

        mass_3 = mass2
        planet_3_x = x2
        planet_3_y = y2
        
        t = 1/6000
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

        f_x = f1_x + f2_x + self.fx
        f_y = f1_y + f2_y + self.fy
        self.fx = f_x
        self.fy = f_y
        fr = math.sqrt(f_x**2 + f_y**2)
        displacement = (fr/mass_2) * t * t

        if f_x < 0:
            if f_y > 0:
                theta = math.degrees(math.atan(f_y/f_x))
                theta = 180 - theta
                delta_x = displacement * math.sin(theta) 
                delta_y = displacement * math.cos(theta)        
            if f_y < 0:
                theta = math.degrees(math.atan(f_y/f_x))
                theta = 270 - theta
                delta_x = displacement * math.sin(theta) 
                delta_y = displacement * math.cos(theta)
        if f_x > 0:
            if f_y < 0:
                theta = math.degrees(math.atan(f_y/f_x))
                theta = 360 - theta
                delta_x = displacement * math.sin(theta) 
                delta_y = displacement * math.cos(theta)                 
            if f_y > 0:
                theta = math.degrees(math.atan(f_y/f_x))
                delta_x = displacement * math.sin(theta) 
                delta_y = displacement * math.cos(theta)
        if f_x == 0:
            if f_y > 0:
                delta_x = 0
                delta_y = displacement
            if f_y < 0:
                delta_x = 0
                delta_y = displacement * -1
        if f_y == 0:
            if f_x > 0:
                delta_x = displacement
                delta_y = 0
            if f_x < 0:
                delta_x = displacement * -1
                delta_y = 0

        print('deltas: {}'.format(delta_x))
        print('self.x : {}'.format(self.x))
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        #25000 m/pixel

    def draw(self):
        def cast_As_pixel(value):
            return value / PIXEL_CONSTANT
        arcade.draw_circle_filled(cast_As_pixel(self.x), cast_As_pixel(self.y), self.radius, arcade.color.WHITE, 0)
        print('x = {}, y = {}'.format(self.x, self.y))




class MyGame(arcade.Window):


    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        #initalizes 3 planets
        self.planet1 = planet(mass_1, planet_1x, planet_1y, fx1, fy1)

        self.planet2 = planet(mass_2, planet_2x, planet_2y, fx2, fy2)

        self.planet3 = planet(mass_3, planet_3x, planet_3y, fx3, fy3)
        

        arcade.set_background_color(arcade.color.BLACK)

        # If you have sprite lists, you should create them here,
        # and set them to None
        """
    def on_key_press(self, symbol,modifier):
        for i in range(10):
            if symbol == arcade.key.UP:
                mass_1 = self.planet1.mass
                planet1_x = self.planet1.x
                planet1_y = self.planet1.y

                mass_2 = self.planet2.mass
                planet2_x = self.planet2.x
                planet2_y = self.planet2.y

                mass_3 = self.planet3.mass
                planet3_x = self.planet3.x
                planet3_y = self.planet3.y        

                self.planet1.update_pos(mass_2, planet2_x, planet2_y, mass_3, planet3_x, planet3_y)
                print('updated 1')
                self.planet2.update_pos(mass_1, planet1_x, planet1_y, mass_3, planet3_x, planet3_y)
                print('updated 2')
                self.planet3.update_pos(mass_1, planet1_x, planet1_y, mass_2, planet2_x, planet2_y)
                print('updated 3')
                """

    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass
    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        self.planet1.draw()
        self.planet2.draw()
        self.planet3.draw()
        print('draw')
        # Call draw() on all your sprite lists below
#"""
    def on_update(self, delta_time):

        mass_1 = self.planet1.mass
        planet1_x = self.planet1.x
        planet1_y = self.planet1.y

        mass_2 = self.planet2.mass
        planet2_x = self.planet2.x
        planet2_y = self.planet2.y

        mass_3 = self.planet3.mass
        planet3_x = self.planet3.x
        planet3_y = self.planet3.y        

        self.planet1.update_pos(mass_2, planet2_x, planet2_y, mass_3, planet3_x, planet3_y)
        print('updated 1')
        self.planet2.update_pos(mass_1, planet1_x, planet1_y, mass_3, planet3_x, planet3_y)
        print('updated 2')
        self.planet3.update_pos(mass_1, planet1_x, planet1_y, mass_2, planet2_x, planet2_y)
        print('updated 3')
        
def main():
    """ Main function """
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()