import heapq
import sys

sys.stdin = open("../z_input.text", "r")

def input_():
    return sys.stdin.readline().rstrip()

N = int(input_())

heap = []
for i in range(N):
    value = int(input_())
    if value == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap, (-value, value))

# class MaxHeap:
#     def __init__(self):
#         self.heap = []
#
#     def parent(self, index):
#         return (index - 1) // 2
#
#     def left_child(self, index):
#         return 2 * index + 1
#
#     def right_child(self, index):
#         return 2 * index + 2
#
#     def insert(self, element):
#         self.heap.append(element)
#         self.heapify_up(len(self.heap) - 1)
#
#     def heapify_up(self, index):
#         while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
#             # 부모와 현재 요소를 교환
#             self.heap[self.parent(index)], self.heap[index] = self.heap[index], self.heap[self.parent(index)]
#             index = self.parent(index)
#
#     def extract_max(self):
#         if len(self.heap) == 0:
#             return 0  # 힙이 비어있으면 0을 반환
#         if len(self.heap) == 1:
#             return self.heap.pop()
#
#         root = self.heap[0]
#         self.heap[0] = self.heap.pop()
#         self.heapify_down(0)
#         return root
#
#     def heapify_down(self, index):
#         largest = index
#         left = self.left_child(index)
#         right = self.right_child(index)
#
#         if left < len(self.heap) and self.heap[left] > self.heap[largest]:
#             largest = left
#
#         if right < len(self.heap) and self.heap[right] > self.heap[largest]:
#             largest = right
#
#         if largest != index:
#             self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
#             self.heapify_down(largest)
#
#
# # 최대 힙 객체 생성
# max_heap = MaxHeap()
#
# # 입력 처리
# n = int(input_())  # 연산의 개수 입력
# for _ in range(n):
#     x = int(input_())  # 자연수 또는 0 입력
#     if x == 0:
#         # 0이 입력되면 최대 힙에서 가장 큰 값 출력 및 제거
#         print(max_heap.extract_max())
#     else:
#         # 자연수가 입력되면 최대 힙에 삽입
#         max_heap.insert(x)
