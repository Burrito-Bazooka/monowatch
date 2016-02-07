# monowatch
A very simple stopwatch script, for command line or Python use.

# CLI usage:
```
$ python3 ./monowatch.py
0:00:08.078806
```

Using `python2` or `python` is also fine. Pause with ^C (Ctrl+C on most systems, or whatever will trigger KeyboardInterrupt).

```
0:00:12.42306^C
Stopwatch paused.  KeyboardInterrupt (^C) again to stop. Input numbers to offset the stopwatch ('-10' for 10 seconds subtracted, '10' for 10 seconds added). Input 'u' to resume as if never paused. Press Return to resume stopwatch: 
```

# Python usage:
```python
>>> import monowatch
>>> monowatch.monowatch()
0:00:01.169368
```

Everything else is the same as CLI usage, shown above. Here, we trigger KeyboardInterrupt twice:

```python
0:00:04.817535^C
Stopwatch paused.  KeyboardInterrupt (^C) again to stop. Input numbers to offset the stopwatch ('-10' for 10 seconds subtracted, '10' for 10 seconds added). Input 'u' to resume as if never paused. Press Return to resume stopwatch: 

datetime.timedelta(0, 4, 863235)
>>>
```

When the function is done (stopped without errors), it returns a `datetime.timedelta` for the time it ran.
