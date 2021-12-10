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
  img = Image.open("img.jpeg")
  result = get_pghi(img, (33,150,243), "Roboto-Regular.ttf", 30, text)

  result.save("temp.jpeg")

app = Flask(__name__)

@app.route("/")
def index():
  return "<a href='https://nvcoder.pythonanywhere.com/'>Made by NVcoder!</a>"

@app.route("/img/<rnd>.jpeg")
def send_img(rnd):
  ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
  generate_img(ip)
  return send_file("temp.jpeg")
