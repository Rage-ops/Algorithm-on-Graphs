# Uses python3

import queue


def distance(adj, s, t):
    visited = [False for _ in range(len(adj))]
    visited[s] = True
    q = queue.Queue()
    q.put(s)
    level = [-1 for _ in range(len(adj))]
    level[s] = 0
    curr = 0
    while q.qsize() > 0:
        curr += 1
        size = q.qsize()
        for _ in range(size):
            start = q.get()
            for w in adj[start]:
                if not visited[w]:
                    q.put(w)
                    visited[w] = True
                    level[w] = curr
                    if w == t:
                        return level[w]
    return level[t]


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = map(int, input().split())
    s, t = s-1, t-1
    print(distance(adj, s, t))
