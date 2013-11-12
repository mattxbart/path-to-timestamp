import sys, os
import time
import datetime

def make_tuple(time_dirs):
    parts = []
    for part in time_dirs:
        try:
            part = int(part)
            parts.append(part)
        except ValueError:
            print "'%s' not a valid integer for time conversion" % part
            return []
    return tuple(parts)

def run(path):

    for base, dirs, files in os.walk(path):
        time_dirs = base.split(os.sep)[-3:]
        time_tuple = make_tuple(time_dirs)
        if time_tuple:
            struct = time.mktime(make_tuple(time_dirs) + (0, 0, 0, 0, 0, 0))
            for f in files:
                os.utime(os.path.join(base, f), (struct, struct,))
                print os.path.join(base, f), struct

        



if __name__ == "__main__":
    
    run(sys.argv[1])
