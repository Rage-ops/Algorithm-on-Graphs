# Uses python3
# https://www.youtube.com/watch?v=0dJmTuMrUZM

def explore(v, visited, adj, explored):
    explored[v] = True
    visited[v] = True
    for w in adj[v]:
        if visited[w]:
            return 1
        if not visited[w]:
            if explore(w, visited, adj, explored):
                return 1
            visited[w] = False
    visited[v] = False
    return 0


def acyclic(adj):
    visited = [False for _ in range(len(adj))]
    explored = [False for _ in range(len(adj))]
    for i in range(len(explored)):
        if not explored[i]:
            if explore(i, visited, adj, explored):
                return 1
    return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
