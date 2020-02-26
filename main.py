import requests, json, config

base_url = config.url
username = config.username
auth = (username, config.token)
per_page = config.per_page


def get_repos():
    url = f'{base_url}/users/{username}/repos?per_page={per_page}'
    r = requests.get(url, auth=auth)
    return r.json()


def del_repo(repo):
    url = f"{base_url}/repos/{username}/{repo['name']}"
    r = requests.delete(url, auth=auth)


if __name__ == '__main__':
    for repo in get_repos():
        if repo['fork']:
            del_repo(repo)
            print('Deleted {}'.format(repo['name']))
