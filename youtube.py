from pytube import YouTube
import os

link = input("유튜브 URL : ")
youtube = YouTube(link)
PATH = os.getcwd()

if youtube.age_restricted:
    print("해당 영상이 연령 제한 있어서 불가능합니다.")
    
try:
    youtube.streams.filter(only_audio=True).first().download(PATH)
    print("저장 성공")
except Exception as e:
    print("에러 :", e)
