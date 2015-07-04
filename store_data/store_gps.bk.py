
import MySQLdb

class StoreClass:
	
	def __init__(self,db_host,db_user,db_passwd,db_name):
		try:
			self.db_handler=MySQLdb.connect(db_host,db_user,db_passwd,db_name)
			print 'success ..'
		except MySQLdb.Error,e:
			try:
				sqlError = "Error %d:%s" % (e.args[0],e.args[1])
			except IndexError:
				print "MySQL Error:%s" % str(e)

	def hello(self):
		print 'hello...'
	
	def sayTime(self,time):
		print 'The time is:',time

