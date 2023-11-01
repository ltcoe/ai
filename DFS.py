def dfs(graph, start, goal):
    stack = [(start, [start])]  # Create a stack for DFS, and each element in the stack is a tuple (node, path).
    visited = set()  # Create a set to keep track of visited nodes.

    while stack:
        current_node, path = stack.pop()  # Pop the current node and its path from the stack.

        print("Visiting node:", current_node)  # Print the current node.

        if current_node == goal:
            return path  # Goal node found, return the path.

        visited.add(current_node)  # Mark the current node as visited.

        # Explore all unvisited neighbors of the current node.
        unvisited_neighbors = [neighbor for neighbor in graph[current_node] if neighbor not in visited]
        for neighbor in unvisited_neighbors:
            new_path = path + [neighbor]  # Extend the path with the neighbor.
            stack.append((neighbor, new_path))  # Push the neighbor and its path onto the stack.

    return []  # Goal node not found, return an empty path.

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

start_node = 'A'
goal_node = 'F'

path_to_goal = dfs(graph, start_node, goal_node)

if path_to_goal:
    print("Goal node found. Path:", path_to_goal)
else:
    print("Goal node not found.")
