"""
cislo = int(input())
if cislo % 2 == 0:
    if cislo % 3 == 0:
        print("číslo je dělitelné dvěma i třemi")
"""

cislo = int(input())
if cislo % 2 == 0 and cislo % 3 == 0:
        print("číslo je dělitelné dvěma i třemi")

if cislo % 2 == 0 or cislo % 3 == 0:
        print("číslo je dělitelné dvěma nebo třemi")