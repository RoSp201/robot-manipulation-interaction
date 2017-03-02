""" Homework 3 Problem 4 Name: Robert Spark """ 

import numpy as np
from math import *

def force_closure(contacts, normals, num_facets, mu, gamma):     
	"""
	This function will apply Corrollary 3 of Section 4 of the Nguyen paper on constructing force closure grasps, (1988)
	For the case of two opposing fingers, we will check the vector connecting both contact points and check if the vector lies
	completely within both of the friction cones created by the contact points. If it does (angles less than angle caused by friction coef), it is force-closure.
	"""    
	# the angle that characterizes both friction cones can be determined from mu
	alpha = atan(mu)
	vector = contacts[:,1] - contacts[:,0]

	#note we don't even need to use gamma because paper states corrollary 3 extends to 3D
	#check that that angle of the normalized dot product with the surface normals and the vector between the contact points
	angle1 = acos(-normals[:,0].dot(vector) / (np.norm(vector)*np.norm(normals[:,0])))
	angle2 = acos(normals[:,1].dot(vector) / (np.norm(vector)*np.norm(normals[:,1])))

	#if both angles lie with the allowed friction cones of both point contacts, then force-closure
	if angle1 <= alpha and angle2 <= alpha:
		return 1
	return 0


	#Test
	