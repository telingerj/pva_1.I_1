import time

"""
print("teď budu čekat 1s")
time.sleep(1)
print("hotovo")
"""

cas = time.gmtime(8000)  # unix čas -> lidský čas
print(cas.tm_hour,":",cas.tm_min)
time.time()  # aktuální okamžik v sekundách
#(year, month, day, hour, minute, second, weekday, day of the year, daylight saving)
mujCas = (2017, 1, 5, 8, 17, 21, 0, 0, 0)
print(time.mktime(mujCas)) #  lidský čas -> unix čas (epoch time)

# kolik sekund jsem na světě?

datumNarozeni = (2003, 12, 1, 0, 0, 0, 0, 0, 0)
datumNarozeniUnix = time.mktime(datumNarozeni)
print(time.time() - datumNarozeniUnix)