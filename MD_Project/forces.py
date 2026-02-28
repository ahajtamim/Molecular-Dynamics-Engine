import numpy as np
from .wrapping import Displacement_Wrapper

def Lenanard_Jones_Force(k_2d, position, lennard_sigma, epsilon, particles,box_length):
    '''
    Calculates the Lennard Jones Force for the MD Engine
    '''
    F = -k_2d * position # old harmonic force equation
    F_part = np.zeros_like(F)
    lennard_force = 0.0
    r_min = 0.8 * lennard_sigma   

    for a in range(particles): # double loop avoids double-counting pairs
        for b in range(a + 1, particles): 
            r_vector = Displacement_Wrapper(position[a],position[b], box_length)
            r = np.sqrt(r_vector[0]**2 + r_vector[1]**2) #scalar distance for r

            if r < r_min:
                r = r_min

            sigma_r_12 = (lennard_sigma / r)**12 ; sigma_r_6  = (lennard_sigma / r)**6

            lennard_force = 3.0 * epsilon * (2.0 * sigma_r_12 - sigma_r_6) / r
            F_part = lennard_force * (r_vector / r)

            F[a] += F_part ; F[b] -= F_part

    return F

def Lenanard_Jones_PE(k_2d, position, lennard_sigma, epsilon, particles, box_length):
    '''
    Calculates the Lennard Jones PE for the MD Engine
    '''
    lennard_pe = 0.0
    r_min = 0.8 * lennard_sigma

    for a in range(particles):
        for b in range(a + 1, particles):
            r_vector = Displacement_Wrapper(position[a],position[b], box_length) ; r = np.sqrt(r_vector[0]**2 + r_vector[1]**2) # r = distance between two particles, sqrt((xa-xb)^2 + (ya-yb)^2)
            if r < r_min:
                r = r_min

            sigma_r_12 = (lennard_sigma / r)**12 ; sigma_r_6 = (lennard_sigma / r)**6

            lennard_pe += (sigma_r_12 - sigma_r_6) * (epsilon/4)
            
    return lennard_pe