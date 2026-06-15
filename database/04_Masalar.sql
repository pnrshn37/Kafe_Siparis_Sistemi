CREATE TABLE Masalar
(
    MasaID INT IDENTITY(1,1) PRIMARY KEY,
    MasaNo NVARCHAR(20) NOT NULL,
    Kapasite INT NOT NULL,
    Konum NVARCHAR(50) NOT NULL,
    QRKod NVARCHAR(255) NULL,
    Durum BIT NOT NULL DEFAULT 0,
    KayitTarihi DATETIME NOT NULL DEFAULT GETDATE()
);
GO

INSERT INTO Masalar
(
    MasaNo,
    Kapasite,
    Konum,
    QRKod
)
VALUES
('Masa 1', 4, 'İç Mekan', 'masa1'),
('Masa 2', 4, 'İç Mekan', 'masa2'),
('Masa 3', 2, 'Bahçe', 'masa3'),
('Masa 4', 6, 'Bahçe', 'masa4'),
('Masa 5', 4, 'Teras', 'masa5'),
('Masa 6', 2, 'Teras', 'masa6');
GO