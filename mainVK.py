import requests
import json
import csv


def write_json(data):
    with open('person.json', 'w') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


def writer_csv(data):
    #newline = '' убирает пустую строку
    with open('person.csv.txt', 'a', newline='') as file:
        writer = csv.writer(file, delimiter=',')

        writer.writerow((data['id'],
                         data['first_name'],
                         data['second_name']
                         ))


def get_tada(person):  # получаем необходимые данные из списка, pers = data['response'][0]
    try:
        id_person = person['id']
    except:
        id_person = 0

    try:
        name_person = person['first_name']
    except:
        name_person = 'None'

    try:
        last_name_person = person['last_name']
    except:
        last_name_person = 'None'

    person_data = {
        'id': id_person,
        'first_name': name_person,
        'second_name': last_name_person
    }

    return person_data


def main():
    # https://api.vk.com/method/users.get?user_id=210700286&v=5.52

    id = input('Please input VK user ID: ')  # ID человека для запроса, пример: a_gamilkar или 2974856
    access_token = ''  # Токен для запросов, получаем при создание Standalone приложение ВК.
    respons = requests.get(f'https://api.vk.com/method/users.get?user_ids={id}&v=5.74&access_token={access_token}')
    write_json(respons.json())  # Трансформируем в словарь и записываем в файл person.json

    data = json.load(open('person.json'))
    pers = data['response'][0]

    writer_csv(get_tada(pers))
    print(pers)

if __name__ == '__main__':
    main()
