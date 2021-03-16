import requests

def get_intelligence(TOKEN, names):

    hero_intelligence = {}
    for name in names:
        url = f'https://superheroapi.com/api/{TOKEN}/search/{name}'
        response = requests.get(url)
        data = response.json()['results']
        hero_intelligence[name] = int(data[0]['powerstats']['intelligence'])
    return hero_intelligence

def smart_guy(hero_intelligence):

    max_value = max(hero_intelligence.values())
    the_smart_guy = {key: value for key, value in hero_intelligence.items() if value == max_value}
    for key, velye in the_smart_guy.items():
        return f'Самый умный  - "{key}". Его интеллект - "{velye}".\n'


if __name__ == '__main__':
    TOKEN = '2619421814940190'
    names = ['Hulk', 'Captain America', 'Thanos']
    print(smart_guy(get_intelligence(TOKEN, names)))
