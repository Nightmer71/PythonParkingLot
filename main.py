class ParkingLot:
    def __init__(self, total_spots = 10):

        self.parking_spots = {i: 'Avaliable' for i in range(1, total_spots + 1)}

    def find_avaliable(self):

        avaliable = [spot for spot, status in self.parking_spots.items() if status == 'Avaliable']

        if avaliable:

            print(f"Avaliable spots: {avaliable}")

        else:

            print("No parking spots avaliable")