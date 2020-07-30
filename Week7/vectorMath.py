import math

vector_A = [int(x) for x in input("Enter vector A: ").split()]
# vector_A = []

# vector_A.append(x)
# vector_A.append(y)
# vector_A.append(z)

vector_B = [int(c) for c in input("Enter vector B: ").split()]

# vector_B = []

# vector_B.append(c)
# vector_B.append(d)
# vector_B.append(e)

# print(A)
# print(B)
# b = int(input("Enter vector B:\n"))

# Addition

# sum = [vector_A[i] + vector_B[i] for i in range(len(vector_A))]
sum = [vector_A[0] + vector_B[0], vector_A[1] + vector_B[1], vector_A[2] + vector_B[2]]
print("A + B =", sum)

#Dot product

product = vector_A[0] * vector_B[0] + vector_A[1] * vector_B[1] + vector_A[2] * vector_B[2]

print("A.B = ", product)

#Norm of vector A

norm_A = math.sqrt(vector_A[0] ** 2 + vector_A[1] ** 2 + vector_A[2] ** 2)

print( "|A| = " + "%.2f" % norm_A)
# numpy.linalg.norm(x, ord=None, axis=None, keepdims=False)[source]

#Norm of vector_B

norm_B = math.sqrt(vector_B[0] ** 2 + vector_B[1] ** 2 + vector_B[2] ** 2)

print("|B| = " + "%.2f" % norm_B)