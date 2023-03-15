# 使い方
# python3 py_seach_str.py
import subprocess
import re

log_data = r"""
:441:[23-03-15 03:00:12] staging.DEBUG - test\test\test\test\test\test(64) - test.remove(): npo/dummy/dummy-npo-profile_6.png"""

base_url = 'https://www.sample.jp/'
# jpg、png、jpeg、webpの拡張子を持つファイル名を抽出する正規表現
file_extensions = ['jpg', 'png', 'jpeg', 'webp']

# 正規表現にマッチするファイル名を抽出
regex_pattern = '|'.join([f'{ext}' for ext in file_extensions])
file_list = re.findall(r'(?<=remove\(\): ).*\.(?:'+regex_pattern+')', log_data)

# BASIC認証がある場合
username = ""
password = ""
for url in file_list:
    print(base_url + url)
    # curlコマンドの生成
    command = ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', '--user', f'{username}:{password}', base_url + url]
    # curlコマンドの実行
    status_code = subprocess.check_output(command)
    print(f"Status code: {status_code.decode().strip()}")

