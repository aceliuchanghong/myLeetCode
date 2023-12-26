# 给出一个二维的图，图上有很多点，找出一条穿过最多点的直线
# 对于图中的每一对点 ( (x_1, y_1) ) 和 ( (x_2, y_2) )，计算它们之间的斜率。
# 注意，如果 ( x_2 ) 和 ( x_1 ) 相等，斜率是无限的，这意味着直线是垂直的。
# 使用一个哈希表（或字典）来存储每个斜率对应的点的数量。键是斜率，值是一个列表，列表中包含具有该斜率的所有点对。
# 对于每个点，计算它与其他所有点形成的直线的斜率，并更新哈希表。
# 遍历哈希表，找到具有最多点对的斜率。
# 返回穿过最多点的直线的斜率和截距。
from collections import defaultdict
import math


def max_points_on_a_line(points):
    def get_slope_and_intercept(p1, p2):
        if p1[0] == p2[0]:  # Vertical line
            return math.inf, p1[0]  # Slope is infinity, intercept is x-value
        else:
            slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
            intercept = p1[1] - slope * p1[0]  # y = mx + b => b = y - mx
            return slope, intercept

    n = len(points)
    if n < 2:
        return None

    max_points = 0
    best_line = (0, 0)  # Placeholder for slope, intercept
    for i in range(n - 1):
        lines = defaultdict(int)
        duplicates = 0
        cur_max_points = 1
        for j in range(i + 1, n):
            if points[i] == points[j]:
                duplicates += 1
                continue
            slope, intercept = get_slope_and_intercept(points[i], points[j])
            lines[(slope, intercept)] += 1
            cur_max_points = max(cur_max_points, lines[(slope, intercept)])

        cur_max_points += duplicates
        if cur_max_points > max_points:
            max_points = cur_max_points
            best_line = max(lines, key=lines.get)  # Get the line with the most points

    return best_line, max_points


# 自己写的,明显有问题
def max_points_on_a_line2(points):
    def get_slope(p1, p2):
        if p1[0] == p2[0]:
            return math.inf
        else:
            return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def get_line(p1, p2):
        slope = get_slope(p1, p2)
        little_b = p2[1] - slope * p2[0]
        return [slope, little_b]

    def get_nums(points):
        pass

    n = len(points)
    if n < 2:
        return None
    # 初始化一个set
    my_set = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            my_set.append(get_line(points[0], points[1]))


# Example usage:
points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (1, 2), (2, 3), (3, 4)]
line, num_points = max_points_on_a_line(points)
print(f"Line with most points: Slope = {line[0]}, Intercept = {line[1]}, Points = {num_points}")
