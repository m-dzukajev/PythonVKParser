from time import sleep
from datetime import datetime
import requests
import json
import csv


def to_json(post_dict):
    try:
        data = json.load(open('posts_data.json'))
    except:
        data = []
    data.append(post_dict)

    with open('posts_data.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def writer_csv(data):
    with open('posts_data.csv', 'a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=';')

        writer.writerow((data['likes'],
                         data['reposts'],
                         data['text']
                         ))


def get_data(post):  # получаем необходимые данные из списка, pers = data['response'][0]
    try:
        post_id = post['id']
    except:
        post_id = 0

    try:
        likes = post['likes']['count']
    except:
        likes = 'None'

    try:
        reposts = post['reposts']['count']
    except:
        reposts = 'None'

    try:
        text = post['text']
    except:
        text = '***'

    data = {
        'id': post_id,
        'likes': likes,
        'reposts': reposts,
        'text': text
    }

    return data


def main():
    start = datetime.now()
    # https://api.vk.com/method/users.get?user_id=210700286&v=5.52
    group_id = '-1'  # ID группы для запроса, всегда начинается с "-"
    access_token = ''  # Токен для запросов, получаем при создание Standalone приложение ВК.
    version = '5.92'  # Версия запросов в ВК
    offset = 0  # смещение постов
    all_posts = []
    date_x = 1514821586  # Epoch время
    while True:
        sleep(3)
        myparams = {'owner_id': group_id, 'v': version, 'access_token': access_token, 'count': 100, 'offset': offset}
        respons = requests.get('https://api.vk.com/method/wall.get', params=myparams)
        posts = respons.json()['response']['items']
        all_posts.extend(posts)

        oldest_post_date = posts[-1]['date']
        print(oldest_post_date)
        offset = offset + 100
        print(offset)
        if oldest_post_date < date_x:
            break

    for post in all_posts:
        post_data = get_data(post)
        writer_csv(post_data)

    end = datetime.now()
    total = end - start
    print(str(total))
    to_json(respons.json())  # Трансформируем в словарь и записываем в файл person.json
    print(len(all_posts))


if __name__ == '__main__':
    main()
