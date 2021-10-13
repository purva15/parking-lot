from data import carType as ct

#car = {carNo: [{carType:MT},{color:'Red'},{money: 15},{spotId:1323}]}
#cars = [car,car]
#spot = {spotId: [{blockId: 1},{availability: True}]}
#spots = [spot, spot]
cars = {
	1:{"carType":ct.CarType.MT,"money":15, "spotId":11},
}



# Assumption :
# spot ids incrementing unique id


spots = {
	1:{"blockId":1, "availability":True},
	2:{"blockId":1,"availability":False},
	3:{"blockId":1,"availability":True},
	4:{"blockId":2,"availability":True},
	9:{"blockId":3,"availability":True},
	5:{"blockId":2,"availability":False},
	6:{"blockId":2,"availability":True},
	7:{"blockId":2,"availability":False},
	8:{"blockId":3,"availability":True},
	
	}


	