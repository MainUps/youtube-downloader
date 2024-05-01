from pytube import YouTube
import os


PATH = os.getcwd()


while True :
    link = input("유튜브 URL (종료 : exit): ")
    if link == "exit" :
        break
    
    youtube = YouTube(link)
    if youtube.age_restricted:
        print("해당 영상이 연령 제한 있어서 불가능합니다.")
        
    try:
        #youtube.streams.filter(only_audio=True).first().download(PATH)
        audio = youtube.streams.filter(only_audio=True).order_by('abr').last()
        audio.download(output_path=PATH)
        print("저장 성공")
    except Exception as e:
        print("에러 :", e)
