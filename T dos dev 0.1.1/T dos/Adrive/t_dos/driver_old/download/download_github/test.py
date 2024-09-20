import os
import pathlib
import time
import requests            

# 바탕화면 경로와 저장할 폴더 이름
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
project_folder = os.path.join(desktop_path, f'download folder', "app")
# 저장할 폴더가 없으면 생성
if not os.path.exists(project_folder):
    os.makedirs(project_folder)
print('enter github raw link.')
file_url=input(':')
# 파일 다운로드
response = requests.get(file_url)
if response.status_code == 200:
     # 파일 이름 추출
    file_name = file_url.split("/")[-1]
    file_path = os.path.join(project_folder, file_name)            
    # 파일 저장
    with open(file_path, 'wb') as file:
        file.write(response.content)            
        print(f"{file_name}이 {project_folder}에 다운로드되었습니다.")
        time.sleep(1)
        print('다운로드가 완료되었습니다.')
else:
    print("파일 다운로드 중 오류 발생:", response.status_code)
    time.sleep(5)