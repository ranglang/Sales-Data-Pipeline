from kafka import KafkaProducer
import asyncio
from asyncio import coroutine
import time
import datetime
import random

class MockProducer(object):

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='kafka1:9092')
        self.stockcode_ini = { '85123A': ['WHITE HANGING HEART T-LIGHT HOLDER', 3.24], \
                               '84580':  ['MOUSE TOY WITH PINK T-SHIRT', 3.75], \
                               '21558':  ['SKULL LUNCH BOX WITH CUTLERY', 2.55], \
                               '22726':  ['ALARM CLOCK BAKELIKE GREEN', 3.75], \
                               '20819':  ['SILVER TEDDY BEAR', 3.75], \
                               '47590A': ['BLUE HAPPY BIRTHDAY BUNTING', 5.45], \
                               '84879':  ['ASSORTED COLOUR BIRD ORNAMENT', 1.69], \
                               '84993B': ['75 BLACK PETIT FOUR CASES', 0.42], \
                               '22090':  ['PAPER BUNTING RETROSPOT', 2.95], \
                               '84347':  ['ROTATING SILVER ANGELS T-LIGHT HLDR', 2.55], \
                               '22726':  ['ALARM CLOCK BAKELIKE GREEN', 3.75], \
                               '22154':  ['ANGEL DECORATION 3 BUTTONS', 0.42]
                             }
        self.customerid_ini = {
                               '13831': 'United Kingdom', \
                               '12605': 'Germany', \
                               '17519': 'United Kingdom', \
                               '14527': 'United Kingdom', \
                               '17223': 'United Kingdom', \
                               '14657': 'United Kingdom', \
                               '12490': 'France', \
                               '18198': 'United Kingdom' \
                              }

        self.invoiceno_pool = ['537127', '536539', '540414', '541518', '537890', '537395', '537225', '536570', '539050']
        self.stockcode_pool = {}
        self.customerid_pool = {}


    def run(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(
                asyncio.wait([
                    self.send_product()
                ])
            )
        finally:
            loop.close()

    # invoiceno,stockcode,quantity,invoicedate,customerid
    @coroutine
    def send_invoice(self):
        while True:
            # The self.stockcode_pool & self.customerid_pool cannot be empty
            if len(self.stockcode_pool) and len(self.customerid_pool):
                invoiceno = random.choice(self.invoiceno_pool)
                stockcode = random.choice(list(self.stockcode_pool.keys()))
                quantity = str(random.randint(1, 100))
                invoicedate = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
                customerid = random.choice(list(self.customerid_pool.keys()))
                message = ",".join([invoiceno, stockcode, quantity, invoicedate, customerid])
                self.producer.send('invoice_in', str.encode(message))
                yield from asyncio.sleep(1)

    # customerid,country
    @coroutine
    def send_customer(self):
        while len(self.customerid_ini):
            # Select from customerid_ini
            customerid = random.choice(list(self.customerid_ini.keys()))
            country = self.customerid_ini[customerid]
            # Remove from customerid_ini
            del self.customerid_ini[customerid]
            # Insert into customerid_pool
            self.customerid_pool[customerid] = [country]
            # Construct and send the message
            message = ",".join([customerid, country])
            self.producer.send('customer_in', str.encode(message))
            yield from asyncio.sleep(1)

    # stockcode,description,unitprice
    @coroutine
    def send_product(self):
        for stockcode in self.stockcode_ini.keys():
            description = self.stockcode_ini[stockcode][0]
            unitprice = str(self.stockcode_ini[stockcode][1])
            del self.stockcode_ini[stockcode]
            self.stock_pool[stockcode] = [description, unitprice]
            message = ",".join([stockcode, description, unitprice])
            self.producer.send('product_in', str.encode(message))
            yield from asyncio.sleep(1)

        # while len(self.stockcode_ini):
        #     # Select from stockcode_ini
        #     stockcode = random.choice(list(self.stockcode_ini.keys()))
        #     description = self.stockcode_ini[stockcode][0]
        #     unitprice = str(self.stockcode_ini[stockcode][1])
        #     # Remove from stockcode_ini
        #     del self.stockcode_ini[stockcode]
        #     # Insert into stock_pool
        #     self.stock_pool[stockcode] = [description, unitprice]
        #     # Construct and send the message
        #     message = ",".join([stockcode, description, unitprice])
        #     self.producer.send('product_in', str.encode(message))
        #     yield from asyncio.sleep(1)


if __name__ == "__main__":
    mock_producer = MockProducer()
    mock_producer.run()
