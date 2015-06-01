from __future__ import print_function

import time
import sys
import datetime

try:
    input = raw_input # py2
except NameError:
    pass # py3

def monowatch(showdocs=True):
    if showdocs:
        pausetext = "\nStopwatch paused.  KeyboardInterrupt (^C) again to stop. Input numbers to offset the stopwatch ('-10' for 10 seconds subtracted, '10' for 10 seconds added). Input 'u' to resume as if never paused. Press Return to resume stopwatch: "
    else:
        pausetext = "\nStopwatch paused. Input offset, 'u', or ^C: "

    timestart = time.time()
    while True:
        try:
            i = str(datetime.timedelta(seconds=time.time() - timestart))
            sys.stdout.write("\r%s" % i)
            time.sleep(0.05)
            sys.stdout.flush()
        except KeyboardInterrupt:
            try:
                pausedtime = time.time() - timestart

                while True:
                    try:
                        offset = input(pausetext)
                        timestart = time.time() - (pausedtime - float(offset))
                        break
                    except ValueError:
                        if offset == "":
                            timestart = time.time() - pausedtime
                            break
                        elif offset.lower() == "u":
                            break
                        print("Error, you must input a number to offset and resume, or nothing to just resume, or 'u' to resume as if never paused, or ^C to stop.")

            except KeyboardInterrupt:
                print("\n")
                return datetime.timedelta(seconds=pausedtime)

if __name__ == "__main__":
    monowatch()
