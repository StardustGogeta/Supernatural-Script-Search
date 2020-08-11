import requests, re, os, time, pickle

# Suggested search terms:
# - Lore
# - Get this
# - Always you
# - Had to be you
# - Sammy

filepath = r"transcripts.txt"
if os.path.exists(filepath):
    transcripts = pickle.load(open(filepath, "rb"))

    s = input("Query strings? (separate with colons): ").split(':')

    for ep in transcripts:
        t = transcripts[ep].text.lower()
        for ss in s:
            if ss.lower() in t:
                print(f"Match for '{ss}' found in {ep}!")
                print("\t", re.findall(f"<br>[^<]*{ss.lower()}[^<]*<br>", t), "\n")
                      
    print("Search complete.")
    
else:
    print("Getting transcripts...")

    url = "https://subslikescript.com/series/Supernatural-460681"

    web = requests.get(url)

    t = web.text

    episodes = re.findall('/season-[^\']*', t)

    pages = dict()

    for episode in episodes:
        print(f"Downloading {episode}...")
        pages[episode] = requests.get(url + episode)
        time.sleep(.125)

    pickle.dump(pages, open(filepath, "wb"))
    print("Saving complete!")
