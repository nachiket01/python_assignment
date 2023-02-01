import random
import json
class parking_lot:
	def __init__(self,square_footage):
		self.square_footage = square_footage
		self.parking_spots = [None] * (square_footage // 96+1)
		self.parking_spots[0] = "route"

	
	def parking(self,spot,car):
		if self.parking_spots[spot] is None:
			self.parking_spots[spot] = car
			return f"Car with license plate {car} parked successfully in spot {spot}"
		else:
			return f"Spot {spot} is already occupied by car with license plate {self.parking_spots[spot]}"

	def jsonfy(self):
		parking_dict = {}

		for i in self.parking_spots:
			if str(i) != "None": parking_dict[self.parking_spots.index(i)] = str(i)

		parking_json = json.dumps(parking_dict, indent=4) # convert Dict into a json object
		with open("Parking_lot_status.json", "w") as outfile:
			outfile.write(parking_json)

class Car:

	def __init__(self,license_plate):
		self.license_plate = license_plate

	def __str__(self):
		return self.license_plate

	def park(self,lot, spot):
		return lot.parking(spot,self)


def main(cars,square_footage):
	lot = parking_lot(square_footage)

	for car in cars:
		parked = False
		while not parked:
			spot = lot.parking_spots.index(None) if None in lot.parking_spots else None
			if spot is not None:
				result = car.park(lot,spot)
				print(result)
				parked = True
			else:
				break	
	lot.jsonfy()
	if parking_spots > len(cars):
		print(f"Avilable parking spots: {parking_spots-len(cars)} ")

	else:
		print(f"parking lot is full {total_cars- parking_spots }cars remain to park")




if __name__ =='__main__':
	
	square_footage = int(input("Enter square footage of parking lot : "))
	parking_spots = square_footage // 96
	total_cars = int(input("Enter total number of cars : "))
	cars = [Car(f"MH {random.randint(1,99)}-AZ-{random.randint(1000,9999)}") for i in range(1,total_cars+1)]		
	main(cars,square_footage)
	
