CREATE TABLE Siparisler
(
    SiparisID INT IDENTITY(1,1) PRIMARY KEY,
    MasaID INT NOT NULL,
    MusteriID INT NULL,
    ToplamTutar DECIMAL(10,2) NOT NULL,
    SiparisDurumu NVARCHAR(50) NOT NULL DEFAULT 'Hazırlanıyor',
    SiparisTarihi DATETIME NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Siparisler_Masalar
        FOREIGN KEY (MasaID)
        REFERENCES Masalar(MasaID),

    CONSTRAINT FK_Siparisler_Musteriler
        FOREIGN KEY (MusteriID)
        REFERENCES Musteriler(MusteriID)
);
GO

INSERT INTO Siparisler
(
    MasaID,
    MusteriID,
    ToplamTutar
)
VALUES
(
    1,
    1,
    250.00
);
GO