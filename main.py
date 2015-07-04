#!/usr/bin/python
import time
from superParser import akParser
from get_data.get_gps import GetClass
from parser_data.parser_gps import ParserClass
from store_data.store_gps import StoreClass

if __name__ == '__main__':
	
	gc=GetClass()
	res_gc=gc.getTime()

	pc=ParserClass()
	res_pc=pc.parserTime(res_gc)
	for i in range(0,1000):
		#sample_data="*|GPS|1729|K2|2006-01-04|13:15:08|6000.0000|2000.0000|40|140|4|5|1|2006-01-04|13:01:04|0|0|0|01000932|1|#*"
		sample_data="*|1729|K2|12345|6000.0000|2000.0000|40|140|4|5|1|123455|0|0|0|01000932|1|#*"
		item_name=['bus_no','line_no','gps_datetime','latitude',
					'longitude','speed','angle','next_station',
					'people_num','start_end_flag','send_datetime',
					'direction','run_status','leave_flag',
					'driver_num','driver_flag']
		item_len =16
		obj_data=akParser(sample_data,item_name,item_len)

		res_dict=obj_data.parser('|',False,False)
		ruler=['s','s',1,'s','s',9,'s',1]
		new_dict=obj_data.transType(ruler)
		aData=StoreClass(**new_dict)
		res_dict.clear()
		time.sleep(0.5)
