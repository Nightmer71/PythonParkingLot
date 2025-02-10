class ParkingLot:
    def __init__(self, total_spots = 10):

        self.parking_spots = {i: 'Avaliable' for i in range(1, total_spots + 1)}

    def find_avaliable(self):

        avaliable = [spot for spot, status in self.parking_spots.items() if status == 'Avaliable']

        if avaliable:

            print(f"Avaliable spots: {avaliable}")

        else:

            print("No parking spots avaliable")

    def reserve_spot(self, spot):

        if spot in self.parking_spots and self.parking_spots[spot] == 'Avaliable':

            self.parking_spots[spot] = 'Reserved'

            print(f"Spot {spot} has benn reserved")

        else:

            print("Invalid or already reserved spot")

    def release_spot(self, spot):

        if spot in self.parking_spots and self.parking_spots[spot] == 'Reserved':

            self.parking_spots[spot] = 'Avaliable'

            print(f"Spot {spot} is now avaliable")

        else:

            print("Invalid or already avaliable spot")

    def view_status(self):

        for spot, status in self.parking_spots.items():

            print(f"Spot {spot}: {status}")

def menu():

    parking_lot = ParkingLot()

    while True:

        print("\n--- Parking Finder Menu ---")

        print("1. Find avaliable parking spot")

        print("2. Reserve a parking spot")

        print("3. Release a reserved spot")

        print("4. View parking status")

        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            parking_lot.find_avaliable()

        elif choice == '2':
            spot = int(input("Enter spot number to reserve: "))
            parking_lot.reserve_spot(spot)

        elif choice == '3':
            spot = int(input("Enter spot number to release: "))
            parking_lot.release_spot(spot)

        elif choice == '4':
            parking_lot.view_status()

        elif choice == '5':
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again")

if __name__ == '__main__':

    menu()