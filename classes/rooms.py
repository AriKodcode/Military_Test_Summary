class Room:
    def __init__(self,room_number):
        self.room_number = room_number
        self.list_soldiers = [
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            None,
        ]
    def __str__(self):
        return self.list_soldiers

