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


def set_position(x, y, messaggio):
    handle = _getStdHandle(STDOUT)
    position = Coordinates(x, y)
    res = _setPosition(handle, position)
    print(messaggio)
    return res
