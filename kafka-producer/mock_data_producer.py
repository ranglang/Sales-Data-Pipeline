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
        self.stockcode_pool = ['85123A', '84580', '21558', '22726']
        self.customerid_pool = ['13831']

    def run(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([self.send_invoice()]))
        loop.close()

    @coroutine
    def send_invoice(self):
        invoiceno = random.choice(self.invoiceno_pool)
        stockcode = random.choice(self.stockcode_pool)
        quantity = str(random.randint(1, 100))
        invoicedate = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        customerid = random.choice(self.customerid_pool)
        message = ",".join([invoiceno, stockcode, quantity, invoicedate, customerid])
        self.producer.send('invoice_in', b'some_message_bytes')
        yield from asyncio.sleep(1)

    @coroutine
    def send_customer(self):
        pass

    @coroutine
    def send_product(self):
        pass



if __name__ == "__main__":
    mock_producer = MockProducer()
    mock_producer.run()
