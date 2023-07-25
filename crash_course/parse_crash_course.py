import json

with open('file.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for item in data:
    print(item["video_link"])
