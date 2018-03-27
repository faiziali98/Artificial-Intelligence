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
	grid = None
	dimensions = (0,0)
	### YOUR CODE GOES BELOW HERE ###
	dimensions = (int(world.getDimensions()[0]/cellsize+1), int(world.getDimensions()[1]/cellsize+1))
	grid =[[True for x in range(dimensions[1])]for y in range(dimensions[0])] #decclared a grid of appropriate size
	for i in range(dimensions[0]):
		for j in range(dimensions[1]):
			for obst in world.getObstacles():
				if obst.pointInside([i*cellsize,j*cellsize]):
					grid[i][j] = False
				for line in obst.getLines():
					if rayTrace((i*cellsize,j*cellsize),(i*cellsize,(j+1)*cellsize),line)\
					   or rayTrace((i*cellsize,j*cellsize),((i+1)*cellsize,j*cellsize),line)\
					   or rayTrace(((i+1)*cellsize,j*cellsize),((i+1)*cellsize,(j+1)*cellsize),line)\
					   or rayTrace((i*cellsize,(j+1)*cellsize),((i+1)*cellsize,(j+1)*cellsize),line):
						grid[i][j] = False
				
	### YOUR CODE GOES ABOVE HERE ###
	return grid, dimensions



