import requests


class User:
    def __init__(self, token_access, user_id):
        self.token_access = token_access
        self.user_id = user_id

    def __str__(self):
        url_profile = 'https://vk.com/id' + str(self.user_id)
        return url_profile

    def get_user_info(self, id_of_user):
        response = requests.get(
            'https://api.vk.com/method/users.get',
            params={
                'access_token': self.token_access,
                'user_ids': id_of_user,
                'v': 5.21
            }
        )
        return response.json()

    def get_friends(self, id_of_user):
        response = requests.get('https://api.vk.com/method/friends.get', params={

                'user_id': id_of_user,
                'order': 'name',
                'v': 5.21,
                'access_token': self.token_access,
            }
        )
        return response.json()

    def get_mutual_friends(self, user_id1, user_id2):
        try:
            user1 = set(self.get_friends(user_id1)['response']['items'])
            user2 = set(self.get_friends(user_id2)['response']['items'])
            mutual_friends = user1 & user2
            list_of_friends = []
            for ids in mutual_friends:
                user_first_name = self.get_user_info(ids)['response'][0]['first_name']
                user_last_name = self.get_user_info(ids)['response'][0]['last_name']
                list_of_friends.append(user_first_name + ' ' + user_last_name)
            if not list_of_friends:
                print('Общих друзей нет.')
            else:
                print(f'Общих друзей у пользователей - {len(mutual_friends)}.')
                print('Общие друзья: ')
                for count, name in enumerate(list_of_friends):
                    print(f'{count + 1}. {name}')
        except KeyError:
            print('К сожалению доступ к профилю одного из пользователей закрыт, попробуйте ввести id другого '
                  'пользователя!')


token = '10b2e6b1a90a01875cfaa0d2dd307b7a73a15ceb1acf0c0f2a9e9c586f3b597815652e5c28ed8a1baf13c'
first_user_id = int(input('Введите id первого пользователя: '))
second_user_id = int(input('Введите id второго пользователя: '))
user = User(token, first_user_id)
user.get_mutual_friends(first_user_id, second_user_id)
print(user)


