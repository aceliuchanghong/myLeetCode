# Robot Navigation
#
# A robot needs move from top left corner to bottom right corner in a 2D map. In this map, there are 0s and 1s. 0 means the robot can pass and 1 means the wall.
#
# Please write a function that returns True or False, given at most k number of walls to demolish.
#
# Note: The robots can only move up, down, left, right.
#
# Example 1:
#
# Input: grid = [[0, 1 ,0], [0, 1, 0]], k = 0
# Output: False
# Explanation: The robot cannot demolish any wall due to k == 0, the robot cannot reach the bottom right corner.
#
# Example 2:
#
# Input: grid = [[0, 1, 0], [0, 1, 0]], k = 1
# Output: True
# Explanation: The robot can demolish the wall (0, 1) or (1, 1) to reach the destination.
#
# The function interface should be:
#
# def robot_navigation(grid: list[list[int]], k:int)->bool:
#     pass
grid = [[0, 1, 0], [0, 1, 0]]
k1 = 0
k2 = 1
# 类似 面试题72：二维数组最小路径和

def robot_navigation(grid: list[list[int]], k: int) -> bool:
    m, n = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x_position, y_position, walls_can_remove_nums, visited_positions):
        # 如果挨着
        if x_position == m - 1 and y_position == n - 1:
            return True

        for dx, dy in directions:
            # 往四周测试
            nx, ny = x_position + dx, y_position + dy
            # 由于在最左侧开始,设定起始为(0,0)
            if 0 <= nx < m and 0 <= ny < n and (nx, ny) not in visited_positions:
                if grid[nx][ny] == 1:
                    if walls_can_remove_nums > 0:
                        visited_positions.add((nx, ny))
                        if dfs(nx, ny, walls_can_remove_nums - 1, visited_positions):
                            return True
                        visited_positions.remove((nx, ny))
                else:
                    visited_positions.add((nx, ny))
                    if dfs(nx, ny, walls_can_remove_nums, visited_positions):
                        return True
                    visited_positions.remove((nx, ny))
        return False

    return dfs(0, 0, k, {(0, 0)})


print(robot_navigation(grid, k1))
print(robot_navigation(grid, k2))
