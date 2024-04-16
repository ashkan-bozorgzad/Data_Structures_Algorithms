def bfs(data, start):

    discovered = set()
    parent = {}
    dist = {}

    queue = [start]
    dist[start] = 0
    parent[start] = None
    discovered.add(start)

    while queue:
        current_node = queue.pop(0)
        for u in data[current_node]:
            if u not in discovered:
                discovered.add(u)
                dist[u] = dist[current_node] + 1
                parent[u] = current_node
                queue.append(u)

    print(f'distance of each node from {start}: {dist}')
    print(f'parents of each node for start={start}: {parent}')


if __name__ == "__main__":
    data = {
        'A': {'B'}, 'B': {'A', 'C', 'D'}, 'C': {'B', 'E'}, 'D': {'B', 'E'},
        'E': {'C', 'D', 'F'}, 'F': {'E'}
    }
    bfs(data, 'A')



