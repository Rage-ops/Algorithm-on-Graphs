# Uses python3
import math
from collections import namedtuple


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"(X: {self.x}, Y: {self.y})"


def pt_distance(pt1, pt2):
    return math.sqrt(math.pow(pt1.x - pt2.x, 2) + math.pow(pt1.y - pt2.y, 2))


def creating_edges(pts):
    EDGE = namedtuple('EDGE', ['start', 'end', 'distance'])
    all_edges = []
    for i in range(len(pts)):
        for j in range(i + 1, len(pts)):
            all_edges.append(EDGE(pts[i], pts[j], pt_distance(pts[i], pts[j])))
    return sorted(all_edges, key=lambda info: info.distance)


class UnionFind:
    def __init__(self, pts):
        self.info = {}
        for i in range(len(pts)):
            self.info[pts[i]] = {'Rank': 0, 'Parent': pts[i]}

    def get_root(self, pt):
        if pt != self.info[pt]['Parent']:
            self.info[pt]['Parent'] = self.get_root(self.info[pt]['Parent'])
        return self.info[pt]['Parent']

    def union(self, a, b):
        root_a = self.get_root(a)
        root_b = self.get_root(b)
        # print('r_a:', root_a)
        # print('r_b:', root_b)
        if root_a == root_b:
            return 0
        else:
            if self.info[root_a]['Rank'] > self.info[root_b]['Rank']:
                self.info[root_b]['Parent'] = root_a
            elif self.info[root_b]['Rank'] > self.info[root_a]['Rank']:
                self.info[root_a]['Parent'] = root_b
            else:
                self.info[root_a]['Parent'] = root_b
                self.info[self.info[root_a]['Parent']]['Rank'] += 1
            return 1


def minimum_distance(pts, edges):
    result = 0
    h = UnionFind(pts)
    # print(h.info)
    for edge in edges:
        # print(edge)
        if h.union(edge.start, edge.end):
            result += edge.distance
        # print(h.info)
    return result


if __name__ == '__main__':
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().split())
        points.append(Point(x, y))
    edges = creating_edges(points)
    print("{0:.9f}".format(minimum_distance(points, edges)))
