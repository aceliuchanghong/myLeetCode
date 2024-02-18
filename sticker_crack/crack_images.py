import subprocess
import os
from pathlib import Path


class ImageCracker:
    def deal_pic(self, input_image_path, pixel_w=240, pixel_h=240, output_dir='../files/240x240'):
        # 获取输入图片的文件名和扩展名
        base_name = os.path.basename(input_image_path)
        file_name, file_ext = os.path.splitext(base_name)

        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 构建输出图片的路径
        output_image = os.path.join(output_dir, f"{file_name}_pixeled{file_ext}")

        # 构建ffmpeg命令
        ffmpeg_cmd = [
            'ffmpeg',
            '-y',  # 覆盖输出文件而不询问
            '-i', input_image_path,  # 输入图片路径
            '-vf', f'scale={pixel_w}:{pixel_h}:flags=lanczos,unsharp=5:5:1.0:5:5:0.0',  # 设置目标分辨率和锐化
            output_image  # 输出图片路径
        ]

        # 执行ffmpeg命令
        try:
            subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

    def get_files_with_ext(self, directory='../files/original', ext='png'):
        directory_path = Path(directory)

        # 使用glob方法列出所有匹配的文件路径
        image_files = list(directory_path.glob(f"*.{ext}"))

        # 将路径对象转换为统一格式的字符串列表
        image_files_str = [str(file).replace('\\', '/') for file in image_files]

        return image_files_str

    def crop_image(self, input_path, output_dir, crop_width, crop_height):
        # 构建输出文件路径
        output_path = os.path.join(output_dir, os.path.basename(input_path))
        output_path = output_path.replace('\\', '/')  # 确保使用'/'作为路径分隔符
        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        # 构建ffmpeg命令
        # 假设我们要从每一边裁剪相同的宽度/高度
        crop_filter = f"crop=in_w-{2 * crop_width}:in_h-{2 * crop_height}"
        cmd = [
            'ffmpeg',
            '-i', input_path,
            '-vf', crop_filter,
            '-y',  # 覆盖输出文件
            output_path
        ]

        # 执行ffmpeg命令
        try:
            subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # 如果执行成功，什么也不输出
        except subprocess.CalledProcessError as e:
            # 如果ffmpeg处理出错，则输出错误信息
            print(f"Error occurred: {e.stderr.decode().strip()}")

        return output_path

    def add_black_border(self, input_image_path, border_size, output_dir='../files/with_border'):
        # 获取输入图片的文件名和扩展名
        base_name = os.path.basename(input_image_path)
        file_name, file_ext = os.path.splitext(base_name)

        # 确保输出目录存在
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 构建输出图片的路径
        output_image = os.path.join(output_dir, f"{file_name}_bordered{file_ext}")

        # 构建ffmpeg命令
        ffmpeg_cmd = [
            'ffmpeg',
            '-y',  # 覆盖输出文件而不询问
            '-i', input_image_path,  # 输入图片路径
            '-vf',
            f'pad=width=iw+{2 * border_size}:height=ih+{2 * border_size}:x={border_size}:y={border_size}:color=black',
            # 添加黑色边框
            output_image  # 输出图片路径
        ]

        # 执行ffmpeg命令
        try:
            subprocess.run(ffmpeg_cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")

        return output_image  # 返回带边框的图片路径


if __name__ == '__main__':
    image_cracker = ImageCracker()
    input_path = '../files/original'
    input_path2 = '../files/240x240'
    input_path3 = '../files/cut'
    input_path4 = '../files/50x50'
    input_path5 = '../files/border_50x50'

    # 裁剪多余边框 到 input_path3
    for in1 in image_cracker.get_files_with_ext(input_path, 'png'):
        image_cracker.crop_image(in1, input_path3, 50, 50)
    print('end1')
    # 开始变换大小
    for in0 in image_cracker.get_files_with_ext(input_path3, 'png'):
        image_cracker.deal_pic(in0, 234, 234)
        image_cracker.deal_pic(in0, 48, 48, input_path4)
    print('end2')
    # 增加黑色边框1
    for input_image_path in image_cracker.get_files_with_ext(input_path2, 'png'):
        image_cracker.add_black_border(input_image_path, 3)
    print('end3')
    # 增加黑色边框2
    for in2 in image_cracker.get_files_with_ext(input_path4, 'png'):
        image_cracker.add_black_border(in2, 1, input_path5)
    print('end4')

    print('end')
