import time

t = time.localtime()
current_time = time.strftime("%d/%m/%y, %H:%M:%S", t)
print("it is currently", current_time)
