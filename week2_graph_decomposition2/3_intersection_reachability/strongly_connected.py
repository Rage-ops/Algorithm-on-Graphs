# Uses python3

import sys

sys.setrecursionlimit(200000)


def graph_reverse(adj):
    adj_r = [[] for _ in range(n)]
    for i in range(len(adj)):
        for v in adj[i]:
            adj_r[v].append(i)
    return adj_r


def order_explore(adj, visited, x, pre, post, clock):
    visited[x] = True
    clock += 1
    pre[x][0] = clock
    for w in adj[x]:
        if not visited[w]:
            clock = order_explore(adj, visited, w, pre, post, clock)
    clock += 1
    post[x][0] = clock
    return clock


def explore(adj, visited, x):
    visited[x] = True
    for w in adj[x]:
        if not visited[w]:
            explore(adj, visited, w)


def dfs(adj):
    pre = [[0, i] for i in range(len(adj))]
    post = [[0, i] for i in range(len(adj))]
    visited = [False for _ in range(len(adj))]
    clock = 0
    for i in range(len(visited)):
        if not visited[i]:
            clock = order_explore(adj, visited, i, pre, post, clock)
    return pre, post


def number_of_strongly_connected_components(adj):
    result = 0
    adj_rev = graph_reverse(adj)
    pre, post = dfs(adj_rev)
    post = sorted(post, key=lambda x: x[0], reverse=True)
    visited = [False for _ in range(len(adj))]
    for vertex in post:
        if not visited[vertex[1]]:
            explore(adj, visited, vertex[1])
            result += 1
    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
