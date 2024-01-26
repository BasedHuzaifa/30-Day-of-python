import math
point1 = (2, 3)
point2 = (10, 8)
x1, y1 = point1
x2, y2 = point2
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(f"The Euclidean distance between {point1} and {point2} is: {distance}")
