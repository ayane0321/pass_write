import os
from pathlib import Path

img_dir_name = input('Input image directory name:')

#絶対パスを取得
file = os.path.abspath(img_dir_name)
print(file)

basename = os.path.basename(file)
split = basename.split('.')

#fileに入れた絶対パスのPathオブジェクトを生成
ppath = Path(file)
#file直下のファイルとディレクトリを取得してリストにする
list1 = list(ppath.glob("*"))

with open(split[0] + '.txt','w') as f:
    for tmp in list1:
        list_lines = str(tmp)
        f.write(list_lines)
        f.write('\n')