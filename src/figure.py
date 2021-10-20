class Figure:

    def __init__(self):
        self.area = None
        raise NotImplementedError("Cannot instantiate abstract base class")

    def add_area(self, figure):
        try:
            return self.area + figure.area
        except:
            #print("Incorrect Class")
            return "Incorrect Class"