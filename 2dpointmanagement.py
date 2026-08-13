
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return d

def farthest_point(points):
    origin = (0, 0)

    farthest = points[0]
    max_distance = distance(farthest, origin)

    for point in points:
        d = distance(point, origin)

        if d > max_distance:
            max_distance = d
            farthest = point

    return farthest, max_distance


n = int(input("Enter number of points: "))

points = []

for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))

    point = (x, y)    
    points.append(point)


print("\nPoints:", points)

print("\nEnter two point numbers to calculate distance:")
p1 = int(input("Enter first point number: "))
p2 = int(input("Enter second point number: "))

d = distance(points[p1 - 1], points[p2 - 1])

print("Distance between points:", d)

point, d = farthest_point(points)

print("Farthest point from origin:", point)
print("Distance from origin:", d)