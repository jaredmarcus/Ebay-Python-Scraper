import requests
import re
import urllib3
import os
import shutil
from halo import Halo
http = urllib3.PoolManager()
from bs4 import BeautifulSoup
okay = True


def get_page(url):
    response = requests.get(url)
    #print(response.ok)
    #print(response.status_code)
    if not response.ok:
        print('Server responded:', response.status_code)
        okay = False
    else:
        soup = BeautifulSoup(response.text, 'lxml')
    return soup

def get_detail_data(soup):
    #TITLE
    h1 = soup.select('h1.it-ttl')[0].text.strip()
    sub_str = "  "
    
    ##removes Details About before title in HTML
    h1 = h1[h1.index(sub_str)+ len(sub_str):]
    
    #removes extra space
    h1 = h1[1:]
    print("Title of listing: " + h1)

    #create title file
    file_path = get_download_path()
    textfile = 'Title.txt'
    textpath= str(file_path)
    with open(os.path.join(textpath, textfile), 'w') as fp: 
        pass
    textpath += "/Title.txt"

    #writing Title to file
    text_file = open(textpath, "w")
    n = text_file.write(h1)
    text_file.close()
    
    #PRICE
    div = soup.find("span", {"id": "prcIsum"})
    
    #gets the price from the Div
    price = str(div.text)
    
    #removes other characters (US $) or 4 characters
    #content = content[4:]
    
    with open('price.txt', 'w') as p:
        p.write(price)

    print("Price is: " + price)

def get_description(url):
    #gets item description via item ID from URL    
    item_descr_url = 'https://vi.vipr.ebaydesc.com/ws/eBayISAPI.dll?item={item_id}'

    item_id = url.split('?')[0].split('/')[-1]  # this is the string of numbers after https://www.ebay.com/itm/########

    soup = BeautifulSoup(requests.get(item_descr_url.format(item_id=item_id)).content, 'html.parser')
    description = (soup.get_text(strip=True, separator='\n'))
    
    #removes unwanted characters
    description = description[5:]
    return description

def Find(string):
    #find all URLs in string
	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
	url = re.findall(regex,string)	
	return [x[0] for x in url]

def get_download_path():
	"""Returns the default downloads path for linux or windows"""
	if os.name == 'nt':
		import winreg
		sub_key = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'
		downloads_guid = '{374DE290-123F-4565-9164-39C4925E467B}'
		with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
			location = winreg.QueryValueEx(key, downloads_guid)[0]
		return location
	else:
		return os.path.join(os.path.expanduser('~'), 'Downloads')

@Halo(text='Loading', spinner='dots')
def get_pictures(soup):
    URL_TO_PARSE = []
    div = soup.find_all("td", {"class": "tdThumb"})
    div = str(div)
    #print(div)
    URL_TO_PARSE = Find(div)
    #print(URL_TO_PARSE)
    res = []
    [res.append(x) for x in URL_TO_PARSE if x not in res]

    # printing list after removal 
    #print ("The list after removing duplicates : " + str(res))

    # Replace substring in list of strings
    results = [sub.replace('s-l64.jpg', 's-l1600.jpg') for sub in res]

    #deletes the first entry of the list because the scraper pulls a loading gif from ebay
    results.pop(0)

    #list is now just of actual listing pictures
    #print("The list after substring replacement : " + str(results))

    #Downloading Pictures
    spinner = Halo(text='Downloading images from eBay...', spinner='dots3')
    spinner.start()
    N = 0
    for url in results:
        r = requests.get(url)
        Name = str(N+1) 
        N += 1

        file_path = get_download_path()
        stringpath = str(file_path)
        #replaces the stringpath from C:\User\Downloads to C:\User\Desktop
        stringpath = stringpath.replace("Downloads", "Desktop")
        stringpath += "/EbayScript/pictures/"
        with open(str(stringpath)+'file'+ Name + ".jpg", 'wb') as f:
            f.write(r.content)
    spinner.stop()
    print("Pictures saved to: " + stringpath)


def main():
    url = input("Enter Ebay URL: ")
    get_detail_data(get_page(url))
    if okay == True:
        des_file = "description.txt"
        with Halo(text='Loading', spinner='dots'):
            description = get_description(url)
            #print(description)
            with open(des_file, 'w') as d:
                d.write(description)
        print("Description saved to: " + des_file)
        get_pictures(get_page(url))
    else:
        return
    
if __name__ == '__main__':
    main()