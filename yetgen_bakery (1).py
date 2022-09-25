# YETGEN BAKERY   BY "THE DEVELOPERS ON THE ROAD" , YETGEN JUMP  2022
cikolatali_menu = {
    "1.Profiterol": 15,
    "2.Ekler": 17 
}

sutlu_menu = {
    "1.Sütlaç":5,
    "2.Muhallebi":7  
}

serbetli_menu = {
    "1.Baklava": 28,
    "2.Kadayıf": 24
}

menu = {
    1:"Çikolatalı Menü",
    2:"Sütlü Menü",
    3:"Şerbetli Menü",
    4:"Cupcake Tasarımı"
}

cupcake = {
    "1.Kakao" :12,
    "2.Sade":10, 
    "3.Üzümlü":11,
    "4.Fındıklı":13
}

#FONKSİYON YAPILARI

def display_sutlu_menu():
  total_hesap = 0
  print("----------SÜTLÜ TATLILAR----------")
  print("""
  "1.Sütlaç": 5
  "2.Muhallebi": 7 """)
  while 1:
    secim = int(input("Lütfen almak istediğiniz sütlü tatlının numarasını giriniz: "))
    if secim ==1:
      total_hesap = total_hesap + 5
      print("TOPLAM HESAP: ", total_hesap)
    elif secim == 2:
      total_hesap = total_hesap + 7
      print("TOPLAM HESAP: ", total_hesap)
    break


def display_serbetli_menu():
  total_hesap = 0
  print("----------ŞERBETLİ TATLILAR----------")
  print(""" 
    "1.Baklava": 28
    "2.Kadayıf": 24 """) 
  while 1:
    secim = int(input("Lütfen almak istediğiniz şerbetli tatlının numarasını giriniz: "))
    if secim == 1:
        total_hesap = total_hesap + 28
        print("TOPLAM HESAP: ", total_hesap)
    elif secim ==2:
        total_hesap = total_hesap + 24
        print("TOPLAM HESAP: ",total_hesap)  
    break

def display_cikolatali_menu():
  total_hesap = 0
  print("----------ÇİKOLATALI TATLILAR----------")
  print("""
    "1.Profiterol": 15

    "2.Ekler": 17 """)

#DÖNGÜLER
  while 1:

    secim=int(input("Lütfen almak istediğiniz ürünün numarasını giriniz: "))
    if secim==1:

      total_hesap = total_hesap + 15   
      print("TOPLAM HESAP: ",total_hesap)
    elif secim == 2:
        
      total_hesap = total_hesap + 17
      print("TOPLAM HESAP: ",total_hesap)
    break


def display_cupcake():
  total_hesap=0
  
  while 1:
    secim=int(input(""""
    Cupcake özellikleri, kekin neli olsun?

    1.Kakao: 12 tl
    2.Sade: 10tl 
    3.Üzümlü: 11tl
    4.Fındıklı: 13tl

    Lütfen almak istediğiniz ürünün numarasını giriniz: """))
    
#KOŞUL YAPILARI

    if secim==1:
      total_hesap = total_hesap + 12   
      print("TOPLAM HESAP: ",total_hesap)

    elif secim==2:
      total_hesap = total_hesap + 10   
      print("TOPLAM HESAP: ",total_hesap)

    elif secim==3:
      total_hesap = total_hesap + 11   
      print("TOPLAM HESAP: ",total_hesap)

    elif secim==4:
      total_hesap = total_hesap + 13   
      print("TOPLAM HESAP: ",total_hesap)
    else:
      print("Yanlış bir giriş yaptınız, lütfen tekrar giriş yapınız. ")
    break
  
  kremşanti = int(input("""
  Ne tür bir kremşanti istiyorsunuz? 

  1.Vanilyalı: 10 TL 
  2.Kakaolu: 25 TL 
  3.Çilekli: 10 TL

  Eklemek istemiyorsanız '99' giriniz.

  Lütfen almak istediğiniz ürünün numarasını giriniz: """))
  
  if kremşanti == 1:
    total_hesap += 10
    print("TOPLAM HESAP: ",total_hesap)

  elif kremşanti == 2:
    total_hesap += 25
    print("TOPLAM HESAP: ",total_hesap)
  elif kremşanti == 3:
    total_hesap += 10
    print("TOPLAM HESAP: ",total_hesap)
  elif kremşanti == 99:
    total_hesap += 0
    print("TOPLAM HESAP: ",total_hesap)
  print()

  tanecik = int(input("""
  Ne tür bir tanecik istiyorsunuz? 

  1.İnci: 5 TL
  2.Krokan: 8 TL 
  3.Damla çikolatalı: 7 TL
  4.Kuru meyve: 6 TL 
  5.Antep fıstığı: 13 TL 

  Eklemek istemiyorsanız '99' giriniz:


  Lütfen almak istediğiniz ürünün numarasını giriniz: """))
  
  print()
  if tanecik == 1:
    total_hesap += 5
    print("TOPLAM HESAP: ",total_hesap)
  elif tanecik == 2:
    total_hesap += 8
    print("TOPLAM HESAP: ",total_hesap)
  elif tanecik == 3:
    total_hesap += 7
    print("TOPLAM HESAP: ",total_hesap)
  elif tanecik == 4:
    total_hesap += 6
    print("TOPLAM HESAP: ",total_hesap)
  elif tanecik == 5:
    total_hesap += 13
    print("TOPLAM HESAP: ",total_hesap)
  elif tanecik == 99:
    total_hesap += 0
    print("TOPLAM HESAP: ",total_hesap)
  
  print()

  sos = int(input("""
  Ne tür bir sos istiyorsunuz? 

  1.Sütlü Çikolata: 2 TL 
  2.Bitter Çikolata: 1 TL
  3.Beyaz Çikolata: 2 TL
  4.Karamel: 4 TL

  Eklemek istemiyorsanız '99' giriniz.

  Lütfen almak istediğiniz ürünün numarasını giriniz: """))
  
  if sos == 1:
    total_hesap += 2
    print("TOPLAM HESAP: ",total_hesap)
  elif sos == 2:
    total_hesap += 1
    print("TOPLAM HESAP: ",total_hesap)
  elif sos == 3:
    total_hesap += 2
    print("TOPLAM HESAP: ",total_hesap)
  elif sos == 4:
    total_hesap += 4
    print("TOPLAM HESAP: ",total_hesap)
  elif sos == 99:
    total_hesap += 0
    print("TOPLAM HESAP: ",total_hesap)
  print()

  print("Kekiniz hazır! Toplam fiyat tutarınız: ",total_hesap, "TL'dir.")


def display_menu():

  print("-----YETGEN BAKERY'E HOŞ GELDİNİZ!-----\nSİPRAİŞ OLUŞTURMAK İÇİN BİLGİLERİNİZİ GİRİNİZ.")

#CLASS YAPISI
  class Personal():
    def __init__(self,isim,soyisim):
      self.isim=isim
      self.soyisim=soyisim

    def show_info(self):
      print(f"Merhaba {self.isim} {self.soyisim}.\nSiparişinizi oluşturmaya başlayınız... ")
   
  personal1=Personal(input("Lütfen isminizi giriniz: "),input("Lütfen soy isminizi giriniz: "))
  personal1.show_info()


  print("""
    --------------------------------------|
     |         YETGEN BAKERY              |
     |                                    |
     |    1. Çikolatalı  Tatlı            |
     |    2. Sütlü Tatlı                  |
     |    3. Şerbetli Tatlı               |
     |    4. Kendi Kekini Tasarla         |
     |                                    |
     |                                    |
     | -----------------------------------|""")  
  print()

#HATA AYIKLAMA

  try:
    giris=int(input("Menüyü görüntülemek için 'numaralara göre' seçim yapınız: "))
  except ValueError:
    print("LÜTFEN SAYI İLE GİRİŞ YAPINIZ!")

  if giris==1:
    display_cikolatali_menu()
     

  if giris==2:
    display_sutlu_menu()
    
 
  if giris==3:
    display_serbetli_menu()
    
  if giris==4:
    display_cupcake()

display_menu()

ödeme = str(input ("Ürünü almak istiyor musunuz? 'Evet' veya 'Hayır' giriniz: "))
if ödeme.lower() == "evet":
  print("Ücretiniz alındı.")
  print()
  makbuz = str(input ("Makbuz ister misiniz 'Evet' veya 'Hayır' giriniz: "))
  if makbuz.lower() =="evet":
    print("İşleminiz tamamlanmıştır, bizi tercih ettiğiniz için teşekkür ederiz. YetGen Bakery'den sevgilerle. Makbuzunuz iletilmiştir...")
    print()
  elif makbuz.lower() =="hayır":
    print("İşleminiz tamamlandı, makbuz iletilmeyecektir. Bizi tercih ettiğiniz için teşekkür ederiz. YetGen Bakery'den sevgilerle.")
  else:
    print("Yanlış bir giriş yaptınız..." )
elif ödeme.lower() =="hayır":
  print("İşleminiz iptal edildi.")
else:
  print("Yanlış bir giriş yaptınız..." )
