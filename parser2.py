from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    edge_matrix= new_matrix(4,4)
    trans= new_matrix(4, 4)
    trans= transform
    scale= new_matrix(4,4)
    move= new_matrix(4,4)
    rot= new_matrix(4,4)
    
    f = open(fname, "r")

    for x in range(len(points)/3):
        add_point(edge_matrix, points[x * 3], points[x * 3]+1, points[x * 3] + 2)


    command= f.readline().strip()
    
    while (command!= ""):
        if command == "line":
            print "command is line"
            point= f.readline().strip().split(" ")
            #print "here are the points:"
            #print point
            add_edge(edge_matrix,int(point[0]),int(point[1]),int(point[2]),int(point[3]),int(point[4]),int(point[5]))
        elif command == "ident":
            print "command is ident"
            ident(trans)
        elif command == "scale":
            print "command is scale"
            scales= f.readline().strip().split(" ")
            #print "here are the scales"
            #print scales
            scale= make_scale(int(scales[0]), int(scales[1]), int(scales[2]))
            matrix_mult(scale, trans)
        elif command == "move":
            print "command is move"
            moves= f.readline().strip().split(" ")
            move= make_translate(int(moves[0]), int(moves[1]), int(moves[2]))
            #print "here are the moves"
            #print moves
            matrix_mult(move, trans)
        elif command == "rotate":
            print "command is rotate"
            rots= f.readline().strip().split(" ")
            if rots[0] == "x":
                print "rotate about x by "+ str(rots[1])
                rot= make_rotX(rots[1])
            elif rots[0] == "y":
                print "rotate about y by "+ str(rots[1])
                rot= make_rotY(rots[1])
            elif rots[0] == "z":
                print "rotate about z by "+ str(rots[1])
                rot= make_rotZ(rots[1])

            print "multiplying matrices"
            print rot
            print trans
            matrix_mult(rot, trans)
        elif command == "apply":
            print "command is apply"
            matrix_mult(trans, edge_matrix)
        elif command == "display":
            print "command is display"
            draw_lines(edge_matrix, screen, color)
            display(screen)
        elif command == "save":
            print "command is save"
            name= f.readline()
            draw_lines(edge_matrix, screen, color)
            save_ppm(screen, name)
            save_extention(screen, name)
        elif command == "quit":
            print "command is quit"
            break
        print "this is current edge matrix"
        print_matrix(edge_matrix)
        print "this is current transform matrix"
        print_matrix(trans)
        command= f.readline().strip()

    print "done"
