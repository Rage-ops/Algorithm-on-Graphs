# Uses python3

import math

# Time Complexity:  O(V * E)
# Space Complexity: O(V)


def negative_cycle(adj):
    dist = [math.inf for _ in range(len(adj))]
    for i in range(len(adj)):
        dist[i] = 0
        for u in range(len(adj)):
            for (v, w) in adj[u]:
                if dist[v] > dist[u] + w:
                    flag = False
                    dist[v] = dist[u] + w
                    if i == len(adj) - 1:
                        return 1
    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        adj[a-1].append((b-1, c))
    print(negative_cycle(adj))
