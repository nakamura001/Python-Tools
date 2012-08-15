#! /usr/bin/env python
# coding: utf-8

# 連番ファイルでダミー画像ファイルを作成

import os,re,sys
import random
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

in_dir = "images"
out_dir = "crop_images"
image_size_x = 128
image_size_y = image_size_x
create_num = 25

fontFile = '../M+/mplus-1c/mplus-1c-regular.ttf'

font_size = 24
font = ImageFont.truetype(fontFile, font_size, encoding='utf-8')

for i in range(create_num):
  out_file = 'img%dx%d_%d.png' % (image_size_x, image_size_y, i)
  print out_file
  img = Image.new('RGBA', (image_size_x, image_size_y), (255,255,255,255))
  draw = ImageDraw.Draw(img)
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  for y in range(image_size_y):
    s = float(y)/image_size_y
    draw.line((0, y, image_size_x, y), fill='rgb(%d,%d,%d)' % (r*s,g*s,b*s))
  draw.text((10, 10), str(i), fill=(255,255,255), font=font)
  img.save(out_file)
