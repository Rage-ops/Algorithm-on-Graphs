# Uses python3

def explore(v, dest, visited, adj):
    if v == dest:
        return 1
    visited[v] = True
    for w in adj[v]:
        if not visited[w]:
            if explore(w, dest, visited, adj):
                return 1
    return 0


def reach(adj, x, y):
    visited = [False for _ in range(len(adj))]
    return explore(x, y, visited, adj)
    # Iterative sol
    # stack = [x]
    # visited[x] = True
    # while stack:
    #     start = stack.pop()
    #     for i in adj[start]:
    #         if not visited[i]:
    #             stack.append(i)
    #             visited[i] = True
    #             if i == y:
    #                 return 1
    # return 0


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    source, destination = map(int, input().split())
    source, destination = source - 1, destination - 1
    print(reach(adj, source, destination))
