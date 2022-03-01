class Weapon:
    def __init__(self, ammo):
        self.ammo = ammo
        self.current_ammo = self.ammo

    def get_ammo(self):
        return self.current_ammo

    def shoot(self):
        if self.current_ammo <= 0:
            print("Press space bar to reload")
            return

        self.current_ammo -= 1

    def empty(self) -> bool:
        return self.current_ammo == 0

    def reload(self):
        self.current_ammo = self.ammo
