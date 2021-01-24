import time


class ResourceTimer:
    def __init__(self, get_cooldown_s, last_run_epoch_s=time.time()):
        self.last_epoch_s = last_run_epoch_s
        self.get_cooldown_s = get_cooldown_s

    def get_s_remaining(self):
        time_s = time.time()
        next_runnable_time_s = self.last_epoch_s + self.get_cooldown_s()
        return max(0, int(next_runnable_time_s - time_s))

    def can_run(self) -> bool:
        return self.get_s_remaining() == 0

    def reset(self):
        self.last_epoch_s = time.time()
