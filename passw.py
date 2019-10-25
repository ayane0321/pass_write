import os

#絶対パスを取得
file = os.path.abspath("")
print(file)

basename = os.path.basename(file)
split = basename.split('.')
with open(split[0] + '.txt','w')as f:
    f.write(file)