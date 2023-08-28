"""The length of the ring road is 109 kilometers. Biker Vasya starts from zero kilometer start and rides with speed v
  kilometers per hour. At what mark will it stop after t
  hours?

The program receives the value v as input
  and t
. If v>0
, then Vasya moves in the positive direction at the start, if the value v<0
, then in the negative.

The program should output an integer from 0 to 108 — the number of the mark where Vasya will stop."""

v = int(input())
t = int(input())
x = 109
f = ((v*t)%109 )

print(f)
