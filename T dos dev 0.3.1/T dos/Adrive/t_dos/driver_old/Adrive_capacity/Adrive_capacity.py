import os

def get_folder_size(folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            try:
                fp = os.path.join(dirpath, filename)
                total_size += os.path.getsize(fp)
            except Exception as e:
                print(f'파일 크기 가져오기 중 오류 발생: {fp} - {e}')
    return total_size

# 현재 폴더의 부모 폴더 경로 가져오기
current_directory = os.getcwd()
parent_directory = os.path.dirname(current_directory)  # 부모 폴더 경로

# 부모 폴더의 용량 계산
try:
    size = get_folder_size(parent_directory)
    print(f'부모 폴더의 용량: {size / (1024 * 1024):.2f} MB')  # MB 단위로 출력
except Exception as e:
    print(f'부모 폴더 용량 계산 중 오류 발생: {e}')
