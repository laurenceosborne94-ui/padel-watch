import re, requests

URL = "https://app.playtomic.com/tournaments/88d3089a-83b0-48bf-97c5-cf7958ec041d"
NTFY = "https://ntfy.sh/laurie-padel-8nov-x7k2"   # your topic

resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"}, timeout=20)
print("HTTP status:", resp.status_code)

text = re.sub(r"<[^>]+>", " ", resp.text)   # strip HTML tags/comments
text = re.sub(r"\s+", " ", text)            # tidy whitespace

m = re.search(r"(\d+)\s*of\s*(\d+)\s*spots", text, re.IGNORECASE)
print("Match:", m.group(0) if m else "NONE")

if not m:
    i = text.lower().find("spot")
    print("Around 'spot':", text[max(0, i-150):i+50] if i >= 0 else "word not found")
    requests.post(NTFY, data="Padel watcher: couldn't read spots - check the script")
elif int(m.group(1)) > 0:
    requests.post(NTFY, data=f"{m.group(1)} spot(s) open for Sunday Americano! Book now",
                  headers={"Priority": "urgent", "Click": URL})
else:
    print("Still full - no alert sent")
