import math

def make_translate( x, y, z ):
    trans= new_matrix(4,4)
    ident(trans)
    trans[3][0]=x
    trans[3][1]=y
    trans[3][2]=z
    return trans
    
def make_scale( x, y, z ):
    scale= new_matrix(4,4)
    ident(scale)
    scale[0][0]=x
    scale[1][1]=y
    scale[2][2]=z
    return scale

def make_rotX( theta ):
    theta= float(theta)
    theta= math.radians(theta)
    rotX= new_matrix(4, 4)
    ident(rotX)
    rotX[1][1]= int(math.ceil(math.cos(theta)))
    rotX[2][1]= -1 * int(math.ceil(math.sin(theta)))
    rotX[1][2]= int(math.ceil(math.sin(theta)))
    rotX[2][2]= int(math.ceil(math.cos(theta)))
    return rotX

def make_rotY( theta ):
    theta= float(theta)
    theta= math.radians(theta)
    rotY= new_matrix(4, 4)
    ident(rotY)
    rotY[0][0]= int(math.ceil(math.cos(theta)))
    rotY[2][0]= int(math.ceil(math.sin(theta)))
    rotY[0][2]= -1 * int(math.ceil(math.sin(theta)))
    rotY[2][2]= int(math.ceil(math.cos(theta)))
    return rotY

def make_rotZ( theta ):
    theta= float(theta)
    theta= math.radians(theta)
    rotZ= new_matrix(4, 4)
    ident(rotZ)
    rotZ[0][0]= int(math.ceil(math.cos(theta)))
    rotZ[1][0]= -1 * int(math.ceil(math.sin(theta)))
    rotZ[0][1]= int(math.ceil(math.sin(theta)))
    rotZ[1][1]= int(math.ceil(math.cos(theta)))
    return rotZ

def print_matrix( matrix ):
    s = ''
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            s+= str(matrix[c][r]) + ' '
        s+= '\n'
    print s

def ident( matrix ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            if r == c:
                matrix[c][r] = 1
            else:
                matrix[c][r] = 0

def scalar_mult( matrix, s ):
    for r in range( len( matrix[0] ) ):
        for c in range( len(matrix) ):
            matrix[c][r]*= s
            
#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    point = 0
    for row in m2:
        #get a copy of the next point
        tmp = row[:]
        
        for r in range(4):
            m2[point][r] = (m1[0][r] * tmp[0] +
                            m1[1][r] * tmp[1] +
                            m1[2][r] * tmp[2] +
                            m1[3][r] * tmp[3])
        point+= 1


def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
