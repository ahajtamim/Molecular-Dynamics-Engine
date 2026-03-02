import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter, FuncAnimation
import random

def static_plot(position, particles, box_length):
    '''
    Creates a static plot projecting data from particle positions
    '''
    fig, ax = plt.subplots(1,1, figsize=(6,6))
    color_list = ['red', 'blue', 'green', 'orange', 'brown', 'gray']

    for p in range(particles):
        if len(color_list) == 0:
            color_list = ['red', 'blue', 'green', 'orange', 'brown', 'gray']
        selected_color = random.choice(color_list)
        color_list.remove(selected_color)

        ax.plot(position[:,p,0], position[:,p,1],
                color = selected_color,
                linestyle = "-",
                linewidth=2,
                label = "Particle: " + str(p + 1))

    ax.set_xlabel('$x(t)$ (m)') 
    ax.set_ylabel('$y(t)$ (m)') 
    ax.set_xlim(-box_length/2, box_length/2) 
    ax.set_ylim(-box_length/2, box_length/2)
    ax.legend(loc="upper right") 
    ax.set_title("MD Engine - Particle Positions") 
    ax.grid(True)
    plt.savefig('Files/Particle_Positions.png')
    
    return fig, ax


def animate_plot(position, time, box_length, filename="Files/Particle_Animation.mp4"):
    '''
    Creates an animation projecting data from particle positions
    '''
    fig, ax = plt.subplots() 

    scatter = ax.scatter(position[0,:,0], position[0,:,1], s=40, c= 'red') #size (s) color (c)

    ax.set_xlabel('$x(t)$ (m)') 
    ax.set_ylabel('$y(t)$ (m)') 
    ax.set_xlim(-box_length/2, box_length/2) 
    ax.set_ylim(-box_length/2, box_length/2) 
    ax.grid(True)
    ax.set_title("MD Engine - Particle Positions") 

    step = 1  # skips every other frame
    frame_ind = np.arange(0, len(time), step)

    def init():
        scatter.set_offsets(position[0])
        return (scatter,)

    def update_data(frames): #Updates particle at each frame
        scatter.set_offsets(position[frames]) #updates scatter points
        return scatter,

    writer = FFMpegWriter(fps = 30)
    animation = FuncAnimation(fig, update_data, frames=frame_ind, init_func = init, blit=True)
    animation.save(filename, writer=writer, dpi=80)
    plt.close(fig)