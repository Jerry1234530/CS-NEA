class Upgrades: 
    def __init__(self): 
        self.speed_upgrade = 0
        self.value_upgrade = 0 

    def upgrade_speed(self): 
        if self.speed_upgrade <= 10: 
            self.speed_upgrade += 1
            print(f"Speed upgrade level: {self.speed_upgrade}")
        else: 
            print("Speed upgrade limit reached!") 
            return False
        
    def upgrade_value(self): 
        if self.value_upgrade <= 10: 
            self.value_upgrade += 1
            print(f"Value upgrade level: {self.value_upgrade}")
        else: 
            print("Value upgrade limit reached!") 
            return False
    
    def get_upgrade_value(self): 
        return self.upgrade_value
        