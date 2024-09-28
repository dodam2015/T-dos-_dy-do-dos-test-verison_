import os

# 현재 작업 디렉토리 가져오기
current_directory = os.getcwd()

# 만들 폴더 경로
new_folder_path = os.path.join(current_directory, 'make_folder')

# 폴더 생성
try:
    os.makedirs(new_folder_path, exist_ok=True)  # exist_ok=True로 기존 폴더가 있어도 오류 발생 안 함
except Exception as e:
    print(f'error: {e}')
