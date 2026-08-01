import numpy as np
print("Enter Matrix A")

a11 = int(input("A[1][1]: "))
a12 = int(input("A[1][2]: "))
a21 = int(input("A[2][1]: "))
a22 = int(input("A[2][2]: "))

A = np.array([
    [a11, a12],
    [a21, a22]
])

print("Matrix A:")
print(A)

print("Enter Matrix B")

b11 = int(input("B[1][1]: "))
b12 = int(input("B[1][2]: "))
b21 = int(input("B[2][1]: "))
b22 = int(input("B[2][2]: "))

B = np.array([
    [b11, b12],
    [b21, b22]
])

print("Matrix B:")
print(B)

print("1. Addition of two matrices\n2. Subtraction of two matrices\n3. Multiplication of two matrices\n4. Division of two matrices")
choice = int(input("Enter your choice (1/2/3/4): "))


if choice == 1:
    # Matrix addition
    C = A + B
    print("Matrix C (A + B):")
    print(C)
elif choice == 2:
    # Matrix subtraction
    D = A - B
    print("Matrix D (A - B):")
    print(D)
elif choice == 3:
    # Matrix multiplication
    E = np.dot(A, B)
    print("Matrix E (A * B):")
    print(E)
elif choice == 4:
    # Matrix division
    F = np.dot(A, np.linalg.inv(B))
    print("Matrix F (A / B):")
    print(F)
else:
    print("Invalid choice. Please select a valid option (1/2/3/4).")