def find_employees(data, start, employee, visited = set()):

    if start not in visited:
        print(start, end=" ")
        if start == employee:
            print(':', end=' ')

    visited.add(start)

    for neighbor in data[start]:
        if neighbor not in visited:
            find_employees(data, neighbor, visited)

    return visited


if __name__ == '__main__':
    data = {
        "karan": {"darshan", "nikhil"},
        "darshan": {"khantil", "tanuj"},
        "tanuj": {"nikhil"},
        "krinish": {"hetul"},
        "khantil": set(),
        "nikhil": set()
    }

    find_employees(data, 'karan', 'karan')
