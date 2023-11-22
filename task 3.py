class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
        return True

def minimumCost(N, connections):
    connections.sort(key=lambda x: x[2])  # Sort connections by their costs
    uf = UnionFind(N + 1)
    min_cost = 0
    edges_added = 0

    for city1, city2, cost in connections:
        if uf.union(city1, city2):
            min_cost += cost
            edges_added += 1

    # Check if all cities are connected
    return min_cost if edges_added == N - 1 else -1

# Test cases
print(minimumCost(3, [[1,2,5],[1,3,6],[2,3,1]])) # Output: 6
print(minimumCost(4, [[1,2,3],[3,4,4]])) # Output: -1
