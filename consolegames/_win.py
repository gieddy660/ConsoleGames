"""inspired by colorama"""
from ctypes import windll
from ctypes import wintypes

STDOUT = -11

Coordinates = wintypes._COORD
Handle = wintypes.HANDLE

_getStdHandle = windll.kernel32.GetStdHandle
_getStdHandle.argtypes = [wintypes.DWORD]
_getStdHandle.restype = Handle

_setPosition = windll.kernel32.SetConsoleCursorPosition
_setPosition.argtypes = [Handle, Coordinates]
_setPosition.restype = wintypes.BOOL


def set_position(x, y):
    handle = _getStdHandle(STDOUT)
    position = Coordinates(x, y)
    return _setPosition(handle, position)


if __name__ == '__main__':
    from time import sleep
    from os import system

    while True:
        a = system('cls')
        print('######\n' * 3)
        for _ in range(1, 5):
            sleep(1)
            f = set_position(_, 1)
            print('-')
        sleep(1)
