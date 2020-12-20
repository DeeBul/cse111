DROP TABLE Product;
DROP TABLE Distributor;
DROP TABLE Price_Cube;

-- CREATE TABLE Product(
--     model integer PRIMARY KEY,
--     type char(25),
--     maker char(15)
-- );

-- CREATE TABLE Distributor(
--     model integer PRIMARY KEY,
--     name char(25), 
--     price integer,

--     FOREIGN KEY(model) REFERENCES Product(model)
--         ON UPDATE CASCADE
--         ON DELETE CASCADE
-- );

-- CREATE TABLE Price_Cube(
--     distributor_type char(255),
--     product_type char(255),
--     num_prod integer,
--     tot_price integer,
--     PRIMARY KEY(distributor_type, product_type)
-- );

-- -- INSERT INTO Price_Cube
--     -- SELECT Product.maker AS distributor_type, product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
--     -- FROM Product
--     -- INNER JOIN Distributor ON Product.model=Distributor.model
--     -- WHERE Product.maker = Distributor.name
--     -- GROUP BY distributor_type, product_type
--     -- UNION
--     -- SELECT Product.maker AS distributor_type, '*' AS product_type, COUNT(*) AS num_prod, SUM(Distributor.price) AS tot_price
--     -- FROM Product
--     -- INNER JOIN Distributor ON Product.model=Distributor.model
--     -- WHERE Product.maker = Distributor.name
--     -- GROUP BY product_type
--     -- UNION
--     -- SELECT '*' AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, SUM(Distributor.price) AS tot_price
--     -- FROM Product
--     -- INNER JOIN Distributor ON Product.model=Distributor.model
--     -- WHERE Product.maker = Distributor.name
--     -- GROUP BY distributor_type;
--     -- UNION
--     -- SELECT '*' AS distributor_type, '*' AS product_type, COUNT(*) AS num_prod, SUM(Distributor.price) AS tot_price
--     -- FROM Product
--     -- INNER JOIN Distributor ON Product.model=Distributor.model
--     -- WHERE Product.maker = Distributor.name
--     -- GROUP BY distributor_type, product_type;


--         SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
--     FROM Product
--     INNER JOIN Distributor ON Product.model=Distributor.model
--     -- WHERE Product.maker = Distributor.name
--     GROUP BY distributor_type, product_type
--     UNION
--     SELECT Product.maker AS distributor_type, '*' AS product_type, COUNT(*) AS num_prod, SUM(Distributor.price) AS tot_price
--     FROM Product
--     INNER JOIN Distributor ON Product.model=Distributor.model
--     -- WHERE Product.maker = Distributor.name
--     GROUP BY product_type
--     UNION
--     SELECT '*' AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, SUM(Distributor.price) AS tot_price
--     FROM Product
--     INNER JOIN Distributor ON Product.model=Distributor.model
--     WHERE Product.maker = Distributor.name
--     GROUP BY distributor_type, product_type;
--     UNION
--     SELECT '*' AS distributor_type, '*' AS product_type, COUNT(*) AS num_prod, SUM(Distributor.price) AS tot_price
--     FROM Product
--     INNER JOIN Distributor ON Product.model=Distributor.model
--     WHERE Product.maker = Distributor.name
--     GROUP BY distributor_type, product_type;



--     SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
--     FROM Product
--     INNER JOIN Distributor ON Product.model=Distributor.model
--     GROUP BY distributor_type, product_type
--     UNION
--     SELECT '*' AS distributor_type, product_type, num_prod, tot_price
--     FROM (
--         SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
--         FROM Product
--         INNER JOIN Distributor ON Product.model=Distributor.model
--         GROUP BY product_type
--     )
--     UNION
--     SELECT distributor_type, '*' AS product_type, num_prod, tot_price
--     FROM (
--         SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
--         FROM Product
--         INNER JOIN Distributor ON Product.model=Distributor.model
--         GROUP BY distributor_type
--     )
--     UNION
--     SELECT '*' AS distributor_type, '*' AS product_type, num_prod, tot_price
--     FROM (
--         SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
--         FROM Product
--         INNER JOIN Distributor ON Product.model=Distributor.model
--     );










--     SELECT '*' AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, SUM(Distributor.price) AS tot_price
--     FROM Product
--     INNER JOIN Distributor ON Product.model=Distributor.model
--     -- WHERE Product.maker = Distributor.name
--     GROUP BY product_type
--     UNION
--     SELECT Product.maker AS distributor_type, '*' AS product_type, COUNT(*) AS num_prod, SUM(Distributor.price) AS tot_price
--     FROM Product
--     INNER JOIN Distributor ON Product.model=Distributor.model
--     -- WHERE Product.maker = Distributor.name
--     GROUP BY distributor_type;



