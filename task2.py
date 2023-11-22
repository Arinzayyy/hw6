def longestCycle(edges):
    n = len(edges)
    visited = [False] * n
    max_length = -1

    def dfs(node, start, depth):
        nonlocal max_length
        if visited[node]:
            if node == start and depth > 1:
                max_length = max(max_length, depth)
            return

        visited[node] = True
        next_node = edges[node]

        if next_node != -1:
            dfs(next_node, start, depth + 1)

        visited[node] = False

    for i in range(n):
        dfs(i, i, 0)

    return max_length if max_length != -1 else -1

# Test cases
print(longestCycle([3,3,4,2,3])) # Output: 3
print(longestCycle([2,-1,3,1])) # Output: -1
