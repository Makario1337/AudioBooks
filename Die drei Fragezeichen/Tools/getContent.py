import requests
import html

# ddf mbz id = e028fab5-39ae-4ed9-b8c2-c4344d88b171

#https://musicbrainz.org/ws/2/release-group/?artist=e028fab5-39ae-4ed9-b8c2-c4344d88b171&limit=100&offset=0&fmt=json&type=other&secondary_type=%22audio%20drama%22

for x in [0, 100, 200, 300, 400]:

    r = requests.get(f'https://musicbrainz.org/ws/2/release-group/?artist=e028fab5-39ae-4ed9-b8c2-c4344d88b171&limit=100&offset={x}&fmt=json&type=other&secondary_type=%22audio%20drama%22')
    for release in r.json()['release-groups']:
        if "Box" in str(release): 
            continue
        if not ":" in str(release):
            continue
        folgen_name = release['title'].split(": ")
        if len(folgen_name) == 1:continue

        folgen_nummer = folgen_name[0].split("Die drei ??? ")[1]

        folgen_name = str(folgen_name[1]).replace(" ", "-").replace("ä","a").replace("ö","o").replace("ü","u").replace("ß","ss")

        print(folgen_name)
        print(folgen_nummer)
        print(f'https://www.dreifragezeichen.de/produktwelt/details/{folgen_name}')
        r = requests.get(f'https://www.dreifragezeichen.de/produktwelt/details/{folgen_name}')
        inhalt = str(r.text).split("<p>")[1].split("</p>")[0]
        if 'Copyright <i class="far fa-copyright"></i> 2023 Sony Music Entertainment Germany GmbH. All Rights Reserved' in inhalt:
            r = requests.get(f'https://www.dreifragezeichen.de/produktwelt/details/{folgen_name}-1')
            inhalt = str(r.text).split("<p>")[1].split("</p>")[0]
            if 'Copyright <i class="far fa-copyright"></i> 2023 Sony Music Entertainment Germany GmbH. All Rights Reserved' in inhalt:
                if 'Copyright <i class="far fa-copyright"></i> 2023 Sony Music Entertainment Germany GmbH. All Rights Reserved' in inhalt:
                    r = requests.get(f'https://www.dreifragezeichen.de/produktwelt/details/{folgen_name}-2')
                    inhalt = str(r.text).split("<p>")[1].split("</p>")[0]
                else:
                    if len(str(folgen_nummer)) == 1:
                        folgen_nummer = str("00"+str(folgen_nummer))
                    elif len(str(folgen_nummer)) == 2:
                        folgen_nummer = str("0"+str(folgen_nummer))
                    else:
                        folgen_nummer = str(folgen_nummer)
                    open (f'Die_drei_Fragezeichen_Folge_{folgen_nummer}.txt', 'w').write(html.unescape(inhalt))
            else:
                if len(str(folgen_nummer)) == 1:
                    folgen_nummer = str("00"+str(folgen_nummer))
                elif len(str(folgen_nummer)) == 2:
                    folgen_nummer = str("0"+str(folgen_nummer))
                else:
                    folgen_nummer = str(folgen_nummer)
                open (f'Die_drei_Fragezeichen_Folge_{folgen_nummer}.txt', 'w').write(html.unescape(inhalt))
        else:    
            if len(str(folgen_nummer)) == 1:
                folgen_nummer = str("00"+str(folgen_nummer))
            elif len(str(folgen_nummer)) == 2:
                folgen_nummer = str("0"+str(folgen_nummer))
            else:
                folgen_nummer = str(folgen_nummer)
            open (f'Die_drei_Fragezeichen_Folge_{folgen_nummer}.txt', 'w').write(html.unescape(inhalt))
