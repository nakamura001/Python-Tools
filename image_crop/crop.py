#! /usr/bin/env python
# coding: utf-8

# 「画像ファイルの一部切り取り」＆「ファイル名を画像に記述」

import os,re,sys
import tempfile
import shutil
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

in_dir = "images"
out_dir = "crop_images"
image_size = 320
count = 0

fontFile = '../M+/mplus-1c/mplus-1c-regular.ttf'

font_size = 24
font = ImageFont.truetype(fontFile, font_size, encoding='utf-8')
for (root, dirs, files) in os.walk(in_dir):
  for f in files:
    d, ext = os.path.splitext(f)
    if ext == '':
     continue
    in_file = os.path.join(in_dir, f)
    if not os.path.exists(out_dir):
      os.mkdir(out_dir)
    out_file = os.path.join(out_dir, d+'.png')
    print out_file
    im = Image.open(in_file)
    x = 175
    y = 0
    w = 275
    h = 320
    offset_y = 224
    box = (x, y+offset_y, x+w, y+h+offset_y)
    im2 = im.crop(box)
    draw = ImageDraw.Draw(im2)
    output_name = os.path.basename(out_file)
    output_name = os.path.splitext(f)[0]
    img_h = im2.size[1]
    w, h = draw.textsize(output_name, font=font)
    w = w + 6
    h = h + 6
    draw.rectangle([0, img_h-h, w, img_h], fill=(0,0,0))
    draw.text((3, img_h-h+5), output_name, fill=(255,255,255), font=font)
    im2.save(out_file)
    