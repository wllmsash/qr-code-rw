#!/usr/bin/env python3

from argparse import ArgumentParser
from PIL import Image
from qrcode import make

parser = ArgumentParser(
  description='Create QR code from text')
parser.add_argument(
  'text',
  metavar='text',
  type=str,
  help='Text to encode')
parser.add_argument(
  'image_path',
  metavar='image_path',
  type=str,
  help='Image path')

args = parser.parse_args()

img = make(args.text)
img.save(args.image_path)
