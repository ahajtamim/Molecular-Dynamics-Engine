import numpy as np

def Position_Wrapper(position, box_length):
    '''
    Wraps position to box_length
    '''
    return ((position + box_length/2) % box_length) - box_length/2

def Displacement_Wrapper(ri, rj, box_length):
    '''
    Minimum Image Convention
    '''

    r_vector = ri - rj

    for d in range(len(r_vector)):

        while r_vector[d] > box_length/2:
            r_vector[d] -= box_length

        while r_vector[d] < -box_length/2:
            r_vector[d] += box_length

    return r_vector
