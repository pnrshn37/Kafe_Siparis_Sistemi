from flask import Flask, render_template, request, redirect, url_for
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, "templates"),
    static_folder=os.path.join(base_dir, "static")
)

siparisler = []

menu = {
    "icecekler": {
        "ana_kategori": "İçecekler",
        "ikon": "☕",
        "alt_kategoriler": {
            "sicak_icecekler": {
                "kategori": "Kahveler & Sıcak İçecekler",
                "ikon": "☕",
                "alt_baslik": "Sıcak ve aromatik lezzetler",
                "urunler": {
                    "1": ("Türk Kahvesi", 100.00, "türkkahve.jpg", "Geleneksel, bol köpüklü Türk kahvesi"),
                    "2": ("Damla Sakızlı Kahve", 100.00, "Damla-Sakızlı.jpg", "Ege esintili, damla sakızı aromalı özel kahve"),
                    "3": ("Sütlü Türk Kahvesi", 100.00, "sutlu-kahvee.jpg", "Süt ile yumuşatılmış, hafif içimli Türk kahvesi"),
                    "4": ("Menengiç Kahvesi", 100.00, "menengickahvesi.jpg", "Kafeinsiz, doğal menengiç aromalı yöresel lezzet"),
                    "5": ("Filtre Kahve", 100.00, "filtre-kahve.jpg", "Yumuşak içimli, dengeli aromalı klasik filtre kahve"),
                    "6": ("Espresso", 120.00, "espresso.jpg", "Yoğun aromalı, sert ve güçlü içim"),
                    "7": ("Americano", 130.00, "americano.jpg", "Espresso bazlı, su ile hafifletilmiş kahve"),
                    "8": ("Cappuccino", 135.00, "cappuccino.jpg", "Süt köpüğü ile dengelenmiş, yumuşak içim"),
                    "9": ("Macchiato", 140.00, "macchiato.jpg", "Espresso üzerine hafif süt dokunuşu"),
                    "10": ("Mocha", 150.00, "mochakahvesi.jpg", "Çikolata ve kahvenin uyumlu birleşimi"),
                    "11": ("Latte", 100.00, "latte.jpg", "Süt ağırlıklı, yumuşak ve hafif içimli kahve"),
                    "12": ("Sıcak Çikolata", 100.00, "sıcakçioklata.jpg", "Yoğun çikolatalı, sıcak ve tatlı keyif"),
                    "13": ("Flat White", 145.00, "flat-white.jpg", "Yoğun espresso, ince süt dokusu"),
                    "14": ("Salep", 90.00, "salep.jpg", "Tarçın eşliğinde, sıcak ve geleneksel kış içeceği")
                }
            },

            "soguk_icecekler": {
                "kategori": "Soğuk Kahveler & Soğuk İçecekler",
                "ikon": "🍹",
                "alt_baslik": "Ferahlatıcı içecekler",
                "urunler": {
                    "1": ("Limonata", 75.00, "limonata.jpg", "Taze sıkılmış limon ile ferahlatıcı içim"),
                    "2": ("Portakal Suyu", 85.00, "portakalsuyu.jpg", "Doğal ve taze sıkılmış portakal suyu"),
                    "3": ("Nar Suyu", 90.00, "narsuyu.jpg", "Yoğun aromalı, doğal nar suyu"),
                    "4": ("Coca Cola", 90.00, "cocacola.jpg", "Soğuk servis edilen klasik gazlı içecek"),
                    "5": ("Sprite", 90.00, "sprite.jpg", "Limon aromalı, ferahlatıcı gazlı içecek"),
                    "6": ("Lipton Ice Tea", 85.00, "liptonıcetea.jpg", "Soğuk çay, hafif ve ferahlatıcı içim"),
                    "7": ("Kapalı Ayran", 70.00, "Kapalıayran.jpg", "Serinletici, yoğurt bazlı geleneksel içecek"),
                    "8": ("Açık Ayran", 70.00, "açık_ayran.jpg", "Serinletici, yoğurt bazlı geleneksel içecek"),
                    "9": ("Sade Soda", 60.00, "soda.jpg", "Doğal mineralli sade soda"),
                    "10": ("Limonlu Soda", 70.00, "limonlu_Soda.jpg", "Limon aromalı ferah soda"),
                    "11": ("Mandalinalı Soda", 70.00, "mandalinalısoda.jpg", "Mandalina aromalı hafif içim"),
                    "12": ("Elmalı Soda", 70.00, "elmali_soda.jpg", "Elma aromalı gazlı içecek"),
                    "13": ("Su", 30.00, "su.jpg", "Doğal içme suyu"),
                    "14": ("Cold Brew", 110.00, "coldbrew.jpg", "Soğuk demleme, yumuşak içimli kahve"),
                    "15": ("Ice Latte", 115.00, "ıcelatte.jpg", "Soğuk sütlü kahve, ferah içim"),
                    "16": ("Ice Americano", 110.00, "Ice-Americano.jpg", "Soğuk espresso bazlı kahve"),
                    "17": ("Milkshake", 120.00, "milkshake.jpg", "Yoğun kıvamlı, sütlü ve tatlı içecek"),
                    "18": ("Frozen (Meyveli)", 125.00, "frozen.jpg", "Buzlu, meyve aromalı ferahlatıcı içecek"),
                    "19": ("Smoothie", 130.00, "smoothiee.jpg", "Taze meyvelerle hazırlanmış sağlıklı içecek")
                }
            },

            "caylar": {
                "kategori": "Çaylar",
                "ikon": "🍵",
                "alt_baslik": "Demli ve aromatik çaylar",
                "urunler": {
                    "1": ("Demleme Çay", 75.00, "siyah-cay.jpg", "Demli, klasik Türk çayı"),
                    "2": ("Fincan Çay", 100.00, "fincancay.jpg", "Hafif içimli, fincanda servis edilen çay"),
                    "3": ("Bitki Çayları", 85.00, "bitki-cayi.jpg", "Rahatlatıcı, doğal bitki aromaları"),
                    "4": ("Meyve Aromalı Fincan Çay", 100.00, "meyvearomalı.jpg", "Meyve aromalarıyla zenginleştirilmiş çay"),
                    "5": ("Chai Tea Latte", 90.00, "chai-tea-latte.jpg", "Baharatlı, sütlü ve aromatik çay")
                }
            }
        }
    },

    "yiyecekler": {
        "ana_kategori": "Yiyecekler",
        "ikon": "🍽️",
        "alt_kategoriler": {
            "corbalar": {
                "kategori": "Çorbalar",
                "ikon": "🥣",
                "alt_baslik": "Sıcak başlangıçlar",
                "urunler": {
                    "1": ("Mercimek Çorbası", 75.00, "mercimek-corbasi.jpg", "Klasik, sıcak ve doyurucu mercimek çorbası"),
                    "2": ("Ezogelin Çorbası", 100.00, "ezogelin.jpg", "Baharatlı, geleneksel ezogelin çorbası"),
                    "3": ("Domates Çorbası", 85.00, "domates-corbasi.jpg", "Kaşar eşliğinde servis edilen domates çorbası"),
                    "4": ("Mantar Çorbası", 100.00, "mantar-corbasi.jpg", "Kremalı, yumuşak içimli mantar çorbası"),
                    "5": ("Tavuk Suyu Çorbası", 90.00, "tavuk-suyu.jpg", "Besleyici, sıcak tavuk suyu çorbası")
                }
            },

            "tatlilar": {
                "kategori": "Tatlılar",
                "ikon": "🍰",
                "alt_baslik": "Tatlı dokunuşlar",
                "urunler": {
                    "1": ("Pasta Dilimleri", 175.00, "pasta.jpg", "Meyveli ve çikolatalı günlük pasta çeşitleri"),
                    "2": ("Kurabiyeler", 95.00, "kurabiye.jpg", "Çikolatalı ve fındıklı ev yapımı kurabiyeler"),
                    "3": ("Cheesecake", 180.00, "cheesecake.jpg", "Frambuazlı ve sade seçeneklerle hafif tatlı"),
                    "4": ("Tiramisu", 170.00, "tiramisu.jpg", "Kahve aromalı, mascarpone kremalı klasik tatlı"),
                    "5": ("Brownie", 185.00, "brownie.jpg", "Yoğun çikolatalı, yumuşak dokulu brownie"),
                    "6": ("Magnolia", 165.00, "magnolia.jpg", "Muz ve bisküvi ile hazırlanan hafif sütlü tatlı"),
                    "7": ("Profiterol", 170.00, "profiterol.jpg", "Çikolata soslu, kremalı toplar"),
                    "8": ("Sufle", 190.00, "sufle.jpg", "İçi akışkan çikolatalı sıcak tatlı"),
                    "9": ("Waffle", 210.00, "waffle.jpg", "Meyve ve çikolata soslu sıcak waffle"),
                    "10": ("Pankek", 180.00, "pankek.jpg", "Ballı ve meyveli yumuşak pankekler"),
                    "11": ("Dondurma", 120.00, "dondurma.jpg", "Farklı aromalarda serinletici lezzet"),
                    "12": ("San Sebastian Cheesecake", 200.00, "sansebastian.jpg", "Yoğun kıvamlı, yanık yüzeyli cheesecake"),
                    "13": ("Trileçe", 165.00, "triliçe.jpg", "Süt şerbetli hafif Balkan tatlısı"),
                    "14": ("Kazandibi", 140.00, "kazandibi.jpg", "Karamelize yüzeyli sütlü tatlı"),
                    "15": ("Sütlaç", 135.00, "sütlac.jpg", "Fırınlanmış, geleneksel sütlü tatlı"),
                    "16": ("Aşure", 150.00, "aşure.jpg", "Bakliyat ve meyvelerle hazırlanan geleneksel tatlı"),
                    "17": ("Çikolatalı Cupcake", 130.00, "çilokalatalıcupcake.jpg", "Kremalı, küçük ve tatlı atıştırmalık"),
                    "18": ("Meyveli Tart", 170.00, "meyveli-tart.jpg", "Taze meyvelerle hazırlanmış hafif tatlı"),
                    "19": ("Ekler", 145.00, "ekler.jpg", "Kremalı ve çikolata kaplı klasik tatlı")
                }
            },

            "atistirmaliklar": {
                "kategori": "Atıştırmalıklar",
                "ikon": "🥐",
                "alt_baslik": "Umay’ın sofrası",
                "urunler": {
                    "1": ("Kruvasan", 80.00, "kruvasan.jpg", "Tereyağlı, kat kat yumuşak hamur"),
                    "2": ("Tostlar", 125.00, "tost.jpg", "Kaşarlı ve sucuklu sıcak tost seçenekleri"),
                    "3": ("Sandviçler", 135.00, "sandvic.jpg", "Tavuklu ve peynirli günlük sandviçler"),
                    "4": ("Salatalar", 185.00, "salata.jpg", "Taze malzemelerle hazırlanan hafif seçenekler"),
                    "5": ("Patates Kızartması", 95.00, "patates.jpg", "Çıtır, sıcak servis edilen patates"),
                    "6": ("Sigara Böreği", 100.00, "sigaraboregi.jpg", "Peynir dolgulu, kızarmış börek"),
                    "7": ("Peynir Tabağı", 160.00, "peynirtabagi.jpg", "Farklı peynir çeşitleriyle sunum"),
                    "8": ("Zeytin Tabağı", 120.00, "zeytin.jpg", "Yeşil ve siyah zeytin çeşitleri"),
                    "9": ("Mini Pizza", 140.00, "minipizza.jpg", "Küçük boy, bol malzemeli pizza"),
                    "10": ("Omlet", 130.00, "omlet.jpg", "Sade veya karışık omlet seçenekleri"),
                    "11": ("Menemen", 145.00, "menemen.jpg", "Domatesli, biberli klasik lezzet"),
                    "12": ("Gözleme", 135.00, "gozleme.jpg", "Peynirli ve patatesli geleneksel gözleme"),
                    "13": ("Kaşarlı Simit", 90.00, "kasarlisimit.jpg", "Simit içinde erimiş kaşar peyniri"),
                    "14": ("Sosis Tabağı", 130.00, "sosis.jpg", "Kızarmış sosis ve yanında soslar"),
                    "15": ("Chicken Nuggets", 140.00, "nuggets.jpg", "Çıtır tavuk parçaları"),
                    "16": ("Mozzarella Sticks", 150.00, "mozzarella.jpg", "İçi eriyen peynir çubukları"),
                    "17": ("Soğan Halkası", 120.00, "sogan.jpg", "Kızarmış çıtır soğan halkaları"),
                    "18": ("Avokado Tost", 165.00, "avokado.jpg", "Avokado ve ekmekle sağlıklı atıştırmalık"),
                    "19": ("Peynirli Poğaça", 75.00, "pogaca.jpg", "Yumuşak hamurlu klasik poğaça")
                }
            }
        }
    }
}


def toplam_hesapla():
    return sum(urun["fiyat"] * urun["adet"] for urun in siparisler)


@app.route("/")
def index():
    toplam = toplam_hesapla()
    return render_template("index.html", menu=menu, siparisler=siparisler, toplam=toplam)


@app.route("/ekle", methods=["POST"])
def ekle():
    urun_adi = request.form.get("urun_adi")
    fiyat = float(request.form.get("fiyat"))
    anchor = request.form.get("anchor")

    for urun in siparisler:
        if urun["urun"] == urun_adi:
            urun["adet"] += 1

            if anchor:
                return redirect(url_for("index") + "#" + anchor)

            return redirect(url_for("index"))

    siparisler.append({
        "urun": urun_adi,
        "fiyat": fiyat,
        "adet": 1
    })

    if anchor:
        return redirect(url_for("index") + "#" + anchor)

    return redirect(url_for("index"))


@app.route("/azalt", methods=["POST"])
def azalt():
    urun_adi = request.form.get("urun_adi")
    anchor = request.form.get("anchor")

    for urun in siparisler:
        if urun["urun"] == urun_adi:
            urun["adet"] -= 1

            if urun["adet"] <= 0:
                siparisler.remove(urun)

            break

    if anchor:
        return redirect(url_for("index") + "#" + anchor)

    return redirect(url_for("index"))


@app.route("/temizle", methods=["POST"])
def temizle():
    siparisler.clear()
    return redirect(url_for("index") + "#sepet")


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5050)