import requests

url = "https://opensky-network.org/api/states/all?lamin=-56&lomin=-75&lamax=-17&lomax=-66"
r = requests.get(url).json()

for state in r["states"]:
    print(state[1], "→", state[2])  # callsign y país
