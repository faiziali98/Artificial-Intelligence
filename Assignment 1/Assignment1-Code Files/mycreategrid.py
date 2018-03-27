'''
 * Copyright (c) 2014, 2015 Entertainment Intelligence Lab, Georgia Institute of Technology.
 * Originally developed by Mark Riedl.
 * Last edited by Mark Riedl 05/2015
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
'''

import sys, pygame, math, numpy, random, time, copy
from pygame.locals import *

from constants import *
from utils import *
from core import *

# Creates a grid as a 2D array of True/False values (True =  traversable). Also returns the dimensions of the grid as a (columns, rows) list.
def myCreateGrid(world, cellsize):
	dimensions = (0.0, 0.0)
	dimensions = list(dimensions)
	
	### YOUR CODE GOES BELOW HERE ###

	# getting points and obstacles #

	points=world.getPoints()
	obts=world.getObstacles()

	# Dimensions of grid #

	dimensions[0]=int(math.ceil((points[1][0]-points[0][0])/cellsize))
	dimensions[1]=int(math.ceil((points[2][1]-points[0][1])/cellsize))
	dimensions = tuple(dimensions)
	x=int(dimensions[0])
	y=int(dimensions[1])
	numobts=len(obts)
	minx=[];maxx=[];miny=[];maxy=[]

	# getting minimum and maximum x and y axis of obstacles #

	for obs in xrange(0,numobts):
	    opoints=obts[obs].getPoints()
	    minx.append(opoints[0][0]);maxx.append(opoints[0][0])
	    miny.append(opoints[0][1]);maxy.append(opoints[0][1])
	    for p in opoints:
		if (p[0]<minx[obs]):
		    minx[obs]=p[0]
		    pass
		elif (p[0]>maxx[obs]):
		    maxx[obs]=p[0]
		    pass
		if (p[1]<miny[obs]):
		    miny[obs]=p[1]
		    pass
		elif (p[1]>maxy[obs]):
		    maxy[obs]=p[1]
		    pass
	    pass
	pass

	# Making boolean array of grid #

	grid=numpy.ones((x, y))
	for obs in xrange(0,numobts):
	    for xo in xrange(int(minx[obs]),int(maxx[obs])):
		yo=miny[obs]
		while yo<maxy[obs]:
		    curPoint = (xo,yo)
		    if (obts[obs].pointInside(curPoint)):
			xcell=int(math.floor(xo/cellsize))
			ycell=int(math.floor(yo/cellsize))
			grid[xcell][ycell] = 0
			yo=ycell*38+38
		    yo+=1
		pass
	    pass
	pass

	### YOUR CODE GOES ABOVE HERE ###

    	return grid, dimensions