#!/usr/bin/env python

from pprint import pprint
import re
import sys
import math


class SystemStack(object):

    def __init__(self):
        self.stack = ['------------']

    def pop(self):
        self.stack.pop()

    def push(self, elem):
        self.stack.append(elem)

    def display(self):
        for x in reversed(self.stack):
            print(x)

SYSTEM_STACK = SystemStack()


class Grid(object):

    def __init__(self, n):
        self.size = 2**n

        # First generate all of the vertices
        self.vertices = [i for i in range(1, self.size**2+1)]

        # Second generate all of the edges (all horizontal and vertical edges allowable in a grid)
        self.edges = []
        for i in range(1, self.size+1):
            for j in range(1, self.size):
                self.edges.append((j+(i-1)*self.size, j+(i-1)*self.size+1))

        for i in range(1, self.size):
            for j in range(1, self.size+1):
                self.edges.append((j+(i-1)*self.size, j+i*self.size))

    def display(self):
        for i in range(self.size):
            if i > 0:
                for j in range(self.size):
                    if j > 0:
                        sys.stdout.write('   ')
                    if (self.size * (i - 1) + j + 1, self.size * i + j + 1) in self.edges:
                        sys.stdout.write(' | ')
                    else:
                        sys.stdout.write('   ')
                print()
            for j in range(self.size):
                if j > 0:
                    if (self.size * i + j, self.size * i + j + 1) in self.edges:
                        sys.stdout.write(' - ')
                    else:
                        sys.stdout.write('   ')
                sys.stdout.write(' * ')
            print()

    def savitch(self, u, v, i):
        SYSTEM_STACK.push('R({},{},{})'.format(u,v,i))
        SYSTEM_STACK.display()

        if i == 0:
            if u == v:
                SYSTEM_STACK.pop()
                SYSTEM_STACK.push('T')
                return True
            elif (u, v) in self.edges:
                SYSTEM_STACK.pop()
                SYSTEM_STACK.push('T')
                return True
        else:
            for w in self.vertices:
                if self.savitch(u, w, i-1) and self.savitch(w, v, i-1):
                    SYSTEM_STACK.pop()
                    SYSTEM_STACK.pop()
                    SYSTEM_STACK.pop()
                    SYSTEM_STACK.push('T')
                    return True
        SYSTEM_STACK.pop()
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        grid = Grid(sys.argv[1])
    else:
        grid = Grid(int(input("Grid Size: ")))
    grid.display()
    print(grid.savitch(1, grid.size**2, grid.size))
