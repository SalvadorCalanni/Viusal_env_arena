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

def add_polar_grid(win, radial_spacing=50, angular_spacing=30):
    """
    Draw a polar coordinate grid on the window
    
    Parameters:
    -----------
    win : psychopy.visual.Window
        The window to draw on
    radial_spacing : int
        Distance between concentric circles (pixels)
    angular_spacing : int
        Degrees between radial spokes
    """
    size = win.size
    center = [size[0]//2, size[1]//2]
    max_radius = min(size)//2  # Largest radius that fits in window
    
    win._permanent_polar_stim = []
    
    # Create concentric circles (radial lines)
    for r in range(radial_spacing, max_radius, radial_spacing):
        circle = visual.Circle(
            win,
            radius=r,
            pos=center,
            edges=128,  # Smooth circle
            lineColor='black',
            fillColor=None,
            lineWidth=1,
            autoDraw=True
        )
        win._permanent_polar_stim.append(circle)
    
    # Create radial spokes (angular lines)
    for angle in range(0, 360, angular_spacing):
        theta = np.radians(angle)
        end_x = center[0] + max_radius * np.cos(theta)
        end_y = center[1] + max_radius * np.sin(theta)
        
        line = visual.Line(
            win,
            start=center,
            end=[end_x, end_y],
            lineColor='black',
            lineWidth=1,
            autoDraw=True
        )
        win._permanent_polar_stim.append(line)
    
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

######################## CARTESIAN TO POLAR #############################


def polar_to_cartesian(r, theta, center):
    """Convert polar coordinates (r, theta) to Cartesian coordinates (x, y) relative to center"""
    x = r * np.cos(theta) + center[0]
    y = r * np.sin(theta) + center[1]
    return [x, y]

def cartesian_to_polar(x, y, center):
    """Convert Cartesian coordinates (x, y) to polar coordinates (r, theta) relative to center"""
    dx = x - center[0]
    dy = y - center[1]
    r = np.sqrt(dx**2 + dy**2)
    theta = np.arctan2(dy, dx)
    return [r, theta]