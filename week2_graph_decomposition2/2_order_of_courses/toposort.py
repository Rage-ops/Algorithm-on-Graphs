# Uses python3


def dfs(adj, used, order, x):
    used[x] = True
    for w in adj[x]:
        if not used[w]:
            dfs(adj, used, order, w)
    order.append(x)

def toposort(adj):
    visited = [False for _ in range(len(adj))]
    order = []
    for i in range(len(visited)):
        if not visited[i]:
            dfs(adj, visited, order, i)
    return order[::-1]

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

