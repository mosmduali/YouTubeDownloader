import os
import sys

from pytube import YouTube, Playlist
from pytube.exceptions import VideoUnavailable, RegexMatchError

# Konsol temizleme fonksiyonu
clear_console = lambda: os.system('cls')

# Ana menü fonksiyonu
def main():
    print("""
[1]. Video (.mp4)
[2]. Sound (.mp3)
[3]. Playlist Video (.mp4)
[4]. Playlist Sound (.mp3)
[5]. Banner
[0]. Exit
    """)
    inp = input("Lütfen, bir numara girin: ")
    if inp == '0':
        sys.exit()
    elif inp == '1':
        downloadYouTubeVideo()
    elif inp == '2':
        downloadYouTubeMusic()
    elif inp == '3':
        downloadYouTubePlayListVideos()
    elif inp == '4':
        downloadYouTubePlayListSounds()
    elif inp == '5':
        banner()
    else:
        main()

# YouTube Video İndirme Fonksiyonu
def downloadYouTubeVideo():
    try:
        ytLink = YouTube(input("YouTube üzerindeki ilgili içeriğin linkini giriniz: ").strip())
        print(f'"{ytLink.title}" Video dosyası indiriliyor...')
        ytLink.streams.get_highest_resolution().download("Videos")
        clear_console()
        print(f'"{ytLink.title}" İndirme işlemi başarıyla tamamlandı!')
    except RegexMatchError:
        input("[!] Üzgünüm, belirtilen link geçersiz veya eksik. (Herhangi bir tuşa basın): ")
        clear_console()
        downloadYouTubeVideo()
    except VideoUnavailable:
        input("[!] Üzgünüm, belirtilen linkteki videoya şu an erişilemiyor. (Herhangi bir tuşa basın):")
        clear_console()
        downloadYouTubeVideo()

# YouTube Müzik İndirme Fonksiyonu
def downloadYouTubeMusic():
    try:
        ytLink = YouTube(input("YouTube üzerindeki ilgili içeriğin linkini giriniz: ").strip())
        print(f'"{ytLink.title}" Ses dosyası indiriliyor...')
        mp3 = ytLink.streams.filter(only_audio=True).first().download("Sounds")

        convertToMp3(mp3)
        clear_console()
        print(f'"{ytLink.title}" İndirme işlemi başarıyla tamamlandı!')
    except RegexMatchError:
        input("[!] Üzgünüm, belirtilen link geçersiz veya eksik. (Herhangi bir tuşa basın): ")
        clear_console()
        downloadYouTubeVideo()
    except VideoUnavailable:
        input("[!] Üzgünüm, belirtilen linkteki videoya şu an erişilemiyor. (Herhangi bir tuşa basın):")
        clear_console()
        downloadYouTubeVideo()

# YouTube Çalma Listesi Video İndirme Fonksiyonu
def downloadYouTubePlayListVideos():
    try:
        ytLink = Playlist(input("Lütfen YouTube çalma listesi linkini giriniz: ").strip())
        lenPlaylist = len(ytLink)
        print(f"'{ytLink.title}' çalma listesi'ndeki '{lenPlaylist}' video indirme işlemi başlatıldı...")
        x = 1
        for video in ytLink.videos:
            video.streams.get_highest_resolution().download(f"PlaylistVideos/{ytLink.title}")
            print(f"{x}. '{video.title}' indirildi.")
            x += 1
        clear_console()
        print(f'"{ytLink.title}" çalma listesi İndirme işlemi başarıyla tamamlandı!')
    except KeyError:
        input("[!] Üzgünüm, hatalı bir giriş yaptınız. (Herhangi bir tuşa basın): ")
        clear_console()
        downloadYouTubeVideo()
    except RegexMatchError:
        input("[!] Üzgünüm, belirtilen link geçersiz veya eksik. (Herhangi bir tuşa basın): ")
        clear_console()
        downloadYouTubeVideo()
    except VideoUnavailable:
        input("[!] Üzgünüm, belirtilen linkteki videoya şu an erişilemiyor. (Herhangi bir tuşa basın):")
        clear_console()
        downloadYouTubeVideo()

# YouTube Çalma Listesi Ses İndirme Fonksiyonu
def downloadYouTubePlayListSounds():
    try:
        ytLink = Playlist(input("Lütfen YouTube çalma listesi linkini giriniz: ").strip())
        lenPlaylist = len(ytLink)
        print(f"'{ytLink.title}' çalma Listesi'ndeki '{lenPlaylist}' ses indirilmeye başlandı...")
        x = 1
        for video in ytLink.videos:
            mp3 = video.streams.filter(only_audio=True).first().download(f"PlaylistSounds/{ytLink.title}")
            convertToMp3(mp3)
            print(f"{x}. '{video.title}' indirildi.")
            x += 1
        clear_console()
        print(f'"{ytLink.title}" çalma listesi İndirme işlemi başarıyla tamamlandı!')
    except KeyError:
        input("[!] Üzgünüm, hatalı bir giriş yaptınız. (Herhangi bir tuşa basın): ")
        clear_console()
        downloadYouTubeVideo()
    except RegexMatchError:
        input("[!] Üzgünüm, belirtilen link geçersiz veya eksik. (Herhangi bir tuşa basın): ")
        clear_console()
        downloadYouTubeVideo()
    except VideoUnavailable:
        input("[!] Üzgünüm, belirtilen linkteki videoya şu an erişilemiyor. (Herhangi bir tuşa basın):")
        clear_console()
        downloadYouTubeVideo()

# .mp4 dosyasını .mp3'e çeviren fonksiyon
def convertToMp3(mp3):
    base, ext = os.path.splitext(mp3)
    to_mp3 = base + ".mp3"
    os.rename(mp3, to_mp3)

# Gerekli klasörleri oluşturan fonksiyon
def createFolder():
    if not os.path.exists("Sounds"):
        os.mkdir("Sounds")
    if not os.path.exists("Videos"):
        os.mkdir("Videos")
    if not os.path.exists("PlaylistVideos"):
        os.mkdir("PlaylistVideos")
    if not os.path.exists("PlaylistSounds"):
        os.mkdir("PlaylistSounds")


def banner():
    input("""
*******************************************
*            My Python Project            *
*******************************************
     github.com/mosmduali 
         linkedin.com/in/mosmduali/
             instagram.com/mosmanduali
                 t.me/mosmduali       
*******************************************
> (Herhangi bir tuşa basın): """)
    clear_console()


# Ana döngü
while True:
    if __name__ == "__main__":
        main()
