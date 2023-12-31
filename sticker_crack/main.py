from sticker_crack.crack_images import ImageCracker

if __name__ == '__main__':
    """
横幅==>750x400
https://cdn.discordapp.com/attachments/1088864336006631466/1190981820699910144/lawrence_aceliuchanghong_Illustrate_an_emotive_2D_white_cat_emo_5ef39d7d-bfc9-43e6-bc50-5e4795fb31ab.png?ex=65a3c741&is=65915241&hm=14e4fd6296f99a61907e4bab5d28ff83dfc634002e767fcc4a7f5fb2c326d92d& Create a 2D emoticon of a white cat on a 100% white background, with ears pressed close to its head, blinking eyes, and a slightly open mouth that conveys shyness and timidity. The cat's body should be subtly turned to the side, its tail gently swaying, with paws hidden behind its back, as if shyly introducing itself. The emoticon should radiate a sense of bashfulness, complemented by the words "Hi there, I'm a little shy..." to reflect the cat's introverted personality.  in the style of animated shapes,simple, meme art, animated gifs, chibi, sticker --ar 15:8 --style raw --iw 2
赞赏引导图==>750x560
https://cdn.discordapp.com/attachments/1088864336006631466/1190981820699910144/lawrence_aceliuchanghong_Illustrate_an_emotive_2D_white_cat_emo_5ef39d7d-bfc9-43e6-bc50-5e4795fb31ab.png?ex=65a3c741&is=65915241&hm=14e4fd6296f99a61907e4bab5d28ff83dfc634002e767fcc4a7f5fb2c326d92d& Create a 2D emoticon of a white cat on a 100% white background, with ears pressed close to its head, blinking eyes, and a slightly open mouth that conveys shyness and timidity. The cat's body should be subtly turned to the side, its tail gently swaying, with paws hidden behind its back, as if shyly introducing itself. The emoticon should radiate a sense of bashfulness, complemented by the words "Thankyou!!" to reflect the cat's introverted personality.  in the style of animated shapes,simple, meme art, animated gifs, chibi, sticker --ar 15:11 --style raw --iw 2
赞赏致谢图==>750x750
https://cdn.discordapp.com/attachments/1088864336006631466/1190981820699910144/lawrence_aceliuchanghong_Illustrate_an_emotive_2D_white_cat_emo_5ef39d7d-bfc9-43e6-bc50-5e4795fb31ab.png?ex=65a3c741&is=65915241&hm=14e4fd6296f99a61907e4bab5d28ff83dfc634002e767fcc4a7f5fb2c326d92d& Create a 2D emoticon of a white cat on a 100% white background, with ears pressed close to its head, blinking eyes, and a slightly open mouth that conveys shyness and timidity. The cat's body should be subtly turned to the side, its tail gently swaying, with paws hidden behind its back, as if shyly introducing itself. The emoticon should radiate a sense of bashfulness, complemented by the words "Thankyou!!" to reflect the cat's introverted personality.  in the style of animated shapes,simple, meme art, animated gifs, chibi, sticker --ar 1:1 --style raw --iw 2
    """
    image_cracker = ImageCracker()
    input_image_path_heng = '../files/other/750x400.png'
    input_image_path_zang = '../files/other/750x560.png'
    input_image_path3 = '../files/other/750x750.png'

    input_image_path_heng_2 = '../files/240x240/750x400_pixeled.png'
    input_image_path_zang_2 = '../files/240x240/750x560_pixeled.png'
    input_image_path3_2 = '../files/240x240/750x750_pixeled.png'

    image_cracker.deal_pic(input_image_path_heng, 730, 380)
    image_cracker.deal_pic(input_image_path_zang, 730, 540)
    image_cracker.deal_pic(input_image_path3, 730, 730)

    image_cracker.add_black_border(input_image_path_heng_2, 10)
    image_cracker.add_black_border(input_image_path_zang_2, 10)
    image_cracker.add_black_border(input_image_path3_2, 10)
