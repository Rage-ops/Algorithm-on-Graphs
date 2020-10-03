# Uses python3

from collections import namedtuple
import math


class PriorityQueue:

    def __init__(self):
        self.q = []
        self.map = {}

    def GetQ(self):
        return self.q

    @staticmethod
    def GetLeftChild(i: int) -> int:
        return 2 * i + 1

    @staticmethod
    def GetRightChild(i: int) -> int:
        return 2 * i + 2

    @staticmethod
    def GetParent(i: int) -> int:
        return (i - 1) // 2

    def sift_up(self, i: int):
        q = self.GetQ()
        parent = PriorityQueue.GetParent(i)
        while i > 0 and q[i][0] < q[parent][0]:
            q[i], q[parent] = q[parent], q[i]
            self.map[q[i][1]] = i
            self.map[q[parent][1]] = parent
            i = parent
            parent = PriorityQueue.GetParent(i)

    def sift_down(self, i: int):
        q = self.GetQ()
        min_index = i
        left = self.GetLeftChild(i)
        right = self.GetRightChild(i)
        if left < len(q) and q[min_index][0] > q[left][0]:
            min_index = left
        if right < len(q) and q[min_index][0] > q[right][0]:
            min_index = right
        if min_index != i:
            q[min_index], q[i] = q[i], q[min_index]
            self.map[q[min_index][1]] = min_index
            self.map[q[i][1]] = i
            self.sift_down(min_index)

    def extract_min(self):
        q = self.GetQ()
        q[len(q) - 1], q[0] = q[0], q[len(q) - 1]
        self.map[q[len(q) - 1][1]] = len(q) - 1
        self.map[q[0][1]] = 0
        value = q.pop()
        del self.map[value[1]]
        self.sift_down(0)
        return value

    def insert(self, element: list):
        q = self.GetQ()
        q.append(element)
        self.map[element[1]] = len(q) - 1
        self.sift_up(len(q) - 1)

    def ChangePriority(self, i: int, new_priority):
        q = self.GetQ()
        # print(f'p:{i}')
        old_priority = q[i][0]
        q[i][0] = new_priority
        if new_priority < old_priority:
            # print("up")
            self.sift_up(i)
        elif new_priority > old_priority:
            # print('down')
            self.sift_down(i)

    def remove(self, i):
        q = self.GetQ()
        q[i][0] = -math.inf
        self.sift_up(i)
        return self.extract_min()


def distance(adj, s, t):
    dist = [math.inf for _ in range(len(adj))]
    dist[s] = 0
    prev = [None for _ in range(len(adj))]
    prev[s] = s
    h = PriorityQueue()
    for i in range(len(dist)):
        h.insert([dist[i], i])
    # print(f"dist:{dist}")
    # print(f"prev:{prev}")
    # print(f"h:{h.GetQ()}")
    # print(f"adj:{adj}")
    # print(f"map:{h.map}")
    while len(h.GetQ()) > 0:
        u = h.extract_min()
        # print(f"min:{u}")
        # print(f"h:{h.GetQ()}")
        # print(f"map:{h.map}")
        vertex = u[1]
        for neighbour in adj[vertex]:
            # print(f"n:{neighbour}")
            if dist[neighbour.to] > dist[vertex] + neighbour.cost:
                # print(f"d[n]:{dist[neighbour.to]}, d[v] + cost: {dist[vertex]} + {neighbour.cost}")
                dist[neighbour.to] = dist[vertex] + neighbour.cost
                prev[neighbour.to] = vertex
                h.ChangePriority(h.map[neighbour.to], dist[neighbour.to])
                # print("after change")
                # print(f"h:{h.GetQ()}")
                # print(f"map:{h.map}")
    # print(f"Shortest Path from {s + 1} to {t + 1} : {path_construct(prev, t)}")
    return -1 if dist[t] == math.inf else dist[t]


def path_construct(prev, end):
    path = []
    while prev[end] != end:
        path.append(prev[end] + 1)
        end = prev[end]
    return path[::-1]


if __name__ == '__main__':
    EDGE = namedtuple('Edge', ['to', 'cost'])
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a - 1].append(EDGE(b - 1, c))
    s, t = map(int, input().split())
    s, t = s - 1, t - 1
    print(distance(adj, s, t))
