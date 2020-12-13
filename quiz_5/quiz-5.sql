DROP TABLE Classes;
DROP TABLE Ships;
DROP TABLE Battles;
DROP TABLE Outcomes;

CREATE TABLE Classes (
    class char(25) PRIMARY KEY,
    type char(5),
    country char(20) NOT NULL, 
    numGuns integer,
    bore integer, 
    displacement integer,

    CHECK(type IN ('bb', 'bc'))
);

CREATE TABLE Ships (
    name char(25) PRIMARY KEY, 
    class char(25) NOT NULL,
    launched integer NOT NULL,

    FOREIGN KEY(class) REFERENCES Classes(class) 
        ON UPDATE CASCADE 
        ON DELETE CASCADE
);

CREATE TABLE Battles (
    name char(35) PRIMARY KEY,
    date date NOT NULL
);

CREATE TABLE Outcomes (
    ship char(25),
    battle char(35) NOT NULL, 
    result char(20),

    FOREIGN KEY(ship) REFERENCES Ships(name) ON UPDATE SET NULL ON DELETE SET NULL,
    FOREIGN KEY(battle) REFERENCES Battles(name) ON UPDATE CASCADE ON DELETE CASCADE,
    CHECK(result IN ('ok', 'sunk', 'damaged'))
);

-- 1
INSERT INTO Classes (class, type, country, numGuns, bore, displacement) VALUES 
('Bismarck', 'bb', 'Germany', 8, 15, 42000),
('Iowa', 'bb', 'USA', 9, 16, 46000),
('Kongo', 'bc', 'Japan', 8, 14, 32000),
('North Carolina', 'bb', 'USA', 9, 16, 37000),
('Renown', 'bc', 'Britain', 6, 15, 32000),
('Revenge', 'bb', 'Britain', 8, 15, 29000),
('Tennessee', 'bb', 'USA', 12, 14, 32000),
('Yamato', 'bb', 'Japan', 9, 18, 65000);

INSERT INTO Ships (name, class, launched) VALUES
('California', 'Tennessee', 1915),
('Haruna', 'Kongo', 1915),
('Hiei', 'Kongo', 1915),
('Iowa', 'Iowa', 1933),
('Kirishima', 'Kongo', 1915),
('Kongo', 'Kongo', 1913),
('Missouri', 'Iowa', 1935),
('Musashi', 'Yamato', 1942),
('New Jersey', 'Iowa', 1936),
('North Carolina', 'North Carolina', 1941),
('Ramillies', 'Revenge', 1917),
('Renown', 'Renown', 1916),
('Repulse', 'Renown', 1916),
('Resolution', 'Revenge', 1916),
('Revenge', 'Revenge', 1916),
('Royal Oak', 'Revenge', 1916),
('Royal Sovereign', 'Revenge', 1916),
('Tennessee', 'Tennessee', 1915),
('Washington', 'North Carolina', 1941),
('Wisconsin', 'Iowa', 1940),
('Yamato','Yamato', 1941);

INSERT INTO Battles (name, date) VALUES
('Denmark Strait', '1941-05-24'),
('Guadalcanal', '1942-11-15'),
('North Cape', '1943-12-26'),
('Surigao Strait', '1944-10-25');

INSERT INTO Outcomes (ship, battle, result) VALUES 
('California', 'Surigao Strait', 'ok'),
('Kirishima', 'Guadalcanal', 'sunk'),
('Resolution', 'Denmark Strait', 'ok'),
('Wisconsin', 'Guadalcanal', 'damaged'),
('Tennessee', 'Surigao Strait', 'ok'),
('Washington', 'Guadalcanal', 'ok'),
('New Jersey', 'Surigao Strait', 'ok'),
('Yamato', 'Surigao Strait', 'sunk'),
('Wisconsin', 'Surigao Strait', 'damaged');

-- 2
 -- have to run the pragma statement with schema
PRAGMA foreign_keys = ON;
DELETE FROM Classes
WHERE (displacement > 50000) OR (numGuns > 10);

-- 3
PRAGMA foreign_keys = ON;
INSERT INTO Classes
SELECT sh.name, clas.type, clas.country, clas.numGuns, clas.bore, clas.displacement
FROM Classes clas
INNER JOIN Ships sh ON clas.class=sh.class
WHERE clas.country = 'USA'
AND sh.class <> sh.name; 

UPDATE Ships
SET class=name
WHERE class IN (
    SELECT Classes.class
    FROM Classes
    INNER JOIN Ships ON Classes.class=Ships.class
    WHERE Classes.country = 'USA' and Ships.Class <> Ships.name    
    );

-- 4
PRAGMA foreign_keys = ON;
DELETE FROM Battles
WHERE name = 'North Cape';

-- 5
PRAGMA foreign_keys = ON;
UPDATE Battles
SET name = 'North Cape'
WHERE name = 'Guadalcanal';

-- 6
PRAGMA foreign_keys = ON;
UPDATE Battles
SET name = 'Strait of Surigao'
WHERE name = 'Surigao Strait';

-- 7
PRAGMA foreign_keys = ON;
DELETE FROM Ships
WHERE class = (SELECT Classes.class
FROM Classes
INNER JOIN Ships ON Classes.class = Ships.class
GROUP BY Classes.class
HAVING count(Ships.name) > 4);

-- 8
SELECT * 
FROM Ships;

-- 9
SELECT *
FROM Outcomes;
