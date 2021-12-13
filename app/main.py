from flask import Flask, send_file, request
from PIL import Image, ImageDraw, ImageFont
import os

print(os.listdir())

def get_pghi(img, text_color:tuple=(0, 0, 0), text_font:str="", text_size:int=20, text:str=""):
  fnt = ImageFont.truetype(text_font, text_size)
  draw = ImageDraw.Draw(img)

  _w, _h = img.size

  w, h = draw.textsize(text, font=fnt)

  draw.text(((_w-w)/2,(_h-h)/2), text, font=fnt, fill=text_color)

  return img

def generate_img(text):
  img = Image.open("app/img.jpeg")
  result = get_pghi(img, (33,150,243), "app/Roboto-Regular.ttf", 50, text)

  result.save("temp.jpeg")

app = Flask(__name__)

@app.route("/")
def index():
  return "<a href='https://nvcoder.pythonanywhere.com/'>Made by NVcoder!</a>"

@app.route("/img/<rnd>.jpeg")
def send_img(rnd):
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    ip = request.environ['REMOTE_ADDR']
  else:
    ip = request.environ['HTTP_X_FORWARDED_FOR']
  generate_img(ip)
  return send_file("../temp.jpeg")
