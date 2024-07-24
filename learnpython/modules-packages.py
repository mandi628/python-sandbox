# Module is a piece of software that has a specific functionality.
# For example, when building a ping pong game, one module may be reponsible for the game logic,
# and another module draws the game on the screen. Each module consists of a different file,
# which may be edited separately.

# game.py
# import the draw module
import draw

def play_game():
	...

def main():
	result = play_game()
	draw.draw_game(result)

# this means that if this script is executed, then main() will be executed
if __name__ == '__main__':
	main()

# The draw module may look something like this:

# draw.py

def draw_game():
	...

def clear_screen(screen):
	...

# In this example, the game module imports the draw module, which enables it to use
# functions implemented in that module. The main function uses the local function
# play_game to run the game, and thend raws the result of the game using a function
# implemented in the draw module called draw_game. To use the function draw_game from
# the draw module, we need to specify in which module the function is implemented,
# using the dot operator. To reference the draw_game function from the game module,
# we need to import the draw module and then call draw.draw_game().

# When the import_draw directive runs, the Python interpreter looks for a file in the
# directory in which the script was executed with the module name and a .py suffix.
# In this case it will look for draw.py. If it is found, it will be imported. If it's
# not found, it will continue looking for built-in modules.

# You may have noticed that when importing a module, a .pyc file is created. This is a
# compiled Python file. Python compiles files into Python bytecode so that it won't
# have to parse the files each time modules are loaded. If a .pyc file exist, it gets
# loaded instead of the .py file. This process is transparent to the user.

# A namespace is a system where every object is named and can be accessed in Python.
# We import the function draw_game into the main script's namespace by uning the
# from command.

# game.py
# import the draw module
from draw import draw_game

def main():
	result = play_game()
	draw_game(result)
# By using this version, we don't have to specify the location of the draw_game module.

# You can also use the import * command to import all the objects in a module

# game.py
# import the draw module
from draw import *

def main():
	result = play_game()
	draw_game(result)

# You can also use cutom names for modules.

# game.py
# import the draw module
if visual_mode:
	# in vidual mode, we draw using graphics
	import draw_visual as draw
ele:
	# in textual mode, we print out text
	import draw_textual as draw

def main():
	result = play_game()
	# this can either be visual or textual depending on visual_mode
	draw.draw_game(result)


