class Cal_density:
    def __init__(self,num_of_people,area_square):  # or any other parameters which can represent the space volume
        self.num_of_people = num_of_people
        self.area_square = area_square

    def method1(self):
        density = self.num_of_people / self.area_square
        return density
    
