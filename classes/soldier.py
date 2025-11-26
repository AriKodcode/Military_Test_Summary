class Soldier:

    def __init__(self, personal_number:int, first_name:str, lest_name:str, gender:str, city:str, distance_from_base:int):
        self.personal_number = personal_number
        self.first_name = first_name
        self.lest_name = lest_name
        self.gender = gender
        self.city = city
        self.distance_from_base = distance_from_base
        self.waiting = True

    def __str__(self):
        return {"id":self.personal_number,"first name":self.first_name,"last name":self.lest_name,"gender":self.gender,"city":self.city,"distance from base":self.distance_from_base}

    def status(self):
        if self.waiting:
            return True
        else:
            return False