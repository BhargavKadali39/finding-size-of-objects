
import sys

size_1 = ["I","am","groot"]

size_2 = ("I","am","groot")

print("size of first object:",end=" ")
print(sys.getsizeof(size_1))

print("size of second object:",end=" ")
print(sys.getsizeof(size_2))
