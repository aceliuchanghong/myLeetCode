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
        # lines 是一个 defaultdict(int) 的实例。这意味着如果我们试图访问一个不存在的键，defaultdict 会自动创建这个键，并将其值初始化为 int() 的结果，即 0
        lines = defaultdict(int)
        duplicates = 1  # Start with 1 to count the point itself
        cur_max_points = 1  # 当前直线上最多点的数量，起始为 1
        for j in range(i + 1, n):
            if points[i] == points[j]:
                duplicates += 1  # 如果发现重复的点，则增加重复计数
                continue
            slope, intercept = get_slope_and_intercept(points[i], points[j])
            lines[(slope, intercept)] += 1  # 在字典中记录这条直线，增加经过的点的数量
            # 更新当前直线上的最大点数，考虑重复点的情况
            cur_max_points = max(cur_max_points, lines[(slope, intercept)] + duplicates)

        if cur_max_points > max_points:
            max_points = cur_max_points
            # 选出当前有最多点的直线，考虑重复点的情况
            best_line = max(lines, key=lambda k: lines[k] + duplicates)  # Get the line with the most points

    return best_line, max_points


# Example usage:
points = [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (1, 2), (2, 3), (3, 4)]
line, num_points = max_points_on_a_line(points)
print(f"Line with most points: Slope = {line[0]}, Intercept = {line[1]}, Points = {num_points}")
