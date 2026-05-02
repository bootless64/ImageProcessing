from numpy import array

x1 = array([9, 8, 7],[6, 5, 4])
x2 = array([7, 8, 9],[1, 2, 3])

print("x1 =")
print(x1)
print("x2 =")
print(x2)

print("Sum (x1 + x2) =")
print(x1 + x2)

print("Subtraction (x1 - x2) =")
print(x1 - x2)

print("Multiplication (x1 * x2) =")
print(x1 * x2)

print("Division (x1 / x2) =")
print(x1 / x2)

v1 = x1[0]
v2 = x2[0]

ip = v1 @ v2
print("Inner Product (x1[0] . x2[0]) =")
print(ip)

sm = 10 * x1
print("Scalar Multiplication (10 * x1) =")
print(sm)

v = array([1, 0, 1, 0])
vmm = v @ x1
print("Vector-Matrix Multiplication (v @ x1) =")
print(vmm)

t1 = x1.T
print("Transpose x1 =")

print(t1)
