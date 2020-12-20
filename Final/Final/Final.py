import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn


def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def create_tables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("CREATE TABLES")

    try:
        sqlProduct = """CREATE TABLE Product (
                model integer PRIMARY KEY NOT NULL,
                type char(25),
                maker char(15)
        )"""
        _conn.execute(sqlProduct)

        sqlDistributor = """CREATE TABLE Distributor(
                    model integer,
                    name char(25),
                    price integer,
                    PRIMARY KEY(model, name)
                    
                    FOREIGN KEY(model) REFERENCES Product(model) 
                        ON UPDATE CASCADE
                        ON DELETE CASCADE
                    )"""
        _conn.execute(sqlDistributor)

        sqldataCube = """CREATE TABLE Price_Cube (
                distributor_type char(255),
                product_type char(255),
                num_prod integer,
                tot_price integer
                
             )"""
        _conn.execute(sqldataCube)

        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)

    print("++++++++++++++++++++++++++++++++++")


def populate_tables(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("POPULATE TABLES")
    curr = _conn.cursor()

# this works vvvvvv
    file_data = [i.strip('\n').split('|') for i in open('product.txt')]
    new_data = [[int(a), *b] for a, *b in file_data]
    curr.executemany('INSERT INTO Product(model, type, maker) VALUES (?, ?, ?)', new_data)

    file_data2 = [i2.strip('\n').split('|') for i2 in open('distributor.txt')]
    new_data2 = [[int(a2), *b2] for a2, *b2 in file_data2]
    curr.executemany('INSERT INTO Distributor(model, name, price) VALUES (?, ?, ?)', new_data2)

    print("++++++++++++++++++++++++++++++++++")


def build_data_cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("BUILD DATA CUBE")
    
    try:
        sql = '''INSERT INTO Price_Cube
                    SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
                    FROM Product
                    INNER JOIN Distributor ON Product.model=Distributor.model
                    GROUP BY distributor_type, product_type
                    UNION
                    SELECT '*' AS distributor_type, product_type, num_prod, tot_price
                    FROM (
                        SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
                        FROM Product
                        INNER JOIN Distributor ON Product.model=Distributor.model
                        GROUP BY product_type
                    )
                    UNION
                    SELECT distributor_type, '*' AS product_type, num_prod, tot_price
                    FROM (
                        SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
                        FROM Product
                        INNER JOIN Distributor ON Product.model=Distributor.model
                        GROUP BY distributor_type
                    )
                    UNION
                    SELECT '*' AS distributor_type, '*' AS product_type, num_prod, tot_price
                    FROM (
                        SELECT substr(Distributor.name, 1, 1) AS distributor_type, Product.type AS product_type, COUNT(*) AS num_prod, sum(distributor.price) AS tot_price
                        FROM Product
                        INNER JOIN Distributor ON Product.model=Distributor.model
                    )'''
        args = []
        _conn.execute(sql, args)
        _conn.commit()

    except Error as e:
        _conn.rollback()
        print(e)
            

    print("++++++++++++++++++++++++++++++++++")


def print_Product(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT PRODUCT")

    try:
        sql = '''SELECT * FROM Product'''
        args = []
        curr = _conn.cursor()
        curr.execute(sql, args)  
        
        l = '{:<20} {:<20} {:<20}'.format("model", "type", "maker")
        print(l)

        rows = curr.fetchall()
        for rows in rows:
            printProduct = '{:<20}{:<20}{:<20}\n'.format(rows[0], rows[1], rows[2])
            print(printProduct)
    except Error as e:
        print(e)

    # l = '{:<20} {:<20} {:<20}'.format("model", "type", "maker")
    # print(l)

    print("++++++++++++++++++++++++++++++++++")


def print_Distributor(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT DISTRIBUTOR")

    try:
        sql = """SELECT * FROM Distributor"""
        args = []
        curr = _conn.cursor()
        curr.execute(sql, args)

        l = '{:<20} {:<20} {:>20}'.format("model", "name", "price")
        print(l)

        rows = curr.fetchall()
        for rows in rows:
            printDistribute = '{:<20}{:<20}{:>20}\n'.format(rows[0], rows[1], rows[2])
            print(printDistribute)
    
    except Error as e:
        print(e)

    # l = '{:<20} {:<20} {:>20}'.format("model", "name", "price")
    # print(l)

    print("++++++++++++++++++++++++++++++++++")


def print_Cube(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("PRINT DATA CUBE")

    try:
        sql = '''SELECT * FROM Price_Cube'''
        args = []
        curr = _conn.cursor()
        curr.execute(sql, args)

        l = '{:<20} {:<20} {:>10} {:>10}'.format("dist", "prod", "cnt", "total")
        print(l)

        rows = curr.fetchall()
        for rows in rows:
            printCube = '{:<20} {:<20} {:>10} {:>10}\n'.format(rows[0], rows[1], rows[2], rows[3])
            print(printCube)

    except Error as e:
        print(e)


    print("++++++++++++++++++++++++++++++++++")

def insertProduct(_conn, model, prodType, maker):
    # l = 'Insert Product ({}, {})'.format(model, type, maker)
    try:
        sql = '''INSERT INTO Product(model, type, maker) VALUES(?, ?, ?)'''
        args = [model, prodType, maker]
        curr = _conn.cursor()
        curr.execute(sql, args)
        _conn.commit()
    
    except Error as e:
        print(e)

def insertDistributor(_conn, model, name, price):
    try:
        sql = '''INSERT INTO Distributor(model, name, price) VALUES(?, ?, ?)'''
        args = [model, name, price]
        curr = _conn.cursor()
        curr.execute(sql, args)
        _conn.commit()
   
    except Error as e:
        _conn.rollback()
        print(e)

def deleteProd(_conn, model):
    try:
        sql = '''DELETE FROM Product
                    WHERE model = ?'''
        args = [model]
        curr = _conn.cursor()
        curr.execute(sql, args)
        _conn.commit()
    
    except Error as e:
        _conn.rollback()
        print(e)

def deleteDist(_conn, model, name):
    try:
        sql = '''DELETE FROM Product
                    WHERE model = ?
                    AND name = ?'''
        args = [model, name]
        curr = _conn.cursor()
        curr.execute(sql, args)
        _conn.commit()
    
    except Error as e:
        _conn.rollback()
        print(e)

def modifications(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("MODIFICATIONS")

    file = open('modifications.txt', 'r')
    lines = file.readlines()
    for line in lines:
        print(line.strip())

        tok = line.strip().split(' ')
        if (tok[0] == 'Product' and tok[1] == 'I'):
            insertProduct(_conn, tok[2], tok[3], tok[4])
        
        if (tok[0] == 'Distributor' and tok[1] == 'I'):
            insertDistributor(_conn, tok[2], tok[3], tok[4])
        
        if (tok[0] == 'Product' and tok[1] == 'D'):
            deleteProd(_conn, tok[2])
        
        if (tok[0] == 'Distributor' and tok[1] == 'D'):
            deleteDist(_conn, tok[2], tok[3])


    print("++++++++++++++++++++++++++++++++++")



def main():
    database = r"data.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        create_tables(conn)

        populate_tables(conn)

        print_Product(conn)
        print_Distributor(conn)

        build_data_cube(conn)
        print_Cube(conn)

        modifications(conn)

        print_Product(conn)
        print_Distributor(conn)

        build_data_cube(conn)
        print_Cube(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
