# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    start = problem.getStartState()
    cost = 0
    direction = []
    path = ([start], direction, cost)
    if problem.isGoalState(problem.getStartState()):
        return direction
    stack = util.Stack()
    stack.push(path)


    while not stack.isEmpty():
        cur_path = stack.pop()
        cur_node = cur_path[0][-1]
        if problem.isGoalState(cur_node):
            return cur_path[1]
        else:
            successors = problem.getSuccessors(cur_node)
            for successor in successors:
                next_node = successor[0]
                next_direction = successor[1]
                next_cost = successor[2]
                if next_node not in cur_path[0]:
                    new_node = cur_path[0][:]
                    new_node.append(next_node)
                    new_direction = cur_path[1][:]
                    new_direction.append(next_direction)
                    new_cost = cur_path[2]
                    new_cost += next_cost

                stack.push((new_node, new_direction, new_cost))
    return []
    
    
    
    
def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visited = []
    start = problem.getStartState()
    cost = 0
    direction = []
    path = ([start], direction, cost)
    visited.append(start)

    queue = util.Queue()
    queue.push(path)

    while not queue.isEmpty():
        cur_path = queue.pop()
        cur_node = cur_path[0][-1]
        if problem.isGoalState(cur_node):
            return cur_path[1]
        else:
            successors = problem.getSuccessors(cur_node)
            for successor in successors:
                next_node = successor[0]
                next_direction = successor[1]
                next_cost = successor[2]
                if next_node not in visited:
                    visited.append(next_node)
                    new_node = cur_path[0][:]
                    new_node.append(next_node)
                    new_direction = cur_path[1][:]
                    new_direction.append(next_direction)
                    new_cost = cur_path[2]
                    new_cost += next_cost
                    queue.push((new_node, new_direction, new_cost))
    return []
    

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visited = []
    start = problem.getStartState()
    cost = 0
    direction = []
    path = ([start], direction, cost)
    visited.append(start)

    queue = util.PriorityQueue()
    queue.push(path, 0)

    while not queue.isEmpty():
        cur_path = queue.pop()
        cur_node = cur_path[0][-1]
        if problem.isGoalState(cur_node):
            return cur_path[1]
        else:
            successors = problem.getSuccessors(cur_node)
            for successor in successors:
                next_node = successor[0]
                next_direction = successor[1]
                next_cost = successor[2]
                if next_node not in visited:
                    if not problem.isGoalState(next_node):
                        visited.append(next_node)
                        


                    
                    new_node = cur_path[0][:]
                    new_node.append(next_node)
                    new_direction = cur_path[1][:]
                    new_direction.append(next_direction)
                    new_cost = cur_path[2]
                    new_cost +=next_cost
                    queue.push((new_node, new_direction, new_cost), new_cost)
    return []

    

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visited_cost = {}
    start = problem.getStartState()
    cost = 0
    direction = []
    path = ([start], direction, cost)
    visited_cost[start] = 0

    queue = util.PriorityQueue()
    queue.push(path, 0)

    while not queue.isEmpty():
        cur_path = queue.pop()
        cur_node = cur_path[0][-1]
        if problem.isGoalState(cur_node):
            return cur_path[1]
        else:
            successors = problem.getSuccessors(cur_node)
            for successor in successors:
                next_node = successor[0]
                next_direction = successor[1]
                next_cost = successor[2]
                new_cost = cur_path[2]
                new_cost += next_cost


                if next_node not in visited_cost or new_cost < visited_cost[next_node]:
                    if not problem.isGoalState(next_node):
                        visited_cost[next_node] = new_cost
                        


                    
                    new_node = cur_path[0][:]
                    new_node.append(next_node)
                    new_direction = cur_path[1][:]
                    new_direction.append(next_direction)
                    
                    hn = heuristic(next_node, problem)
                    queue.push((new_node, new_direction, new_cost), new_cost+hn)
    return []

   


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
