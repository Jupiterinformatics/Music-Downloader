from pytube import YouTube 

def müzikindir():
    y = YouTube(input("müzik bağlantısını yapıştırın : "))
    müzik = y.streams.filter(only_audio=True).first()
    müzik.download()

müzikindir()
print("_______________________________")
print("indirme işlemi tamamlandı..")