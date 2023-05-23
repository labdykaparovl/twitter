from PIL import Image, ImageDraw, ImageFont

file_path = 'media/jelly.png'

image = Image.open(file_path)


#показать изображение
# image.show()


#обрезка изображения
# cropped_image = image.crop((0, 80, 200, 400))
# cropped_image.save('media/jelly_cropped.png')


#поворот изображения
# rotated_image = image.rotate(90)
# rotated_image.save('media/rotated_jelly.png')



#написание текста на изоб
# img_draw = ImageDraw.Draw(image)
#
#
# text = 'This is Codify Property'
# font = ImageFont.truetype('arial.ttf', size=32)
#
# img_draw.text((10, 10), text, font=font)
# image.save('media/jelly_watermark.png')


#конвертация изображения
# image = image.convert('RGB')
# image.save('media/jelly.jpg', 'JPEG')


#изменение разрешения
# image_resized = image.resize((400, 400))
# image_resized.save('media/jelly_resized.png')



#изменение разрешения
# width, height = image.size
# new_height = 300
# new_width = int(width * new_height / height)
#
# image_resized = image.resize(
#     (new_width, new_height)
# )
# image_resized.save('media/jelly_correct_resize.png')



width, height = image.size
new_width = 400
new_height = int(height * new_width / width)

image_resized = image.resize(
    (new_width, new_height)
)
image_resized.save('media/jelly_correct_resize.png')