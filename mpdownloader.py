from pytube import YouTube 

def indir():
    y = YouTube(input("bağlantı : "))
    ses = y.streams.filter(only_audio=True).first()
    ses.download()

indir()
print("_______________________________")
print("indirme işlemi tamamlandı..")
