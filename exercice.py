#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    return math.sqrt(a)


def square(a: float) -> float:
    return a**2


def average(a: float, b: float, c: float) -> float:
    return (a+b+c)/3


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    r1 = math.radians(angle_degs)
    r2 = math.radians(angle_mins/60) 
    r3 = math.radians(angle_secs/3600)
    return r1+r2+r3


def to_degrees(angle_rads: float) -> tuple:
    degrees = math.degrees(angle_rads)
    minutes = (degrees % 1) * 60
    secondes = (degrees % 1) * 3600
    
    return (degrees, minutes, secondes)


def to_celsius(temperature: float) -> float:
    return round((temperature-32)*(5/9),1)
    

def to_farenheit(temperature: float) -> float:
    return  round((temperature*1.8)+32,1)


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")
    
    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")
    
    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
