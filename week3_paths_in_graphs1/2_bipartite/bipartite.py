# Uses python3

import queue


def bfs(adj, s, visited, color):
    visited[s] = True
    q = queue.Queue()
    q.put(s)
    color[s] = 1
    while q.qsize() > 0:
        start = q.get()
        for w in adj[start]:
            if not visited[w]:
                q.put(w)
                visited[w] = True
                color[w] = 0 if color[start] else 1


def bipartite(adj):
    visited = [False for _ in range(len(adj))]
    color = [None for _ in range(len(adj))]
    for i in range(len(adj)):
        if not visited[i]:
            bfs(adj, i, visited, color)
    for i in range(len(adj)):
        for j in adj[i]:
            if color[i] == color[j]:
                return 0
    return 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
