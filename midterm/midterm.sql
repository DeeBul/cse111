-- 1)
SELECT DISTINCT maker
FROM Product
WHERE type='printer';

-- 2)
SELECT maker
FROM Product
INNER JOIN printer ON Product.model = printer.model
WHERE color = 1 AND price < 200;

-- 3)
SELECT maker
FROM Product
WHERE type = 'pc' 
INTERSECT
SELECT maker
FROM Product
WHERE type = 'laptop'
INTERSECT
SELECT maker
FROM Product
WHERE type = 'printer';  

-- 4) 
SELECT maker
FROM Product
WHERE type = 'pc'
INTERSECT
SELECT maker
FROM Product
WHERE type = 'printer'
EXCEPT
SELECT maker
FROM Product
WHERE type = 'laptop';

-- 5)
SELECT prodPC.maker, prodPC.model AS pcModel, l.model AS laptopModel, (prodPC.minPC + l.minLaptop) AS Price
FROM (
    SELECT product.maker, PC.model, min(price) AS minPC
    FROM Product
    INNER JOIN PC ON Product.model=PC.model
    WHERE maker IN (
    SELECT DISTINCT maker
    FROM Product
    INNER JOIN PC ON Product.model = PC.model
    INTERSECT
    SELECT DISTINCT maker
    from Product
    INNER JOIN Laptop ON Product.model=Laptop.model)
    GROUP BY maker) prodPC,
    (SELECT Product.maker, Laptop.model, min(price) AS minLaptop
    FROM Product
    INNER JOIN Laptop ON Product.model=Laptop.model
    WHERE maker IN (
            SELECT DISTINCT maker
            FROM Product
            INNER JOIN PC ON Product.model=PC.model
            INTERSECT
            SELECT DISTINCT maker
            FROM Product
            INNER JOIN Laptop ON Product.model=Laptop.model)
            GROUP BY maker) l
WHERE prodPC.maker=l.maker;

-- 6)
SELECT AVG(price)
FROM Printer;

-- 7)
SELECT type, COUNT(model) as cnt
FROM Printer
GROUP BY type;

-- 8)
SELECT count(model)
FROM Printer
WHERE color = 1 and type = 'laser';

-- 9) 
SELECT maker
FROM Product
INNER JOIN Printer ON product.model=Printer.model
GROUP BY maker
HAVING COUNT(printer.type) >= 2;

-- 10)
SELECT screen, MIN(price) as MinPrice
FROM Laptop
GROUP BY screen;

-- 11)
SELECT screen
FROM Laptop
GROUP BY screen
HAVING COUNT(model) >= 3;

-- 12)
SELECT screen
FROM Laptop
GROUP BY screen
HAVING COUNT(speed) >= 2;

-- 13)
SELECT model, price
FROM Laptop
WHERE Laptop.price > (SELECT MAX(PC.price) FROM PC);

-- 14)
SELECT Printer.model, min(Printer.price) AS minPrice
FROM Product
INNER JOIN Printer ON Product.model=Printer.model
WHERE maker IN 
    (SELECT maker
    FROM (SELECT DISTINCT maker, max(price)
        FROM Product
        INNER JOIN PC ON Product.model = PC.model
        WHERE maker IN (SELECT DISTINCT maker
                    FROM Product
                    WHERE type = 'printer')
                    AND type = 'pc'));

-- 15)
SELECT pcTBL.avgPC, laptopTBL.avgLaptop, printerTBL.avgPrinter
FROM (SELECT avg(PC.price) AS avgPC
    FROM Product
    INNER JOIN PC ON Product.model=PC.model
    WHERE maker IN
        (SELECT maker
        FROM Product
        WHERE type = 'pc'
        INTERSECT
        SELECT maker
        FROM Product
        WHERE type = 'laptop'
        INTERSECT
        SELECT maker
        FROM Product
        WHERE type = 'printer')) pcTBL,
    (SELECT avg(Laptop.price) as avgLaptop
    FROM Product
    INNER JOIN Laptop ON Product.model=Laptop.model
    WHERE maker IN
        (SELECT maker
        FROM Product
        WHERE type = 'pc'
        INTERSECT
        SELECT maker
        FROM Product
        WHERE type = 'laptop'
        INTERSECT
        SELECT maker
        FROM Product
        WHERE type = 'printer'))laptopTBL,
    (SELECT avg(Printer.price) AS avgPrinter
    FROM Product
    INNER JOIN Printer ON Product.model=Printer.model
    WHERE maker IN
        (SELECT maker
        FROM Product
        WHERE type = 'pc'
        INTERSECT
        SELECT maker
        FROM Product
        WHERE type = 'laptop'
        INTERSECT
        SELECT maker
        FROM Product
        WHERE type = 'printer'))printerTBL;


-- 16)
SELECT maker 
FROM Product
WHERE type = 'laptop'
GROUP BY maker
HAVING COUNT(type) = 1;

-- 17)
SELECT DISTINCT maker
FROM Product
WHERE maker NOT IN (SELECT maker FROM Product WHERE type = 'laptop');

-- 18)
SELECT maker
FROM Product
INNER JOIN Laptop ON Product.model=Laptop.model
GROUP BY maker
HAVING COUNT(Laptop.model)=1
INTERSECT
SELECT maker
FROM Product
INNER JOIN PC ON Product.model=PC.model
GROUP BY maker 
HAVING COUNT(PC.model) = 3;

-- 19) 
SELECT maker
FROM Product
INNER JOIN Laptop ON Product.model=Laptop.model
GROUP BY maker
HAVING COUNT(Laptop.model) >= 1
UNION
SELECT maker
FROM Product
INNER JOIN PC ON Product.model=PC.model
GROUP BY maker 
HAVING COUNT(PC.model) >= 1
INTERSECT
SELECT maker
FROM Product
INNER JOIN Printer ON Product.model=Printer.model
GROUP BY maker
HAVING COUNT(Printer.model) <= 3;

-- 20)
SELECT Product.maker, Laptop.model, Laptop.screen, Laptop.speed
FROM Laptop, Product
WHERE Laptop.model = Product.model
AND Laptop.screen >= 15 
AND speed < 2
AND maker IN(SELECT maker FROM Product WHERE type='printer')
GROUP BY screen;

