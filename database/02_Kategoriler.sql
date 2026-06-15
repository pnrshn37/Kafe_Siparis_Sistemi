USE UmayAnaCafeDB;
GO

CREATE TABLE Kategoriler
(
    KategoriID INT IDENTITY(1,1) PRIMARY KEY,
    KategoriAdi NVARCHAR(100) NOT NULL,
    Durum BIT NOT NULL DEFAULT 1,
    KayitTarihi DATETIME NOT NULL DEFAULT GETDATE()
);
GO

INSERT INTO Kategoriler (KategoriAdi)
VALUES
('Kahveler & Sıcak İçecekler'),
('Soğuk Kahveler & Soğuk İçecekler'),
('Çaylar'),
('Çorbalar'),
('Tatlılar'),
('Atıştırmalıklar');
GO