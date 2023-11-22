from collections import defaultdict

def validPath(n, edges, source, destination):
    # Create an adjacency list representation of the graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    # DFS function to traverse the graph
    def dfs(current):
        if current == destination:
            return True
        visited[current] = True
        for neighbor in graph[current]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
        return False

    # Initialize visited array
    visited = [False] * n

    # Start DFS from the source vertex
    return dfs(source)

# Test cases
print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) # Output: True
print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # Output: False
