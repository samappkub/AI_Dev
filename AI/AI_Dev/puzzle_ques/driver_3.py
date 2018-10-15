import time
import sys
import math

class PuzzleState:
    """docstring for PuzzleState"""
    def __init__(self, config, n, parent=None, action="Initial", cost=0):
        if n*n != len(config) or n < 2:
            raise Exception("the length of config is not correct!")
        self.n = n
        self.cost = cost
        self.parent = parent
        self.action = action
        self.dimension = n
        self.config = config
        self.children = []
        for i, item in enumerate(self.config):
            if item == 0:
                self.blank_row = i // self.n
                self.blank_col = i % self.n
                break

    def display(self):
        for i in range(self.n):
            line = []
            offset = i * self.n
            for j in range(self.n):
                line.append(self.config[offset + j])
            print(line)

    def move_left(self):
        if self.blank_col == 0:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index - 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Left", cost=self.cost + 1)

    def move_right(self):
        if self.blank_col == self.n - 1:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index + 1
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Right", cost=self.cost + 1)

    def move_up(self):
        if self.blank_row == 0:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index - self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Up", cost=self.cost + 1)

    def move_down(self):
        if self.blank_row == self.n - 1:
            return None
        else:
            blank_index = int(self.blank_row * self.n + self.blank_col)
            target = blank_index + self.n
            new_config = list(self.config)
            new_config[blank_index], new_config[target] = new_config[target], new_config[blank_index]
            return PuzzleState(tuple(new_config), self.n, parent=self, action="Down", cost=self.cost + 1)

    def expand(self):
        """expand the node"""
        # add child nodes in order of UDLR
        if len(self.children) == 0:
            up_child = self.move_up()
            if up_child is not None:
                self.children.append(up_child)
            down_child = self.move_down()
            if down_child is not None:
                self.children.append(down_child)
            left_child = self.move_left()
            if left_child is not None:
                self.children.append(left_child)
            right_child = self.move_right()
            if right_child is not None:
                self.children.append(right_child)
        return self.children


class Stack:
    def __init__(self):
        self.data = []
        self.hashes = []

    def empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.insert(0, item)
        self.hashes.append(item[0].config)

    def pop(self):
        return self.data.pop(0)

    def __contains__(self, el):
        return el.config in self.hashes


class Queue:
    def __init__(self):
        self.data = []
        self.hashes = []

    def empty(self):
        return len(self.data) == 0

    def enqueue(self, item):
        self.data.append(item)
        self.hashes.append(item[0].config)

    def dequeue(self):
        return self.data.pop(0)

    def __contains__(self, el):
        return el.config in self.hashes


class PriorityQueue:
    def __init__(self):
        self.data = []
        self.hashes = []

    def put(self, item):
        self.data.append(item)
        self.data.sort(key=lambda x: x[0])
        self.hashes.append(item[1][0].config)

    def get(self):
        return self.data.pop(0)[1]

    def empty(self):
        return len(self.data) == 0

    def __contains__(self, el):
        return el.config in self.hashes


# Function that Writes to output.txt
def writeOutput(path, cost, nodes, depth, max_depth,
                run_time):
    with open('output.txt', 'w') as f:
        f.write('path_to_cost: {}'.format(path))
        f.write('\n')
        f.write('cost_of_path: {}'.format(cost))
        f.write('\n')
        f.write('nodes_expanded: {}'.format(nodes))
        f.write('\n')
        f.write('search_depth: {}'.format(depth))
        f.write('\n')
        f.write('max_search_depth: {}'.format(max_depth))

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

def is_goal(state):
    return state.config == (0,1,2,3,4,5,6,7,8)

def calculate_manhattan_dist(puzzle_state):
    """calculate the manhattan distance of a tile"""
    total_diff = 0
    for i, num in enumerate(puzzle_state.config):
        total_diff += abs(i - num)
    return total_diff

def main():
    sm = sys.argv[1].lower()
    begin_state = sys.argv[2].split(",")
    begin_state = tuple(map(int, begin_state))
    size = int(math.sqrt(len(begin_state)))
    hard_state = PuzzleState(begin_state, size)
    start = time.time()
    if sm == "bfs":
        expanded, goal, level, m_level = bfs_search(hard_state)
    elif sm == "dfs":
        expanded, goal, level, m_level = dfs_search(hard_state)
    elif sm == "ast":
        expanded, goal, level, m_level = A_star_search(hard_state)
    else:
        print("Enter valid command arguments !")
    end = time.time()
    writeOutput(get_path_to_goal(goal), goal.cost, expanded,
                level, m_level, end - start)

if __name__ == '__main__':
    main()
