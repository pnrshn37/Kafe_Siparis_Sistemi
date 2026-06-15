USE UmayAnaCafeDB;
GO

-- TÜM TABLOLARI LİSTELEME
SELECT name
FROM sys.tables;
GO

-- KATEGORİLER
SELECT * FROM Kategoriler;
GO

-- ÜRÜNLER
SELECT * FROM Urunler;
GO

-- MASALAR
SELECT * FROM Masalar;
GO

-- MÜŞTERİLER
SELECT * FROM Musteriler;
GO

-- SİPARİŞLER
SELECT * FROM Siparisler;
GO

-- SİPARİŞ DETAYLARI
SELECT * FROM SiparisDetaylari;
GO

-- ÖDEMELER
SELECT * FROM Odemeler;
GO

-- ÜRÜNLERİ KATEGORİ ADIYLA GETİRME
SELECT
    U.UrunID,
    U.UrunAdi,
    K.KategoriAdi,
    U.Aciklama,
    U.Fiyat,
    U.Gorsel,
    U.Durum
FROM Urunler U
INNER JOIN Kategoriler K
    ON U.KategoriID = K.KategoriID;
GO

-- SİPARİŞ DETAY RAPORU
SELECT
    S.SiparisID,
    M.MasaNo,
    MS.AdSoyad,
    U.UrunAdi,
    SD.Adet,
    SD.BirimFiyat,
    SD.ToplamFiyat,
    S.ToplamTutar,
    S.SiparisDurumu,
    S.SiparisTarihi
FROM Siparisler S
INNER JOIN Masalar M
    ON S.MasaID = M.MasaID
LEFT JOIN Musteriler MS
    ON S.MusteriID = MS.MusteriID
INNER JOIN SiparisDetaylari SD
    ON S.SiparisID = SD.SiparisID
INNER JOIN Urunler U
    ON SD.UrunID = U.UrunID;
GO

-- ÖDEME RAPORU
SELECT
    O.OdemeID,
    S.SiparisID,
    M.MasaNo,
    O.OdemeTuru,
    O.OdemeTutari,
    O.OdemeDurumu,
    O.OdemeTarihi
FROM Odemeler O
INNER JOIN Siparisler S
    ON O.SiparisID = S.SiparisID
INNER JOIN Masalar M
    ON S.MasaID = M.MasaID;
GO

-- VIEW RAPORU
SELECT * FROM VW_SiparisRaporu;
GO