def find_path(data, start, end):

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

    if end not in discovered:
        print(f'A path does not exist between {start} and {end}.')
    else:
        path = f'{end}'
        node = parent[end]
        while node:
            path = f'{node}->' + path
            node = parent[node]

        print(f'path: {path}')


if __name__ == "__main__":
    data = {
        'A': {'B'},
        'B': {'A', 'C', 'D'},
        'C': {'B', 'E'},
        'D': {'B', 'E'},
        'E': {'C', 'D', 'F'},
        'F': {'E'}
    }
    find_path(data, 'A', 'D')



