
#	Radius Function for HW 3, Question 3b
#	Robert Spark
#	EE106B: Robotic Manipulation and Interaction, UC Berkeley, Spring 2017

import matplotlib.pyplot as plt
import numpy as np
from math import *



def radius(theta):
    '''
    input: list of x, y pairs of coordinates for vertices of convex polygon
    we will map the different quadrants of the shape based upon their difference in angle w/r COM
    these angles will be stored as tuples of points which will be mapped to the line used to interpolate
    
    using the correct line between points, we will construct a linear equation using the y/x slope
    find the point of intersection between the two lines 
    '''
    angles = [np.pi/2, atan(1/-2)+np.pi, atan(1)+np.pi, 3*np.pi/2, 2*np.pi - atan(-2/3)]
    line_slopes = [-5/3.00, 1, 4, 2/3.00, -1/3.00]

    if angles[0] - 0.000001 <= theta <= angles[0]+0.000001:
        return 3
    elif angles[1] - 0.000001 <= theta <= angles[1]+0.000001:
        return sqrt(5)
    elif angles[2] - 0.000001 <= theta <= angles[2]+0.000001:
        return sqrt(18)
    elif angles[3] - 0.000001 <= theta <= angles[3]+0.000001:
        return -1
    elif angles[2] - 0.000001 <= theta <= angles[2]+0.000001:
        return sqrt(13)
    elif theta > angles[4] or theta < angles[0]:
    	return find_radius_from_lines(theta, line_slopes[0], 3)
    elif angles[0] < theta < angles[1]:
    	return find_radius_from_lines(theta, line_slopes[1], 3)
    elif angles[1] < theta < angles[2]:
    	return find_radius_from_lines(theta, line_slopes[2], -3*line_slopes[2] + 3)
    elif angles[2] < theta < angles[3]:
    	return find_radius_from_lines(theta, line_slopes[3], -1)
    elif angles[3] < theta < angles[4]:
    	return find_radius_from_lines(theta, line_slopes[4], -1)

def find_radius_from_lines(angle, m, b):
    if angle == 0:
        ts = 0
    else:
        ts = sin(angle) / cos(angle)
	x = b / (ts-m)
	y = m*x + b
	return sqrt(x**2 + y**2)

test = list(np.linspace(start=0, stop=2*np.pi, num=50, endpoint=False))
results = [radius(t) for t in test]
plt.plot(test, results)
plt.ylabel("Radius (units)")
plt.xlabel("Angle (Radians)")
plt.title("Radius Function for Problem 3")
plt.show()


