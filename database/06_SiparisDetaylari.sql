CREATE TABLE SiparisDetaylari
(
    DetayID INT IDENTITY(1,1) PRIMARY KEY,
    SiparisID INT NOT NULL,
    UrunID INT NOT NULL,
    Adet INT NOT NULL,
    BirimFiyat DECIMAL(10,2) NOT NULL,
    ToplamFiyat DECIMAL(10,2) NOT NULL,

    CONSTRAINT FK_SiparisDetaylari_Siparisler
        FOREIGN KEY (SiparisID)
        REFERENCES Siparisler(SiparisID),

    CONSTRAINT FK_SiparisDetaylari_Urunler
        FOREIGN KEY (UrunID)
        REFERENCES Urunler(UrunID)
);
GO

INSERT INTO SiparisDetaylari
(
    SiparisID,
    UrunID,
    Adet,
    BirimFiyat,
    ToplamFiyat
)
VALUES
(
    1,
    1,
    2,
    100.00,
    200.00
);
GO