#!/usr/bin/env python3

import os
import sys
import subprocess
import requests
from requests.structures import CaseInsensitiveDict

# Config
from config import *
# from config import droneBaseUrl
# from config import repoExclude
# from config import droneCliPath

# ENV
droneEnv = os.environ.copy()
droneEnv["DRONE_SERVER"] = droneBaseUrl
droneEnv["DRONE_TOKEN"] = droneToken

# Request headers

headers = CaseInsensitiveDict()
headers["Authorization"] = 'Bearer ' + droneToken
headers["Accept"] = "application/json"


def reqdrone(urlAPIEndpoint):

    response = requests.get(droneBaseAPIUrl + urlAPIEndpoint, headers=headers)
    # print(response.text)

    return response


repos = reqdrone("user/repos").json()

for i in range(len(repos)):
    if repos[i]['active']:
        print(repos[i]['name'])
        print(repos[i]['active'])
        print(repos[i]['counter'])
        namespace = repos[i]['namespace']
        repoName = repos[i]['name']
        slug = repos[i]['slug']
        counter = repos[i]['counter']
        counternext = repos[i]['counter'] + 1
        print(counter)
        if repoName not in str(repoExclude):
            print(repoName + ' not in exclude list')
            subprocess.call([droneCliPath, 'build', 'create', namespace+'/'+repoName], env=droneEnv)
        else:
            print(repoName + ' in exclude list')





# subprocess.call([droneCliPath, 'info'], env=droneEnv)

# repoList = subprocess.call([droneCliPath, 'repo', 'ls'], env=droneEnv)
