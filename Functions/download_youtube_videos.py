from pytube import YouTube
import pytube
"""
  Requirements:
    pytube
"""


def convert_to_audio(urls:list) -> None:
  for video in urls:
    print(f'Downloading video')
    YouTube(video).streams.filter(only_audio=True).first().download()
    print('Done!')

def download_videos(urls:list) -> None:
  for video in urls:
    print(f'Downloading video')
    YouTube(video).streams.get_highest_resolution().download()
    print('Done!')
