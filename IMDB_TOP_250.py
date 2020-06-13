import requests
from bs4 import BeautifulSoup



imdburl = "https://www.imdb.com/chart/top/"

#Get isteği
r = requests.get(imdburl)
#Gelen içeriğin HTML kodlarına göre ayrıştırılması
soup = BeautifulSoup(r.content, "html.parser")

rating_numarası = float(input("Enter Minimum Number of Rating"))

#Bütün tabloları bul, daha sonra o tabloların içindeki belirtilen sınıfları getir
#gelen_veri = soup.find_all("table", {"class":"chart full-width"})

#Başlıkları ve retingleri aldık
basliklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class":"ratingColumn imdbRating"})

#Başlıklar ile retingleri birleştireceğiz
for baslik, rating in zip(basliklar, ratingler):
    #Sadece textleri almak için
    baslik = baslik.text
    rating = rating.text

    #Sondaki boşlukarı silmek için
    baslik = baslik.strip()

    #Sondaki "\n" leri silmek için
    baslik = baslik.replace("\n","")

    rating = rating.strip()
    rating = rating.replace("\n", "")

    if (float(rating) > rating_numarası):
        print("Film Name: {} Rating of Film: {}".format(baslik, rating))



