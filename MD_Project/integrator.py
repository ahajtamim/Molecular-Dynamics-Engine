import numpy as np
from .forces import Lenanard_Jones_Force, Lenanard_Jones_PE
from .wrapping import Position_Wrapper

def Particle_Detection_Loop(snapshots, k_2d, mass, epsilon, gamma, lennard_sigma, ke_list, x_2d, v_2d, force_2d, particles, x, v, F, boltzmann, D, target_temp, energy, timestep, box_length):
    '''
    Loops MD data to calculate position, velocity, and energy at each particle snapshot
    '''
    sigma = np.sqrt(2 * gamma * boltzmann * target_temp / mass)
    for i in range(1, snapshots):
        force_random = np.sqrt(timestep) * sigma * np.random.normal(size=(particles, 2))
       
        v_halfstep = v + (((F/mass) - gamma * v) * (timestep/2)) + force_random/2 
        x_next = x + (v_halfstep * timestep)
        x_next = Position_Wrapper(x_next, box_length) #NEW

        F = Lenanard_Jones_Force(k_2d, x_next, lennard_sigma, epsilon, particles, box_length)
        f_next = F

        lennard_pe = Lenanard_Jones_PE(k_2d, x_next, lennard_sigma, epsilon, particles, box_length)

        v_next = v_halfstep + (((f_next / mass) - gamma * v_halfstep) * (timestep / 2.0)) + 0.5 * force_random 

        x_2d[i] = x_next ; v_2d[i] = v_next ; force_2d[i] = f_next

        pe = 0.5 * k_2d * np.power(x_next, 2)
        ke = 0.5 * mass * np.power(v_next, 2)
        
        ke_list[i] = ke.sum() ; energy[i] = pe.sum() + lennard_pe + ke.sum()

        x = x_next ; v = v_next ; F = f_next

    pe_list = energy - ke_list
    temperature = (ke_list * 2) / (boltzmann * D * particles)

    return x_2d, v_2d, energy, pe_list, ke_list, temperature 