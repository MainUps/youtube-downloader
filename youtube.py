from pytube import YouTube



YouTube(input("URL : ")).streams.first().download(r"C:\Users\UserK\Documents\유튭mp3")
print("성공!")
