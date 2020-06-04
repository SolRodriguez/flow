###INITIALIZES FLOW GAME###


class Game():  # dont know if actually useful

    def __init__(self, board):
        self.board = board


class Board():

    def __init__(self, sizex, sizey):
        # TODO: x and y should be ints- add ways to catch that
        self.x = int(sizex)
        self.y = int(sizey)
        self.mtrx = [['0' for x in range(self.x)] for y in range(
            self.y)]  # to help visualize in the meantime
        self.best = 0  # same as current number or flows
        self.flows = set()
        self.occupied = set()  # tentative

    def size(self):
        return self.x * self.y
    # TODO: Find max and min number of color pairs

    def maxflow(self):
        # can have as many pairs as largest dimension
        return max(self.x, self.y)

    def minflow(self):
        # should have at least 2 less pairs than the smallest dimension
        return min(self.x, self.y)-2

    # TODO: add flow nodes- check they're not placed in existing dots-if so ask, move, otherwise del?
    def valid_flow(self, flow):
        # new flow and in available coordinates!
        if flow not in self.flows and (flow.start not in self.occupied) and (flow.end not in self.occupied):
            return True
        else:
            return False

    def have_space(self):
        #within bounds of number of flows we can add (based on board dimensions)
        if self.minflow() <= self.best < self.maxflow():
            return True
        else:
            return False

    def set_flow(self, flow):
        if self.valid_flow(flow) and self.have_space():
            self.flows.add(flow)
            self.occupied.add(flow.start)
            self.occupied.add(flow.end)
            self.best += 1

        else:
            raise InvalidFlow

    # TODO: find way to render board- colors T-T

class Flow():

    def __init__(self, start, end):  # actually arbitrary, but for order's sake
        self.start = start
        self.end = end

    # TODO: hopefully give each flow a unique color ^-^

class InvalidFlow(Exception): #credit to StephenFordham's MyCustomError
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'Invalid Flow, {0} '.format(self.message)
        else:
            return 'Invalid Flow'
