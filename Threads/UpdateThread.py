from threading import Thread, Timer
import time


class UpdateThread(Thread):
    def __init__(self, func, interval):
        super().__init__()
        self.delay = interval
        self.is_done = False
        self.func = func
        self.func_was_executed = False
        self.initial_time = time.time()

    def done(self):
        self.is_done = True

    def run(self):
        while not self.is_done:
            if not self.func_was_executed:
                self.func()
                self.initial_time = time.time()
                self.func_was_executed = True

            if int(self.initial_time) + self.delay == int(time.time()):
                self.func()
                self.func_was_executed = True
                self.initial_time = time.time()

            time.sleep(0.1)
