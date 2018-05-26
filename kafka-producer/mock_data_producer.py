from kafka import KafkaProducer
import asyncio
from asyncio import coroutine
import time
import datetime
import random

class MockProducer(object):

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers='kafka1:9092')
        self.invoiceno_pool = ['537127', '536539', '540414']
        self.stockcode_pool = {'85123A': ['WHITE HANGING HEART T-LIGHT HOLDER', 3.24], \
                               '84580':  ['MOUSE TOY WITH PINK T-SHIRT', 3.75], \
                               '21558':  ['SKULL LUNCH BOX WITH CUTLERY', 2.55], \
                               '22726':  ['ALARM CLOCK BAKELIKE GREEN', 3.75]}
        self.customerid_pool = {'13831': 'United Kingdom', \
                                '12605': 'Germany'}

    def run(self):
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(
                asyncio.wait([
                    self.send_invoice(),
                    self.send_customer(),
                    self.send_product()
                ])
            )
        finally:
            loop.close()

    # invoiceno,stockcode,quantity,invoicedate,customerid
    @coroutine
    def send_invoice(self):
        while True:
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
        while True:
            customerid = random.choice(list(self.customerid_pool.keys()))
            country = self.customerid_pool[customerid]
            message = ",".join([customerid, country])
            self.producer.send('customer_in', str.encode(message))
            yield from asyncio.sleep(20)

    # stockcode,description,unitprice
    @coroutine
    def send_product(self):
        while True:
            stockcode = random.choice(list(self.stockcode_pool.keys()))
            description = self.stockcode_pool[stockcode][0]
            unitprice = str(self.stockcode_pool[stockcode][1])
            message = ",".join([stockcode, description, unitprice])
            self.producer.send('product_in', str.encode(message))
            yield from asyncio.sleep(20)


if __name__ == "__main__":
    mock_producer = MockProducer()
    mock_producer.run()
