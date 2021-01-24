from src.scenes.resources.resource_timer import ResourceTimer


class ShipResources:
    def __init__(self):
        self.reset()

    def reset(self):
        self.got_outta_here = False
        self.energy = 100
        self.fuel = 30
        self.shields = 50

        self.draw_cooldown_s = 10
        self.draw_size = 3
        self.energy_recharge_cooldown_s = 10
        self.energy_recharge_amount = 10
        self.fuel_use_cooldown_s = 5
        self.fuel_use_amount = 1
        self.card_choices = 3
        self.pirate_cooldown_s = 2
        self.pirate_time_left = 255

        # timers
        self.draw_timer = ResourceTimer(lambda: self.draw_cooldown_s, 0)
        self.energy_timer = ResourceTimer(lambda: self.energy_recharge_cooldown_s)
        self.fuel_timer = ResourceTimer(lambda: self.fuel_use_cooldown_s)
        self.pirate_timer = ResourceTimer(lambda: self.pirate_cooldown_s)

        self.pirate_timer.reset()
        self.auto_update_timers = {
            self.energy_timer: self.update_energy,
            self.fuel_timer: self.update_fuel,
            self.pirate_timer: self.update_pirate_time_left
        }

    def update_energy(self):
        self.energy += self.energy_recharge_amount

    def update_fuel(self):
        self.fuel -= self.fuel_use_amount

    def update_pirate_time_left(self):
        self.pirate_time_left -= 1

    def update(self, dt):
        for t, a in self.auto_update_timers.items():
            if t.can_run():
                a()
                t.reset()

    def modify(self, k, v):
        if k == "energy":
            self.energy += v
        elif k == "fuel":
            self.fuel += v
        elif k == "shields":
            self.shields += v
        elif k == "draw_cooldown_s":
            self.draw_cooldown_s += v
        elif k == "draw_size":
            self.draw_size += v
        elif k == "energy_recharge_cooldown_s":
            self.energy_recharge_cooldown_s += v
        elif k == "energy_recharge_amount":
            self.energy_recharge_amount += v
        elif k == "card_choices":
            self.card_choices += v
        elif k == "pirate_timer_s":
            self.pirate_timer_s += v
        else:
            print(f"ERROR, can't adjust resource type {k}")