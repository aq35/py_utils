# 使い方
# python3 ./py_log_analyzer/search_logs.py [検索パス] [検索ワード] [出力ファイル]
# python3 ./py_log_analyzer/search_logs.py <directory> <keyword> <output_file>
# python3 ./py_log_analyzer/search_logs.py ./sample "local.ERROR" debug_all.log
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

# ディレクトリ内のlogファイルを検索する
matches = []
for root, dirnames, filenames in os.walk(directory):
    for filename in filenames:
        if filename.endswith('.log'):
            # logファイル内のキーワードを検索する
            with open(os.path.join(root, filename), 'r') as f:
                for i, line in enumerate(f):
                    if keyword in line:
                        matches.append(f"{os.path.join(root, filename)}:{i+1}:{line.strip()}")

# 一致した行をファイルに出力する
if matches:
    with open(output_file, 'w') as f:
        for match in matches:
            f.write(f"{match}\n")
else:
    print('No matches found.')