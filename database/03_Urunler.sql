CREATE TABLE Urunler
(
    UrunID INT IDENTITY(1,1) PRIMARY KEY,
    KategoriID INT NOT NULL,
    UrunAdi NVARCHAR(100) NOT NULL,
    Aciklama NVARCHAR(500) NULL,
    Fiyat DECIMAL(10,2) NOT NULL,
    Gorsel NVARCHAR(255) NULL,
    Durum BIT NOT NULL DEFAULT 1,
    KayitTarihi DATETIME NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Urunler_Kategoriler
        FOREIGN KEY (KategoriID)
        REFERENCES Kategoriler(KategoriID)
);
GO

INSERT INTO Urunler
(
    KategoriID,
    UrunAdi,
    Aciklama,
    Fiyat,
    Gorsel
)
VALUES
(1, 'Türk Kahvesi', 'Geleneksel bol köpüklü Türk kahvesi', 100.00, 'turk-kahvesi.jpg'),
(1, 'Filtre Kahve', 'Yumuşak içimli filtre kahve', 100.00, 'filtre-kahve.jpg'),
(1, 'Americano', 'Espresso bazlı sade kahve', 130.00, 'americano.jpg'),
(2, 'Limonata', 'Taze sıkılmış limon ile hazırlanır', 100.00, 'limonata.jpg'),
(2, 'Ice Latte', 'Soğuk sütlü kahve', 120.00, 'ice-latte.jpg'),
(3, 'Siyah Çay', 'Demli klasik çay', 40.00, 'siyah-cay.jpg'),
(3, 'Ihlamur', 'Rahatlatıcı bitki çayı', 60.00, 'ihlamur.jpg'),
(4, 'Mercimek Çorbası', 'Sıcak günlük mercimek çorbası', 90.00, 'mercimek-corbasi.jpg'),
(5, 'Cheesecake', 'Günlük taze cheesecake', 175.00, 'cheesecake.jpg'),
(5, 'Brownie', 'Yoğun çikolatalı brownie', 150.00, 'brownie.jpg'),
(6, 'Kaşarlı Tost', 'Sıcak kaşarlı tost', 120.00, 'kasarli-tost.jpg'),
(6, 'Kruvasan', 'Taze tereyağlı kruvasan', 110.00, 'kruvasan.jpg');
GO