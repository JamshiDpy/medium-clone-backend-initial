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

from decouple import config


# def fibonacci(number):
#     if number < 0:
#         return 'incorrect input'
#     elif number == 0:
#         return 0
#     elif number == 1:
#         return 1
#     else:
#         return fibonacci(number-1) + fibonacci(number-2)
#
# print(fibonacci(number=int(input(': '))))

# def max_area(heights):
#     left = 0
#     right = len(heights) - 1
#     max_water = 0
#
#     while left < right:
#         width = right - left
#         height = min(heights[left], heights[right])
#         max_water = max(max_water, width * height)
#
#         if heights[left] < heights[right]:
#             left += 1
#         else:
#             right -= 1
#
#     return max_water
#
# heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# print(max_area(heights))

# def left_right_difference(nums: list) -> list:
#     result = []
#     for i in range(len(nums)):
#         if sum(nums[i+1:]) > sum(nums[:i]):
#             result.append(1)
#         elif sum(nums[:i]) > sum(nums[i+1:]):
#             result.append(-1)
#         else:
#             result.append(0)
#     return result
#
# print(left_right_difference([1, 2, 3, 4]))


def true_or_false(s: str) -> bool:
    if len(s) % 2 > 0:
        return  False
    s_len = len(s) // 2
    right = s[:s_len]
    left = s[-1:s_len - 1:-1]
    for x, y in dict(zip(right, left)).items():
        if x == '(' and y == ")":
            continue
        elif x == '[' and y == ']':
            continue
        elif x == '{' and y == '}':
            continue
        else:
            return False
    return True

print(true_or_false("((()))"))

# a  =  "1234567890"
# x = len(a) // 2
# r = a[:x]
# l = a[-1:x-1:-1]
# print(dict(zip(r, l)))
