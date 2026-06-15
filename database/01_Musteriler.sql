CREATE TABLE Musteriler
(
    MusteriID INT IDENTITY(1,1) PRIMARY KEY,
    AdSoyad NVARCHAR(100) NOT NULL,
    Telefon NVARCHAR(20) NULL,
    DogumTarihi DATE NULL,
    ToplamSiparis INT NOT NULL DEFAULT 0,
    ToplamHarcama DECIMAL(10,2) NOT NULL DEFAULT 0,
    FavoriUrun NVARCHAR(100) NULL,
    SonSiparisTarihi DATETIME NULL,
    Durum BIT NOT NULL DEFAULT 1,
    KayitTarihi DATETIME NOT NULL DEFAULT GETDATE()
);
GO

INSERT INTO Musteriler
(
    AdSoyad,
    Telefon,
    DogumTarihi,
    ToplamSiparis,
    ToplamHarcama,
    FavoriUrun,
    SonSiparisTarihi
)
VALUES
('Ayşe Kaya', '0555 111 22 33', '1998-04-12', 18, 3450.00, 'Latte', '2026-06-03'),
('Mehmet Demir', '0555 222 33 44', '1995-09-21', 12, 2180.00, 'Türk Kahvesi', '2026-06-02'),
('Elif Yılmaz', '0555 333 44 55', '2000-01-18', 9, 1750.00, 'Cheesecake', '2026-06-01'),
('Can Arslan', '0555 444 55 66', '1997-11-05', 5, 920.00, 'Limonata', '2026-05-30');
GO