import os
import re

def extract_titles(directory):
    titles = []
    # ディレクトリ内の全ての.mdファイルを走査
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                # テストのタイトルを抽出
                match = re.search(r'^# テストのタイトル\s?\n\n?(.+)$', content, re.M)
                if match:
                    # ファイル名からテストIDを抽出
                    test_id = filename.replace('.md', '')
                    titles.append((test_id, match.group(1), filename))
    # テストIDでソート
    titles.sort(key=lambda x: x[0])
    return titles

def update_readme(titles, readme_path):
    with open(readme_path, 'w', encoding='utf-8') as readme:
        readme.write('# テストの一覧\n\n')
        for test_id, title, filename in titles:
            readme.write(f'* [{test_id.replace("WAIC-TEST-", "")}: {title}]({filename})\n')

if __name__ == '__main__':
    directory = 'WAIC-TEST/HTML'  # Markdownファイルが格納されているディレクトリ
    readme_path = os.path.join(directory, 'README.md')  # README.mdのパス
    titles = extract_titles(directory)
    update_readme(titles, readme_path)