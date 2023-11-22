def allPathsSourceTarget(graph):
    def dfs(current, path):
        if current == len(graph) - 1:  # Reached the target node
            result.append(path[:])  # Add the current path to the result
            return
        
        for neighbor in graph[current]:
            path.append(neighbor)  # Append the current neighbor to the path
            dfs(neighbor, path)  # Explore the path from the neighbor
            path.pop()  # Backtrack to explore other paths
    
    result = []
    dfs(0, [0])  # Start DFS from node 0 with the initial path [0]
    return result

# Test cases
print(allPathsSourceTarget([[1,2],[3],[3],[]])) 
# Output: [[0,1,3],[0,2,3]]

print(allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]])) 
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
