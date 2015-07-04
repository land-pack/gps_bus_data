import sqlobject
from Connection import conn

class gpsData(sqlobject.SQLObject):
	_connection = conn
	
	class sqlmeta:
		table='new02'
	bus_no = sqlobject.StringCol(length=10)
	line_no = sqlobject.StringCol(length=10)
	gps_datetime = sqlobject.IntCol(length=10)
	latitude = sqlobject.StringCol(length=10)
	longitude = sqlobject.StringCol(length=10)
	speed = sqlobject.IntCol(length=4)
	angle = sqlobject.IntCol(length=4)
	next_station = sqlobject.IntCol(length=11)
	people_num = sqlobject.IntCol(length=11)
	start_end_flag = sqlobject.IntCol(length=11)
	send_datetime = sqlobject.IntCol(length=10)
	direction = sqlobject.IntCol(length=11)
	run_status = sqlobject.IntCol(length=11)
	leave_flag = sqlobject.IntCol(length=11)
	driver_num = sqlobject.StringCol(length=10)
	driver_flag = sqlobject.IntCol(length=4)

gpsData.createTable(ifNotExists=True)
