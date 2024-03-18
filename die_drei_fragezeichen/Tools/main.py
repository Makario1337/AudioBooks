import requests
import os


for i in range(1, 226):
    if len(str(i)) == 1:
        i = str("00"+str(i))
    elif len(str(i)) == 2:
        i = str("0"+str(i))
    else:
        i = str(i)

    print("Downloading " + i)
    url1 = f'https://cdn.smehost.net/hcmssmeappscom-delabelsprod/produkte/hoerspiele/ddf_cd_{i}.jpg'
    print("Downloading: " +url1)
    r = requests.get(url1, allow_redirects=True)
    if "The specified" in str(r.content):
        url2 = f'https://cdn.smehost.net/hcmssmeappscom-delabelsprod/produkte/hoerspiele/ddf-{i}.jpg'
        print("Downloading: " +url2)
        r = requests.get(url2, allow_redirects=True)
        if "The specified" in str(r.content):
            url3 = f'https://cdn.smehost.net/hcmssmeappscom-delabelsprod/produkte/hoerspiele/01_ab_213/01_ddf_{i}_cover_digital.jpg'
            print("Downloading: " +url3)
            r = requests.get(url3, allow_redirects=True)
            if "The specified" in str(r.content):
                print("Not able to find image")
            else:
                open (f'Die_drei_Fragezeichen_Folge_{i}.jpg', 'wb').write(r.content)
        else:
            open (f'Die_drei_Fragezeichen_Folge_{i}.jpg', 'wb').write(r.content)
    else:
        open (f'Die_drei_Fragezeichen_Folge_{i}.jpg', 'wb').write(r.content)

  


