# import datetime
# from src.mock_invoice_generator import mock_invoice_generator
#
#
# # Test quantity, invoicedate format
# # tmpdir fixture: per test temporary directory
# def test_mock_invoice_generator_plain_0(tmpdir):
#     invoiceno_pool_file = tmpdir.join('dummy_invoiceno_pool.txt')
#     stockcode_pool_file = tmpdir.join('dummy_stockcode_pool.txt')
#     customerid_pool_file = tmpdir.join('dummy_customerid_pool.txt')
#
#     output_file = tmpdir.join('dummy_output.csv')
#     # Dummy data
#     invoiceno_pool_file.write("537127\n536539\n540414")
#     stockcode_pool_file.write("85123A\n84580\n21558\n22726")
#     customerid_pool_file.write("13831")
#
#     mock_invoice_generator(invoiceno_pool_file.strpath, stockcode_pool_file.strpath, customerid_pool_file.strpath, output_file.strpath, 10)
#     lines = output_file.readlines()
#
#     try:
#         assert len(lines) == 11
#         assert lines[0] == "invoiceno,stockcode,quantity,invoicedate,customerid\n"
#         for line in lines[1:]:
#             fields = line.split(',')
#             # ‘quantity’ should be integer
#             assert type(fields[2]) == type("A")
#             try:
#                 int(fields[2])
#             except:
#                 raise ValueError("Incorrect quantity format, should be string of integer: " + str(fields[2]))
#             # 'invoicedate' shoud be like 2010-12-05 12:13:00
#             try:
#                 datetime.datetime.strptime(fields[3], '%Y-%m-%d %H:%M:%S')
#             except ValueError:
#                 raise ValueError("Incorrect invoicedate format, should be YYYY-MM-DD")
#     except AssertionError as e:
#         for i in range(len(lines)):
#             print(lines[i])
#         raise Exception(e.args)
#
#
# # tmpdir fixture: per test temporary directory
# def test_mock_invoice_generator_corner_0(tmpdir):
#     invoiceno_pool_file = tmpdir.join('dummy_invoiceno_pool.txt')
#     stockcode_pool_file = tmpdir.join('dummy_stockcode_pool.txt')
#     customerid_pool_file = tmpdir.join('dummy_customerid_pool.txt')
#
#     output_file = tmpdir.join('dummy_output.csv')
#     # Dummy data
#     invoiceno_pool_file.write("537127")
#     stockcode_pool_file.write("85123A")
#     customerid_pool_file.write("13831")
#
#     mock_invoice_generator(invoiceno_pool_file.strpath, stockcode_pool_file.strpath, customerid_pool_file.strpath, output_file.strpath, 1)
#     lines = output_file.readlines()
#
#     try:
#         assert len(lines) == 2
#         assert lines[0] == "invoiceno,stockcode,quantity,invoicedate,customerid\n"
#         fields = lines[1].strip().split(',')
#         assert fields[0] == "537127"
#         assert fields[1] == "85123A"
#         assert fields[4] == "13831"
#     except AssertionError as e:
#         for i in range(len(lines)):
#             print(lines[i])
#         raise Exception(e.args)
