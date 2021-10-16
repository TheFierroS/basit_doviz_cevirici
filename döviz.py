from typing import SupportsAbs
from bs4.element import ProcessingInstruction
import requests
from bs4 import BeautifulSoup
import time

header = {"User-Agent":} #Kendi User Agentinizi Giriniz !

r = requests.get("https://www.doviz.com/", headers=header) 
soup = BeautifulSoup(r.content, "lxml")

doviz = soup.find("div", {"class":"table-narrow"}).find_all("tbody")

for i in doviz:
    list = i.find_all("td", {"class":"text-bold"})
    usd = list[0].text
    eur = list[2].text
    gbp = list[4].text
    chf = list[6].text
    cad = list[8].text
    print("-"*50)
    print("↓ Değerler ↓")
    print(f"USD -> {usd}")
    print(f"EUR -> {eur}")
    print(f"GBP (İngiliz Sterlini) -> {gbp}")
    print(f"CHF (İsviçre Frangı) -> {chf}")
    print(f"CAD (Kanada Doları) -> {cad}")
    print("-"*50)

while True:
    tl_to_x = input("1- USD - TL\n2- EUR - TR\n3- GBP - TL\n4- CHF - TL\n5- CAD - TL\nHangi Birimi Çevirmek İstersiniz(Çıkış Yapmak İçin 'q' Tuşuna Basınız...) : ")
    #########################################################
    if tl_to_x == "1":
        choice = input("1- TL - USD\n2- USD - TL\nSeçiminiz : ")
        if choice == "1":
            tl_miktar = int(input("Kaç TL'yi USD'ye Çevirmek İstersiniz -> "))
            sonuc = str(tl_miktar/float(usd.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if choice == "2":
            usd_miktar = int(input("Kaç USD'yi TL'ye Çevirmek İstersiniz -> "))
            sonuc = str(usd_miktar*float(usd.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if int(choice) > 2:
            print("-"*50)
            print("Hatalı Değer Girdiniz !")
            print("-"*50)
    #####################################################
    if tl_to_x == "2":
        choice = input("1- TL - EUR\n2- EURO - TL\nSeçiminiz : ")
        if choice == "1":
            tl_miktar = int(input("Kaç TL'yi EUR'a Çevirmek İstersiniz -> "))
            sonuc = str(tl_miktar/float(eur.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if choice == "2":
            eur_miktar = int(input("Kaç EUR'u TL'ye Çevirmek İstersiniz -> "))
            sonuc = str(eur_miktar*float(eur.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if int(choice) > 2:
            print("-"*50)
            print("Hatalı Değer Girdiniz !")
            print("-"*50)
    ######################################################
    if tl_to_x == "3":
        choice = input("1- GBP - EUR\n2- EURO - GBP\nSeçiminiz : ")
        if choice == "1":
            tl_miktar = int(input("Kaç TL'yi GBP'ye Çevirmek İstersiniz -> "))
            sonuc = str(tl_miktar/float(gbp.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if choice == "2":
            gbp_miktar = int(input("Kaç GBP'yi TL'ye Çevirmek İstersiniz -> "))
            sonuc = str(gbp_miktar*float(gbp.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if int(choice) > 2:
            print("-"*50)
            print("Hatalı Değer Girdiniz !")
            print("-"*50)
    ######################################################
    if tl_to_x == "4":
        choice = input("1- CHF - EUR\n2- EURO - CHF\nSeçiminiz : ")
        if choice == "1":
            tl_miktar = int(input("Kaç TL'yi CHF'ye Çevirmek İstersiniz -> "))
            sonuc = str(tl_miktar/float(chf.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if choice == "2":
            chf_miktar = int(input("Kaç CHF'yi TL'ye Çevirmek İstersiniz -> "))
            sonuc = str(chf_miktar*float(chf.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if int(choice) > 2:
            print("-"*50)
            print("Hatalı Değer Girdiniz !")
            print("-"*50)
    ######################################################
    if tl_to_x == "5":
        choice = input("1- CAD - EUR\n2- EURO - CAD\nSeçiminiz : ")
        if choice == "1":
            tl_miktar = int(input("Kaç TL'yi CAD'a Çevirmek İstersiniz -> "))
            sonuc = str(tl_miktar/float(cad.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if choice == "2":
            cad_miktar = int(input("Kaç CAD'i TL'ye Çevirmek İstersiniz -> "))
            sonuc = str(cad_miktar*float(cad.replace(",", ".")))
            print("-"*50)
            print("Sonuç ->",sonuc)
            print("-"*50)
        if int(choice) > 2:
            print("-"*50)
            print("Hatalı Değer Girdiniz !")
            print("-"*50)

    if tl_to_x == "q":
        print("Çıkış Yapılıyor...")
        time.sleep(1)
        break

    if int(tl_to_x) > 5:
        print("-"*50)
        print("Hatalı Değer Girdiniz !")
        print("-"*50) 

   




    

