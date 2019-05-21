# alternate solution without using re

class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = list()
        rows = matrix_string.split("\n")
        for row in rows:
            self.matrix.append([int(n) for n in row.split(" ")])

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]