# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
      A reflex agent chooses an action at each choice point by examining
      its alternatives via a state evaluation function.

      The code below is provided as a guide.  You are welcome to change
      it in any way you see fit, so long as you don't touch our method
      headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {North, South, West, East, Stop}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = currentGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

	score = successorGameState.getScore()

	#setting the minimum distance pacman should worry at:
	alarm_dist=3;

	#finding distance b/w pacman and ghosts:
	dist_ghost = [ manhattanDistance(newPos, ghostState.getPosition()) for ghostState in newGhostStates if ghostState.scaredTimer == 0 ];
	dist_ghost_ns = [ manhattanDistance(newPos, ghostState.getPosition()) for ghostState in newGhostStates ];
	min_ghost=5;
	min_ghost_ns=min(dist_ghost_ns);
	ghost_Scared=0;
	#Run away code from the active ghosts (putting the action to -inf so it cant be selected):
	if ( len(dist_ghost) > 0 ): 
	    min_ghost = min(dist_ghost);
	else:
	    ghost_Scared=100/min_ghost_ns;
	if ( min_ghost < alarm_dist ):
	    return -(float('inf'));

	#finding distance b/w pacman and remaining food:
	dist_food = [ ( manhattanDistance(newPos, food) ) for food in newFood.asList() ];
	min_food = min(dist_food);
	hurestic=0;

	# putting the action to inf it will be selected if food is near by keeping in view the ghost is not close:
	if (min_food > 0 ): 
	    hurestic = (100/min_food);
	elif (min_food==0):
	    return (float('inf'));

	return ghost_Scared+hurestic + score;

def scoreEvaluationFunction(currentGameState):
    """
      This default evaluation function just returns the score of the state.
      The score is the same one displayed in the Pacman GUI.

      This evaluation function is meant for use with adversarial search agents
      (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
      This class provides some common elements to all of your
      multi-agent searchers.  Any methods defined here will be available
      to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

      You *do not* need to make any changes here, but you can if you want to
      add functionality to all your adversarial search agents.  Please do not
      remove anything, however.

      Note: this is an abstract class: one that should not be instantiated.  It's
      only partially specified, and designed to be extended.  Agent (game.py)
      is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
      Your minimax agent (TASK 2)
    """

    def getAction(self, gameState):
        """
          Returns the minimax action from the current gameState using self.depth
          and self.evaluationFunction.

          Here are some method calls that might be useful when implementing minimax.

          gameState.getLegalActions(agentIndex):
            Returns a list of legal actions for an agent
            agentIndex=0 means Pacman, ghosts are >= 1

          gameState.generateSuccessor(agentIndex, action):
            Returns the successor game state after an agent takes an action

          gameState.getNumAgents():
            Returns the total number of agents in the game
        """
        "*** YOUR CODE HERE ***"
        def pacman_move(state, depth):
            if state.isWin() or state.isLose(): # if the game is over we won't need to check the state
                return state.getScore() # we can just return the score for that state it is our terminal node

            pac_actions = state.getLegalActions(0) # as 0 is for pacman
            best_score = float("-inf")
            score = best_score
            best_action = Directions.STOP

            for action in pac_actions:
                score = max(best_score,ghost_move(state.generateSuccessor(0, action), depth, 1)) # check for the move of 
												 # ghost if pacman does a specific move 
                if score != best_score: # if best_score is changed
                    best_score = score
                    best_action = action

            if depth == 0: # when we get to the top of tree, we return the action to be done
                return best_action
            else: # otherwise when we are yet inside the tree we have to return the score calculated by the 
		  # agent
                return best_score

        def ghost_move(state, depth, ghost):
            if state.isLose() or state.isWin():  # if the game is over we won't need to check the state
                return state.getScore() # we can just return the score for that state it is our terminal node

            actions = state.getLegalActions(ghost)
            best_score = float("inf")
            for action in actions:
                if ghost == state.getNumAgents() - 1: # We are on the last ghost and it will be Pacman's turn next.
						      # as there are state.getNumAgents() - 1 ghosts
                    if depth == self.depth - 1:
			# if we are at leaf
                        best_score = min(best_score,self.evaluationFunction(state.generateSuccessor(ghost, action)))
                    else:
			# if we are somewhere at the middle
                        best_score = min(best_score,pacman_move(state.generateSuccessor(ghost, action), depth + 1))
                else:
                    best_score = min(best_score,ghost_move(state.generateSuccessor(ghost, action), depth, ghost+1))
            return best_score

	# main function code
        return pacman_move(gameState, 0)

class ExpectiminimaxAgent(MultiAgentSearchAgent):
    """
      Your expeciminimax agent (TASK 4)
    """

    def getAction(self, gameState):
        """
          Use your already written code in Task 2 and Task 3 
        """
        "*** YOUR CODE HERE ***"
        def pacman_move(state, depth):
            if state.isWin() or state.isLose(): # if the game is over we won't need to check the state
                return state.getScore() # we can just return the score for that state it is our terminal node

            pac_actions = state.getLegalActions(0) # as 0 is for pacman
            best_score = float("-inf")
            score = best_score
            best_action = Directions.STOP

            for action in pac_actions:
                score = max(best_score,ghost_move_em(state.generateSuccessor(0, action), depth, 1)) # check for the move of 
												 # ghost if pacman does a specific move 
                if score != best_score: # if best_score is changed
                    best_score = score
                    best_action = action

            if depth == 0: # when we get to the top of tree, we return the action to be done
                return best_action
            else: # otherwise when we are yet inside the tree we have to return the score calculated by the agent
                return best_score

        def ghost_move_em(state, depth, ghost): # first ghost do expecti_max
            if state.isLose() or state.isWin():  # if the game is over we won't need to check the state
                return state.getScore() # we can just return the score for that state it is our terminal node

            actions = state.getLegalActions(ghost)
	    successors = [state.generateSuccessor(ghost, action) for action in actions]
	    p = 1.0/len(successors)
            best_score = 0.0
            for successor in successors:
                    best_score += p*ghost_move_mm(successor, depth, ghost+1) # as oly first ghost comes here we dont 
									     # need leef condition 
            return best_score

	def ghost_move_mm(state, depth, ghost): # 2nd ghost do mini_max
            if state.isLose() or state.isWin():  # if the game is over we won't need to check the state
                return state.getScore() # we can just return the score for that state it is our terminal node

            actions = state.getLegalActions(ghost)
            best_score = float("inf")
            for action in actions: # as only last ghost comes here we do not need condition for first one
		if depth == self.depth - 1:
		    best_score = min(best_score,self.evaluationFunction(state.generateSuccessor(ghost, action)))
		else:
		    best_score = min(best_score,pacman_move(state.generateSuccessor(ghost, action), depth + 1))
            return best_score

	# main function code
        return pacman_move(gameState, 0)

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (TASK 3)
    """

    def getAction(self, gameState):
        """
          Returns the expectimax action using self.depth and self.evaluationFunction

          All ghosts should be modeled as choosing uniformly at random from their
          legal moves.
        """
        "*** YOUR CODE HERE ***"
        def pacman_move(state, depth):
            if state.isWin() or state.isLose(): # if the game is over we won't need to check the state
                return state.getScore() # we can just return the score for that state it is our terminal node

            pac_actions = state.getLegalActions(0) # as 0 is for pacman
            best_score = float("-inf")
            score = best_score
            best_action = Directions.STOP

            for action in pac_actions:
                score = max(best_score,ghost_move(state.generateSuccessor(0, action), depth, 1)) # check for the move of 
												 # ghost if pacman does a specific move 
                if score != best_score: # if best_score is changed
                    best_score = score
                    best_action = action

            if depth == 0: # when we get to the top of tree, we return the action to be done
                return best_action
            else: # otherwise when we are yet inside the tree we have to return the score calculated by the 
		  # agent
                return best_score

        def ghost_move(state, depth, ghost):
            if state.isLose() or state.isWin():  # if the game is over we won't need to check the state
                return state.getScore() # we can just return the score for that state it is our terminal node

            actions = state.getLegalActions(ghost)
	    successors = [state.generateSuccessor(ghost, action) for action in actions]
	    p = 1.0/len(successors)
            best_score = 0.0

            for successor in successors:
                if ghost == state.getNumAgents() - 1: # We are on the last ghost and it will be Pacman's turn next.
						      # as there are state.getNumAgents() - 1 ghosts
                    if depth == self.depth - 1:
			# if we are at leaf
                        best_score = p*self.evaluationFunction(successor)
                    else:
			# if we are somewhere at the middle as thsi layer would be for prediction for ghost
                        best_score += p*pacman_move(successor, depth + 1)
                else:
		    
                    best_score += p*ghost_move(successor, depth, ghost+1)
            return best_score

	# main function code
        return pacman_move(gameState, 0)

def betterEvaluationFunction(currentGameState):
    """
      Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
      evaluation function.

      DESCRIPTION: <write something here so we know what you did>
    """
 
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
    """
      Your agent for the mini-contest
    """

    def getAction(self, gameState):
        """
          Returns an action.  You can use any method you want and search to any depth you want.
          Just remember that the mini-contest is timed, so you have to trade off speed and computation.

          Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
          just make a beeline straight towards Pacman (or away from him if they're scared!)
        """
      
        util.raiseNotDefined()

