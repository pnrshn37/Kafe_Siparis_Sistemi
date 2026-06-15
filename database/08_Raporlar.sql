USE UmayAnaCafeDB;
GO

CREATE VIEW VW_SiparisRaporu
AS
SELECT
    S.SiparisID,
    M.MasaNo,
    MS.AdSoyad,
    U.UrunAdi,
    SD.Adet,
    SD.BirimFiyat,
    SD.ToplamFiyat,
    O.OdemeTuru,
    O.OdemeTutari,
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
    ON SD.UrunID = U.UrunID
LEFT JOIN Odemeler O
    ON S.SiparisID = O.SiparisID;
GO