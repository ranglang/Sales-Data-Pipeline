import os
import time
import datetime
import logging
import random

# invoice dataset head:
# invoiceno,stockcode,quantity,invoicedate,customerid

def mock_invoice_output(invoiceno_pool, stockcode_pool, customerid_pool, output_f):
    invoiceno = random.choice(list(invoiceno_pool)).strip()
    stockcode = random.choice(list(stockcode_pool)).strip()
    quantity = str(random.randint(1, 100))
    invoicedate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    customerid = random.choice(list(customerid_pool)).strip()

    output_f.write(",".join([invoiceno, stockcode, quantity, invoicedate, customerid]) + '\n')
    time.sleep(0.1)


# lines: num of lines to generate
#        -1 means generat forever
def mock_invoice_generator(invoiceno_pool_file, stockcode_pool_file, customerid_pool_file, output_file, lines=-1):
    invoiceno_pool_f = open(invoiceno_pool_file, 'r+')
    stockcode_pool_f = open(stockcode_pool_file, 'r+')
    customerid_pool_f = open(customerid_pool_file, 'r+')
    output_f = open(output_file, 'a+')

    invoiceno_lines = invoiceno_pool_f.readlines()
    stockcode_lines = stockcode_pool_f.readlines()
    customerid_lines = customerid_pool_f.readlines()

    invoiceno_pool = set()
    stockcode_pool = set()
    customerid_pool = set()

    for line in invoiceno_lines:
        invoiceno_pool.add(line)

    for line in stockcode_lines:
        stockcode_pool.add(line)

    for line in customerid_lines:
        customerid_pool.add(line)

    # Write head
    output_f.write("invoiceno,stockcode,quantity,invoicedate,customerid\n")

    # Runs forever
    if lines == -1:
        while True:
            mock_invoice_output(invoiceno_pool, stockcode_pool, customerid_pool, output_f)
    # Invalid value
    elif lines < 0:
        pass
    else:
        for i in range(lines):
            mock_invoice_output(invoiceno_pool, stockcode_pool, customerid_pool, output_f)

    invoiceno_pool_f.close()
    stockcode_pool_f.close()
    customerid_pool_f.close()
    output_f.close()


if __name__ == "__main__":
    invoiceno_pool_file = open("config/invoiceno_pool.txt", "r+")
    stockcode_pool_file = open("config/stockcode_pool.txt", "r+")
    customerid_pool_file = open("config/customerid_pool.txt", "r+")
    output_file = open("data/out/invoice_"+datetime.datetime.utcnow().strftime("%Y-%m-%d")+".csv", "a+")
    mock_invoice_generator(invoiceno_pool_file.strpath, stockcode_pool_file.strpath, customerid_pool_file.strpath, output_file.strpath, -1)
