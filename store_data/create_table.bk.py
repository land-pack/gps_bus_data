import sqlobject
from Connection import conn

class gpsData(sqlobject.SQLObject):
	_connection = conn
	
	class sqlmeta:
		table='new01'
	phone = sqlobject.StringCol(length=14,unique=True)
	name = sqlobject.StringCol(length=14,unique=True)
	home = sqlobject.StringCol(length=14,unique=True)

gpsData.createTable(ifNotExists=True)
