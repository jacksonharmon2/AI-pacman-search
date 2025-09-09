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

# search.py

def depthFirstSearch(problem):
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
    HIT_MAX = 2
    start = problem.getStartState()

    fringe = util.Stack()
    # node = (state, actions, hits)
    hits0 = 1 if problem.isWall(start) else 0
    fringe.push((start, [], hits0))
    visited = set()  # (state, hits)

    while not fringe.isEmpty():
        state, actions, hits = fringe.pop()
        key = (state, hits)
        if key in visited:
            continue
        visited.add(key)

        if problem.isGoalState(state) and 1 <= hits <= HIT_MAX:
            return actions

        for succ, act, step in problem.getSuccessors(state):
            nhits = hits + (1 if problem.isWall(succ) else 0)
            if nhits <= HIT_MAX and (succ, nhits) not in visited:
                fringe.push((succ, actions + [act], nhits))
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    HIT_MAX = 2
    start = problem.getStartState()

    fringe = util.Queue()
    hits0 = 1 if problem.isWall(start) else 0
    fringe.push((start, [], hits0))
    visited = {(start, hits0)}  # mark on enqueue

    while not fringe.isEmpty():
        state, actions, hits = fringe.pop()

        if problem.isGoalState(state) and 1 <= hits <= HIT_MAX:
            return actions

        for succ, act, step in problem.getSuccessors(state):
            nhits = hits + (1 if problem.isWall(succ) else 0)
            key = (succ, nhits)
            if nhits <= HIT_MAX and key not in visited:
                visited.add(key)
                fringe.push((succ, actions + [act], nhits))
    return []
    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    HIT_MAX = 2
    start = problem.getStartState()

    fringe = util.PriorityQueue()
    g0 = 0
    hits0 = 1 if problem.isWall(start) else 0
    # item = (state, actions, g, hits) with priority g
    fringe.push((start, [], g0, hits0), g0)
    best_g = {(start, hits0): g0}

    while not fringe.isEmpty():
        state, actions, g, hits = fringe.pop()
        key = (state, hits)
        if g > best_g.get(key, float('inf')):
            continue

        if problem.isGoalState(state) and 1 <= hits <= HIT_MAX:
            return actions

        for succ, act, step in problem.getSuccessors(state):
            nhits = hits + (1 if problem.isWall(succ) else 0)
            if nhits > HIT_MAX:
                continue
            ng = g + step
            skey = (succ, nhits)
            if ng < best_g.get(skey, float('inf')):
                best_g[skey] = ng
                fringe.push((succ, actions + [act], ng, nhits), ng)
    return []
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    HIT_MAX = 2
    start = problem.getStartState()

    fringe = util.PriorityQueue()
    g0 = 0
    hits0 = 1 if problem.isWall(start) else 0
    f0 = g0 + heuristic(start, problem)
    # item = (state, actions, g, hits) with priority f = g + h
    fringe.push((start, [], g0, hits0), f0)
    best_g = {(start, hits0): g0}

    while not fringe.isEmpty():
        state, actions, g, hits = fringe.pop()
        key = (state, hits)
        if g > best_g.get(key, float('inf')):
            continue

        if problem.isGoalState(state) and 1 <= hits <= HIT_MAX:
            return actions

        for succ, act, step in problem.getSuccessors(state):
            nhits = hits + (1 if problem.isWall(succ) else 0)
            if nhits > HIT_MAX:
                continue
            ng = g + step
            skey = (succ, nhits)
            if ng < best_g.get(skey, float('inf')):
                best_g[skey] = ng
                f = ng + heuristic(succ, problem)
                fringe.push((succ, actions + [act], ng, nhits), f)
    return []
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch