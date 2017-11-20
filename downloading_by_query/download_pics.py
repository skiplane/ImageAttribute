
from bs4 import BeautifulSoup
import urllib2
import os
import itertools
import json

def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def download_pics_by_query(num_images, query, save_directory='Pictures'):
    image_type="ActiOn"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch"
    print url
    #add the directory for your image here
    DIR=save_directory
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
    }
    soup = get_soup(url,header)

    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    print  "There are " , len(ActualImages),"images available"

    if not os.path.exists(DIR):
                os.mkdir(DIR)
    DIR = os.path.join(DIR, query.split()[0])

    if not os.path.exists(DIR):
                os.mkdir(DIR)

    for i , (img , Type) in enumerate( ActualImages[:num_images]):
        try:
            req = urllib2.Request(img, headers={'User-Agent' : header})
            raw_img = urllib2.urlopen(req).read()

            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            print cntr
            if len(Type)==0:
                f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
            else :
                f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')

            f.write(raw_img)
            f.close()
        except Exception as e:
            print "could not load : "+img
            print e

if __name__=='__main__':
    class_of_object = ['man', 'woman', 'boy', 'girl']
    emotion = ['happy', 'sad', 'suspicious', 'attractive', 'unattractive', 'smart', 'thin', 'fat',
               'energy', 'lazy', 'tired']

    # Cartesian product
    obj_emt = list(itertools.product(class_of_object, emotion))

    for o, e in obj_emt:
        download_pics_by_query(num_images=100, query=' '.join([o,e]))

