a = int(input())
b = int(input())
c = int(input())

prumer = (a + b + c) / 3
if prumer <= 1.5:
    print("prospěl s vyznamenáním")
elif prumer >= 4.5:
    print("neprospěl")
elif prumer > 1.5 and prumer < 4.5:
    print("prospěl")