### Author: Stephanie Marbella
### Course: CSc 110
### Description: This program displays a landscape with motion parallax. It 
###              uses the mouse's x and y coordinates to give the illusion
###              of motion parallax. The landscape is designed from gui
###              shapes. Ellipses define the sun, clouds, fruits on the trees,
###              and the leaves of trees. Triangles define the three mountains
###              in the background and detailed grass blades. A rectangle is
###              used to form the sky and the foreground. Moving the mouse
###              around inside the gui window changes perspective of the
###              landscape. Loops are used to give the landscape multiple 
###              trees, blades The program doesn't take any input values
###              from the command-line nor prints out anything.

# Each of these imported modules except random module were installed from
# base.py.
import random
import sys
import os 
cwd = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, cwd)
from graphics import graphics

# Calling the functions below will draw each components needed to create
# the landscape.
def background(gui):
    """The rectangle in this function creates the sky background. The round
    ellipse creates the sun."""
    x = gui.mouse_x
    y = gui.mouse_y
    gui.rectangle(0, 0, 800, 800, 'lightskyblue1')
    gui.ellipse((x / 50) + 600, (y / 50) + 100, 100, 100, 'yellow')

def cloud(gui, cloud_x, cloud_y):
    """This function defines each individual cloud in the sky."""
    x = gui.mouse_x
    y = gui.mouse_y
    OFFSET = 100
    gui.ellipse((x / 50) - OFFSET + cloud_x, (y / 50) + cloud_y, 200, 50,
                'white')

def get_random_color_string(gui):
    """This function makes each mountain different colors each time
    the window is opened after it has been closed."""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return gui.get_color_string(r, g, b)

def middle_mountain(gui, color):
    """This is the function for the mountain in the center of the
    window."""
    x = gui.mouse_x
    y = gui.mouse_y
    gui.triangle((x / 20) + 400, (y / 20) + 250, (x / 20) + 600, 
                 (y / 20) + 800, (x / 20) + 100, (y / 20) + 900, color)

def side_mountains(gui, lm, rm):
    """This is the function for both mountains at both edges of the
    window."""
    x = gui.mouse_x
    y = gui.mouse_y
    #  left mountain
    gui.triangle((x / 10) + 200, (y / 10) + 300, (x / 10) - 500, 
                 (y / 10) + 900, (x / 10) + 700, (y / 10) + 900, lm)
    #  right mountain
    gui.triangle((x / 10) + 600, (y / 10) + 300, (x / 10) + 1100, 
                 (y / 10) + 900, (x / 10) + 100, (y / 10) + 900, rm)

def foreground(gui):
    """This function creates the ground and the grass blades for the
    landscape."""
    x = gui.mouse_x
    y = gui.mouse_y
    gui.rectangle(-10, (y / 5) + 600, 820, 500, 'yellow green')  # ground
    i = 0
    # The code below draws the intricate details of the grass blades.
    BLADE_HEIGHT = 550
    while i < 100:
        offset = i * 20
        if i % 2 == 0:
            gui.line((offset + x / 3) - 800, (y / 5) + BLADE_HEIGHT,
                     (offset + x / 3) -
                     800, (gui.mouse_y / 5) + 601, 'olivedrab3', 15)
            gui.line((offset + x / 3) - 800, (y / 5) + BLADE_HEIGHT,
                     (offset + x / 3) -
                     800, (gui.mouse_y / 5) + 601, 'olivedrab4', 5)
            gui.triangle((offset + x / 3) - 900, (y / 5) + 560,
                         (offset + x / 3) - 400, (y / 5) + 700,
                         (offset + x / 3) - 700, (y / 5) + 700, 'yellow green')
    # Using the else statement gives off different patterns for the grass if
    # the if statement is false.
        else:
            gui.line((offset + x / 3) - 800, (y / 5) + 550, (offset + x / 3) -
                     800, (y / 5) + 601, 'darkolivegreen2', 15)
            gui.line((offset + x / 3) - 800, (y / 5) + 550, (offset + x / 3) -
                     800, (y / 5) + 601, 'darkolivegreen3', 5)
        i += 1
    i = 0

def trees(gui):
    """This function adds trees to the foreground. There are more than
    one tree in the landscape, and each tree bears fruits and different
    foliage. The trees are arranged in a pattern."""
    i = 0 
    x = gui.mouse_x
    y = gui.mouse_y
    # The random.randint function below allows only shades of green to
    # be generated for the leaves of all trees. Green is left out
    # because adding green into the while loop that designs the leaves
    # will give them a fixed color instead of different shades of green.
    r = random.randint(0, 30)
    b = random.randint(0, 100)
    # This while loop generates the trees.
    while i < 60:
        # The offset is the spacing between the trees.
        offset = i * 20
        # When i is divisible by 20, trees that bear apples are generated.
        if i % 20 == 0:
            gui.ellipse((offset + x / 3) - 180, (y / 5) + 530, 100, 100,
                        'springgreen4')
            gui.ellipse((offset + x / 3) - 187, (y / 5) + 490, 100, 100,
                        'darkolivegreen1')
            gui.rectangle((offset + x / 3) - 200, (y / 5) + 525, 25, 100,
                          'brown')
            gui.ellipse((offset + x / 3) - 187, (y / 5) + 530, 100, 100,
                        'darkolivegreen3')
            # The count variable is resetted to 0, so other details in the
            # trees can be generated.
            count = 0
            # This while loop generates details in the apple tree leaves.
            while count < 10:
                LEAVES_X = random.randint(170, 230)
                LEAVES_Y = random.randint(490, 540)
                LEAVES_WIDTH = random.randint(60, 80)
                LEAVES_HEIGHT = random.randint(50, 80)
                gui.ellipse((offset + x / 3) - LEAVES_X, (y / 5) + LEAVES_Y,
                            LEAVES_WIDTH, LEAVES_HEIGHT,
                            gui.get_color_string(r, random.randint(50, 255),
                            b))
                # Adding 1 to count draws 1 more foliage.
                count += 1
            # The count variable is resetted to 0, so other details in the
            # trees can be generated.
            count = 0
            gui.line((offset - 50 + x / 3) - 180, (y / 5) + 550, (offset +
                     x / 3) - 190, (y / 5) + 600, 'brown', 8)
            gui.ellipse((offset + x / 3) - 230, (y / 5) + 535, 70, 50,
                        'chartreuse2')
            # The while loop below generates 20 apples on each apple tree.
            while count < 20:
                APPLES_X = random.randint(150, 260)
                APPLES_Y = random.randint(460, 565)
                gui.ellipse((offset + x / 3) - APPLES_X, (y / 5) + APPLES_Y,
                            10, 10, 'red2')
                # Adding 1 to count draws 1 more apple.
                count += 1
        # If i is divisible by 10, trees that bear oranges are generated.
        elif i % 10 == 0:
            gui.rectangle((offset + x / 3) - 200, (y / 5) + 525, 25, 100,
                          'brown')
            gui.ellipse((offset + x / 3) - 187, (y / 5) + 500, 150, 150,
                        'olive drab')
            gui.ellipse((offset + x / 3) - 220, (y / 5) + 530, 100, 100,
                        'darkolivegreen3')
            gui.ellipse((offset + x / 3) - 180, (y / 5) + 460, 100, 100,
                        'springgreen4')
            # The count variable is resetted to 0, so other details in the
            # trees can be generated.
            count = 0
            while count < 10:
                LEAVES_X = random.randint(110, 230)
                LEAVES_Y = random.randint(430, 555)
                LEAVES_WIDTH = random.randint(60, 90)
                LEAVES_HEIGHT = random.randint(50, 90)
                gui.ellipse((offset + x/3) - LEAVES_X, (y / 5) +
                            LEAVES_Y, LEAVES_WIDTH, LEAVES_HEIGHT,
                            gui.get_color_string(r, random.randint(50, 255),
                            b))
                # Adding 1 to count draws 1 more apple.
                count += 1
            # The count variable is resetted to 0, so other details in the
            # trees can be generated.
            count = 0
            gui.line((offset + 50 + x / 3) - 180, (y / 5) + 550,
                     (offset + x / 3) - 190, (y / 5) + 600, 'brown', 8)
            gui.ellipse((offset + x / 3) - 130, (y / 5) + 550, 70, 50,
                        'darkolivegreen3')
            # The while loop below generates 20 oranges on each orange tree.
            while count < 20:
                ORANGES_X = random.randint(130, 260)
                ORANGES_Y = random.randint(460, 565)
                gui.ellipse((offset + x / 3) - ORANGES_X, (y / 5) + ORANGES_Y,
                            10, 10, 'orange')
                # Adding 1 to count draws 1 more orange.
                count += 1
            # The seed value from the random module keeps the leaves and
            # fruits in place. Without it, the leaves and fruits would
            # buzz all over the trees.
            random.seed(5)
        i += 1
    
def bird(gui, X_1, Y_1):
    """This function generates one bird that flies across the gui window
    from left to right. The x axis and the y_axis of each bird are used
    to change their locations on the screen. Calling this function five
    times will create five birds in this program."""
    i = 0
    left_wing_tip = 170
    right_wing_tip = 230
    BODY_Y = 160
    WING_Y = 150
    BODY_X = 140
    # The while loop below generates one bird.
    while i < 2:
        offset = i * 20
        if i % 2 == 0:
            gui.line(X_1 - left_wing_tip, WING_Y + Y_1, X_1 - BODY_X, BODY_Y +
                     Y_1, 'gray30', 5)
        else:
            gui.line(X_1 + offset-right_wing_tip, WING_Y + Y_1, X_1 - BODY_X,
                     BODY_Y + Y_1, 'gray30', 5)
        i += 1
        right_wing_tip -= 100

def main():
    # The gui variable is used to create the window that displays the
    # landscape.
    gui = graphics(800, 800, 'Landscape')
    # These color variables give the mountains the ability to change
    # colors each time the program is opened.
    color_1 = get_random_color_string(gui)
    color_2 = get_random_color_string(gui)
    color_3 = get_random_color_string(gui)
    # This row of x-axis are used to give each birds their positions
    # in the flock. Adding some values in each x_axis shifts each
    # bird closer to the right edge of the window. The x-axis values
    # also animate the birds.
    X_1 = 0
    X_2 = 100
    X_3 = 200
    X_4 = 300
    X_5 = 400
    # This row of y-axis are used to give their birds their own
    # altitudes in the sky. The higher the value, the lower the bird.
    Y_1 = 0
    Y_2 = 25
    Y_3 = 50
    Y_4 = 75
    Y_5 = 100
    # This row of x-axis for the clouds give them their x coordinates
    # shifts just like the x-axis for the birds. The x-axis values
    # values animate the clouds.
    CX_1 = 0
    CX_2 = 400
    CX_3 = 800
    CX_4 = 1200
    # This row of y-axis values for the clouds give them their altitudes
    # in the sky. The higher the value, the lower the clouds.
    CY_1 = 100
    CY_2 = 200
    CY_3 = 150
    CY_4 = 250
    while True:
        gui.clear()
        # Layer 1
        background(gui)
        cloud(gui, CX_1, CY_1)
        cloud(gui, CX_2, CY_2)
        cloud(gui, CX_3, CY_3)
        cloud(gui, CX_4, CY_4)
        # Layer 2
        middle_mountain(gui, color_1)
        # Layer 3
        side_mountains(gui, color_2, color_3)
        # Layer 4
        foreground(gui)
        trees(gui)
        # The bird function is called five times, so five birds will
        # appear in the gui window.
        bird(gui, X_1, Y_1)
        bird(gui, X_2, Y_2)
        bird(gui, X_3, Y_3)
        bird(gui, X_4, Y_4)
        bird(gui, X_5, Y_5)
        # Each x-axis variable is used to give each bird their speed. The birds
        # will fly across the screen repeatedly because a modulus is used to
        # reset their positions. 1000 is used to reset the birds back to their
        # offscreen positions on the left of the window.
        X_1 += 5
        X_1 = (X_1 % 1000)
        X_2 += 5
        X_2 = (X_2 % 1000)
        X_3 += 5
        X_3 = (X_3 % 1000)
        X_4 += 5
        X_4 = (X_4 % 1000)
        X_5 += 5
        X_5 = (X_5 % 1000)
        # Each x-axis variable is used to give each cloud their speed. The
        # modulus is used to reset the positions of each cloud back to the
        # left side of the screen. The numerical value used for the clouds
        # is 500 pixels more than the birds' because the clouds are longer.
        CX_1 += 1
        CX_1 = (CX_1 % 1500)
        CX_2 += 1
        CX_2 = (CX_2 % 1500)
        CX_3 += 1
        CX_3 = (CX_3 % 1500)
        CX_4 += 1
        CX_4 = (CX_4 % 1500)
        gui.update_frame(60)
        
# The main function is the only function that will be called when the program
# is executed.
main()