from .initializer import MD_Initializer, MD_Initial_Values, Initial_Position_Velocity
from .forces import Lenanard_Jones_Force, Lenanard_Jones_PE
from .integrator import Particle_Detection_Loop


def Molecular_Dynamics_Engine(kx=1, ky=1, mass=1, particles=2, boltzmann=1, gamma=0.1, target_temp=1.0, dt=0.001, total_time=5, 
                        rand_position_scale=1, epsilon = 1.0, lennard_sigma = 1.0, D = 2, box_length = 5.0):
    '''
    kx : Spring constant for x position
    ky : Spring constant for y position

    mass : Mass of particle
    particles : Number of particles

    boltzmann : In the surroundings at given temperature
    gamma : Friction in system
    target_temp : Target temperature of system

    dt = 0.01 : Designated timestep
    total_time : Total runtime of system

    rand_position_scale : Scales the random initial position values of particles

    epsilon : Max strength of particle attraction
    lennard_sigma : Radius of particle
    D : # of Dimensions  
    '''
    
    snapshots, omega, time, timestep, energy, ke_list, x_2d, v_2d, force_2d, temperature, k_2d = MD_Initializer(mass, kx, ky, dt, 
                                                                                                                total_time, D, particles)
    

    x, v = Initial_Position_Velocity(mass, target_temp, particles, D, boltzmann, rand_position_scale, box_length)


    F = Lenanard_Jones_Force(k_2d, x, lennard_sigma, epsilon, particles, box_length)


    lennard_pe = Lenanard_Jones_PE(k_2d, x, lennard_sigma, epsilon, particles, box_length)


    x_2d, v_2d, force_2d, pe_0, ke_0, energy, ke_list = MD_Initial_Values(k_2d, mass, x, v, F, x_2d, v_2d, force_2d, 
                                                                          ke_list, lennard_pe, energy)



    x_2d, v_2d, energy, pe_list, ke_list, temperature = Particle_Detection_Loop(snapshots, k_2d, mass, epsilon, gamma, 
                                                                   lennard_sigma, ke_list, x_2d, v_2d, force_2d, 
                                                                   particles, x, v, F, boltzmann, D, target_temp, energy, timestep, box_length)


    return time, x_2d, v_2d, energy, pe_list, temperature, particles, timestep, force_2d, box_length