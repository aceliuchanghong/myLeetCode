from sticker_crack.crack_images import ImageCracker

if __name__ == '__main__':
    image_cracker = ImageCracker()
    from0 = '../files/original'
    name = 'what\'s_up2'
    ext = 'png'
    input_path3 = '../files/cut'
    input_path4 = '../files/50x50'
    input_path2 = '../files/240x240'
    input_path5 = '../files/border_50x50'
    # 手动剪切了一下
    image_cracker.crop_image(from0 + "/" + name + "." + ext, input_path3, 10, 10)

    image_cracker.deal_pic(input_path3 + "/" + name + "." + ext, 234, 234)
    image_cracker.deal_pic(input_path3 + "/" + name + "." + ext, 48, 48, input_path4)

    image_cracker.add_black_border(input_path2 + "/" + name + "_pixeled." + ext, 3)
    image_cracker.add_black_border(input_path4 + "/" + name + "_pixeled." + ext, 1, input_path5)
