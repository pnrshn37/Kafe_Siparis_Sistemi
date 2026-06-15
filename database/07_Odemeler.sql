USE UmayAnaCafeDB;
GO

CREATE TABLE Odemeler
(
    OdemeID INT IDENTITY(1,1) PRIMARY KEY,

    SiparisID INT NOT NULL,

    OdemeTuru NVARCHAR(50) NOT NULL,

    OdemeTutari DECIMAL(10,2) NOT NULL,

    OdemeDurumu NVARCHAR(50) NOT NULL DEFAULT 'Ödendi',

    OdemeTarihi DATETIME NOT NULL DEFAULT GETDATE(),

    CONSTRAINT FK_Odemeler_Siparisler
        FOREIGN KEY (SiparisID)
        REFERENCES Siparisler(SiparisID)
);
GO

INSERT INTO Odemeler
(
    SiparisID,
    OdemeTuru,
    OdemeTutari,
    OdemeDurumu
)
VALUES
(1, 'Kart', 250.00, 'Ödendi');
GO

SELECT * FROM Odemeler;