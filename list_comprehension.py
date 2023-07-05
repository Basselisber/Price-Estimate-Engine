# 1-	define a list containing all int between deux given numbers a and b
# 2-	modify the list above to include only numbers divisible by a third parameter (c)
# 3-	turn to uppercase all element of a str-list
# 4-	modify the list above to keep only element with a length above a given threshold
# 5-	from a list of string create a list of list. Every inside list contains
# 	the chars of the strings
# 	['abc', 'xyz'] -> [['a', 'b', 'c'], ['x', 'y', 'z']]
# 6-	add the element of 2 lists ->
# 	[3, 7, 5] + [11, 13, 19] -> [14, 20, 24] (use zip)
# 7-	a matrix is a list of list ([0, 0, 0], [0, 0, 0], [0, 0, 0]] is a 3x3 matrix.
# 	given a number N generate the matrix NxN with random numbers
# 8-	add two matrixes
# 9-	from a matrix get the values of a column (column number given)
# import random
# nums = [1,2,3,4,5,6,7,8,9,10]
# lst = [x for x in nums]
# lst_sq = [x*x for x  in nums]
# yz = 'abcdefghij'
# x = [(x,y) for x in nums for y in yz]
# print(x)

# def listOfRange(a,b,c):
#     return [x for x in range(a,b) if x%c == 0]

# print(listOfRange(1,100,3))

# def upperCaseList(list):
#     return [x.upper() for x in list if len(x) > 5]

# print(upperCaseList(['abc', 'xyz','bassel']))

lstU = ['abc', 'xyz','bassel']
def upperCaseList2(list):
    list_down = []
    for x in lstU:
        list_up = []
        for y in x:
            list_up.append(y.upper())
        list_down.append(list_up)
    return list_down
print(upperCaseList2(lstU))

# def splitStringList(list):
#     return [[x for x in y] for y in list]
# print(splitStringList(['abc', 'xyz']))

# def CombinedList(list1,list2):
#     result = []
#     for x,y in zip(list1,list2):
#         result.append(x+y)
#     return result
#     return [x+y for x,y in zip(list1,list2)]
# print(CombinedList([3, 7, 5],[11, 13, 19]))
# import random
# def matrix(n):
#     result = []
#     for y in range(n):
#         x = []
#         for z in range(n):
#             x.append(random.randint(0,100))
#         result.append(x)
#     return result
#     return [[random.randint(0,100) for x in range(n)] for y in range(n)] 
# print(matrix(3))

# def addMatrix(m1,m2):
#     return [[x+y for x,y in zip(m1[i],m2[i])] for i in range(len(m1))]

def addMatrix(m1,m2):
    result = []
    for i in range(len(m1)):
        x = []
        for j in range(len(m1[i])):
            x.append(m1[i][j]+m2[i][j])
        result.append(x)
    return result
print(addMatrix([[1,2,3],
                 [23,4,1]],
                 [[1,2,3],
                  [23,4,1]]))

matrix1 = [[1,2,3],
           [23,4,1],
           [22,12,34]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[i])):
        print(matrix1[i][j],end=' ')
    print()

matrix = [[1,2,3],[23,4,1]]

def getColumn(matrix,n):
    for x in matrix:
        print(x[n])
#     return [x[n] for x in matrix]
print(getColumn(matrix,0))

# print(len(matrix))



