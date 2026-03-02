from MD_Project import Molecular_Dynamics_Engine
from MD_Project.visuals import static_plot, animate_plot
import matplotlib.pyplot as plt

if __name__ == "__main__": #Only run this code when this file is executed directly, not when it’s imported
    time, position, velocity, energy, potential_energy, temperature, particles, timestep, force, box_length = Molecular_Dynamics_Engine(
                                                                                                            kx = 0.0,
                                                                                                            ky = 0.0, 
                                                                                                            mass = 1.0,

                                                                                                            particles = 20,
                                                                                                            boltzmann = 1.0,
                                                                                                            gamma = 0.02,
                                                                                                            target_temp = 1, 
                                                                                                            dt = 0.01,
                                                                                                            total_time = 30.0,

                                                                                                            rand_position_scale = 10.0,   
                                                                                                            epsilon = 1.0,
                                                                                                            lennard_sigma = 1.0,
                                                                                                            D = 2,
                                                                                                            box_length = 10.0)
    
# static plot
static_plot(position, particles, box_length)
plt.show()

# animation (roughly ~5min)
animate_plot(position, time, box_length)