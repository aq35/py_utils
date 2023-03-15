# 使い方
# python3 search.py [検索ワード] [検索対象のファイル名]
# python3 search.py "staging.ERROR" debug.log
import re
import sys

# 引数の数を確認する
if len(sys.argv) < 3:
    print("Usage: python search.py [keyword] [filename]")
    sys.exit(1)

# 検索ワードとファイル名を取得する
keyword = sys.argv[1]
filename = sys.argv[2]

# ファイルを読み込んで、検索ワードにマッチする行を抽出する
with open(filename, 'r') as f:
    lines = f.readlines()
    matched_lines = [line for line in lines if re.search(keyword, line)]

# 抽出した行をファイルに書き出す
with open(f"{keyword}_matches.txt", 'w') as f:
    for line in matched_lines:
        f.write(line)