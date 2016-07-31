from math import sqrt
def d(p1,p2):
    """Returns Euclidian distance between two points"""
    dist = sqrt(sum((p-q)**2 for p,q in zip(p1,p2)))
    return dist
