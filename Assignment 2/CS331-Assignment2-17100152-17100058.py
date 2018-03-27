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
from sets import Set
from constants import *
from utils import *
from core import *
from mycreategrid import *
'from mycreatepathnetwork import *'
from mynavigatorhelpers import *



###################
### GridNavigator
###
### Abstract base class for navigating the world on a grid.
class GridNavigator(Navigator):


	### grid: the grid, a 2D array where each element is True or False indicating navigability of that region of the corresponding region of space.
	### dimensions: the number of columns and rows in the grid: (columns, rows)
	### cellSize: the physical size of each corresponding cell in the map. Automatically set to the agent's radius x 2.

	def __init__(self):
		Navigator.__init__(self)
		self.grid = None
		self.dimensions = (0, 0)
		self.cellSize = 0

	def setAgent(self, agent):
		Navigator.setAgent(self, agent)
		self.cellSize = round(agent.getRadius())*2.0

	### Set the world object
	### self: the navigator object
	### world: the world object
	def setWorld(self, world):
		# Store the world object
		self.world = world
		# Create the path network
		self.createGrid(world)
		# Draw the world
		self.drawGrid(self.world.debug)

	### Create the grid
	### self: the navigator object
	### world: the world object
	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None


	def drawGrid(self, surface):
		if self.grid is not None:
			for y in xrange(self.dimensions[1]):
				for x in xrange(self.dimensions[0]):
					if self.grid[x][y]:
						x1 = x * self.cellSize
						y1 = y * self.cellSize
						x2 = (x+1) * self.cellSize
						y2 = (y+1) * self.cellSize
						pygame.draw.line(surface, (0, 255, 0), (x1, y1), (x2, y1), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y1), (x2, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y2), (x1, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x1, y2), (x1, y1), 1)
		return None


class BFSGridNavigator(GridNavigator):
	
	def __init__(self):
		GridNavigator.__init__(self)
	
	
	### Create the grid
	### self: the navigator object
	### world: the world object
	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None
	def computePath(self, source, dest):
		if self.agent != None and self.world != None and self.grid != None:
			self.source = source
			self.destination = dest
			self.agent.moveToTarget(dest)
			start = findClosestCell(source, self.grid, self.cellSize)
			end = findClosestCell(dest, self.grid, self.cellSize)
			path = implementBFS(start, end, self, self.world); 
			if len(path) > 0:
				first = self.path.pop(0)
				if first is not None:
					self.agent.moveToTarget(first)
	
		

	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None


	def drawGrid(self, surface):
		if self.grid is not None:
			for y in xrange(self.dimensions[1]):
				for x in xrange(self.dimensions[0]):
					if self.grid[x][y]:
						x1 = x * self.cellSize
						y1 = y * self.cellSize
						x2 = (x+1) * self.cellSize
						y2 = (y+1) * self.cellSize
						pygame.draw.line(surface, (0, 255, 0), (x1, y1), (x2, y1), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y1), (x2, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y2), (x1, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x1, y2), (x1, y1), 1)
		return None	
	### Called when the agent gets to a node in the path.
	### self: the navigator object

class DFSGridNavigator(GridNavigator):
	
	def __init__(self):
		GridNavigator.__init__(self)
	
	
	### Create the grid
	### self: the navigator object
	### world: the world object
	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None
	def computePath(self, source, dest):
		if self.agent != None and self.world != None and self.grid != None:
			self.source = source
			self.destination = dest
			self.agent.moveToTarget(dest)
			start = findClosestCell(source, self.grid, self.cellSize)
			end = findClosestCell(dest, self.grid, self.cellSize)
			path = implementDFS(start, end, self, self.world); 
			if len(path) > 0:
				first = self.path.pop(0)
				if first is not None:
					self.agent.moveToTarget(first)
	
		

	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None


	def drawGrid(self, surface):
		if self.grid is not None:
			for y in xrange(self.dimensions[1]):
				for x in xrange(self.dimensions[0]):
					if self.grid[x][y]:
						x1 = x * self.cellSize
						y1 = y * self.cellSize
						x2 = (x+1) * self.cellSize
						y2 = (y+1) * self.cellSize
						pygame.draw.line(surface, (0, 255, 0), (x1, y1), (x2, y1), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y1), (x2, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y2), (x1, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x1, y2), (x1, y1), 1)
		return None	
	### Called when the agent gets to a node in the path.
	### self: the navigator object

class BestFirstGridNavigator(GridNavigator):
	
	def __init__(self):
		GridNavigator.__init__(self)
	
	
	### Create the grid
	### self: the navigator object
	### world: the world object
	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None
	def computePath(self, source, dest):
		if self.agent != None and self.world != None and self.grid != None:
			self.source = source
			self.destination = dest
			self.agent.moveToTarget(dest)
			start = findClosestCell(source, self.grid, self.cellSize)
			end = findClosestCell(dest, self.grid, self.cellSize)
			path = implementBestFirst(start, end, self, self.world); 
			if len(path) > 0:
				first = self.path.pop(0)
				if first is not None:
					self.agent.moveToTarget(first)
	
		

	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None


	def drawGrid(self, surface):
		if self.grid is not None:
			for y in xrange(self.dimensions[1]):
				for x in xrange(self.dimensions[0]):
					if self.grid[x][y]:
						x1 = x * self.cellSize
						y1 = y * self.cellSize
						x2 = (x+1) * self.cellSize
						y2 = (y+1) * self.cellSize
						pygame.draw.line(surface, (0, 255, 0), (x1, y1), (x2, y1), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y1), (x2, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y2), (x1, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x1, y2), (x1, y1), 1)
		return None	
	### Called when the agent gets to a node in the path.
	### self: the navigator object



class AstarGridNavigator(GridNavigator):
	
	def __init__(self):
		GridNavigator.__init__(self)
	
	
	### Create the grid
	### self: the navigator object
	### world: the world object
	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None
	def computePath(self, source, dest):
		if self.agent != None and self.world != None and self.grid != None:
			self.source = source
			self.destination = dest
			self.agent.moveToTarget(dest)
			start = findClosestCell(source, self.grid, self.cellSize)
			end = findClosestCell(dest, self.grid, self.cellSize)
			path = implementAstar(start, end, self, self.world); 
			if len(path) > 0:
				first = self.path.pop(0)
				if first is not None:
					self.agent.moveToTarget(first)
	
		

	def createGrid(self, world):
		self.grid, self.dimensions = myCreateGrid(world, self.cellSize)
		return None


	def drawGrid(self, surface):
		if self.grid is not None:
			for y in xrange(self.dimensions[1]):
				for x in xrange(self.dimensions[0]):
					if self.grid[x][y]:
						x1 = x * self.cellSize
						y1 = y * self.cellSize
						x2 = (x+1) * self.cellSize
						y2 = (y+1) * self.cellSize
						pygame.draw.line(surface, (0, 255, 0), (x1, y1), (x2, y1), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y1), (x2, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x2, y2), (x1, y2), 1)
						pygame.draw.line(surface, (0, 255, 0), (x1, y2), (x1, y1), 1)
		return None	
	### Called when the agent gets to a node in the path.
	### self: the navigator object


######################################  PATH FINDING FUNCTIONS #######################################################
def add_class_var(name, *args, **kwrds):
    def decorator(cls):
        setattr(cls, name, cls(*args, **kwrds))
        return cls
    return decorator

class Nodes():
    def __init__(self,p,h):
        self.points=p;
	self.hauristic=h;
    def __repr__(self):
	return repr((self.points, self.hauristic))
Nodes.parent=Nodes((),0);

#BFS Algorithm
def implementBFS(source, dest, self, world):
	last = source;		#update this later 
	current =source;
	path = []; # Should contain the path that you find. Path should be in the form of coords e.g[(1,2), (2,3), (3,4)] with 
				#the first coord as the starting point and the last as your destination
##############################YOUR CODE BELOW HERE############################################
	q=Queue();
	visited=Set();
	c=Nodes(current,0);
	c.parent=c;
	q.push(c);
	while not q.isEmpty():
	    temp=q.pop();
	    current = temp.points;
	    last = temp.parent.points;
	    visited.add(current);
	    if (current!=dest):
		successors = getCellSuccessors(current, self.grid, self.dimensions, last);
		for p in successors:
		    t=Nodes(p,0);
		    t.parent=temp;
		    if (self.grid[p[0]][p[1]]==True and p not in visited):
			q.push(t);
		    pass
		pass
	    else:
		break;
	    pass
	pass
	while temp.points!=source:
	    path.insert(0,temp.points);
	    temp=temp.parent;
###########################YOUR CODE ABOVE HERE ##############################################

	self.setPath(translatePathToCoordinates(path, self.cellSize))
	self.source = source
	self.destination = translateCellToCoordinates(dest, self.cellSize) #stop at the closest cell to the destination

	return path



#DFS Algorithm
def implementDFS(source, dest, self, world):
	last = source;
	current = source;
	path = []; 
##############################YOUR CODE BELOW HERE############################################
	q=Stack();
	visited=Set();
	c=Nodes(current,0);
	c.parent=c;
	q.push(c);
	while not q.isEmpty():
	    temp=q.pop();
	    current = temp.points;
	    last = temp.parent.points;
	    visited.add(current);
	    if (current!=dest):
		successors = getCellSuccessors(current, self.grid, self.dimensions, last);
		for p in successors:
		    t=Nodes(p,0);
		    t.parent=temp;
		    if (self.grid[p[0]][p[1]]==True and p not in visited):
			q.push(t);
		    pass
		pass
	    else:
		break;
	    pass
	pass
	while temp.points!=source:
	    path.insert(0,temp.points);
	    temp=temp.parent;
###########################YOUR CODE ABOVE HERE ##############################################

	self.setPath(translatePathToCoordinates(path, self.cellSize))
	self.source = source
	self.destination = translateCellToCoordinates(dest, self.cellSize) #stop at the closest cell to the destination

	return path

def calHaur(p,d):
    return abs(p[0]-d[0])+abs(p[1]-d[1]);

#BestFirst Algorithm
def implementBestFirst(source, dest, self, world):
	last = source;
	current =last;
	path = [];
	##############################YOUR CODE BELOW HERE############################################
	q=Queue();
	visited=Set();
	c=Nodes(current,calHaur(source,dest));
	c.parent=c;
	q.push(c);
	while not q.isEmpty():
	    temp=q.pop();
	    current = temp.points;
	    last = temp.parent.points;
	    visited.add(current);
	    if (current!=dest):
		successors = getCellSuccessors(current, self.grid, self.dimensions, last);
		for p in successors:
		    t=Nodes(p,calHaur(p,dest));
		    t.parent=temp;
		    if (self.grid[p[0]][p[1]]==True and p not in visited):
			q.push(t);
		    pass
		pass
		q.list=sorted(q.list, key=lambda x: x.hauristic, reverse=True)
	    else:
		break;
	    pass
	pass
	while temp.points!=source:
	    path.insert(0,temp.points);
	    temp=temp.parent;
	###########################YOUR CODE ABOVE HERE #############################################
	
	self.setPath(translatePathToCoordinates(path, self.cellSize))
	self.source = source
	self.destination = translateCellToCoordinates(dest, self.cellSize) #stop at the closest cell to the destination

	return path

#A* Algorithm

def implementAstar(source, dest, self, world):
	last = source;
	current =last;
	path = []; 
##############################YOUR CODE BELOW HERE############################################
	q=Queue();
	visited=Set();
	c=Nodes(current,calHaur(source,dest)+calHaur(source,source));
	c.parent=c;
	q.push(c);
	while not q.isEmpty():
	    temp=q.pop();
	    current = temp.points;
	    last = temp.parent.points;
	    visited.add(current);
	    if (current!=dest):
		successors = getCellSuccessors(current, self.grid, self.dimensions, last);
		for p in successors:
		    t=Nodes(p,calHaur(p,dest)+calHaur(source,source));
		    t.parent=temp;
		    if (self.grid[p[0]][p[1]]==True and p not in visited):
			q.push(t);
		    pass
		pass
		q.list=sorted(q.list, key=lambda x: x.hauristic, reverse=True)
	    else:
		break;
	    pass
	pass
	while temp.points!=source:
	    path.insert(0,temp.points);
	    temp=temp.parent;
###########################YOUR CODE ABOVE HERE ##############################################
	
	self.setPath(translatePathToCoordinates(path, self.cellSize))
	self.source = source
	self.destination = translateCellToCoordinates(dest, self.cellSize) #stop at the closest cell to the destination

	return path
	


###############
### HELPERS

def translateCoordinatesToCell(point, grid, cellsize):
	# I could do this mathematically, but I am lazy.
	best = None
	dist = 0.0
	for x in xrange(len(grid)):
		for y in xrange(len(grid[x])):
			centery = (y * cellsize) + (cellsize/2.0)
			centerx = (x * cellsize) + (cellsize/2.0)
			d = distance(point, (centerx, centery))
			if best is None or d < dist:
				best = (x, y)
				dist = d
	return best

def translateCellToCoordinates(cell, cellsize):
	return ( (cell[0]*cellsize) + (cellsize/2.0), (cell[1]*cellsize) + (cellsize/2.0) )

def findClosestCell(point, grid, cellsize):
	return translateCoordinatesToCell(point, grid, cellsize);

def getCellSuccessors(cell, grid, dimensions, last = None):
	successors = []
	if cell[0] > 0:
		successors.append( (cell[0]-1, cell[1]) )
	if cell[0] < dimensions[0]-1 :
		successors.append( (cell[0]+1, cell[1]) )
	if cell[1] > 0 :
		successors.append( (cell[0], cell[1]-1) )
	if cell[1] < dimensions[1]-1 :
		successors.append( (cell[0], cell[1]+1) )
	if len(successors) > 1 and last is not None and last in successors:
		successors.remove(last)
	return successors


def translatePathToCoordinates(path, cellsize):
	newpath = []
	for cell in path:
		newpath.append(translateCellToCoordinates(cell, cellsize))
	return newpath


