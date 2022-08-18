# def copy(arr):
#     newarr = []
#     for e in arr:
#         newarr.append(e)
#     return newarr

def cartesian_product(ranges):
    points = [[]]
    for range in ranges:
        extended_pts = []

        for val in range: 
            for pt in points:
                extended_pts.append(pt+[val])

        points = extended_pts
    return points

print(cartesian_product([["a", "b", "c","d","e","f","g"],range(5)]))