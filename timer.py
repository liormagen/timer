import time


class Timer(object):
    """
    A basic class for printing elapsed time easily
    """
    def __init__(self, p_hours=True, p_minutes=True, p_seconds=True):
        self.end = None
        self.start = None
        self.start_stop_timer()
        self.p_hours = p_hours
        self.p_minutes = p_minutes
        self.p_seconds = p_seconds

    def print_timer(self):
        self.start_stop_timer(start=False)
        hours, rem = divmod(self.end - self.start, 3600)
        minutes, seconds = divmod(rem, 60)
        if self.p_seconds:
            if self.p_minutes:
                if self.p_hours:
                    return "%d:%02d:%02d (hh:mm:ss)" % (hours, minutes, seconds)
                else:
                    return "%02d:%02d (mm:ss)" % (minutes, seconds)
            else:
                return "%02d (ss)" % seconds

        if self.p_minutes:
            if self.p_hours:
                    return "%d:%02d (hh:mm)" % (hours, minutes)
            else:
                return "%02d (mm)" % minutes

        if self.p_hours:
            return "%2d (hh)" % hours

    def start_stop_timer(self, start=True):
        if start:
            self.start = time.time()
        else:
            self.end = time.time()


if __name__ == "__main__":
    t = Timer()
    print(t.print_timer())
    t.p_hours = False
    print(t.print_timer())
    t.p_minutes = False
    print(t.print_timer())
    t.p_hours = True
    print(t.print_timer())
