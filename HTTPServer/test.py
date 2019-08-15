import requests

params = {'user': {'name': 'haha',
                   'id': '001',
                   'work': {'job': 'iOS',
                            'job': 'sina'}}}
params = {'user': ['aaa', 'bbb', 'ccc']}
params = ['aaa', 'bbb', 'ccc']
r = requests.get('https://www.baidu.com/s', params = params)
print(r.url)