# Uses python3

import queue


def shortest_paths(n, adj, s, distance, reachable, shortest):
    distance[s] = 0
    reachable[s] = 1
    q = queue.Queue()
    for i in range(n):
        for u in range(n):
            for (v, c) in adj[u]:
                if distance[v] > distance[u] + c:
                    distance[v] = distance[u] + c
                    reachable[v] = 1
                    if i == n - 1:
                        q.put(v)
    visited = [0] * n
    while not q.empty():
        u = q.get()
        for v, _ in adj[u]:
            if visited[v] == 0:
                q.put(v)
                visited[v] = 1
                shortest[v] = 0
    distance[s] = 0
    return distance, shortest


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        adj[a - 1].append((b - 1, w))
    # print(adj)
    s = int(input())
    s -= 1
    distance = [float('inf')] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(n, adj, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

