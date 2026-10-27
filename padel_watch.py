import re, requests

URL = "https://app.playtomic.com/tournaments/88d3089a-83b0-48bf-97c5-cf7958ec041d"
NTFY = "https://ntfy.sh/laurie-padel-8nov-x7k2"   # must match your app topic exactly

html = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20).text
m = re.search(r"(\d+)\s*of\s*(\d+)\s*spots", html)
print("Match:", m.group(0) if m else "NONE")

if not m:
    r = requests.post(NTFY, data="Padel watcher: couldn't read spots - check the script")
    print("ntfy response:", r.status_code)
elif int(m.group(1)) > 0:
    r = requests.post(NTFY, data=f"{m.group(1)} spot(s) open for Sunday Americano! Book now",
                      headers={"Priority": "urgent", "Click": URL})
    print("ntfy response:", r.status_code)
else:
    print("Still full - no alert sent")
