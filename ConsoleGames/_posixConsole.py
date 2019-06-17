from os import system


def set_position(x, y, messaggio):
    t = system('echo "$(tput cup %s %s)%s"' % (y, x, messaggio))
