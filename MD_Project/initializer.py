import numpy as np
from .wrapping import Position_Wrapper

def MD_Initializer(mass, kx, ky, dt, total_time, D, particles):
    '''
    Defines variables for the MD engine
    '''
    omega = np.sqrt(kx/mass)
    timestep = dt#*omega
    snapshots = int(np.floor(total_time / timestep)) + 1
    time = np.arange(snapshots, dtype=float) * timestep
    energy = np.zeros(snapshots, dtype=float)
    ke_list = np.zeros(snapshots, dtype=float)
    x_2d = np.zeros((snapshots, particles, D), dtype=float)
    v_2d = np.zeros((snapshots, particles, D), dtype=float)
    force_2d = np.zeros((snapshots, particles, D), dtype=float)
    temperature = np.zeros(v_2d.size, dtype=float)
    k_2d = np.array([kx, ky], dtype=float) 

    return snapshots, omega, time, timestep, energy, ke_list, x_2d, v_2d, force_2d, temperature, k_2d

def MD_Initial_Values(k_2d, mass, x, v, F, x_2d, v_2d, force_2d, ke_list, lennard_pe, energy):
    '''
    Sets the initial values for the MD engine variables'''
    x_2d[0] = x ; v_2d[0] = v ; force_2d[0] = F
    pe_0 = 0.5 * k_2d * np.power(x, 2) ; ke_0 = 0.5 * mass * np.power(v, 2)
    energy[0] = pe_0.sum() + lennard_pe + ke_0.sum() ; ke_list[0] = ke_0.sum()
    return x_2d, v_2d, force_2d, pe_0, ke_0, energy, ke_list

def Initial_Position_Velocity(mass, target_temp, particles, D, boltzmann, rand_position_scale, box_length):
    '''
    Calculates initial x and v for each particle in the MD engine
    '''

    x = rand_position_scale * np.random.rand(particles, D)
    x = Position_Wrapper(x, box_length) #PBC
    #Maxwell_Velocity_Distribution
    sigma = np.sqrt(boltzmann * target_temp / mass)
    v = np.random.normal(loc=0.0, scale=sigma, size=(particles, D))
    return x, v
