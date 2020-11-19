import csv
with open('warehouse.csv', newline='') as csvfile:
	temp_reader = csv.reader(csvfile, delimiter=',')
	data=list(temp_reader)
row_val, col_val = 0, 0
try:
	for i in range(9, 200):
		print("stmt.setInt(1,",data[i][0],");")
		print("stmt.setString(2,", '"', data[i][1], '"', ");")
		print("stmt.setInt(3,", data[i][2], ");")
		print("stmt.setInt(4,",data[i][3], ");")
		print("stmt.setInt(5,",data[i][4], ");")
		print("stmt.addBatch();")
		print()
except IndexError:
    print('No data found')


# stmt.setInt(1, 10 );
# stmt.setString(2, " Supplier#000000005___EGYPT " );
# stmt.setInt(3, 1730 );
# stmt.setInt(4, 5 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 11 );
# stmt.setString(2, " Supplier#000000006___IRAN " );
# stmt.setInt(3, 1732 );
# stmt.setInt(4, 6 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 12 );
# stmt.setString(2, " Supplier#000000006___CANADA " );
# stmt.setInt(3, 1732 );
# stmt.setInt(4, 6 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 13 );
# stmt.setString(2, " Supplier#000000007___CANADA " );
# stmt.setInt(3, 1894 );
# stmt.setInt(4, 7 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 14 );
# stmt.setString(2, " Supplier#000000007___ROMANIA " );
# stmt.setInt(3, 1894 );
# stmt.setInt(4, 7 );
# stmt.setInt(5, 19 );
# stmt.addBatch();

# stmt.setInt(1, 15 );
# stmt.setString(2, " Supplier#000000008___CANADA " );
# stmt.setInt(3, 2088 );
# stmt.setInt(4, 8 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 16 );
# stmt.setString(2, " Supplier#000000008___EGYPT " );
# stmt.setInt(3, 2088 );
# stmt.setInt(4, 8 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 17 );
# stmt.setString(2, " Supplier#000000009___EGYPT " );
# stmt.setInt(3, 1794 );
# stmt.setInt(4, 9 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 18 );
# stmt.setString(2, " Supplier#000000009___IRAQ " );
# stmt.setInt(3, 1794 );
# stmt.setInt(4, 9 );
# stmt.setInt(5, 11 );
# stmt.addBatch();

# stmt.setInt(1, 19 );
# stmt.setString(2, " Supplier#000000010___GERMANY " );
# stmt.setInt(3, 1928 );
# stmt.setInt(4, 10 );
# stmt.setInt(5, 7 );
# stmt.addBatch();

# stmt.setInt(1, 20 );
# stmt.setString(2, " Supplier#000000010___CANADA " );
# stmt.setInt(3, 1928 );
# stmt.setInt(4, 10 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 21 );
# stmt.setString(2, " Supplier#000000011___EGYPT " );
# stmt.setInt(3, 1840 );
# stmt.setInt(4, 11 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 22 );
# stmt.setString(2, " Supplier#000000011___ROMANIA " );
# stmt.setInt(3, 1840 );
# stmt.setInt(4, 11 );
# stmt.setInt(5, 19 );
# stmt.addBatch();

# stmt.setInt(1, 23 );
# stmt.setString(2, " Supplier#000000012___SAUDI ARABIA " );
# stmt.setInt(3, 1618 );
# stmt.setInt(4, 12 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 24 );
# stmt.setString(2, " Supplier#000000012___INDONESIA " );
# stmt.setInt(3, 1618 );
# stmt.setInt(4, 12 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 25 );
# stmt.setString(2, " Supplier#000000013___EGYPT " );
# stmt.setInt(3, 1872 );
# stmt.setInt(4, 13 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 26 );
# stmt.setString(2, " Supplier#000000013___MOZAMBIQUE " );
# stmt.setInt(3, 1872 );
# stmt.setInt(4, 13 );
# stmt.setInt(5, 16 );
# stmt.addBatch();

# stmt.setInt(1, 27 );
# stmt.setString(2, " Supplier#000000014___CANADA " );
# stmt.setInt(3, 2130 );
# stmt.setInt(4, 14 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 28 );
# stmt.setString(2, " Supplier#000000014___EGYPT " );
# stmt.setInt(3, 2130 );
# stmt.setInt(4, 14 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 29 );
# stmt.setString(2, " Supplier#000000015___SAUDI ARABIA " );
# stmt.setInt(3, 2256 );
# stmt.setInt(4, 15 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 30 );
# stmt.setString(2, " Supplier#000000015___EGYPT " );
# stmt.setInt(3, 2256 );
# stmt.setInt(4, 15 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 31 );
# stmt.setString(2, " Supplier#000000016___SAUDI ARABIA " );
# stmt.setInt(3, 1972 );
# stmt.setInt(4, 16 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 32 );
# stmt.setString(2, " Supplier#000000016___CANADA " );
# stmt.setInt(3, 1972 );
# stmt.setInt(4, 16 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 33 );
# stmt.setString(2, " Supplier#000000017___INDONESIA " );
# stmt.setInt(3, 1740 );
# stmt.setInt(4, 17 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 34 );
# stmt.setString(2, " Supplier#000000017___ROMANIA " );
# stmt.setInt(3, 1740 );
# stmt.setInt(4, 17 );
# stmt.setInt(5, 19 );
# stmt.addBatch();

# stmt.setInt(1, 35 );
# stmt.setString(2, " Supplier#000000018___ROMANIA " );
# stmt.setInt(3, 2046 );
# stmt.setInt(4, 18 );
# stmt.setInt(5, 19 );
# stmt.addBatch();

# stmt.setInt(1, 36 );
# stmt.setString(2, " Supplier#000000018___CANADA " );
# stmt.setInt(3, 2046 );
# stmt.setInt(4, 18 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 37 );
# stmt.setString(2, " Supplier#000000019___ROMANIA " );
# stmt.setInt(3, 2436 );
# stmt.setInt(4, 19 );
# stmt.setInt(5, 19 );
# stmt.addBatch();

# stmt.setInt(1, 38 );
# stmt.setString(2, " Supplier#000000019___EGYPT " );
# stmt.setInt(3, 2436 );
# stmt.setInt(4, 19 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 39 );
# stmt.setString(2, " Supplier#000000020___BRAZIL " );
# stmt.setInt(3, 1908 );
# stmt.setInt(4, 20 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 40 );
# stmt.setString(2, " Supplier#000000020___UNITED STATES " );
# stmt.setInt(3, 1908 );
# stmt.setInt(4, 20 );
# stmt.setInt(5, 24 );
# stmt.addBatch();

# stmt.setInt(1, 41 );
# stmt.setString(2, " Supplier#000000021___CANADA " );
# stmt.setInt(3, 1924 );
# stmt.setInt(4, 21 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 42 );
# stmt.setString(2, " Supplier#000000021___BRAZIL " );
# stmt.setInt(3, 1924 );
# stmt.setInt(4, 21 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 43 );
# stmt.setString(2, " Supplier#000000022___KENYA " );
# stmt.setInt(3, 2174 );
# stmt.setInt(4, 22 );
# stmt.setInt(5, 14 );
# stmt.addBatch();

# stmt.setInt(1, 44 );
# stmt.setString(2, " Supplier#000000022___VIETNAM " );
# stmt.setInt(3, 2174 );
# stmt.setInt(4, 22 );
# stmt.setInt(5, 21 );
# stmt.addBatch();

# stmt.setInt(1, 45 );
# stmt.setString(2, " Supplier#000000023___EGYPT " );
# stmt.setInt(3, 1726 );
# stmt.setInt(4, 23 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 46 );
# stmt.setString(2, " Supplier#000000023___IRAN " );
# stmt.setInt(3, 1726 );
# stmt.setInt(4, 23 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 47 );
# stmt.setString(2, " Supplier#000000024___INDONESIA " );
# stmt.setInt(3, 1788 );
# stmt.setInt(4, 24 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 48 );
# stmt.setString(2, " Supplier#000000024___ALGERIA " );
# stmt.setInt(3, 1788 );
# stmt.setInt(4, 24 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 49 );
# stmt.setString(2, " Supplier#000000025___BRAZIL " );
# stmt.setInt(3, 1882 );
# stmt.setInt(4, 25 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 50 );
# stmt.setString(2, " Supplier#000000025___ALGERIA " );
# stmt.setInt(3, 1882 );
# stmt.setInt(4, 25 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 51 );
# stmt.setString(2, " Supplier#000000026___EGYPT " );
# stmt.setInt(3, 1768 );
# stmt.setInt(4, 26 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 52 );
# stmt.setString(2, " Supplier#000000026___VIETNAM " );
# stmt.setInt(3, 1768 );
# stmt.setInt(4, 26 );
# stmt.setInt(5, 21 );
# stmt.addBatch();

# stmt.setInt(1, 53 );
# stmt.setString(2, " Supplier#000000027___EGYPT " );
# stmt.setInt(3, 1864 );
# stmt.setInt(4, 27 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 54 );
# stmt.setString(2, " Supplier#000000027___IRAN " );
# stmt.setInt(3, 1864 );
# stmt.setInt(4, 27 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 55 );
# stmt.setString(2, " Supplier#000000028___MOZAMBIQUE " );
# stmt.setInt(3, 2274 );
# stmt.setInt(4, 28 );
# stmt.setInt(5, 16 );
# stmt.addBatch();

# stmt.setInt(1, 56 );
# stmt.setString(2, " Supplier#000000028___INDONESIA " );
# stmt.setInt(3, 2274 );
# stmt.setInt(4, 28 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 57 );
# stmt.setString(2, " Supplier#000000029___JAPAN " );
# stmt.setInt(3, 1538 );
# stmt.setInt(4, 29 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 58 );
# stmt.setString(2, " Supplier#000000029___INDONESIA " );
# stmt.setInt(3, 1538 );
# stmt.setInt(4, 29 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 59 );
# stmt.setString(2, " Supplier#000000030___CANADA " );
# stmt.setInt(3, 2108 );
# stmt.setInt(4, 30 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 60 );
# stmt.setString(2, " Supplier#000000030___IRAN " );
# stmt.setInt(3, 2108 );
# stmt.setInt(4, 30 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 61 );
# stmt.setString(2, " Supplier#000000031___ALGERIA " );
# stmt.setInt(3, 1600 );
# stmt.setInt(4, 31 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 62 );
# stmt.setString(2, " Supplier#000000031___IRAN " );
# stmt.setInt(3, 1600 );
# stmt.setInt(4, 31 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 63 );
# stmt.setString(2, " Supplier#000000032___CANADA " );
# stmt.setInt(3, 1942 );
# stmt.setInt(4, 32 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 64 );
# stmt.setString(2, " Supplier#000000032___INDIA " );
# stmt.setInt(3, 1942 );
# stmt.setInt(4, 32 );
# stmt.setInt(5, 8 );
# stmt.addBatch();

# stmt.setInt(1, 65 );
# stmt.setString(2, " Supplier#000000033___EGYPT " );
# stmt.setInt(3, 1578 );
# stmt.setInt(4, 33 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 66 );
# stmt.setString(2, " Supplier#000000033___JAPAN " );
# stmt.setInt(3, 1578 );
# stmt.setInt(4, 33 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 67 );
# stmt.setString(2, " Supplier#000000034___ALGERIA " );
# stmt.setInt(3, 1698 );
# stmt.setInt(4, 34 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 68 );
# stmt.setString(2, " Supplier#000000034___MOZAMBIQUE " );
# stmt.setInt(3, 1698 );
# stmt.setInt(4, 34 );
# stmt.setInt(5, 16 );
# stmt.addBatch();

# stmt.setInt(1, 69 );
# stmt.setString(2, " Supplier#000000035___ROMANIA " );
# stmt.setInt(3, 1932 );
# stmt.setInt(4, 35 );
# stmt.setInt(5, 19 );
# stmt.addBatch();

# stmt.setInt(1, 70 );
# stmt.setString(2, " Supplier#000000035___BRAZIL " );
# stmt.setInt(3, 1932 );
# stmt.setInt(4, 35 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 71 );
# stmt.setString(2, " Supplier#000000036___ALGERIA " );
# stmt.setInt(3, 1504 );
# stmt.setInt(4, 36 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 72 );
# stmt.setString(2, " Supplier#000000036___BRAZIL " );
# stmt.setInt(3, 1504 );
# stmt.setInt(4, 36 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 73 );
# stmt.setString(2, " Supplier#000000037___BRAZIL " );
# stmt.setInt(3, 2046 );
# stmt.setInt(4, 37 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 74 );
# stmt.setString(2, " Supplier#000000037___CANADA " );
# stmt.setInt(3, 2046 );
# stmt.setInt(4, 37 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 75 );
# stmt.setString(2, " Supplier#000000038___JAPAN " );
# stmt.setInt(3, 2200 );
# stmt.setInt(4, 38 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 76 );
# stmt.setString(2, " Supplier#000000038___ROMANIA " );
# stmt.setInt(3, 2200 );
# stmt.setInt(4, 38 );
# stmt.setInt(5, 19 );
# stmt.addBatch();

# stmt.setInt(1, 77 );
# stmt.setString(2, " Supplier#000000039___SAUDI ARABIA " );
# stmt.setInt(3, 1978 );
# stmt.setInt(4, 39 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 78 );
# stmt.setString(2, " Supplier#000000039___CANADA " );
# stmt.setInt(3, 1978 );
# stmt.setInt(4, 39 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 79 );
# stmt.setString(2, " Supplier#000000040___BRAZIL " );
# stmt.setInt(3, 1922 );
# stmt.setInt(4, 40 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 80 );
# stmt.setString(2, " Supplier#000000040___INDONESIA " );
# stmt.setInt(3, 1922 );
# stmt.setInt(4, 40 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 81 );
# stmt.setString(2, " Supplier#000000041___CANADA " );
# stmt.setInt(3, 2088 );
# stmt.setInt(4, 41 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 82 );
# stmt.setString(2, " Supplier#000000041___ALGERIA " );
# stmt.setInt(3, 2088 );
# stmt.setInt(4, 41 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 83 );
# stmt.setString(2, " Supplier#000000042___EGYPT " );
# stmt.setInt(3, 1770 );
# stmt.setInt(4, 42 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 84 );
# stmt.setString(2, " Supplier#000000042___UNITED KINGDOM " );
# stmt.setInt(3, 1770 );
# stmt.setInt(4, 42 );
# stmt.setInt(5, 23 );
# stmt.addBatch();

# stmt.setInt(1, 85 );
# stmt.setString(2, " Supplier#000000043___CANADA " );
# stmt.setInt(3, 1992 );
# stmt.setInt(4, 43 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 86 );
# stmt.setString(2, " Supplier#000000043___BRAZIL " );
# stmt.setInt(3, 1992 );
# stmt.setInt(4, 43 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 87 );
# stmt.setString(2, " Supplier#000000044___MOZAMBIQUE " );
# stmt.setInt(3, 2090 );
# stmt.setInt(4, 44 );
# stmt.setInt(5, 16 );
# stmt.addBatch();

# stmt.setInt(1, 88 );
# stmt.setString(2, " Supplier#000000044___BRAZIL " );
# stmt.setInt(3, 2090 );
# stmt.setInt(4, 44 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 89 );
# stmt.setString(2, " Supplier#000000045___CANADA " );
# stmt.setInt(3, 1932 );
# stmt.setInt(4, 45 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 90 );
# stmt.setString(2, " Supplier#000000045___IRAN " );
# stmt.setInt(3, 1932 );
# stmt.setInt(4, 45 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 91 );
# stmt.setString(2, " Supplier#000000046___MOZAMBIQUE " );
# stmt.setInt(3, 2334 );
# stmt.setInt(4, 46 );
# stmt.setInt(5, 16 );
# stmt.addBatch();

# stmt.setInt(1, 92 );
# stmt.setString(2, " Supplier#000000046___CANADA " );
# stmt.setInt(3, 2334 );
# stmt.setInt(4, 46 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 93 );
# stmt.setString(2, " Supplier#000000047___SAUDI ARABIA " );
# stmt.setInt(3, 1748 );
# stmt.setInt(4, 47 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 94 );
# stmt.setString(2, " Supplier#000000047___INDONESIA " );
# stmt.setInt(3, 1748 );
# stmt.setInt(4, 47 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 95 );
# stmt.setString(2, " Supplier#000000048___IRAN " );
# stmt.setInt(3, 2272 );
# stmt.setInt(4, 48 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 96 );
# stmt.setString(2, " Supplier#000000048___JAPAN " );
# stmt.setInt(3, 2272 );
# stmt.setInt(4, 48 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 97 );
# stmt.setString(2, " Supplier#000000049___CANADA " );
# stmt.setInt(3, 2020 );
# stmt.setInt(4, 49 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 98 );
# stmt.setString(2, " Supplier#000000049___UNITED KINGDOM " );
# stmt.setInt(3, 2020 );
# stmt.setInt(4, 49 );
# stmt.setInt(5, 23 );
# stmt.addBatch();

# stmt.setInt(1, 99 );
# stmt.setString(2, " Supplier#000000050___SAUDI ARABIA " );
# stmt.setInt(3, 2070 );
# stmt.setInt(4, 50 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 100 );
# stmt.setString(2, " Supplier#000000050___GERMANY " );
# stmt.setInt(3, 2070 );
# stmt.setInt(4, 50 );
# stmt.setInt(5, 7 );
# stmt.addBatch();

# stmt.setInt(1, 101 );
# stmt.setString(2, " Supplier#000000051___CANADA " );
# stmt.setInt(3, 2764 );
# stmt.setInt(4, 51 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 102 );
# stmt.setString(2, " Supplier#000000051___SAUDI ARABIA " );
# stmt.setInt(3, 2764 );
# stmt.setInt(4, 51 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 103 );
# stmt.setString(2, " Supplier#000000052___CANADA " );
# stmt.setInt(3, 2018 );
# stmt.setInt(4, 52 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 104 );
# stmt.setString(2, " Supplier#000000052___EGYPT " );
# stmt.setInt(3, 2018 );
# stmt.setInt(4, 52 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 105 );
# stmt.setString(2, " Supplier#000000053___JAPAN " );
# stmt.setInt(3, 1894 );
# stmt.setInt(4, 53 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 106 );
# stmt.setString(2, " Supplier#000000053___BRAZIL " );
# stmt.setInt(3, 1894 );
# stmt.setInt(4, 53 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 107 );
# stmt.setString(2, " Supplier#000000054___BRAZIL " );
# stmt.setInt(3, 1892 );
# stmt.setInt(4, 54 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 108 );
# stmt.setString(2, " Supplier#000000054___SAUDI ARABIA " );
# stmt.setInt(3, 1892 );
# stmt.setInt(4, 54 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 109 );
# stmt.setString(2, " Supplier#000000055___UNITED KINGDOM " );
# stmt.setInt(3, 2018 );
# stmt.setInt(4, 55 );
# stmt.setInt(5, 23 );
# stmt.addBatch();

# stmt.setInt(1, 110 );
# stmt.setString(2, " Supplier#000000055___IRAQ " );
# stmt.setInt(3, 2018 );
# stmt.setInt(4, 55 );
# stmt.setInt(5, 11 );
# stmt.addBatch();

# stmt.setInt(1, 111 );
# stmt.setString(2, " Supplier#000000056___MOROCCO " );
# stmt.setInt(3, 2076 );
# stmt.setInt(4, 56 );
# stmt.setInt(5, 15 );
# stmt.addBatch();

# stmt.setInt(1, 112 );
# stmt.setString(2, " Supplier#000000056___EGYPT " );
# stmt.setInt(3, 2076 );
# stmt.setInt(4, 56 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 113 );
# stmt.setString(2, " Supplier#000000057___CANADA " );
# stmt.setInt(3, 1692 );
# stmt.setInt(4, 57 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 114 );
# stmt.setString(2, " Supplier#000000057___GERMANY " );
# stmt.setInt(3, 1692 );
# stmt.setInt(4, 57 );
# stmt.setInt(5, 7 );
# stmt.addBatch();

# stmt.setInt(1, 115 );
# stmt.setString(2, " Supplier#000000058___ALGERIA " );
# stmt.setInt(3, 1746 );
# stmt.setInt(4, 58 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 116 );
# stmt.setString(2, " Supplier#000000058___EGYPT " );
# stmt.setInt(3, 1746 );
# stmt.setInt(4, 58 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 117 );
# stmt.setString(2, " Supplier#000000059___CANADA " );
# stmt.setInt(3, 2008 );
# stmt.setInt(4, 59 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 118 );
# stmt.setString(2, " Supplier#000000059___IRAN " );
# stmt.setInt(3, 2008 );
# stmt.setInt(4, 59 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 119 );
# stmt.setString(2, " Supplier#000000060___IRAN " );
# stmt.setInt(3, 1868 );
# stmt.setInt(4, 60 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 120 );
# stmt.setString(2, " Supplier#000000060___GERMANY " );
# stmt.setInt(3, 1868 );
# stmt.setInt(4, 60 );
# stmt.setInt(5, 7 );
# stmt.addBatch();

# stmt.setInt(1, 121 );
# stmt.setString(2, " Supplier#000000061___EGYPT " );
# stmt.setInt(3, 1930 );
# stmt.setInt(4, 61 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 122 );
# stmt.setString(2, " Supplier#000000061___IRAN " );
# stmt.setInt(3, 1930 );
# stmt.setInt(4, 61 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 123 );
# stmt.setString(2, " Supplier#000000062___INDONESIA " );
# stmt.setInt(3, 1866 );
# stmt.setInt(4, 62 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 124 );
# stmt.setString(2, " Supplier#000000062___EGYPT " );
# stmt.setInt(3, 1866 );
# stmt.setInt(4, 62 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 125 );
# stmt.setString(2, " Supplier#000000063___IRAN " );
# stmt.setInt(3, 1852 );
# stmt.setInt(4, 63 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 126 );
# stmt.setString(2, " Supplier#000000063___MOZAMBIQUE " );
# stmt.setInt(3, 1852 );
# stmt.setInt(4, 63 );
# stmt.setInt(5, 16 );
# stmt.addBatch();

# stmt.setInt(1, 127 );
# stmt.setString(2, " Supplier#000000064___CANADA " );
# stmt.setInt(3, 2184 );
# stmt.setInt(4, 64 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 128 );
# stmt.setString(2, " Supplier#000000064___IRAN " );
# stmt.setInt(3, 2184 );
# stmt.setInt(4, 64 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 129 );
# stmt.setString(2, " Supplier#000000065___CANADA " );
# stmt.setInt(3, 1646 );
# stmt.setInt(4, 65 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 130 );
# stmt.setString(2, " Supplier#000000065___IRAN " );
# stmt.setInt(3, 1646 );
# stmt.setInt(4, 65 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 131 );
# stmt.setString(2, " Supplier#000000066___EGYPT " );
# stmt.setInt(3, 2330 );
# stmt.setInt(4, 66 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 132 );
# stmt.setString(2, " Supplier#000000066___CANADA " );
# stmt.setInt(3, 2330 );
# stmt.setInt(4, 66 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 133 );
# stmt.setString(2, " Supplier#000000067___CANADA " );
# stmt.setInt(3, 1680 );
# stmt.setInt(4, 67 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 134 );
# stmt.setString(2, " Supplier#000000067___UNITED KINGDOM " );
# stmt.setInt(3, 1680 );
# stmt.setInt(4, 67 );
# stmt.setInt(5, 23 );
# stmt.addBatch();

# stmt.setInt(1, 135 );
# stmt.setString(2, " Supplier#000000068___CANADA " );
# stmt.setInt(3, 2108 );
# stmt.setInt(4, 68 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 136 );
# stmt.setString(2, " Supplier#000000068___ETHIOPIA " );
# stmt.setInt(3, 2108 );
# stmt.setInt(4, 68 );
# stmt.setInt(5, 5 );
# stmt.addBatch();

# stmt.setInt(1, 137 );
# stmt.setString(2, " Supplier#000000069___CANADA " );
# stmt.setInt(3, 1770 );
# stmt.setInt(4, 69 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 138 );
# stmt.setString(2, " Supplier#000000069___BRAZIL " );
# stmt.setInt(3, 1770 );
# stmt.setInt(4, 69 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 139 );
# stmt.setString(2, " Supplier#000000070___INDONESIA " );
# stmt.setInt(3, 1780 );
# stmt.setInt(4, 70 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 140 );
# stmt.setString(2, " Supplier#000000070___ROMANIA " );
# stmt.setInt(3, 1780 );
# stmt.setInt(4, 70 );
# stmt.setInt(5, 19 );
# stmt.addBatch();

# stmt.setInt(1, 141 );
# stmt.setString(2, " Supplier#000000071___CANADA " );
# stmt.setInt(3, 2178 );
# stmt.setInt(4, 71 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 142 );
# stmt.setString(2, " Supplier#000000071___ALGERIA " );
# stmt.setInt(3, 2178 );
# stmt.setInt(4, 71 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 143 );
# stmt.setString(2, " Supplier#000000072___CANADA " );
# stmt.setInt(3, 1832 );
# stmt.setInt(4, 72 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 144 );
# stmt.setString(2, " Supplier#000000072___EGYPT " );
# stmt.setInt(3, 1832 );
# stmt.setInt(4, 72 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 145 );
# stmt.setString(2, " Supplier#000000073___BRAZIL " );
# stmt.setInt(3, 2588 );
# stmt.setInt(4, 73 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 146 );
# stmt.setString(2, " Supplier#000000073___JAPAN " );
# stmt.setInt(3, 2588 );
# stmt.setInt(4, 73 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 147 );
# stmt.setString(2, " Supplier#000000074___IRAN " );
# stmt.setInt(3, 1668 );
# stmt.setInt(4, 74 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 148 );
# stmt.setString(2, " Supplier#000000074___CANADA " );
# stmt.setInt(3, 1668 );
# stmt.setInt(4, 74 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 149 );
# stmt.setString(2, " Supplier#000000075___BRAZIL " );
# stmt.setInt(3, 2100 );
# stmt.setInt(4, 75 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 150 );
# stmt.setString(2, " Supplier#000000075___SAUDI ARABIA " );
# stmt.setInt(3, 2100 );
# stmt.setInt(4, 75 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 151 );
# stmt.setString(2, " Supplier#000000076___IRAN " );
# stmt.setInt(3, 1850 );
# stmt.setInt(4, 76 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 152 );
# stmt.setString(2, " Supplier#000000076___BRAZIL " );
# stmt.setInt(3, 1850 );
# stmt.setInt(4, 76 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 153 );
# stmt.setString(2, " Supplier#000000077___EGYPT " );
# stmt.setInt(3, 2134 );
# stmt.setInt(4, 77 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 154 );
# stmt.setString(2, " Supplier#000000077___KENYA " );
# stmt.setInt(3, 2134 );
# stmt.setInt(4, 77 );
# stmt.setInt(5, 14 );
# stmt.addBatch();

# stmt.setInt(1, 155 );
# stmt.setString(2, " Supplier#000000078___CANADA " );
# stmt.setInt(3, 1964 );
# stmt.setInt(4, 78 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 156 );
# stmt.setString(2, " Supplier#000000078___IRAN " );
# stmt.setInt(3, 1964 );
# stmt.setInt(4, 78 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 157 );
# stmt.setString(2, " Supplier#000000079___IRAN " );
# stmt.setInt(3, 1964 );
# stmt.setInt(4, 79 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 158 );
# stmt.setString(2, " Supplier#000000079___ARGENTINA " );
# stmt.setInt(3, 1964 );
# stmt.setInt(4, 79 );
# stmt.setInt(5, 1 );
# stmt.addBatch();

# stmt.setInt(1, 159 );
# stmt.setString(2, " Supplier#000000080___EGYPT " );
# stmt.setInt(3, 1700 );
# stmt.setInt(4, 80 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 160 );
# stmt.setString(2, " Supplier#000000080___BRAZIL " );
# stmt.setInt(3, 1700 );
# stmt.setInt(4, 80 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 161 );
# stmt.setString(2, " Supplier#000000081___ALGERIA " );
# stmt.setInt(3, 1776 );
# stmt.setInt(4, 81 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 162 );
# stmt.setString(2, " Supplier#000000081___JAPAN " );
# stmt.setInt(3, 1776 );
# stmt.setInt(4, 81 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 163 );
# stmt.setString(2, " Supplier#000000082___CANADA " );
# stmt.setInt(3, 2008 );
# stmt.setInt(4, 82 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 164 );
# stmt.setString(2, " Supplier#000000082___IRAN " );
# stmt.setInt(3, 2008 );
# stmt.setInt(4, 82 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 165 );
# stmt.setString(2, " Supplier#000000083___BRAZIL " );
# stmt.setInt(3, 2016 );
# stmt.setInt(4, 83 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 166 );
# stmt.setString(2, " Supplier#000000083___EGYPT " );
# stmt.setInt(3, 2016 );
# stmt.setInt(4, 83 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 167 );
# stmt.setString(2, " Supplier#000000084___BRAZIL " );
# stmt.setInt(3, 1980 );
# stmt.setInt(4, 84 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 168 );
# stmt.setString(2, " Supplier#000000084___MOROCCO " );
# stmt.setInt(3, 1980 );
# stmt.setInt(4, 84 );
# stmt.setInt(5, 15 );
# stmt.addBatch();

# stmt.setInt(1, 169 );
# stmt.setString(2, " Supplier#000000085___JORDAN " );
# stmt.setInt(3, 1756 );
# stmt.setInt(4, 85 );
# stmt.setInt(5, 13 );
# stmt.addBatch();

# stmt.setInt(1, 170 );
# stmt.setString(2, " Supplier#000000085___UNITED KINGDOM " );
# stmt.setInt(3, 1756 );
# stmt.setInt(4, 85 );
# stmt.setInt(5, 23 );
# stmt.addBatch();

# stmt.setInt(1, 171 );
# stmt.setString(2, " Supplier#000000086___EGYPT " );
# stmt.setInt(3, 1926 );
# stmt.setInt(4, 86 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 172 );
# stmt.setString(2, " Supplier#000000086___MOROCCO " );
# stmt.setInt(3, 1926 );
# stmt.setInt(4, 86 );
# stmt.setInt(5, 15 );
# stmt.addBatch();

# stmt.setInt(1, 173 );
# stmt.setString(2, " Supplier#000000087___EGYPT " );
# stmt.setInt(3, 2114 );
# stmt.setInt(4, 87 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 174 );
# stmt.setString(2, " Supplier#000000087___SAUDI ARABIA " );
# stmt.setInt(3, 2114 );
# stmt.setInt(4, 87 );
# stmt.setInt(5, 20 );
# stmt.addBatch();

# stmt.setInt(1, 175 );
# stmt.setString(2, " Supplier#000000088___ALGERIA " );
# stmt.setInt(3, 1752 );
# stmt.setInt(4, 88 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 176 );
# stmt.setString(2, " Supplier#000000088___VIETNAM " );
# stmt.setInt(3, 1752 );
# stmt.setInt(4, 88 );
# stmt.setInt(5, 21 );
# stmt.addBatch();

# stmt.setInt(1, 177 );
# stmt.setString(2, " Supplier#000000089___ALGERIA " );
# stmt.setInt(3, 1936 );
# stmt.setInt(4, 89 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 178 );
# stmt.setString(2, " Supplier#000000089___IRAN " );
# stmt.setInt(3, 1936 );
# stmt.setInt(4, 89 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 179 );
# stmt.setString(2, " Supplier#000000090___IRAN " );
# stmt.setInt(3, 1858 );
# stmt.setInt(4, 90 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 180 );
# stmt.setString(2, " Supplier#000000090___MOROCCO " );
# stmt.setInt(3, 1858 );
# stmt.setInt(4, 90 );
# stmt.setInt(5, 15 );
# stmt.addBatch();

# stmt.setInt(1, 181 );
# stmt.setString(2, " Supplier#000000091___ALGERIA " );
# stmt.setInt(3, 1696 );
# stmt.setInt(4, 91 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 182 );
# stmt.setString(2, " Supplier#000000091___KENYA " );
# stmt.setInt(3, 1696 );
# stmt.setInt(4, 91 );
# stmt.setInt(5, 14 );
# stmt.addBatch();

# stmt.setInt(1, 183 );
# stmt.setString(2, " Supplier#000000092___JAPAN " );
# stmt.setInt(3, 1694 );
# stmt.setInt(4, 92 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 184 );
# stmt.setString(2, " Supplier#000000092___ALGERIA " );
# stmt.setInt(3, 1694 );
# stmt.setInt(4, 92 );
# stmt.setInt(5, 0 );
# stmt.addBatch();

# stmt.setInt(1, 185 );
# stmt.setString(2, " Supplier#000000093___JORDAN " );
# stmt.setInt(3, 1680 );
# stmt.setInt(4, 93 );
# stmt.setInt(5, 13 );
# stmt.addBatch();

# stmt.setInt(1, 186 );
# stmt.setString(2, " Supplier#000000093___MOROCCO " );
# stmt.setInt(3, 1680 );
# stmt.setInt(4, 93 );
# stmt.setInt(5, 15 );
# stmt.addBatch();

# stmt.setInt(1, 187 );
# stmt.setString(2, " Supplier#000000094___BRAZIL " );
# stmt.setInt(3, 1980 );
# stmt.setInt(4, 94 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 188 );
# stmt.setString(2, " Supplier#000000094___EGYPT " );
# stmt.setInt(3, 1980 );
# stmt.setInt(4, 94 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 189 );
# stmt.setString(2, " Supplier#000000095___EGYPT " );
# stmt.setInt(3, 1686 );
# stmt.setInt(4, 95 );
# stmt.setInt(5, 4 );
# stmt.addBatch();

# stmt.setInt(1, 190 );
# stmt.setString(2, " Supplier#000000095___IRAN " );
# stmt.setInt(3, 1686 );
# stmt.setInt(4, 95 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 191 );
# stmt.setString(2, " Supplier#000000096___MOROCCO " );
# stmt.setInt(3, 2054 );
# stmt.setInt(4, 96 );
# stmt.setInt(5, 15 );
# stmt.addBatch();

# stmt.setInt(1, 192 );
# stmt.setString(2, " Supplier#000000096___CANADA " );
# stmt.setInt(3, 2054 );
# stmt.setInt(4, 96 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 193 );
# stmt.setString(2, " Supplier#000000097___BRAZIL " );
# stmt.setInt(3, 1978 );
# stmt.setInt(4, 97 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 194 );
# stmt.setString(2, " Supplier#000000097___JAPAN " );
# stmt.setInt(3, 1978 );
# stmt.setInt(4, 97 );
# stmt.setInt(5, 12 );
# stmt.addBatch();

# stmt.setInt(1, 195 );
# stmt.setString(2, " Supplier#000000098___CANADA " );
# stmt.setInt(3, 1872 );
# stmt.setInt(4, 98 );
# stmt.setInt(5, 3 );
# stmt.addBatch();

# stmt.setInt(1, 196 );
# stmt.setString(2, " Supplier#000000098___IRAN " );
# stmt.setInt(3, 1872 );
# stmt.setInt(4, 98 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 197 );
# stmt.setString(2, " Supplier#000000099___INDONESIA " );
# stmt.setInt(3, 2454 );
# stmt.setInt(4, 99 );
# stmt.setInt(5, 9 );
# stmt.addBatch();

# stmt.setInt(1, 198 );
# stmt.setString(2, " Supplier#000000099___BRAZIL " );
# stmt.setInt(3, 2454 );
# stmt.setInt(4, 99 );
# stmt.setInt(5, 2 );
# stmt.addBatch();

# stmt.setInt(1, 199 );
# stmt.setString(2, " Supplier#000000100___IRAN " );
# stmt.setInt(3, 1874 );
# stmt.setInt(4, 100 );
# stmt.setInt(5, 10 );
# stmt.addBatch();

# stmt.setInt(1, 200 );
# stmt.setString(2, " Supplier#000000100___JAPAN " );
# stmt.setInt(3, 1874 );
# stmt.setInt(4, 100 );
# stmt.setInt(5, 12 );
# stmt.addBatch();