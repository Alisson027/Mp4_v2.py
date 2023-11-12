from pytube import YouTube
import os

def download_video(url):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
        download_path = "/storage/emulated/0/Download"
        file_path = os.path.join(download_path, f"{yt.title}.mp4")
        print(f"Iniciando o download do vídeo {yt.title}...")
        video_stream.download(output_path=download_path, filename=f"{yt.title}.mp4")
        print(f"O download do vídeo {yt.title} já foi concluído. Está em: {file_path}")
    except Exception as e:
        print(f"Erro durante o download: {e}")
