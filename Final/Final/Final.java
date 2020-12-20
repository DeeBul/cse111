// STEP: Import required packages
import java.sql.*;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.File;

public class Final {
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


    private void create_tables() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("CREATE TABLES");

        try {
            String sqlProduct = "CREATE TABLE Product (" + 
                " model integer PRIMARY KEY NOT NULL," +
                " type char(25)," + 
                " maker char(15)" +
                ")";

            String sqlDistributor = "CREATE TABLE Distributor (" +
                    " model integer PRIMARY KEY," + 
                    " name char(25)," + 
                    " price integer," +
                    " FOREIGN KEY(model) REFERENCES Product(model)" +
                    " ON UPDATE CASCADE" +
                    " ON DELETE CASCADE" + 
                    ")";

            String sqlPriceCube = " CREATE TABLE Price_Cube (" + 
                    " distributor_type char(255)," + 
                    " product_type char(255)," + 
                    " num_prod integer," + 
                    " PRIMARY KEY(distributor_type, product_type)" + 
                    " )";
            
            Statement stmt = c.createStatement();
            stmt.executeUpdate(sqlProduct);
            stmt.executeUpdate(sqlDistributor);
            stmt.executeUpdate(sqlPriceCube);

            c.commit();
            stmt.close();

        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());

            try {
                c.rollback();
            }
            catch(Exception el) {
                System.err.println(el.getClass().getName() + ": " + e.getMessage());
            }
        }


        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    private void populate_tables() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("POPULATE TABLES");
       
    //    try {
    //        String sql = ".mode list" + 
    //                     " .import product.txt Product";

    //         Statement stmt = c.createStatement();
    //         stmt.executeUpdate(sql);
    //         c.getAutoCommit();
    //         c.close();
    //         stmt.close();
    //    } catch (Exception e) {
    //     System.err.println(e.getClass().getName() + ": " + e.getMessage());

    //     try {
    //         c.rollback();
    //     }
    //     catch(Exception el) {
    //         System.err.println(el.getClass().getName() + ": " + e.getMessage());
    //     }
    // }
       
        int model;
        String type;
        String maker;
        PreparedStatement stmt = null;

        try {
            BufferedReader br = new BufferedReader(new FileReader("product.txt"));

            String line = null;

            while((line = br.readLine()) != null) {
                String[] tmp = line.split("|", 50);
                model = Integer.parseInt(tmp[0]);
                type = tmp[1];
                maker = tmp[2];
                // for (int i = 0; i < tmp.length; i++) {
                    System.out.println(model + type + maker);
                // }

                String sqlProduct = "INSERT INTO Product VALUES(?, ?, ?)";
                
                stmt = c.prepareStatement(sqlProduct);
                stmt.setInt(1, model);
                stmt.setString(2, type);
                stmt.setString(3, maker);

                stmt = c.prepareStatement(sqlProduct);
                stmt.executeUpdate();
            }
            br.close();
            c.close();
            stmt.close();
        } catch (Exception e) {
            System.err.println(e.getClass().getName() + ": " + e.getMessage());

            try {
                c.rollback();
            }
            catch(Exception el) {
                System.err.println(el.getClass().getName() + ": " + e.getMessage());
            }
        }

        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    private void build_data_cube() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("BUILD DATA CUBE");



        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    private void print_Product() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("PRINT PRODUCT");

        System.out.printf("%-20s %-20s %-20s\n", "model", "type", "maker");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void print_Distributor() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("PRINT DISTRIBUTOR");

        System.out.printf("%-20s %-20s %20s\n", "model", "name", "price");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }

    private void print_Cube() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("PRINT DATA CUBE");

        System.out.printf("%-20s %-20s %10s %10s\n", "dist", "prod", "cnt", "total");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    private void modifications() {
        System.out.println("++++++++++++++++++++++++++++++++++");
        System.out.println("MODIFICATIONS");

        System.out.println("++++++++++++++++++++++++++++++++++");
    }


    public static void main(String args[]) {
        Final sj = new Final();
        
        sj.openConnection("data.sqlite");

        // sj.create_tables();

        sj.populate_tables();

        sj.print_Product();
        sj.print_Distributor();

        sj.build_data_cube();
        sj.print_Cube();

        sj.modifications();

        sj.print_Product();
        sj.print_Distributor();

        sj.build_data_cube();
        sj.print_Cube();

        sj.closeConnection();
    }
}
