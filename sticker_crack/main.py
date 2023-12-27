from sticker_crack.crack_images import ImageCracker

if __name__ == '__main__':
    image_cracker = ImageCracker()
    input_path = '../files/cut'
    files = image_cracker.get_files_with_ext(input_path, 'png')
    for input_image_path in files:
        image_cracker.deal_pic(input_image_path)
        image_cracker.deal_pic(input_image_path, pixel_w=50, pixel_h=50, output_dir='../files/50x50')
    print('end')
