import os

def replace_in_files(directory):
    # 디렉토리 내 모든 파일에 대해 반복
    for filename in os.listdir(directory):
        # 파일 경로 생성
        file_path = os.path.join(directory, filename)
        
        # 파일인지 디렉토리인지 확인
        if os.path.isfile(file_path):
            # 파일이면 읽어서 문자열 치환
            with open(file_path, 'r', encoding='utf-8') as file:
                file_content = file.read()
                
            # 문자열 치환
            new_content = file_content.replace(".mp4", ".mp3")
            
            # 변경된 내용을 다시 파일에 씀
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(new_content)

directory = os.getcwd()

replace_in_files(directory)

