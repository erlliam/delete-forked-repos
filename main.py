import requests
import json

with open('config.json') as config:
    config = json.load(config)

base_url = config['url']
username = config['username']
auth = (username, config['token'])
per_page = config['per_page']

def get_repos():
    url = base_url+'/users/{}/repos?per_page={}'.format(username, per_page)
    r = requests.get(url, auth=auth)
    return r.json()

def del_repo(repo):
    url = base_url+'/repos/{}/{}'.format(username, repo['name'])
    r = requests.delete(url, auth=auth)

if __name__ == '__main__':
    for repo in get_repos():
        if repo['fork']:
            del_repo(repo)
            print('Deleted {}'.format(repo['name']))
