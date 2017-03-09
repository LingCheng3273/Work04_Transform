from display import *
from draw import *
from parser2 import *
from matrix import *

screen = new_screen()
color = [0, 255, 0]
red = [255, 0, 0]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )