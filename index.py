import requests
import sys
import time

apiData = requests.api.get("https://dmigw.govcloud.dk/v2/metObs/collections/observation/items?period=latest-10-minutes&stationId=06156&api-key=e797e2ed-9924-4801-9025-8f380eb49797")

if apiData.status_code != 200:
    print("LORT I DATA 🤦‍♂️")
    sys.exit()


features = apiData.json()['features']


weatherData = {}

for data in features:
    properti = data["properties"]

    weatherData[properti["parameterId"]] = {
        "value" : properti["value"],
        "observed" : properti["observed"]
    }


# print("\033[1m\033[34m🧭 WIND DIRECTION 🧭\033[0m")
# print("\033[1m\033[34m    N    \033[0m")
# print("\033[1m\033[34m W     E \033[0m")
# print("\033[1m\033[34m    S    \033[0m")
# print("\033[1m\033[34m{}\033[0m".format(weatherData["wind_dir"]["value"]))
directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

while True:
    for direction in directions:
        print("\033c") # clear the terminal
        print("\033[1m\033[34m🧭 WIND DIRECTION 🧭\033[0m")
        print("\033[1m\033[34m      N      \033[0m")
        print("\033[1m\033[34m    W   E    \033[0m")
        print("\033[1m\033[34m      S      \033[0m")
        print("\033[1m\033[34m  {}  \033[0m".format(direction))
        time.sleep(0.5) # wait for 0.5 seconds