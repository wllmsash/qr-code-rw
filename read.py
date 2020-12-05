#!/usr/bin/env python3

from argparse import ArgumentParser
from PIL import Image
from pyzbar.pyzbar import decode

parser = ArgumentParser(
  description='Read QR code')
parser.add_argument(
  'image_path',
  metavar='image_path',
  type=str,
  help='Image path')

args = parser.parse_args()

results = decode(Image.open(args.image_path, mode='r'))

for i, result in enumerate(results): 
  value = result.data.decode('utf-8')
  print('[' + str(i) + ']: ' + value)