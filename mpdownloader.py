from pytube import YouTube 

def indir():
    y = YouTube(input("müzik bağlantısını yapıştırın : "))
    ses = y.streams.filter(only_audio=True).first()
    ses.download()

indir()
print("_______________________________")
print("indirme işlemi tamamlandı..")
