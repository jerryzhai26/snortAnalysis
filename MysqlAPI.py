import MySQLdb
import MySQLdb

class MysqlAPI(object):
	"""docstring for MysqlAPI"""
	def __init__(self, host, user, passwd, db):
		self.host = host
		self.user = user
		self.passwd = passwd
		self.db = db
		self.api = MySQLdb.connect(self.host, self.user, self.passwd, self.db)		
		self.cursor = self.api.cursor()

	def getData(self, cmd):
		sql = cmd
		try:
			self.cursor.execute(sql)
			results = self.cursor.fetchall()
		except:
			print("Error: unable to fetch data")
		return results

	def updateData(self, cmd):
		sql = cmd
		try:
			cursor.execute(sql)
			self.api.commit()
		except:
			self.api.rollback()
			print("Error: unable to update")

	def deleteData(self, cmd):
		sql = cmd
		try:
			self.cursor.execute(sql)
			self.api.commit()
		except:
			self.api.rollback()
			print("Error: unable to update")

	def insertData(self, cmd):
		sql = cmd
		try:
			self.cursor.execute(sql)
			self.api.commit()
		except:
			self.api.rollback()
			print("Error: unable to update")

	def closeAPI(self):
		self.api.close()
