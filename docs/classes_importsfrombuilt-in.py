# 이미 instance화가 되어있는 상태 (built-in)
import os

# 현재 폴더 위치 CLI : pwd(현재 폴더 명령어)
current_folder = os.getcwd() # 바로 부를수 있음
print("현재 실행되는 python 위치 : {}".format(current_folder)) 

# 현재 폴더에 있는 파일과 폴더 리스트 출력
file_folder_list = os.listdir(current_folder)
print('파일과 폴더 리스트 : {}'.format(file_folder_list))
pass