
import MySQLdb
from create_table import gpsData

class StoreClass:
	
	def __init__(self,**data):
		"""input a dict as argument"""
		gpsData(**data)
		

	def hello(self):
		print 'hello...'
	
	def sayTime(self,time):
		print 'The time is:',time

