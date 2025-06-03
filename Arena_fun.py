from psychopy import visual, core, event
import numpy as np


####    WINDOW      #########################

def create_grey_window(size):

    # Create window
    win = visual.Window(
        size=size,
        color=[0.5, 0.5, 0.5],  # Default gray background
        units='pix',
        winType='pyglet',  # Use pyglet for better performance
        viewPos=(-size[0] // 2, -size[1] // 2),  # Center the view
    )

    return win

def add_permamnet_grid(win):

    size = win.size

    #grid elements
    spacing = 50  # Spacing between grid lines
    width, height = size[0]*2, size[1]*2

    win._permanent_stim = []
        # Create grid lines (permanent)
    for y in range(-height, height, spacing):
        line = visual.Line(
            win, 
            start=(-width, y), 
            end=(width, y), 
            lineColor='black',
            autoDraw=True  # Critical for persistence
        )
        win._permanent_stim.append(line)
    
    for x in range(-width, width, spacing):
        line = visual.Line(
            win,
            start=(x, -height),
            end=(x, height),
            lineColor='black',
            autoDraw=True
        )
        win._permanent_stim.append(line)

    
    # Initial flip to commit background
    win.flip()

def add_static_bck(win, bkg_array):
    
    size = win.size
    
    # Create checkerboard pattern
    background= visual.GratingStim(
        win=win,
        tex=bkg_array,
        size=size,
        pos=(size[0] // 2, size[1] // 2),
    )

    # Store the checkerboard in the window for later reference
    win.background_stim = background
    # Initial flip to commit background
    win.background_stim.draw()
    win.flip()





############ BACKGROUNDS #################################
def create_checkerboard(win_size, sq_size):
    # Create a checkerboard pattern as a numpy array
    rows = win_size[1] // sq_size
    cols = win_size[0] // sq_size
    checkerboard = np.indices((rows, cols)).sum(axis=0) % 2
    checkerboard = checkerboard * 2 - 1  # Convert to -1 and 1 for PsychoPy GratingStim

    return checkerboard

def create_white_noise_background(size, contrast=0.5):
    """Generate dynamic white noise texture"""
    return np.random.uniform(-contrast, contrast, (size[1], size[0]))


#####   STIMULI   #########################


def black_dot(win, pos):
    dot = visual.Circle(
        win=win,
        radius=10,
        fillColor='black',
        lineColor='black'
    )

    size = win.size
    pos_x = pos[0]
    pos_y = pos[1]  # Set initial position
    speed = 5

    # Animation loop
    while True:
        pos_x = ((pos_x + speed) % size[0])   # Wrap around the screen
        dot.pos = (pos_x, pos_y)

        # Clear and redraw
        win.clearBuffer()

        if hasattr(win, 'background_stim'):
            win.background_stim.draw()
        
        dot.draw()

        win.flip()

        # Check for quit key (e.g., 'escape')
        if 'escape' in event.getKeys():
            return
        

def white_noise_bkg(win):
    size = win.size

    
    # Draw the background
    while True:

        win.clearBuffer()

        bkg = create_white_noise_background(size, contrast=0.5)

        background = visual.GratingStim(
            win=win,
            tex=bkg,
            size=size,
            pos=(size[0] // 2, size[1] // 2),
        )
        background.draw()
        win.flip()
        # Check for quit key (e.g., 'escape')
        if 'escape' in event.getKeys():
            return
        

def black_dot_white_noise_bkg(win, pos):
    dot = visual.Circle(
        win=win,
        radius=10,
        fillColor='black',
        lineColor='black'
    )

    size = win.size
    pos_x = pos[0]
    pos_y = pos[1]  # Set initial position
    speed = 5

    # Animation loop
    while True:
        pos_x = ((pos_x + speed) % size[0])   # Wrap around the screen
        dot.pos = (pos_x, pos_y)

        # Clear and redraw
        win.clearBuffer()

        bkg = create_white_noise_background(size, contrast=0.5)

        # Draw the background
        background = visual.GratingStim(
            win=win,
            tex=bkg,
            size=size,
            pos=(size[0] // 2, size[1] // 2),
        )
        background.draw()
        dot.draw()
        win.flip()
        # Check for quit key (e.g., 'escape')
        if 'escape' in event.getKeys():
            return


######################################

def create_white_noise_stim(win):
    noise_array = np.random.rand(128, 128) * 2 - 1
    stim = visual.GratingStim(
        win=win,
        tex=noise_array,
        size=win.size,
        pos=(win.size[0] // 2, win.size[1] // 2),
        units='pix',
        interpolate=True
    )
    return stim



def create_black_dot(win):
    return visual.Circle(
        win=win,
        radius=10,
        fillColor='black',
        lineColor='black'
    )


def create_looming_stim(win):
    return visual.Circle(
        win=win,
        radius=1,
        fillColor='black',
        lineColor='black',
        )

