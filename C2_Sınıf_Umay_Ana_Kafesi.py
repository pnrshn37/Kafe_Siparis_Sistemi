siparisler = []
toplam = 0
print("*** Umay Ana Kahve Evi'ne Hoş Geldiniz ***")

# Menü
menu = {
    "1": {
        "kategori": "Kahveler",
        "urunler": {
            "1": ("Türk Kahvesi", 100.00),
            "2": ("Espresso", 120.00),
            "3": ("Americano", 130.00),
            "4": ("Latte", 125.00),
            "5": ("Cappuccino", 135.00),
            "6": ("Macchiato", 140.00),
            "7": ("Mocha", 150.00),
            "8": ("Flat White", 145.00)
        }
    },

    "2": {
        "kategori": "Çaylar",
        "urunler": {
            "1": ("Siyah Çay", 75.00),
            "2": ("Bitki Çayları", 85.00),
            "3": ("Chai Tea Latte", 90.00)
        }
    },

    "3": {
        "kategori": "Tatlılar",
        "urunler": {
            "1": ("Pasta Dilimleri", 175.00),
            "2": ("Kurabiyeler", 95.00),
            "3": ("Cheesecake", 180.00),
            "4": ("Tiramisu", 170.00),
            "5": ("Brownie", 185.00)
        }
    },
    "4":{
        "kategori":"Atıştırmalıklar",
        "urunler":{
            "1":("Kruvasan", 80.00),
            "2":("Bagel", 90.00),
            "3":("Tostlar", 125.00),
            "4":("Sandviçler", 135.00),
            "5":("Salatalar",185.00)
            }
        }
}

while True:# Programın sürekli çalışmasını sağlar # Kullanıcı çıkış yapana kadar menü tekrar tekrar gösterilir
    print("\n--- ANA MENÜ ---")

    # Menü sözlüğündeki tüm kategorileri dolaşarak ekrana yazdırır 
    # key = kullanıcının seçeceği numara
    # value = kategori bilgisi (örn: Kahveler)

    for key, value in menu.items(): 
        print(f"{key} - {value['kategori']}") 
    print("5 - Siparişi Bitir")
    print("0 - Çıkış")

    secim = input("Bir kategori seçiniz: ") # Kullanıcıdan hangi kategoriye girmek istediğini alır

    if secim == "5":
        print("\n*** Sipariş Özeti ***")
        if len(siparisler) == 0:
            print("Henüz sipariş verilmedi. Lütfen sipariş veriniz.")
        else:
            # Kullanıcının seçtiği tüm ürünleri listeler
            for urun in siparisler:
                print(f"{urun[0]} - {urun[1]} TL")
            print(f"Toplam Tutar: {toplam} TL")

    elif secim == "0":  # Kullanıcı 0 girerse programdan çıkar
        print("Programdan çıkılıyor...")
        break

    elif secim in menu: # Kullanıcının seçtiği değer menüde var mı kontrol edilir
        print(f"\n--- {menu[secim]['kategori']} ---")

        alt_menu = menu[secim]["urunler"] # Seçilen kategoriye ait ürünleri alır

        # Seçilen kategorideki ürünleri tek tek ekrana yazdırır
        for key, value in alt_menu.items(): 
            print(f"{key} - {value[0]} : {value[1]} TL")

        urun_secim = input("Bir ürün seçiniz: ") # Kullanıcıdan ürün seçmesini ister

        if urun_secim in alt_menu:
            # Seçilen ürünün adı ve fiyatı alınır
            urun_adi = alt_menu[urun_secim][0] 
            fiyat = alt_menu[urun_secim][1]

            # Ürün sipariş listesine eklenir
            siparisler.append((urun_adi, fiyat))
            # Toplam tutar güncellenir
            toplam += fiyat

            print(f"{urun_adi} siparişe eklendi.")
            # Tüm siparişlerin toplam fiyatını gösterir
            print(f"Güncel Toplam: {toplam} TL")
        else:
            print("Geçersiz ürün seçimi yaptınız.")

    else:
        print("Geçersiz seçim yaptınız.")