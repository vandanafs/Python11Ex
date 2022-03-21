from enum import Enum

class AliveStatus(Enum):
    DECEASED=0
    ALIVE=1


class Person():
    def __init__(self):
     self.first_name=None
     self.last_name=None
     self.date_of_birth=None
     self.alive=None

def update_first_name(self,first_name):
    self.first_name=first_name

def update_last_name(last_name, self):
    self.last_name=last_name

def update_dob(self,dob):
    self.date_of_birth=dob

def update_status(self,alive):
    self.alive=alive

