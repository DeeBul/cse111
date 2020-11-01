-- Creating the tables
CREATE TABLE Classes (
    class char(25) not null,
    type char(5) not null,
    country char(20) not null,
    numGuns integer not null,
    bore decimal(3,0) not null,
    displacement integer not null
);

create table Ships (
    name char(25) not null,
    class char(25) not null,
    launched integer not null
);

create table Battles (
    name char(35),
    date date not null
);

create table Outcomes (
    ship char(25),
    battle char(35),
    result char(20)
);

-- Inserting the values in the tables
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

-- 3)
SELECT class, country
FROM Classes
WHERE bore >= 15;

-- 4)
SELECT name 
FROM Ships
WHERE launched < 1918;

-- 5)
SELECT ship 
FROM outcomes
WHERE battle = 'Surigao Strait' AND result='sunk';

-- 6)
SELECT Ships.name
FROM Ships
INNER JOIN Classes on Ships.class=Classes.class
WHERE launched > 1921 AND displacement > 40000;

-- 7)
SELECT Ships.name, Classes.displacement, Classes.numGuns
FROM Classes, outcomes,Ships
WHERE Ships.class=Classes.class AND Ships.name=outcomes.ship AND outcomes.battle = 'Surigao Strait'
GROUP BY outcomes.ship;

-- 8)
SELECT Ships.name, outcomes.ship, Classes.class
FROM Ships, Classes, outcomes
WHERE Ships.class=Classes.class AND Ships.name=outcomes.ship;

-- 9)
SELECT class
FROM Ships
GROUP BY class
HAVING COUNT(class)=2;

-- 10)
SELECT country
FROM Classes
WHERE type='bb'
INTERSECT
SELECT country
FROM Classes
WHERE type='bc';

-- 11)
SELECT DISTINCT ship
FROM outcomes
INNER JOIN battles on outcomes.battle=battles.name
WHERE outcomes.result='damaged' AND battles.date BETWEEN '1941-05-24' AND '1944-10-25';


