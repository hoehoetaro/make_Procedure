import os
from PIL import Image, ImageDraw, ImageFont

def create_thumbnail(input_image_path, output_image_path, size=(1920, 1080)):
    # タイトル（ディレクトリ名）を取得します
    title = os.path.basename(os.getcwd()).replace("_", "\n")  # アンダースコアを改行に置き換えます

    # 画像を開きます
    original_image = Image.open(input_image_path)

    # 新しい背景画像を作成します（色はRGB形式で指定します）
    image = Image.new('RGB', size, "#00082F")
    draw = ImageDraw.Draw(image)

    # サムネイル画像に使用するフォントを選択します。
    font = ImageFont.truetype('Corporate-Logo-Bold-ver3.otf', 100)

    # テキストの位置を設定します。これはテキストが画像のどこに配置されるかを決定します。
    textbbox = draw.textbbox((0, 0), title, font=font)  # テキストの境界ボックスを取得します
    text_position = None

    # 元の画像が横長か縦長かに応じて処理を分けます
    if original_image.width > original_image.height:  # 横長の場合
        # 画像を読み込んで中央に配置します
        width_percent = 0.8  # 80%の横幅に設定
        new_width = int(size[0] * width_percent)
        new_height = int(new_width * original_image.height / original_image.width)
        resized_image = original_image.resize((new_width, new_height))  # アスペクト比を維持したままリサイズします
        image.paste(resized_image, ((size[0] - resized_image.width) // 2, (size[1] - resized_image.height) // 2))
        text_position = ((size[0] - textbbox[2]) / 2, 10)  # 上部中央
    else:  # 縦長の場合
        # 画像を読み込んで左に配置します
        height_percent = 0.8  # 80%の縦幅に設定
        new_height = int(size[1] * height_percent)
        new_width = int(new_height * original_image.width / original_image.height)
        resized_image = original_image.resize((new_width, new_height))  # アスペクト比を維持したままリサイズします
        image.paste(resized_image, ((size[0] - size[0] // 2 - resized_image.width) // 2, (size[1] - resized_image.height) // 2))
        text_position = (size[0] / 2 + (size[0] / 2 - textbbox[2]) / 2, (size[1] - textbbox[3]) / 2)  # 右半分の中央

    draw.multiline_text(text_position, title, fill=(255, 255, 255), font=font, align='center')  # multiline_textを使うことで複数行のテキストを描画できます

    # サムネイル画像を保存します
    image.save(output_image_path)

# Pythonスクリプトが置かれているディレクトリにカレントディレクトリを変更します
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# フォルダ名を取得
folder_name = os.path.basename(os.getcwd())

# 以下の関数を呼び出すことで、上記の処理を実行します。
create_thumbnail('thumb.png', f'{folder_name}_thumbnail.png')
