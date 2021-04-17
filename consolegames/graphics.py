import os
from consolegames._win import set_position


class Console:
    def __init__(self, size_x, size_y, textures, mode=2, times_x=1, griglia=None):
        self.size_x = size_x
        self.size_y = size_y
        self.grid = [[None for _ in range(size_x)] for __ in range(size_y)]
        self.textures = textures
        self.times_x = times_x
        if griglia is not None:
            self.size_x = len(griglia[0])
            self.size_y = len(griglia)
            self.grid = griglia

        if os.name in ('nt', 'dos'):
            def clear(): a = os.system('cls')
            self.clear = clear
        elif os.name in ('posix', ''):
            def clear(): a = os.system('clear')
            self.clear = clear
        else:
            def clear(): pass
            self.clear = clear

        if mode == 1:  # I actually don't see the point of using mode 1
            from copy import copy
            self._copy = copy
        elif mode == 2:
            from copy import deepcopy
            self._copy = deepcopy
        else:
            self._copy = lambda x: x

    def refresh_un(self):
        self.clear()
        for row in self.grid:
            for cell in row:
                print(self.textures[cell] * self.times_x, end='')
            print()

    def refresh(self, new_grid):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.grid[y][x] != new_grid[y][x]:
                    set_position(x*self.times_x, y)
                    print(self.textures[new_grid[y][x]] * self.times_x)
        self.grid = self._copy(new_grid)

    def __getitem__(self, item):
        if isinstance(item, int) and item < 0:
            raise IndexError('no negative indexes')
        return self.grid[item]
