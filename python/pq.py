import heapq

class student:
    def __init__(self, name, gpa, age) -> None:
        self.name = name
        self.gpa = gpa
        self.age = age
    
    def __lt__(self, other):
        return self.gpa > other.gpa

def object_heap_demo():
    student_1 = student("Alice", 3.9, 21)
    student_2 = student("Bob", 4.0, 20)
    student_3 = student("Charles", 3.8, 22)

    heapqueue = []
    heapq.heappush(heapqueue, student_1)
    heapq.heappush(heapqueue, student_2)
    heapq.heappush(heapqueue, student_3)

    while heapqueue:
        print(heapq.heappop(heapqueue).name)

def tuple_heap_demo():
    tup_1 = (3.9, "Alice", 21)
    tup_2 = (4.0, "Bob", 20)
    tup_3 = (3.8, "Charles", 22)

    heapqueue = []
    heapq.heappush(heapqueue, tup_1)
    heapq.heappush(heapqueue, tup_2)
    heapq.heappush(heapqueue, tup_3)

    while heapqueue:
        print(heapq.heappop(heapqueue)[1])