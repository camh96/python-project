from Ship import Ship
from Grid import Grid
from Command import Command
from itertools import chain
from Welcome import Welcome


def get_command():

	Command().get_user_input()

Welcome.welcome_user()
get_command()