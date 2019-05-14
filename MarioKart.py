
class Racer():
    
    def __init__(self, name='Mario', vehicle='Kart', position=1):
        """
        Instantiate a racer class. Inputs:
        - Name (string)
        - Vehicle (string)
        - Position (non zero int)
        """
        self.name = str(name) #driver name
        self.vehicle = str(vehicle) #driver car
        if (position <1) or (type(position)!= int):
            raise ValueError("Position must be a non zero integer!")
        else:
            self.position= position
        
    def set_position(self, new_position):
        """
        Change the position
        """
        if (new_position <1) or (type(new_position)!= int):
            raise ValueError("Position must be a non zero integer!")
        else:
            self.position= new_position
    
    def set_weapon(self, weapon='Banana'):
        """
        Add/remove weapon to racer
        """
        self.weapon = weapon
        
    def get_status(self):
        print("{} is coming in hot at position {}".format(self.name, self.position))
        
class Human(Racer):

    def __init__(self, name, vehicle, position, job='plumber'):
        Racer.__init__(self, name, vehicle, position)
        self.job = job
        
    def set_job(self, new_job):
        """
        Assign job, can be any type
        """
        self.job = new_job
        
        
class Lizard (Racer):
    def __init__(self, name, vehicle, position, has_shell):
        Racer.__init__(self, name, vehicle, position)
        if type(has_shell)==bool:
            self.has_shell= has_shell
        else:
            raise ValueError("has shell must be boolean")
     
    
    def set_shell(self, new_shell):
        if type(new_shell)==bool:
            self.has_shell= new_shell
        else:
            raise ValueError("has_shell must be boolean")
        
        
            
       
        