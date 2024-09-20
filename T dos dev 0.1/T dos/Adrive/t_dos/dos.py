import time
import os
import pathlib
import requests   
import subprocess

version='dev 0.1'

#[
def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size

# 현재 스크립트가 위치한 디렉토리의 부모 디렉토리 경로
parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 부모 폴더의 용량 계산
folder_size = get_folder_size(parent_directory)

# 바이트 단위로 표시
folder_size_mb = folder_size / (1024 * 1024)
folder_size_kb = folder_size / 1024

# 용량 표시
if folder_size_mb <= 0:
    print(f"load A drive {folder_size_mb:.2f}MB/100mb")
elif folder_size_kb >= 0.99:
    print(f"load A drive {folder_size_kb:.2f}KB/100mb")
else:
    print(f"load A drive {folder_size}Byte/100mb")
#]


print('continue to wait 3s')
time.sleep(3)

print('Tdos is loading...')

# 현재 스크립트가 위치한 디렉토리 경로
script_directory = os.path.dirname(os.path.abspath(__file__))
user_directory = os.path.join(script_directory, "user")

# user 디렉토리 내의 폴더 읽기
if os.path.exists(user_directory):
    folders = [folder for folder in os.listdir(user_directory) if os.path.isdir(os.path.join(user_directory, folder))]
else:
    print("error")

user_name=folders

print()
print('loaded')
print()
print(f'welcome, {str(folders)}')
print()
cmd=0
while cmd!='shutdown -s -lo- -li-'or cmd!='exit':
    cmd=input('A:/')
    if cmd=='get Adrive capacity;':
        def get_folder_size(folder_path):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(folder_path):
                for filename in filenames:
                    file_path = os.path.join(dirpath, filename)
                    total_size += os.path.getsize(file_path)
            return total_size

        # 현재 스크립트가 위치한 디렉토리의 부모 디렉토리 경로
        parent_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # 부모 폴더의 용량 계산
        folder_size = get_folder_size(parent_directory)

        # 바이트 단위로 표시
        folder_size_mb = folder_size / (1024 * 1024)
        folder_size_kb = folder_size / 1024

        #용량 표시
        if folder_size_mb <= 0:
            print(f"capacity: {folder_size_mb:.2f}MB/100mb")
        elif folder_size_kb >= 0.99:
            print(f"capacity: {folder_size_kb:.2f}KB/100mb")
        else:
            print(f"capacity: {folder_size}Byte/100mb")

    elif cmd=='get github rawlink*download;':
        print('loading github system...')
        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))
        project_folder = os.path.join(script_directory, "user", "admin", "app")
        # 저장할 폴더가 없으면 생성
        if not os.path.exists(project_folder):
            os.makedirs(project_folder)
        print('enter github raw link.')
        print('help to {none}')
        file_url = input(':')
        # 파일 다운로드
        response = requests.get(file_url)
        if response.status_code == 200:
            # 파일 이름 추출
            file_name = file_url.split("/")[-1]
            file_path = os.path.join(project_folder, file_name)            
            
            # 파일 저장
            with open(file_path, 'wb') as file:
                file.write(response.content)            
                print('OK')
                time.sleep(1)
                print('download OK.')
        else:
            print("error:", response.status_code)
            time.sleep(5)
    elif cmd=='run python app;':
        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))
        app_directory = os.path.join(script_directory, "user", "admin", "app")

        # 사용자로부터 파일 이름 입력 받기
        file_name = input("enter app name (don't enter .py) :")
        print()
        # 파일 경로 생성
        file_path = os.path.join(app_directory, f"{file_name}.py")

        # 파일이 존재하는지 확인하고 실행
        if os.path.exists(file_path):
            subprocess.run(["python3", file_path])  # Python 3.x를 사용하고 있다면 'python' 대신 'python3'를 사용할 수 있습니다.
        else:
            print(f"error: {file_name}.py")
    elif cmd=='get dir app;':
        # 현재 스크립트가 위치한 디렉토리 경로
        script_directory = os.path.dirname(os.path.abspath(__file__))
        app_directory = os.path.join(script_directory, "user", "admin", "app")

        # app 디렉토리 내의 모든 파일 읽기
        if os.path.exists(app_directory):
            files = [file for file in os.listdir(app_directory) if os.path.isfile(os.path.join(app_directory, file))]
    
            print("dir of user/admin/app:")
            for file in files:
               print('  '+file)
        else:
            print("error not.founded.folder")
    elif cmd=='help' or cmd=='get help;':
        print('index of cmd/help')
