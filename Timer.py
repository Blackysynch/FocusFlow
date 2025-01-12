import time

def countdown(t):
  
  while t:
    mins, secs = divmod(t, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

  print('Time\'s up!')

# Set the timer for 25 minutes (25 * 60 seconds)
countdown(25 * 60)