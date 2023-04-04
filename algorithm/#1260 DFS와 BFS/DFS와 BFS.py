n, m, v = map(int, input().split())

graph = {i: set() for i in range(1, n+1)}

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].add(b)
    graph[b].add(a)


def dfs_search(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(reversed(sorted(graph[node] - set(visited))))
    return visited


def bfs_search(graph, start):
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(graph[node] - set(visited)))
    return visited

print(*dfs_search(graph, v))
print(*bfs_search(graph, v))