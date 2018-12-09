import requests
import json

def write_json(data):
    with open('person.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

def main():
    # https://api.vk.com/method/users.get?user_id=210700286&v=5.52
    id = '2974856'  # ID человека для запроса, пример: a_gamilkar или 2974856
    access_token = 'token'  # Токен для запросов, получаем при создание Standalone приложение ВК.
    r = requests.get(f'https://api.vk.com/method/users.get?user_ids={id}&v=5.74&access_token={access_token}')
    write_json(r.json())


if __name__ == '__main__':
    main()
