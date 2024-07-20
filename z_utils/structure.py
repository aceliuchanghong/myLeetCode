# pip install easy-media-utils
from tree_utils.struct_tree_out import print_tree

path = r'../../myLeetCode'
exclude_dirs_set = {
    'using_files', '__init__.py', 'static', 'LICENSE', 'test', 'eng_learn', 'sticker_crack',
    'web_crack', 'z_my_thoughts', 'z_utils', 'fromBook'
}
print_tree(directory=path, exclude_dirs=exclude_dirs_set)
