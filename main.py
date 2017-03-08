from display import *
from draw import *
from parser2 import *
from matrix import *

screen = new_screen()
color = [0, 0, 0]
edges = [1, 1, 1, 51, 1, 1]
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )

#------------------------------------------------
##matrix= new_matrix(4, 4)
##trans= make_translate(100,100, 0)
##scale= make_scale(2, 2, 2)
##rotx= make_rotX(45)
##
##    
##print "trans matrix:"
##print_matrix(trans)
##
##add_edge(matrix, 1, 1, 1, 51, 1, 1)
##add_edge(matrix, 51, 1, 1, 51, 51, 1)
##add_edge(matrix, 51, 51, 1, 1, 51, 1)
##add_edge(matrix, 1, 51, 1, 1, 1, 1)
##
##print "your matrix"
##print_matrix(matrix)
##draw_lines(matrix, screen, green)
##
##matrix_mult(trans, matrix)
##print "your matrix translated"
##print_matrix(matrix)
##draw_lines(matrix, screen, red)
##
##
##matrix_mult(scale, matrix)
##print "your matrix scaled"
##print_matrix(matrix)
##draw_lines(matrix, screen, blue)
##
##
##
display(screen)
#parse_file( 'script', edges, transform, screen, color )
