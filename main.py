from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = [1, 1, 1, 2, 2, 2]
transform = new_matrix(1, 1)
matrix= new_matrix(1, 1)

add_edge(transform, 1, 1, 1, 2, 2, 2)
print_matrix(transform)

#parse_file( 'script', edges, transform, screen, color )
