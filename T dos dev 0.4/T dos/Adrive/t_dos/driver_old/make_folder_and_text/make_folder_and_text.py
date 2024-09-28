import os

# 원하는 폴더 이름
folder_name = 'make_folder'
# 텍스트 파일 이름
file_name = 'example.txt'
# 파일 경로 설정
file_path = os.path.join(folder_name, file_name)

# 폴더 생성
try:
    os.makedirs(folder_name, exist_ok=True)  # exist_ok=True로 기존 폴더가 있어도 오류 발생 안 함
except Exception as e:
    print(f'error: {e}')

# 텍스트 파일 생성 및 내용 작성
try:
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write('ex')
except Exception as e:
    print(f'error: {e}')
