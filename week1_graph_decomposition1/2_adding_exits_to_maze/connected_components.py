# Uses python3

def reach(adj, x, visited):
    stack = [x]
    visited[x] = 1
    while stack:
        start = stack.pop()
        for i in adj[start]:
            if visited[i] == 0:
                stack.append(i)
                visited[i] = 1

def number_of_components(adj):
    result = 0
    visited = [0 for _ in range(len(adj))]
    for i in range(len(visited)):
        if visited[i] == 0:
            reach(adj, i, visited)
            result += 1
    return result


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
