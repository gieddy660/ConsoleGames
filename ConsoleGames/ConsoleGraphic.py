import os
if os.name == 'nt':
    from ConsoleGames._ntConsole import set_position
elif os.name == 'posix':
    from ConsoleGames._posixConsole import set_position
else:
    def set_position(x, y):
        pass

class Console:
    def __init__(self, size_x, size_y, textures, mode=0, times_x=1, griglia=None):
        self.size_x = size_x
        self.size_y = size_y
        self.griglia = [[None for _ in range(size_x)] for __ in range(size_y)]
        self.textures = textures
        self.times_x = times_x
        if griglia is not None:
            self.size_x = len(griglia[0])
            self.size_y = len(griglia)
            self.griglia = griglia

        if os.name == 'nt':
            def clear(): a = os.system('cls')
            self.clear = clear
        elif os.name == 'posix':
            def clear(): a = os.system('clear')
            self.clear = clear
        else:
            def clear(): print('\n'*50)
            self.clear = clear

        if mode == 0:
            from copy import deepcopy
            self._copy = deepcopy
        elif mode == 1:  # I actually don't see the point of using mode 1
            from copy import copy
            self._copy = copy
        else:  # nor anything that isn't mode 0
            self._copy = lambda x: x

    def refresh_un(self, new_griglia=None):
        if new_griglia is not None:
            self.griglia = new_griglia
        self.clear()
        for row in self.griglia:
            for cell in row:
                print(self.textures[cell] * self.times_x, end='')
            print()

    def refresh(self, new_griglia):
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.griglia[y][x] != new_griglia[y][x]:
                    set_position(x*self.times_x, y, self.textures[new_griglia[y][x]]*self.times_x)
        self.griglia = self._copy(new_griglia)

    def __getitem__(self, item):
        if isinstance(item, int) and item < 0:
            raise IndexError('no negative indexes')
        return self.griglia[item]


def test():
    """test"""
    from time import sleep
    textures = {None: " ", 0: "#", 1: "-"}
    griglia = [[0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]]
    f = Console(6, 3, textures, griglia=griglia)
    f.refresh_un()
    while True:
        for _ in range(1, 5):
            griglia[1][1:_] = [1] * _
            f.refresh(griglia)
            sleep(0.8)
        griglia[1] = [0, 0, 0, 0, 0, 0]
        f.refresh(griglia)
