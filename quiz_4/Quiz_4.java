// STEP: Import required packages
import java.sql.*;

// import sun.print.resources.serviceui_ja;

import java.io.FileWriter;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.File;

public class Quiz_4 {
    private Connection c = null;
    private String dbName;
    private boolean isConnected = false;

    private void openConnection(String _dbName) {
        dbName = _dbName;

        if (false == isConnected) {
            System.out.println("++++++++++++++++++++++++++++++++++");
            System.out.println("Open database: " + _dbName);

            try {
                String connStr = new String("jdbc:sqlite:");
                connStr = connStr + _dbName;

                // STEP: Register JDBC driver
                Class.forName("org.sqlite.JDBC");

                // STEP: Open a connection
                c = DriverManager.getConnection(connStr);

                // STEP: Diable auto transactions
                c.setAutoCommit(false);

                isConnected = true;
                System.out.println("success");
            } catch (Exception e) {
                System.err.println(e.getClass().getName() + ": " + e.getMessage());
                System.exit(0);
            }

            System.out.println("++++++++++++++++++++++++++++++++++");
        }
    }

    private void closeConnection() {
        if (true == isConnected) {
            System.out.println("++++++++++++++++++++++++++++++++++");
            System.out.println("Close database: " + dbName);

            try {
                // STEP: Close connection
                c.close();

                isConnected = false;
                dbName = "";
                System.out.println("success");
            } catch (Exception e) {
                System.err.println(e.getClass().getName() + ": " + e.getMessage());
                System.exit(0);
            }

            System.out.println("++++++++++++++++++++++++++++++++++");
        }
    }

    private void populatePriceRange() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Populate PriceRange");

        try {

            String sql1 = "DELETE FROM PriceRange";
            String sql = "INSERT INTO PriceRange" +
                    " SELECT maker, Product.type, min(price), max(price)" +
                    " FROM Product" +
                    " INNER JOIN PC ON Product.model=PC.model" +
                    " GROUP BY maker, Product.type" + 
                    " UNION" +
                    " SELECT maker, Product.type, min(price), max(price)" +
                    " FROM Product" + 
                    " INNER JOIN Laptop ON Product.model=Laptop.model" +
                    " GROUP BY maker, Product.type" +
                    " UNION" +
                    " SELECT maker, Product.type, min(price), max(price)" +
                    " FROM Product" +
                    " INNER JOIN Printer ON Product.model=Printer.model" + 
                    " GROUP BY maker, Product.type";

            Statement stmt = c.createStatement(); // use statement since there is no inputs
            
            stmt.executeUpdate(sql1);
            stmt.executeUpdate(sql);


            c.commit();
            stmt.close();
     
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
            try {
                c.rollback();
            } catch (Exception e1) {
                System.err.println(e1.getClass().getName() + ": " + e1.getMessage());
            }
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void printPriceRange() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("Print PriceRange");

        System.out.printf("%-10s %-20s %20s %20s\n",
            "maker", "product", "minPrice", "maxPrice");

        try {
            String sql = "SELECT *" +
                        " FROM PriceRange";

            Statement stmt = c.createStatement();
            ResultSet rs = stmt.executeQuery(sql);
            c.commit();

            // System.out.printf("%-10s %-20s %20s %20s\n",
            // "maker", "product", "minPrice", "maxPrice");

            while(rs.next()) {
                String maker = rs.getString(1);
                String product = rs.getString(2);
                String minPrice = rs.getString(3);
                String maxPrice = rs.getString(4);
                System.out.printf("%-10s %-20s %20s %20s\n",
            maker, product, minPrice, maxPrice);
            }

            rs.close();
            stmt.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
            try {
                c.rollback();
            } catch (Exception e1) {
                System.err.println(e1.getClass().getName() + ": " + e1.getMessage());
            }
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void insertPC(String _maker, int _model, double _speed,
        int _ram, int _hd, int _price) {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.printf("Insert PC (%s, %d, %f, %d, %d, %d)\n",
            _maker, _model, _speed, _ram, _hd, _price);

        try {
            String PCsql = "INSERT OR IGNORE INTO PC(model, speed, ram, hd, price)" + 
                        " VALUES(?, ?, ?, ?, ?)";
           
            String Productsql = "INSERT OR IGNORE INTO Product(maker, model, type)" + 
                                " VALUES(?, ?, 'pc')";

            PreparedStatement PCstmt = c.prepareStatement(PCsql);
           

            PCstmt.setInt(1, _model);
            PCstmt.setDouble(2, _speed);
            PCstmt.setInt(3, _ram);
            PCstmt.setInt(4, _hd);
            PCstmt.setInt(5, _price);
            PCstmt.executeUpdate();
            PCstmt.close();
            // c.commit();

            PreparedStatement Prodstmt = c.prepareStatement(Productsql);
            Prodstmt.setString(1, _maker);
            Prodstmt.setInt(2, _model);
            Prodstmt.executeUpdate();
            Prodstmt.close();

            System.out.println("success: Insert into PC and Product table");
            populatePriceRange();

        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
            try {
                c.rollback();
            } catch (Exception e1) {
                System.err.println(e1.getClass().getName() + ": " + e1.getMessage());
            }
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

// updating a printer price
    private void updatePrinter(int _model, int _price) {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.printf("Update Printer (%d, %d)\n", _model, _price);

        try {
            String sql = "UPDATE Printer" +
                        " SET price = ?" +
                        " WHERE model = ?";

            PreparedStatement stmt = c.prepareStatement(sql);
            stmt.setInt(1, _price);
            stmt.setInt(2, _model);

            stmt.executeUpdate();
            c.commit();
            
            stmt.close();
            System.out.println("success");

            populatePriceRange();

        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
            try {
                c.rollback();
            } catch (Exception e1) {
                System.err.println(e1.getClass().getName() + ": " + e1.getMessage());
            }
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

// Deleting a laptop model
    private void deleteLaptop(int _model) {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.printf("Delete Laptop (%d)\n", _model);

       try {
           String sql = "DELETE FROM Laptop" + 
                        " WHERE model = ?"; //question mark for input
            
            //removing from product also
            String sql2 = "DELETE FROM Product" + 
                            " Where model = ?";

            PreparedStatement stmt1 = c.prepareStatement(sql); // since we have input use this 
            stmt1.setInt(1, _model);
            stmt1.executeUpdate(); //executing
            stmt1.close(); 
            // c.commit(); //committing

            PreparedStatement stmt2 = c.prepareStatement(sql2);
            stmt2.setInt(1, _model);
            stmt2.executeUpdate();
            stmt2.close();

            System.out.println("success"); //success if gone through

            populatePriceRange();

       } catch (Exception e) {
           System.err.println(e.getClass().getName() + ": " + e.getMessage());
           try {
               c.rollback();
           } catch (Exception e1) {
               System.err.println(e1.getClass().getName() + ": " + e1.getMessage());
           }
       }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    public static void main(String args[]) {
        Quiz_4 sj = new Quiz_4();
        
        sj.openConnection("data.sqlite");

        sj.populatePriceRange();
        sj.printPriceRange();

        try {
            File fn = new File("input.in");
            FileReader reader = new FileReader(fn);
            BufferedReader in = new BufferedReader(reader);

            String line = null;
            while ((line = in.readLine()) != null) {
                System.out.println(line);

                String[] tok = line.split("[ ]");
                if (tok[0].equals(new String("I"))) {
                    sj.insertPC(tok[2], Integer.parseInt(tok[3]),
                        Double.parseDouble(tok[4]), Integer.parseInt(tok[5]),
                        Integer.parseInt(tok[6]), Integer.parseInt(tok[7]));
                }
                else if (tok[0].equals(new String("U"))) {
                    sj.updatePrinter(Integer.parseInt(tok[2]),
                        Integer.parseInt(tok[3]));
                }
                else if (tok[0].equals(new String("D"))) {
                    sj.deleteLaptop(Integer.parseInt(tok[2]));
                }

                sj.printPriceRange();
            }

            in.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());
        }

        sj.closeConnection();
    }
}
