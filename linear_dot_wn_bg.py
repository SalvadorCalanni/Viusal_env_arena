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

    clock = core.Clock()

    while True:
        keys = event.getKeys()
        if 'escape' in keys:
            break
        if 'space' in keys:
            dot_active = not dot_active
            dot_pos = [0, win_size[1] // 2]

        # Update background noise every frame
        new_noise = np.random.rand(128, 128) * 2 - 1
        white_noise.tex = new_noise
        white_noise.draw()

        if dot_active:
            dot_pos[0] = (dot_pos[0] + dot_speed) % win_size[0]
            dot.pos = dot_pos
            dot.draw()

        win.flip()
        core.wait(0.016)

    win.close()

main((500, 500))

