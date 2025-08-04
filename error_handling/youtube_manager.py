
import json

youtube_file_txt = 'youtube.txt'

def load_data():
    try:
        with open(youtube_file_txt, 'r') as file:
          return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open(youtube_file_txt, 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    for index, video in enumerate(videos, start=1):
        print(f'{index}. ')

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass


