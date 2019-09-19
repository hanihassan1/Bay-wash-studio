# import os
# import pymysql

# username = os.getenv('C9_USER')

# connection = pymysql.connect(host='localhost',
#                             user=username,
#                             password='',
#                             db='SALON',
#                             )


# try:
#     with connection.cursor() as cursor:
#         sql= """CREATE TABLE CUSTOMERS(CUSTOMER_ID INT PRIMARY KEY AUTO_INCREMENT,
#         CUSTOMER_NAME VARCHAR(30),
#         CUSTOMER_TELEPHONE INT)"""
#         cursor.execute(sql)
# finally:
#     connection.close()