import os

# 현재 스크립트가 실행되고 있는 폴더 가져오기
current_directory = os.path.dirname(os.path.abspath(__file__))

# 현재 디렉토리의 모든 파일과 폴더 나열
try:
    items = os.listdir(current_directory)
    print(f'file ({current_directory}):')

    for item in items:
        item_path = os.path.join(current_directory, item)  # 전체 경로 생성
        if os.path.isdir(item_path):
            print(f'    {item} (folder)')
        elif os.path.isfile(item_path):
            if item.endswith('.txt'):
                print(f'    {item} (file .txt)')
            else:
                print(f'    {item}')
except Exception as e:
    print(f'error: {e}')
