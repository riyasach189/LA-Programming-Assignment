#COMPLETED

"""
Write a program in Python to solve the homogenous system Ax=0 and write the general solution in 
parametric vector form. Your program should accept as input the size of the matrix, i.e. the number 
of rows and the number of columns of A, and also the entries of A. The input should ideally be read 
from a text file, but if you haven't learnt how to do this, you may hard-code your input, as long as 
you are able to explain to your TA how to change the input to your program. Your code should be based 
on algorithms learned in the course. No pre-existing routines from Python libraries should be used.
"""

matrix = []
pivots = []
row_count = 0
column_count = 0
output = "Parametric form:\n"

with open(r"matrix.txt","r") as file:
    input_lst = file.readlines()

s = input_lst[0].replace("\n","")
row_count = int(s)

s = input_lst[1].replace("\n","")
column_count = int(s)

for i in input_lst[2:]:
    s = i.replace("\n","")
    s = [float(elt) for elt in s.split()]
    matrix.append(s)

def row_checker(temp, row, row_count, pivot):
    temp += 1

    if temp>row_count-1:
        temp = row   
        pivot += 1           #start checking next pivot index; start iteration from current row

    return temp, pivot

def rref(matrix, row_count, column_count):

    #step 1: initialize master value of pivot
    #NOTE: Do not put this in inner loops - two branching conditions: find way to deal with both
    #RESOLVED

    pivot = 0  

    #step 2: iterate over all rows
    for row in range(row_count):

        #if index of pivot entry exceeds no. of columns, exit 
        if pivot>column_count-1:
            return matrix

        #step 3: find nearest row with non-zero pivot entry
        #cases - same row 
        #      - no pivot entry of index 'pivot': check index pivot+1
        #      - non-zero pivot in other row: swap with current row

        temp = row       #make temp var; don't alter master 'row' var

        while matrix[temp][pivot]==0:

            temp, pivot = row_checker(temp, row, row_count, pivot)            
          
            if pivot>column_count-1:
                return matrix             #if last column reached, terminate loop

        swap = matrix[temp]
        matrix[temp] = matrix[row]
        matrix[row] = swap

        multiple_row = matrix[row][pivot]
        for entry in range(len(matrix[row])):
            matrix[row][entry] /= multiple_row      #make pivot entry of the current row 1

        for other_row in range(row_count):
            if other_row!=row:
                multiple = matrix[other_row][pivot]/matrix[row][pivot]
                for entry in range(column_count):
                    matrix[other_row][entry] -= matrix[row][entry]*multiple
    
        pivots.append(pivot)
        pivot += 1

    return matrix

flag = True
for i in matrix:
    if flag:
        for j in i:
            if j!=0:
                flag = False

if bool(matrix)==0:
    print(f"RREF: {matrix}")

elif flag==True:
    print(f"RREF: {matrix}")

else:       
    echelon = rref(matrix, row_count, column_count)
    free_vars = [i for i in range(column_count) if i not in pivots]

    for i in echelon:
        for j in range(column_count):
            if str(i[j])=="-0.0":
                i[j] = 0.0

    # print(f"Pivot columns: {pivots}")
    # print(f"Non-pivot columns: {free_vars}")
    print(f"RREF: {echelon}")

    if bool(free_vars)==0:
        print(f"Null Space is {[0 for z in range(column_count)]}")

    else:

        for i in free_vars:
            vector = []

            for j in range(row_count):
                if (matrix[j][i])!=0:
                    vector.append((-1)*(matrix[j][i]))
                else:
                    vector.append(0.0)

            for j in free_vars:
                if i==j:
                    vector.insert(i,1.0)
                else:
                    vector.insert(j,0.0)

            output += (f"x{i+1}{vector[:column_count]} + ")

        output = output[::-1]
        output = output.replace(" +","",1)
        output = output[::-1]

        print(output)