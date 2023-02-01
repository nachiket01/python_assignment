import json
import random


class parking_lot:
    def __init__(self, square_footage):
        self.square_footage = square_footage
        self.parking_spots = [None] * (
            square_footage // 96 + 1
        )  # calculate number of spots in given area(96 sqft = 1 spot)
        self.parking_spots[0] = "None"  # For spot index adjusting

    def parking(self, spot, car):

        if self.parking_spots[spot] is None:  # checking avilabilty of spot
            self.parking_spots[spot] = car  # storing Car object at given spot
            return f" Car with license plate {car} parked successfully in spot {spot}"

    def jsonfy(self):

        parking_dict = {}

        for i in self.parking_spots:
            if str(i) != "None":
                parking_dict[self.parking_spots.index(i)] = str(i)

        parking_json = json.dumps(
            parking_dict, indent=4
        )  # convert Dict into a json object

        # writing into json file
        with open("Parking_lot_status.json", "w") as outfile:
            outfile.write(parking_json)


class Car:
    def __init__(self, license_plate):
        self.license_plate = license_plate

    def __str__(self):
        return self.license_plate

    def park(self, lot, spot):
        return lot.parking(spot, self)  # call parking


def main(cars, square_footage):
    lot = parking_lot(square_footage)  # creating object

    for car in cars:
        parked = False
        while not parked:

            spot = int(
                input(f"\n Enter Spot between 1 - { len(lot.parking_spots)-1} : ")
            )
            if spot >= len(lot.parking_spots):
                print(
                    f" spot number sould be less than {len(lot.parking_spots)-1}, Terminated!"
                )
                return

            if lot.parking_spots[spot] == None:
                result = car.park(lot, spot)
                print(result)
                parked = True
                break
            else:
                print(
                    f"\n Spot {spot} is already occupied by car with license plate {lot.parking_spots[spot]}"
                )
                spot = (
                    lot.parking_spots.index(None) if None in lot.parking_spots else None
                )  # get index of empty spot from lot
                if spot != None:
                    result = car.park(lot, spot)  # call park with values
                    print(f"\n Parking in avilable spot :-{result}")
                    parked = True
                else:
                    print(f"\n Parking lot is full! {total_cars - parking_spots} cars remain to park")
                    return 0
    lot.jsonfy()  # convert to Json file

    if parking_spots > len(cars):
        print(f" \n Avilable parking spots: {parking_spots - len(cars)} ")
    else:
        print(
            f"\n Parking lot is full! {total_cars - parking_spots} cars remain to park"
        )


if __name__ == "__main__":

    square_footage = int(input("Enter square footage of parking lot : "))
    parking_spots = square_footage // 96
    total_cars = int(input("\n Enter total number of cars : "))
    cars = [
        Car(f"MH {random.randint(1,99)}-AZ-{random.randint(1000,9999)}")
        for i in range(1, total_cars + 1)
    ]  # random license plate genration

    main(cars, square_footage)  # Main call

