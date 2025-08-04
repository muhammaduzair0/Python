
import json

youtube_file_txt = 'youtube.txt'

def load_data():
    try:
        with open(youtube_file_txt, 'r') as file:
          return json.load(file)
    except FileNotFoundError:
        return []
