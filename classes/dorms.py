class Dorm:

    def __init__(self,dorm_number):
        self.dorm_number = dorm_number
        self.rooms_list = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None
        ]
    def __str__(self):
        return self.rooms_list


