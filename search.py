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
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start'child successors:", problem.getSuccessors(problem.getStartState()))
    """

    # print("Start:",                 problem.getStartState())
    # print("Is the start a goal?",   problem.isGoalState(problem.getStartState()))
    # print("Start'child successors:",    problem.getSuccessors(problem.getStartState()))

    """frontier = util.Stack()
    visited = set()

    frontier.push(problem.getStartState(), list())

    if problem.isGoalState(problem.getStartState()):
        temp = []
        temp[0] = problem.getStartState()
        return temp[0]

    else:
    while not frontier.isEmpty():
        currentNode = frontier.pop()
        if problem.isGoalState(currentNode[0]): return currentNode[1]
            # print("NOT FOUND")
        visited.add(currentNode[0])
        successor = problem.getSuccessors(currentNode[0])
        for child in successor:
            # print(child)
            if child[0] not in visited:
                current_route = list(currentNode[1])
                current_route.append(child[1])
                frontier.push(child[0])

    # return list()
    util.raiseNotDefined()
    return list()"""

    frontier = util.Stack()  # A helper stack of (state,route_to_state)
    visited = set()  # A set of state recording the explored nodes

    if problem.isGoalState(problem.getStartState()):
        return problem.getStartState
    else:
        frontier.push((problem.getStartState(), list()))

        while not frontier.isEmpty():
            curState = frontier.pop()
            if problem.isGoalState(curState[0]):
                # print("Node found)
                return curState[1]
            else:
                visited.add(curState[0])
                successors = problem.getSuccessors(curState[0])
                for child in successors:
                    # print(child)
                    if child[0] not in visited:
                        current_route = list(curState[1])
                        current_route.append(child[1])
                        frontier.push((child[0], current_route))

    #print("No route found!")

    util.raiseNotDefined()
    return list()


def isInFrontier(frontierQueue, item):
    if item not in frontierQueue:
        return True
    else:
        return False


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    frontier = util.Queue()  # A helper stack of (state,route_to_state)
    visited = set()  # A set of state recording the explored nodes

    if problem.isGoalState(problem.getStartState()):
        return problem.getStartState
    else:
        frontier.push((problem.getStartState(), list()))

        while not frontier.isEmpty():
            curState = frontier.pop()
            if problem.isGoalState(curState[0]):
                # print("Node found)
                return curState[1]
            else:
                if curState[0] not in visited:
                    visited.add(curState[0])
                    successors = problem.getSuccessors(curState[0])
                    for child in successors:
                        # print(child)
                        if child[0] not in visited:
                            current_route = list(curState[1])
                            current_route.append(child[1])
                            frontier.push((child[0], current_route))


"""def breadthFirstSearch(problem):
    frontier = util.Queue()  # A helper stack of (state,route_to_state)
    frontierCopy = set()
    visited = set()  # A set of state recording the explored nodes

    if problem.isGoalState(problem.getStartState()):
        return problem.getStartState
    else:
        frontier.push((problem.getStartState(), list()))
        frontierCopy.add(problem.getStartState)

        while not frontier.isEmpty():
            curState = frontier.pop()
            frontierCopy.pop()
            if problem.isGoalState(curState[0]):
                # print("Node found)
                return curState[1]
            else:
                visited.add(curState[0])
                successors = problem.getSuccessors(curState[0])
                for child in successors:
                    # print(child)
                    if child[0] not in visited and isInFrontier(frontierCopy, child[0]):
                        current_route = list(curState[1])
                        current_route.append(child[1])
                        frontier.push((child[0], current_route))
                        frontierCopy.add(child[0])

    #print("No route found!")

    util.raiseNotDefined()
    return list()"""


def uniformCostSearch(problem):

    frontier = util.PriorityQueue()  # A helper stack of (state,route_to_state)
    visited = set()  # A set of state recording the explored nodes

    if problem.isGoalState(problem.getStartState()):
        return problem.getStartState
    else:
        frontier.push((problem.getStartState(), list()), 0)

        while not frontier.isEmpty():
            curState = frontier.pop()
            if problem.isGoalState(curState[0]):
                # print("Node found)
                return curState[1]
            else:
                if curState[0] not in visited:
                    visited.add(curState[0])
                    successors = problem.getSuccessors(curState[0])
                    for child in successors:
                        # print(child)
                        current_route = list(curState[1])
                        current_route.append(child[1])
                        frontier.update((child[0], current_route),
                                        problem.getCostOfActions(current_route) + child[2])
                        # print(child)


def isInFrontierCost(frontierQueue, item):
    for elem in frontierQueue:
        if elem[0] == item[0] and elem[2] >= item[2]:
            frontierQueue.remove(elem)
            frontierQueue.add(0, item)
            return True
        else:
            return False


def calcTotCost(frontier, explored, actions):
    cost = 0
    for item in frontier:
        if item[0] in actions:
            cost += item[2]

    for item in explored:
        if item[0] in actions:
            cost += item[2]

    return cost


def makeList(visited, nodeHistory):
    """  parse list from node actions
    convert set
    use string comp to reverse string"""


"""def uniformCostSearch(problem):
    startState = problem.getStartState()
    frontier = util.PriorityQueue()  # A helper stack of (state,route_to_state)
    frontierCopy = set()
    visited = util.Stack()  # A set of state recording the explored nodes
    visitedCopy = set()
    pathCost = dict()

    if problem.isGoalState(startState):
        return problem.getStartState
    else:
        frontier.push((startState, '', 0), 0)
        frontierCopy.add(startState)
        pathCost[startState] = list(startState)

        while not frontier.isEmpty():
            curState = frontier.pop()
            frontierCopy.remove(curState[0])

            if problem.isGoalState(curState[0]):
                # print("Node found)
                return curState[1]
            else:
                visitedCopy.add(curState[0])
                visited.push(curState[0])
                successors = problem.getSuccessors(curState[0])

                for child in successors:
                    if child[0] not in visitedCopy and not isInFrontier(frontierCopy, child[0]):
                        # print(child)
                        # old list
                        current_route = list(curState[1])
                        current_route.append(child[1])
                        # new list
                        parentActions = pathCost[curState]
                        parentActions.append(child[0])
                        pathCost[child[0]] = parentActions

                        tempCost = calcTotCost(frontierCopy, visitedCopy, pathCost)
                        frontierCopy.add(child)
                        totalCost = tempCost + child[2]
                        frontier.push(child, totalCost)

                    elif isInFrontierCost(frontierCopy, child[0]):
                        # old list
                        current_route = list(curState[1])
                        current_route.append(child[1])
                        # new list
                        parentActions = pathCost[curState]
                        parentActions.append(child[0])
                        pathCost[child[0]] = parentActions

                        tempCost = calcTotCost(frontierCopy, visitedCopy, pathCost)
                        totalCost = tempCost + child[2]
                        frontier.update(child, totalCost)
                makeList(visitedCopy,parentActions)




    # print("No route found!")

    util.raiseNotDefined()
    return list()"""


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    frontier = util.PriorityQueue()  # A helper stack of (state,route_to_state)
    visited = set()  # A set of state recording the explored nodes

    if problem.isGoalState(problem.getStartState()):
        return problem.getStartState
    else:
        frontier.push((problem.getStartState(), list()), 0)

        while not frontier.isEmpty():
            curState = frontier.pop()
            if problem.isGoalState(curState[0]):
                # print("Node found)
                return curState[1]
            else:
                if curState[0] not in visited:
                    visited.add(curState[0])
                    successors = problem.getSuccessors(curState[0])
                    for child in successors:
                        # print(child)
                        if child[0] not in visited:
                            current_route = list(curState[1])
                            current_route.append(child[1])
                            frontier.update((child[0], current_route),
                                            problem.getCostOfActions(current_route) + heuristic(child[0], problem))
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
