import Arena_fun
from psychopy import visual, core, event
import numpy as np



def main(win_size):
    win = Arena_fun.create_grey_window(win_size)

    dot_active = False
    dot = Arena_fun.create_black_dot(win)
    white_noise = Arena_fun.create_white_noise_stim(win)

    dot_pos = [0, win_size[1] // 2]
    dot_speed = 5

    looming_active = False
    looming_stim = Arena_fun.create_looming_stim(win)
    looming_speed = 20


    while True:
        keys = event.getKeys()
        if 'escape' in keys:
            break
        if 'c' in keys:
            dot_active = not dot_active
            dot_pos = [0, win_size[1] // 2]
        if 'l' in keys:
            looming_active = not looming_active
            looming_stim.pos = (np.random.randint(0, win_size[0]), np.random.randint(win_size[1]//2, win_size[1]))
            looming_stim.radius = 1  # Reset size when reactivating
        
        # Update background noise every frame
        new_noise = np.random.rand(128, 128) * 2 - 1
        white_noise.tex = new_noise
        white_noise.draw()

        if dot_active:
            dot_pos[0] = (dot_pos[0] + dot_speed) % win_size[0]
            dot.pos = dot_pos
            dot.draw()

        if looming_active:
            if looming_stim.radius < 300:  # Limit the maximum size
                looming_stim.radius += int(looming_speed)
                looming_stim.draw()
            else:
                looming_active = False  # Stop looming when max size is reached
        win.flip()
        core.wait(0.016)

    win.close()

main((1000, 1000))

