-- Q1
SELECT *
FROM warehouse

-- Q2
SELECT nation.n_name, COUNT(w_warehousekey) as cnt, sum(w_capacity) as sum
FROM warehouse
INNER JOIN nation on warehouse.w_nationkey = nation.n_nationkey
GROUP BY nation.n_name
ORDER BY cnt DESC, sum DESC;

Q3
SELECT supplier.s_name AS Supplier, nation.n_name AS nation, warehouse.w_name AS WarehouseName
FROM supplier
INNER JOIN warehouse ON supplier.s_suppkey=warehouse.w_suppkey
INNER JOIN nation ON supplier.s_nationkey=nation.n_nationkey
WHERE warehouse.w_name LIKE '%JAPAN';

-- Q4
SELECT w_name, w_capacity
FROM warehouse
INNER JOIN nation ON warehouse.w_nationkey=nation.n_nationkey
INNER JOIN region ON nation.n_regionkey=region.r_regionkey
WHERE region.r_name='ASIA'
AND warehouse.w_capacity >= 2000
ORDER BY warehouse.w_capacity DESC;

-- Q5
SELECT region.r_name, sum(warehouse.w_capacity) AS sumCap
FROM warehouse 
INNER JOIN supplier ON warehouse.w_suppkey=supplier.s_suppkey
INNER JOIN nation ON warehouse.w_nationkey=nation.n_nationkey
INNER JOIN region ON nation.n_regionkey=region.r_regionkey
WHERE supplier.s_nationkey IN (
   SELECT s_nationkey
   FROM supplier
   INNER JOIN nation ON supplier.s_nationkey=nation.n_nationkey
   WHERE nation.n_name = 'UNITED STATES'
)
GROUP BY r_name;

-- ***************************************************************

SELECT region.r_name AS regions, sum(warehouse.w_capacity) AS sumCap
FROM warehouse 
INNER JOIN supplier ON warehouse.w_suppkey=supplier.s_suppkey
INNER JOIN nation ON warehouse.w_nationkey=nation.n_nationkey
INNER JOIN region ON nation.n_regionkey=region.r_regionkey
WHERE supplier.s_nationkey IN (
   SELECT s_nationkey
   FROM supplier
   INNER JOIN nation ON nation.n_nationkey=supplier.s_nationkey
   WHERE nation.n_name = 'UNITED STATES'
)

GROUP BY region.r_name

-- ****************************************** Inserting Into Table Queries *************************************************
-- Populating Name 
INSERT INTO warehouse (w_name, w_capacity, w_suppkey, w_nationkey)
   SELECT (supplier.s_name || "___" || nation.n_name) as warehouseName, COUNT(*) AS cnt
   FROM lineitem
   INNER JOIN supplier ON lineitem.l_suppkey=supplier.s_suppkey
   INNER JOIN orders ON lineitem.l_orderkey=orders.o_orderkey
   INNER JOIN customer ON orders.o_custkey=customer.c_custkey
   INNER JOIN nation ON customer.c_nationkey=nation.n_nationkey
   GROUP BY lineitem.l_suppkey, customer.c_nationkey
   ORDER BY lineitem.l_suppkey, cnt DESC, nation.n_name;

-- Populating Name Query
   SELECT (supplier.s_name || "___" || nation.n_name) as warehouseName, supplier.s_suppkey, nation.n_nationkey,(COUNT(part.p_size) * 2) as capacity
   FROM lineitem
   INNER JOIN supplier ON lineitem.l_suppkey=supplier.s_suppkey
   INNER JOIN orders ON lineitem.l_orderkey=orders.o_orderkey
   INNER JOIN customer ON orders.o_custkey=customer.c_custkey
   INNER JOIN nation ON customer.c_nationkey=nation.n_nationkey
   INNER JOIN part ON lineitem.l_partkey=part.p_partkey
   GROUP BY lineitem.l_suppkey, customer.c_nationkey
   ORDER BY lineitem.l_suppkey, capacity DESC, nation.n_name;
   -- LIMIT 2;


   SELECT (supplier.s_name || "___" || nation.n_name) as warehouseName, COUNT(*) AS cnt
   FROM lineitem
   INNER JOIN supplier ON lineitem.l_suppkey=supplier.s_suppkey
   INNER JOIN orders ON lineitem.l_orderkey=orders.o_orderkey
   INNER JOIN customer ON orders.o_custkey=customer.c_custkey
   INNER JOIN nation ON customer.c_nationkey=nation.n_nationkey
   GROUP BY lineitem.l_suppkey, customer.c_nationkey
   ORDER BY lineitem.l_suppkey, cnt DESC, nation.n_name;
   -- LIMIT 2;





   -- Populating Capacity
   -- SELECT (2 * totalSize)
   -- FROM 
   -- (
   -- SELECT SUM(p_size) AS totalSize 
   -- FROM part
   -- INNER JOIN lineitem ON part.p_partkey=lineitem.l_partkey
   -- INNER JOIN orders ON lineitem.l_orderkey=orders.o_orderkey
   -- INNER JOIN supplier ON lineitem.l_suppkey=supplier.s_suppkey
   -- INNER JOIN nation ON supplier.s_nationkey=nation.n_nationkey
   -- INNER JOIN customer ON orders.o_custkey=customer.c_custkey 
   -- GROUP BY nation.n_name
   -- );
