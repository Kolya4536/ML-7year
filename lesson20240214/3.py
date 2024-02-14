Vboat = int(input('Яка буде швидкість човна в км/год?'))
Vtechiya = int(input('Яка буде  швидкість течії км/год?'))
t1 = 2
t2 = 3


Slake = t1 * Vboat
Sriver = t2 * (Vboat + Vtechiya)
S = Slake + Sriver
print("Всього човен проплив - ", S, "км")