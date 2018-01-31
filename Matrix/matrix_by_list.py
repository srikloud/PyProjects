def whzwinr(matrix):
    if ((matrix[0][0] is matrix[0][1]) and (matrix[0][0] is matrix[0][2])):
        print(str(matrix[0][0]) + ": is winner")
        return
    elif matrix[1][0] is matrix[1][1] and matrix[1][0] is matrix[1][2]:
        print(str(matrix[1][0]) + ": is winner")
        return
    elif matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2]:
        print(str(matrix[2][0]) + ": is winner")
        return
    elif matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0]:
        print(str(matrix[0][0]) + ": is winner")
        return
    elif matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1]:
        print(str(matrix[0][1]) + ": is winner")
        return
    elif matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2]:
        print(str(matrix[0][1]) + ": is winner")
        return
    elif matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2]:
        print(str(matrix[0][0]) + ": is winner")
        return
    elif matrix[0][2] == matrix[1][1] and matrix[0][2] == matrix[2][0]:
        print(str(matrix[0][1]) + ": is winner")
        return

def matrix_by_list():
    r = 3
    c = 3

    #matrix = [[None for i in range(r)] for i in range(c)]
    matrix = [['']*r]*c


    print(matrix)
    for i in range(0,c):
        for j in range(0,r):
            print(str(i)+":"+str(j)+" = "+ str(matrix[i][j]))


    b = ''

    print(b == '')

    if matrix[0][1] == matrix[0][2]:
        print("They are same")

    print(1)
    matrix[0][0] = 'X'
    print(2)
    whzwinr(matrix)
    matrix[0][1] = 'Y'
    print(3)
    whzwinr(matrix)
    matrix[0][2] = 'X'
    whzwinr(matrix)
    matrix[1][0] = 'Y'
    whzwinr(matrix)
    matrix[1][1] = 'Y'
    whzwinr(matrix)
    matrix[1][2] = 'X'
    whzwinr(matrix)
    matrix[2][0] = 'Y'
    whzwinr(matrix)
    matrix[2][1] = 'X'
    whzwinr(matrix)
    matrix[2][2] = 'Y'
    whzwinr(matrix)

    print(matrix)


matrix_by_list()