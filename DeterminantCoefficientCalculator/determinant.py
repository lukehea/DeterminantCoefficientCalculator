def main():
    matrix = []
    while True:
        #displays current matrix, takes in space seperated row and breaks into new list
        print("Current matrix: ")
        displayMatrix(matrix)
        newRow = input("enter next row (space seperated): ").split(sep=' ')

        #store current matrix length and new row length
        matrLength = len(matrix)
        rowLength = len(newRow)
        
        #if there is already rows in the matrix, store matrix width and check if the new row is same length as first row
        #if not skip input b/c all rows must be same length in a matrix
        if matrLength > 0:
            matrWidth = len(matrix[0])
            if rowLength != len(matrix[0]):
                print("all rows must be same length")
                continue
        
        #try casting all elements of new row to int
        #if it throws a value error skip the input, all entries must be int
        try:
            list(map(int, newRow))
        except ValueError:
            print("invalid input in row")
            continue
                
        #add new row to matrix if it passes all checks
        matrix.append(newRow)
        
        #once num of rows equals num of cols, matrix is square so exit loop
        if len(matrix) == len(matrix[0]):
            break
    
    print("Determinant of: ")
    displayMatrix(matrix)
    print(f"is {getDeterminant(matrix)}")

#finds the determinant of a given n by n matrix where n>=2
def getDeterminant(matrix: list) -> int:
    
    #gets the row count of the matrix, then checks base cases of 1 x 1, 2 x 2 and 3 x 3 matrices
    matrLength = len(matrix)
    if matrLength == 1:
        return matrix[0][0]
    if matrLength == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    if matrLength == 3:
        return (matrix[0][0]*matrix[1][1]*matrix[2][2]) + (matrix[0][1]*matrix[1][2]*matrix[2][0]) + (matrix[0][2]*matrix[1][0]*matrix[2][1]) - ((matrix[2][0]*matrix[1][1]*matrix[0][2]) + (matrix[2][1]*matrix[1][2]*matrix[0][0]) + (matrix[2][2]*matrix[1][0]*matrix[0][1]))
    
    #initializes the determinant as 0 and gets the base tuple and matrix transpose
    transMatrix = list(map(list, zip(*matrix)))
    deter = 0
    base = findBase(matrix, transMatrix)
    
    #checks if the matrix needs to be transposed, 
    if base[1]:
        matrix = transMatrix
    base = base[0]
    
    #iterates over all columns of the matrix
    for i in range(0, matrLength):
        
        #next addition to the determinant will multiply by this entry
        #if this entry is 0 the calculation is trivial
        if matrix[base][i] == 0:
            continue
        
        #reinitializes the submatrix each loop
        subMatrix = []
        
        #iterates over all rows up to base, then all rows after base to remove the base row
        #for each iteration, adds the row up to i and after to remove the current column
        #this creates the submatrix necessary for the next recursion in the determinant formula
        for j in range(0, base):
            subMatrix.append(matrix[j][0:i] + matrix[j][i+1:])
        for j in range(base+1, matrLength):
            subMatrix.append(matrix[j][0:i] + matrix[j][i+1:])
        
        #updates the determinant with recursive call using new submatrix
        deter = deter + ((-1)**(i+2)) * matrix[base][i] * getDeterminant(subMatrix)
    
    return deter

#finds row in given matrix/matrix transpose with the most 0 entries
#also returns boolean for whether to transpose matrix before continuing
def findBase(matrix: list, transMatrix: list) -> tuple:
    #initialize position and 0 count of base row and a boolean saying whether to transpose the matrix
    base = 0
    baseCount = 0
    transpose = False
    
    #compares the number of 0 entries in each row to the current highest, reassigns if necessary
    for i in range(len(matrix)):
        newCount = matrix[i].count(0)
        if newCount > baseCount:
            base = i
            baseCount = newCount
        
    #compares the number of 0 entries in each row of transposed matrix to the current highest, reassigns if necessary
    #also sets the transpose boolean to true if the highest 0 count is in a row of the transpose matrix
    for i in range(len(transMatrix)):
        newCount = transMatrix[i].count(0)
        if newCount > baseCount:
            if not transpose:
                transpose = True
            base = i
            baseCount = newCount
    
    return (base, transpose)
    
def displayMatrix(matrix: list) -> None:
    for i in range(len(matrix)):
        print(matrix[i])
	
main()