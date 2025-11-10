import requests

LATAM_PREFIXES = (
    "LA", "LP", "LPE",
    "LR", "LRC",
    "TAM", "JJ",
    "LCO", "LGT"
)


def obtener_vuelos_latam():
    url = "https://opensky-network.org/api/states/all?lamin=-60&lomin=-90&lamax=15&lomax=-30"

    try:
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

        if response.status_code != 200:
            return []  # No datos

        data = response.json()
        vuelos = []

        for s in data.get("states", []):
            callsign = (s[1] or "").strip()

            if callsign.startswith(LATAM_PREFIXES):
                vuelos.append({
                    "callsign": callsign,
                    "pais": s[2],
                    "lat": s[6],
                    "lon": s[5],
                    "altitud": s[13],
                    "velocidad": s[9],
                    "rumbo": s[10],
                })

        return vuelos

    except Exception as e:
        print("Error al obtener vuelos:", e)
        return []
