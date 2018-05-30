CREATE DATABASE IF NOT EXISTS sales_data_pipeline;
USE sales_data_pipeline;
CREATE TABLE customer(CUSTOMER_ID VARCHAR(256) PRIMARY KEY, COUNTRY TEXT);
CREATE TABLE product(STOCK_CODE VARCHAR(256) PRIMARY KEY, DESCRIPTION TEXT, UNIT_PRICE VARCHAR(256));
CREATE TABLE invoice(INVOICE_NO VARCHAR(256), STOCK_CODE VARCHAR(256), QUANTITY VARCHAR(256), INVOICE_DATE VARCHAR(256), CUSTOMER_ID VARCHAR(256));
CREATE TABLE hourly_income(INVOICE_NO VARCHAR(256), STOCK_CODE VARCHAR(256), QUANTITY VARCHAR(256), INVOICE_DATE VARCHAR(256), CUSTOMER_ID VARCHAR(256));
-- CREATE TABLE country_purchase(COUNTRY VARCHAR(256) PRIMARY KEY, NUM_CUSTOMER INT, CUSTOMER_AVG_CONSUM FLOAT, TOTAL_CONSUM FLOAT);
-- CREATE TABLE customer_purchase(CUSTOMER_ID INT PRIMARY KEY, NUM_INVOICENO INT, TOTAL_CONSUM FLOAT);
-- CREATE TABLE customer_buy_return(CUSTOMER_ID INT PRIMARY KEY, NUM_PRODUCT_BOUGHT INT, NUM_PRODUCT_RETURN INT, RETURN_RATE FLOAT);
-- CREATE TABLE product_sold_returned(STOCK_CODE VARCHAR(256) PRIMARY KEY, NUM_SOLD INT, NUM_RETURN INT, RETURN_RATE FLOAT);
