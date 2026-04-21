from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

siparisler = []
toplam = 0

menu = {
    "1": {
        "kategori": "Kahveler",
        "urunler": {
            "1": ("Türk Kahvesi", 100.00, "türkkahve.jpg", "Geleneksel, köpüklü"),
            "2": ("Espresso", 120.00, "espresso.jpg", "Yoğun aromalı, sert içim"),
            "3": ("Americano", 130.00, "americano.jpg", "Espresso bazlı, su ile hazırlanır"),
            "4": ("Cappuccino", 135.00, "cappuccino.jpg", "Süt köpüklü, dengeli aroma"),
            "5": ("Macchiato", 140.00, "macchiato.jpg", "Espresso ve hafif süt köpüğü"),
            "6": ("Mocha", 150.00, "mocha.jpg", "Çikolatalı, sütlü kahve"),
            "7": ("Flat White", 145.00, "flat-white.jpg", "Yoğun espresso, ınce süt dokusu")
        }
    },
    "2": {
        "kategori": "Çaylar",
        "urunler": {
            "1": ("Siyah Çay", 75.00, "siyah-cay.jpg", "Demli, klasik çay lezzeti"),
            "2": ("Bitki Çayları", 85.00, "bitki-cayi.jpg", "Rahatlatıcı, hafif aromalı"),
            "3": ("Chai Tea Latte", 90.00, "chai-tea-latte.jpg", "Baharatlı, sütlü çay")
        }
    },
    "3": {
        "kategori": "Tatlılar",
        "urunler": {
            "1": ("Pasta Dilimleri", 175.00, "pasta.jpg", "Meyveli, çikolatalı"),
            "2": ("Kurabiyeler", 95.00, "kurabiye.jpg", "Çikolatalı, fındıklı"),
            "3": ("Cheesecake", 180.00, "cheesecake.jpg", "Frambuazlı, sade"),
            "4": ("Tiramisu", 170.00, "tiramisu.jpg", "Kahveli, mascarpone"),
            "5": ("Brownie", 185.00, "brownie.jpg", "Yoğun çikolatalı, soslu")
        }
    },
    "4": {
        "kategori": "Atıştırmalıklar",
        "urunler": {
            "1": ("Kruvasan", 80.00, "kruvasan.jpg", "Tereyağlı, kat kat hamur"),
            "2": ("Tostlar", 125.00, "tost.jpg", "Kaşarlı, sucuklu seçenekler"),
            "3": ("Sandviçler", 135.00, "sandvic.jpg", "Tavuklu, peynirli çeşitler"),
            "4": ("Salatalar", 185.00, "salata.jpg", "Tavuklu, köfteli seçenekler")
        }
    }
}


@app.route("/")
def index():
    return render_template("index.html", menu=menu, siparisler=siparisler, toplam=toplam)


@app.route("/ekle", methods=["POST"])
def ekle():
    global toplam

    urun_adi = request.form.get("urun_adi")
    fiyat = float(request.form.get("fiyat"))

    siparisler.append((urun_adi, fiyat))
    toplam += fiyat

    return redirect(url_for("index"))


@app.route("/temizle", methods=["POST"])
def temizle():
    global toplam
    siparisler.clear()
    toplam = 0
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)