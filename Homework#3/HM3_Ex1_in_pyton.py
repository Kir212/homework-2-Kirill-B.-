import numpy as np

# Ex.4
T1 = "Ex.4"
A = np.array([[1, -2, 8], [7, 5, -2], [-2, 3, 0]])
B = np.array([[0, 2, 4], [1, -3, -2], [-2, 1, 3]])
C = np.array([[0, 3], [5, -4], [7, -1]])


print(f"{T1}\nРезультат A+B:\n{A + B}")
print(f"\nРезультат B-A:\n{B - A}")
print(f"\nРезультат A*C:\n{A @ C}")
print(f"\nРезультат A*B*C:\n{A @ B @ C}")


# Ex.5
T1 = "Ex.5"
A = np.array([[9, 2, 4], [7, 5, -5], [6, -2, 3]])
B = np.array([[8, 2, 4], [0, 1, -3], [-2, 1, 6]])
C = np.array([[-2, 0], [4, 8], [1, -1]])


print(f"\n{T1}\nРезультат A+B:\n{A + B}")
print(f"\nРезультат B-A:\n{B - A}")
print(f"\nРезультат A*C:\n{A @ C}")
print(f"\nРезультат A*B*C:\n{A @ B @ C}")