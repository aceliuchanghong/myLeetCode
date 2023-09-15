# 假设输入二维数组代表一张位图，元素的不同整数值代表不同颜色，先输入位置（x，y），
# 同时用一个新的颜色A替换原有颜色B，并且向周边（上下前后四个方向）替换颜色，直到遇上新的颜色A为止，以形成一个单色的区域。
from fromBook.util import genBitMap as gb

length, width, max_value = 7, 6, 10
myBitMap = gb.genIt(length, width, max_value)


def replace_color(bitmap, x, y, new_color):
    # 获取原始颜色
    original_color = bitmap[x][y]

    # 如果新颜色与原始颜色相同，则无需替换
    if original_color == new_color:
        return
    bitmap[x][y] = new_color
    if y > 0 and bitmap[x][y - 1] == original_color:
        replace_color(bitmap, x, y - 1, new_color)
    if y < len(bitmap[0]) - 1 and bitmap[x][y + 1] == original_color:
        replace_color(bitmap, x, y + 1, new_color)
    if x > 0 and bitmap[x - 1][y] == original_color:
        replace_color(bitmap, x - 1, y, new_color)
    if x < len(bitmap) - 1 and bitmap[x + 1][y] == original_color:
        replace_color(bitmap, x + 1, y, new_color)


# OLD
for row in myBitMap:
    print(row)
# 变换
x, y, new_color = 3, 3, 7
print(myBitMap[x][y])
replace_color(myBitMap, x, y, new_color)
for row2 in myBitMap:
    print(row2)

bitmap = [
    [1, 1, 2, 2, 2],
    [1, 1, 1, 2, 2],
    [3, 3, 3, 3, 2],
    [3, 3, 3, 2, 2],
    [3, 3, 3, 2, 2]
]

replace_color(bitmap, 2, 2, 4)
for row3 in bitmap:
    print(row3)
