# def pascal_triangle(n):
#
#     matrix = []
#
#     if n <= 0:
#         return matrix
#     matrix = [[1]]
#
#     for i in range(1, n):
#         temp = [1]
#         for j in range(len(matrix[i - 1]) - 1):
#             curr = matrix[i - 1]
#             temp.append(matrix[i - 1][j] + matrix[i - 1][j + 1])
#         temp.append(1)
#         matrix.append(temp)
#     return matrix
#
# print(pascal_triangle(5))
from wsgiref.util import request_uri


def fibonacci(number):
    if number < 0:
        return 'incorrect input'
    elif number == 0:
        return 0
    elif number == 1:
        return 1
    else:
        return fibonacci(number-1) + fibonacci(number-2)

print(fibonacci(number=int(input(': '))))

