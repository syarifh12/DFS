# Representasi graf menggunakan dictionary (adjacency list)
graph = {
    'Q1': ['Q2', 'Q3'],
    'Q2': ['Q4', 'Q5'],
    'Q3': ['Q5'],
    'Q4': [],
    'Q5': []
}

# Set untuk menyimpan node yang sudah dikunjungi
visited = set()

# Fungsi DFS rekursif
def dfs(graph, node, goal, path=[]):
    if node not in visited:
        visited.add(node)
        path.append(node)
        print(f"Visited: {node}")

        if node == goal:
            print(f"Goal '{goal}' ditemukan!")
            return path  # Return path to goal

        for neighbor in graph[node]:
            result = dfs(graph, neighbor, goal, path)
            if result:  # Jika goal ditemukan
                return result

        # Backtrack jika goal tidak ditemukan di cabang ini
        path.pop()
    return None

# Eksekusi DFS dari Q1 ke Q5
start_node = 'Q1'
goal_node = 'Q5'
path = dfs(graph, start_node, goal_node)

# Hasil
print("\nJalur DFS dari Q1 ke Q5:")
print(" -> ".join(path) if path else "Tidak ditemukan")
