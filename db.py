import pymysql
import config
conn = pymysql.connect(host=config.HOST,
                       port=config.PORT,
                       user=config.USERNAME,
                       password=config.PASSWORD,
                       db=config.DBNAME,
                       charset=config.CHARSET,
                       cursorclass=config.CURSORCLASS)