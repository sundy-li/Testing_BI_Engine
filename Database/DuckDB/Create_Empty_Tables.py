import duckdb 
con = duckdb.connect(database='C:/Users/mimoune.djouallah/Desktop/TPC-H-SF10/db/tpch.duckdb')
con.execute("PRAGMA default_collation='nocase';")


df =con.execute('''


DROP TABLE IF EXISTS PART ;
CREATE TABLE PART (

	P_PARTKEY		INTEGER PRIMARY KEY,
	P_NAME			VARCHAR(55),
	P_MFGR			CHAR(25),
	P_BRAND			CHAR(10),
	P_TYPE			VARCHAR(25),
	P_SIZE			INTEGER,
	P_CONTAINER		CHAR(10),
	P_RETAILPRICE	DECIMAL,
	P_COMMENT		VARCHAR(23)
);

DROP TABLE  IF EXISTS SUPPLIER;
CREATE TABLE SUPPLIER (
	S_SUPPKEY		INTEGER PRIMARY KEY,
	S_NAME			CHAR(25),
	S_ADDRESS		VARCHAR(40),
	S_NATIONKEY		INTEGER NOT NULL, -- references N_NATIONKEY
	S_PHONE			CHAR(15),
	S_ACCTBAL		DECIMAL,
	S_COMMENT		VARCHAR(101)
);

DROP TABLE  IF EXISTS PARTSUPP;
CREATE TABLE PARTSUPP (
	PS_PARTKEY		INTEGER NOT NULL, -- references P_PARTKEY
	PS_SUPPKEY		INTEGER NOT NULL, -- references S_SUPPKEY
	PS_AVAILQTY		INTEGER,
	PS_SUPPLYCOST	DECIMAL,
	PS_COMMENT		VARCHAR(199),
	PRIMARY KEY (PS_PARTKEY, PS_SUPPKEY)
);

DROP TABLE  IF EXISTS CUSTOMER;
CREATE TABLE CUSTOMER (
	C_CUSTKEY		INTEGER PRIMARY KEY,
	C_NAME			VARCHAR(25),
	C_ADDRESS		VARCHAR(40),
	C_NATIONKEY		INTEGER NOT NULL, -- references N_NATIONKEY
	C_PHONE			CHAR(15),
	C_ACCTBAL		DECIMAL,
	C_MKTSEGMENT	CHAR(10),
	C_COMMENT		VARCHAR(117)
);

DROP TABLE  IF EXISTS ORDERS;
CREATE TABLE ORDERS (
	O_ORDERKEY		INTEGER PRIMARY KEY,
	O_CUSTKEY		INTEGER NOT NULL, -- references C_CUSTKEY
	O_ORDERSTATUS	CHAR(1),
	O_TOTALPRICE	DECIMAL,
	O_ORDERPRIORITY	CHAR(15),
	O_CLERK			CHAR(15),
	O_SHIPPRIORITY	INTEGER,
	O_COMMENT		VARCHAR(79),
	O_ORDERDATE		DATE,
);

 DROP TABLE  IF EXISTS LINEITEM;
 CREATE TABLE LINEITEM (
	L_ORDERKEY		INTEGER NOT NULL, -- references O_ORDERKEY
 	L_PARTKEY		INTEGER NOT NULL, -- references P_PARTKEY (compound fk to PARTSUPP)
 	L_SUPPKEY		INTEGER NOT NULL, -- references S_SUPPKEY (compound fk to PARTSUPP)
 	L_LINENUMBER	INTEGER,
 	L_QUANTITY		DECIMAL,
 	L_EXTENDEDPRICE	DECIMAL,
 	L_DISCOUNT		DECIMAL,
 	L_TAX			DECIMAL,
 	L_RETURNFLAG	CHAR(1),
 	L_LINESTATUS	CHAR(1),
 	L_SHIPINSTRUCT	CHAR(25),
 	L_SHIPMODE		CHAR(10),
 	L_COMMENT		VARCHAR(44),
 	L_SHIPDATE		DATE,
 	L_COMMITDATE	DATE,
 	L_RECEIPTDATE	DATE,
 	PRIMARY KEY (L_ORDERKEY, L_LINENUMBER)
 );

DROP TABLE  IF EXISTS NATION;
CREATE TABLE NATION (
	N_NATIONKEY		INTEGER PRIMARY KEY,
	N_NAME			CHAR(25),
	N_REGIONKEY		INTEGER NOT NULL,  -- references R_REGIONKEY
	N_COMMENT		VARCHAR(152)
);

DROP TABLE  IF EXISTS REGION;
CREATE TABLE REGION (
	R_REGIONKEY	INTEGER PRIMARY KEY,
	R_NAME		CHAR(25),
	R_COMMENT	VARCHAR(152)
);

''')