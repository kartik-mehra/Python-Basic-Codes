import time
ticks = time.time()
print(ticks)
local_time=time.localtime(time.time())
print (local_time)
loc=time.asctime(time.localtime(time.time()))
print(loc)
