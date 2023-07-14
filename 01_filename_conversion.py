import os

# スクリプトのあるディレクトリに移動
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# フォルダ内の全ファイルを確認
for filename in os.listdir('.'):
    # 'Screenshot'で始まる '.png' ファイルを探す
    if filename.startswith('スクリーンショット') and filename.endswith('.png'):
        # ファイル名を 'Thumb.png' に変更
        os.rename(filename, 'thumb.png')
        break
