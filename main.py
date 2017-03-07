from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
green = [ 0, 255, 0 ]
red = [255, 0, 0]
edges = [1, 1, 1, 2, 2, 2]
matrix= new_matrix(4, 4)
trans= make_translate(0, 50, 0)
print "trans matrix:"
print_matrix(trans)


add_edge(matrix, 1, 1, 1, 50, 1, 1)
print "your matrix"
print_matrix(matrix)
draw_lines(matrix, screen, green)

matrix_mult(trans, matrix)
print "your matrix translated"
print_matrix(matrix)

draw_lines(matrix, screen, red)

display(screen)

#parse_file( 'script', edges, transform, screen, color )
