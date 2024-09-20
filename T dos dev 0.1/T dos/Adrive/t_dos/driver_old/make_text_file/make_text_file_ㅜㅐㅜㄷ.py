# 파일 이름
file_name = 'example.txt'

# 파일 열기 (쓰기 모드)
with open(file_name, 'w', encoding='utf-8') as file:
    # 파일에 내용 작성
    file.write('make file ex')

