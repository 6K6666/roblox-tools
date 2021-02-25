import urllib.request
import requests
import json
cookie = 'roblosecurity cookie'
groupid = 'roblox group id'
def GetCSRFtoken(cookies=None):
    req = requests.get("https://www.roblox.com/", cookies={".ROBLOSECURITY":cookie})
    c1 = req.text
    t2 = c1[c1.find("Roblox.XsrfToken.setToken('")+27:c1.index("Roblox.XsrfToken.setToken('")+39]
    return t2
token = GetCSRFtoken()
def kick(members, cursor):
    for i in members:
        uid = str(i['user']['userId'])
        uname = i['user']['username']
        if uid != '93100189':
            vdel = requests.delete(f'https://groups.roblox.com/v1/groups/{groupid}/users/{uid}', cookies={".ROBLOSECURITY":cookie}, headers={'X-CSRF-TOKEN':token})
            print(f'Exile of user {uid} ({uname}) resulted in status code {vdel.status_code} and text {vdel.text}')
    if cursor:
        members2 = requests.get(f'https://groups.roblox.com/v1/groups/{groupid}/users?cursor={cursor}&limit=10&sortOrder=Desc')
        kick(members2.json()['data'], members2.json()['nextPageCursor'])
members = requests.get(f'https://groups.roblox.com/v1/groups/{groupid}/users?cursor=&limit=100&sortOrder=Desc')
kick(members.json()['data'], members.json()['nextPageCursor'])