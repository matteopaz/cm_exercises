def copy(arr):
    newarr = []
    for e in arr:
        newarr.append(e)
    return newarr

def cartesian_product(ranges):
    order = 1
    for range in ranges:
        order = order * len(range)
    pts = []

    for i in range(order):
        pts.append([])
    
    for range in ranges:
        points = copy(pts)
        for val in range:
            for point in points:
                point.append(val)
        pts = points
    return pts

print(cartesian_product([[0,1],[2,3]]))