import json

INPUT_JSON = "playlist.json"
OUTPUT_M3U = "playlist.m3u"

with open(INPUT_JSON, "r", encoding="utf-8") as f:
    channels = json.load(f)

with open(OUTPUT_M3U, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n")

    for ch in channels:
        name = ch.get("name", "Unknown")
        url = ch.get("url", "")
        group = ch.get("group", "")
        logo = ch.get("logo", "")

        f.write(
            f'#EXTINF:-1 tvg-name="{name}" tvg-logo="{logo}" group-title="{group}",{name}\n'
        )
        f.write(f"{url}\n")

print("Conversion complete! Saved as playlist.m3u")
