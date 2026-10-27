import re, requests

URL = "https://app.playtomic.com/tournaments/88d3089a-83b0-48bf-97c5-cf7958ec041d"
NTFY = "https://ntfy.sh/laurie-padel-8nov-x7k2"   # pick your own unguessable name

html = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20).text
m = re.search(r"(\d+)\s*of\s*(\d+)\s*spots", html)

if not m:
    requests.post(NTFY, data="Padel watcher: couldn't read spots - check the script")
elif int(m.group(1)) >=0:
    requests.post(NTFY, data=f"{m.group(1)} spot(s) open for Sunday Americano! Book now",
                  headers={"Priority": "urgent", "Click": URL})
