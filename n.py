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
from logging import lastResort
from os import lseek
from wsgiref.util import request_uri

from decouple import config

from django.db.models.expressions import result


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


# def true_or_false(s: str) -> bool:
#     if len(s) % 2 > 0:
#         return  False
#     s_len = len(s) // 2
#     right = s[:s_len]
#     left = s[-1:s_len - 1:-1]
#     for x, y in dict(zip(right, left)).items():
#         if x == '(' and y == ")":
#             continue
#         elif x == '[' and y == ']':
#             continue
#         elif x == '{' and y == '}':
#             continue
#         else:
#             return False
#     return True
#
# print(true_or_false("((()))"))

# a  =  "1234567890"
# x = len(a) // 2
# r = a[:x]
# l = a[-1:x-1:-1]
# print(dict(zip(r, l)))


# def up_low(word: str) -> bool:
#     if word[0].isupper() and word[1:].islower():
#         return True
#     elif word.islower():
#         return True
#     elif word.isupper():
#         return True
#     return False
#
#
# print(up_low('UZBb'))


# def longest_palindromic_substring(s: str) -> str:
    # if not s:
    #     return ""
    #
    # start = 0
    # end = 0
    #
    # def expand_around_center(left: int, right: int):
    #     while left >= 0 and right < len(s) and s[left] == s[right]:
    #         left -= 1
    #         right += 1
    #     return left + 1, right - 1
    #
    # for i in range(len(s)):
    #
    #     l1, r1 = expand_around_center(i, i)
    #
    #     l2, r2 = expand_around_center(i, i + 1)
    #
    #     if (r1 - l1) > (end - start):
    #         start, end = l1, r1
    #     if (r2 - l2) > (end - start):
    #         start, end = l2, r2
    #
    # return s[start:end + 1]




# Nümunə
# text = "babad"
# print(longest_palindromic_substring(text))

# def long_unique(s: str) -> int:
#     n = len(s)
#     char_set = set()
#     left = 0
#     max_length = 0
#
#     for right in range(n):
#         while s[right] in char_set:
#             char_set.remove(s[left])
#             left += 1
#         char_set.add(s[right])
#         max_length = max(max_length, right - left + 1)
#
#     return max_length
#
#
#
# print(long_unique("bbbbbb"))


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
#
# llist = LinkedList()
#
# llist.head = Node('Dushanba')
# tuesday = Node('Seshanba')
# wednesday = Node('Chorshanba')
#
# llist.head.next = tuesday
# tuesday.next = wednesday
#
# print(llist.head.data)
# print(llist.head.next.data)
# print(llist.head.next.next.data)


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse(head):
    """
       ' Reverse a linked list and return the new head node. '
       list_to_node funksiya listdan Linked List yasab beradi
       kodni davom etkazing
    """
    ll = head
    array = []
    while ll.next:
        array.append(ll.val)
        ll = ll.next
    array.append(ll.val)
    array.reverse()
    head = ListNode(array[0])
    current = head
    for i in array[1:]:
        current.next = ListNode(i)
        current = current.next
    return head

# bu kodlargaga tegmang

def list_to_node(array):
    if not array:
        return None

    head = ListNode(array[0])
    current = head

    for val in array[1:]:
        current.next = ListNode(val)
        current = current.next

    return head


def node_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result


input_str = input().strip()
nums = list(map(int, input_str.split(',')))

head = list_to_node(nums)
reversed_head = reverse(head)
result = node_to_list(reversed_head)
print(result)


