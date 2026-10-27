import requests

ID = "88d3089a-83b0-48bf-97c5-cf7958ec041d"
for url in [f"https://api.playtomic.io/v1/tournaments/{ID}",
            f"https://api.playtomic.io/v2/tournaments/{ID}"]:
    r = requests.get(url, headers={"User-Agent": "Playtomic/iOS"}, timeout=20)
    print(url, "->", r.status_code)
    print(r.text[:1500])
    print("-----")
