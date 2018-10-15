def calculate_manhattan_dist(puzzle_state):
    """calculate the manhattan distance of a tile"""
    total_diff = 0
    for i, num in enumerate(puzzle_state.config):
        total_diff += abs(i - num)
    return total_diff
