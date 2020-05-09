#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

# 打开一个jpg的图像文件，注意是当前路径
im = Image.open('./resources/test.jpg')
# 获得图像尺寸
w, h = im.size
print('Original image size: %sx%s' % (w, h))
# 缩放到50%
im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 把缩放后的图像用jpeg格式保存
im.save('./resources/thumbnail.jpg', 'jpeg')

# 模糊效果
# 打开一个jpg图像文件
im = Image.open('./resources/thumbnail.jpg')
# 应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('./resources/blur.jpg', 'jpeg')


# 生成随机验证码

# 随机字母
def rnd_char():
    return chr(random.randint(65, 90))


# 随机颜色
def rnd_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2
def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


# 240*60
width = 60 * 6
height = 60
# 新建一个画布
image = Image.new('RGB', (width, height), (255, 255, 255))
res_char = ''
# 创建font对象
font = ImageFont.truetype('./resources/arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())
# 输出文字
for t in range(6):
    temp = rnd_char()
    res_char += temp
    draw.text((60 * t + 10, 10), temp, font=font, fill=rnd_color2())
print('验证码是：%s' % res_char)
# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('./resources/code.jpg', 'jpeg')
