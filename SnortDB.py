from MysqlAPI import *
import datetime
import json

class SnortDB(MysqlAPI):
	"""docstring for SnortDB"""
	def __init__(self, host, user, passwd, db, arg):
		super(SnortDB, self).__init__(host, user, passwd, db)
		self.arg = arg

	def getRecord(self, period, proto):
		word_list = TABLE_WORD[proto]
		date_now = datetime.datetime.now()
		date_now = date_now.replace(day = 12, hour = 9, minute = 27)
		date_now_str = date_now.strftime('%Y-%m-%d %H:%M:%S')

		date_begin = (date_now - datetime.timedelta(seconds = period))
		date_begin_str = date_begin.strftime('%Y-%m-%d %H:%M:%S')
		cmd = 'select * from event where timestamp between "%s" and "%s"' %(date_begin_str, date_now_str)
		results = self.getData(cmd)
		msgDic = {}
		num = 0
		for row in results:
			sid = row[0]
			cid = row[1]
			cmd = 'select * from %shdr where sid = %d and cid = %d' %(proto, sid, cid)
			num += 1
			trapMsg = self.getData(cmd)
			msgDic[num] = dict(zip(word_list, trapMsg[0]))

		with open('log','wb') as fw:
			fw.write(json.dumps(msgDic))


