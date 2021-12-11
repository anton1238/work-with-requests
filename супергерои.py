import requests

TOKEN = '2619421814940190'
urls = [
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Hulk',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Thanos',
    f'https://www.superheroapi.com/api.php/{TOKEN}/search/Captain%America',
    ]

def requests_get(url_all):
    r = (requests.get(url) for url in url_all)
    return r

def super_hero():
    super_heroes = []
    for item in requests_get(urls):
        intelligence = item.json()
        for power_stats in intelligence['results']:
            super_heroes.append({
                'name': power_stats['name'],
                'intelligence': power_stats['powerstats']['intelligence'],
                })
    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_heroes:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']
    print(f"Имя: {name}, Интеллект: {intelligence_super_hero}")