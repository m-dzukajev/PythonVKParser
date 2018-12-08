import requests

def main():
    #https://api.vk.com/method/users.get?user_id=210700286&v=5.52
    id = ''
    access_token = 'bbe5afa6bbe5afa6bbe5afa685bb82c972bbbe5bbe5afa6e7ee4c05399f87e19973c1b7'
    r = requests.get('https://api.vk.com/method/users.get?user_ids=210700286&v=5.74&access_token={}'.format(access_token))
    print(r.json())

if __name__ == '__main__':
    main()
