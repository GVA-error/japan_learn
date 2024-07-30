import time

def DOWNLOAD_FROM_YOUTUBE(urls):
    print("DOWNLOADING...")
    for url in urls:
        __DOWNLOAD_FROM_YOUTUBE(url)
    print("DOWNLOAD SUCCESS!")

def __DOWNLOAD_FROM_YOUTUBE(url):
    from pytube import YouTube
    yt = YouTube(url)  # ссылка на видео.
    # yt.stream показывает какое видео ты можешь скачать
    # (mp4(720) + audio или только mp4(1080) без звука).
    # Сейчас стоит фильтр по mp4.
    try:
        print(yt.streams.filter(file_extension='mp4'))
        stream = yt.streams.get_by_itag(22)  # выбираем по тегу, в каком формате будем скачивать.
        stream.download()  # загружаем видео.
    except:
        print(f"WE HAVE PROBLEMS WITH {url} ")
        return
    time.sleep(6)