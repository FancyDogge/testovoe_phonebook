"""
Hexadecimal - 16ричная система исчисления aka base-16
0 1 2 3 4 5 6 7 8 9 A B C D E F

юзается, например, для обозначения RGB вэлью

все системы исчисления работают одинаково, меняется только БАЗА
отсюда и base-16

16^1 16^0 - как и с бинарной системой, база просто возводится в +1 степень за каждый "0"

 16   1  

 0    0    - посчитаем как отобразить 17

 1    1    - 16 + 1

 2    A    - 32 + 10 = 42

 F    F    - 240 + 15 = 255 (предельное значение для каждого из RGB цветов) а еще FF - это байт, т.к. F = 1111 = 4 бита

 Ну и тд.


"""