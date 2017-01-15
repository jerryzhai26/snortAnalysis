from SnortDB import *
import os

snort_db = SnortDB(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWD, DB_NAME)
period = int(sys.argv[1])
proto = sys.argv[2]
snort_db.getRecord(period, proto)