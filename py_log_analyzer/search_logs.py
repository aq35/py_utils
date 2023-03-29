# 使い方
# python3 ./py_log_analyzer/search_logs.py [検索パス] [検索ワード] [出力ファイル]
# python3 ./py_log_analyzer/search_logs.py <directory> <keyword> <output_file>
# python3 ./py_log_analyzer/search_logs.py ./py_log_analyzer/sample "local.ERROR" debug_all.log
import os
import sys

# 引数の数を確認する
if len(sys.argv) != 4:
    print("Usage: python search_logs.py <directory> <keyword> <output_file>")
    sys.exit(1)

# 引数からディレクトリ、キーワード、出力ファイル名を取得する
directory = sys.argv[1]
keyword = sys.argv[2]
output_file = sys.argv[3]

# 対応するエンコーディングリストを定義
encodings = ['utf-8', 'shift-jis', 'euc-jp', 'iso-2022-jp', 'us-ascii']

# ディレクトリ内のlogファイルとtxtファイルを検索する
matches = []
for root, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        _, extension = os.path.splitext(filename)
        if extension == '.log' or extension == '.txt' or not extension:
            # ファイル内のキーワードを検索する
            for encoding in encodings:
                try:
                    with open(os.path.join(root, filename), encoding=encoding) as f:
                        for i, line in enumerate(f):
                            if keyword in line:
                                matches.append(f"{os.path.join(root, filename)}:{i+1}:{line.strip()}")
                except UnicodeDecodeError:
                    print('aa')
                    pass

# 一致した行をファイルに出力する
if matches:
    with open(output_file, 'w') as f:
        for match in matches:
            f.write(f"{match}\n")
else:
    print('No matches found.')