from PIL import Image, ImageDraw, ImageFont
import subprocess


#テキスト
print("== プロセカ風宣伝画像ジェネレーター --------------------")
print("   制作:はるくん (@halkun19)")
print("   バージョン: 0.1")
print("")
print("   pjsekai-background-gen:名無し。(@sevenc_nanashi)")
print("")
print("   初めて作ったアプリケーションなので、")
print("   バグがあっても見逃してやってくださいm(_ _)m")
print("   あまりに致命的だったら頑張って直しますので")
print("   僕のDMなどで教えていただけるとありがたいです")
print("--------------------------------------------------------")


#下準備
cover_img = Image.open("resource/template.png")

title_font = ImageFont.truetype('resource/font/bold.ttf', 100)
composer_font = ImageFont.truetype('resource/font/thin.ttf', 48)
singer_font = ImageFont.truetype('resource/font/thin.ttf', 38)

jacket_path = input("ジャケットのパスを入力してください：")
title = input("楽曲のタイトルを入力してください：")
lyricer = input("作詞者を入力してください：")
composer = input("作曲者を入力してください：")
mixer = input("編曲者を入力してください：")
singer = input("歌手を入力してください：")


#前面画像処理
draw = ImageDraw.Draw(cover_img)
draw.text((771, 335), title, "white", font=title_font, anchor='lm')
draw.text((921, 490), lyricer, "white", font=composer_font, anchor='lm')
draw.text((921, 594), composer, "white", font=composer_font, anchor='lm')
draw.text((921, 697), mixer, "white", font=composer_font, anchor='lm')
draw.text((1474, 930), singer, "#545776", font=singer_font, anchor='mm')


jacket_img = Image.open(jacket_path)

img_resize = jacket_img.resize((680, 680), Image.LANCZOS)
img_resize.save("resource/resize_jacket.png")

resize_jacket = Image.open("resource/resize_jacket.png")
cover_img.paste(resize_jacket, (50, 47))
cover_img.save("resource/cover.png")


#背景画像処理
subprocess.run("pjsekai-background-gen-by-nanashi.exe resource/resize_jacket.png")

bg_img = Image.open("resource/resize_jacket.output.png")
bg_img = bg_img.resize((2550, 1455), Image.LANCZOS)
bg_img_crop = bg_img.crop((315, 90, 2235, 1170))
bg_img_resize = bg_img_crop.resize((1920, 1080), Image.LANCZOS)
bg_img_resize.save("resource/bg.png")


#結合
bg = Image.open("resource/bg.png").convert("RGBA")
cover = Image.open("resource/cover.png").convert("RGBA")
dummy = Image.new("RGBA", bg.size, (255, 255, 255, 0))

dummy.paste(cover)

bg = Image.alpha_composite(bg, dummy)
bg.save("result.png")


print("画像が生成されました")
