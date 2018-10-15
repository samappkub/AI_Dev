def bfs_search(initial_state):
    """BFS search"""
    if is_goal(initial_state): return initial_state
    frontier, visited = Queue(), set()
    frontier.enqueue((initial_state, 0))
    mlevel = 0
    while (not frontier.empty()):
        current, level = frontier.dequeue()
        visited.add(hash(current))
        if is_goal(current):
            return (len(visited), current, level, mlevel)
        for child in current.expand():
            if (hash(child) not in visited) and (child not in frontier):
                frontier.enqueue((child, level + 1))
                if level + 1 > mlevel:
                    mlevel = level + 1

def dfs_search(initial_state):
    """DFS search"""
    if is_goal(initial_state): return initial_state
    frontier, visited = Stack(), set()
    frontier.push((initial_state, 0))
    mlevel = 0
    while not frontier.empty():
        current, level = frontier.pop()
        visited.add(hash(current))
        if is_goal(current):
            return (len(visited), current, level, mlevel)
        for child in current.expand():
            if (hash(child) not in visited) and (child not in frontier):
                frontier.push((child, level + 1))
                if level + 1 > mlevel:
                    mlevel = level + 1

def uniform_cost_search(initial_state):
    """Uniform Cost Search"""
    if is_goal(initial_state):return initial_state
    frontier, visited = PriorityQueue, set()
    f_n = 

def A_star_search(initial_state):
    """A * search"""
    if is_goal(initial_state): return initial_state
    frontier, visited = PriorityQueue(), set()
    f_n = calculate_manhattan_dist(initial_state) + initial_state.cost
    frontier.put((f_n, (initial_state, 0)))
    mlevel = 0
    while not frontier.empty():
        current, level = frontier.get()
        visited.add(hash(current))
        if is_goal(current):
            return (len(visited), current, level, mlevel)
        for child in current.expand():
            if (hash(child) not in visited) and (child not in frontier):
                f_n = calculate_manhattan_dist(child) + child.cost
                frontier.put((f_n, (child, level + 1)))
            if level + 1 > mlevel:
                mlevel = level + 1


def get_path_to_goal(goal_state):
    if not goal_state: return []
    path = []
    current = goal_state
    while current.action != 'Initial':
        path.insert(0, current.action)
        current = current.parent
    return path
