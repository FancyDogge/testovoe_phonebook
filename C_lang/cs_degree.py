"""
bit = binary, so either 0 or 1

transistors switching berween 1 or 2

 8   4   2   1
 0   0   0   0
2^3 2^2 2^1 2^0

выше - 4 бита, четыре 0 или 1

как бы выдрюченны не были технологии сегодня - смысл один и тот же, компис получает 
информацию и инструкции через 0 и 1


1 2 4 8  16  32  64  128 - 8 бит или один БАЙТ
1 1 1 1  1   1   1   1 = 128 Х 2 = 256, т.к. каждая ячейка активна.


Как, скажем, вывести букву А на экран?
когда комп видит комбинацию =>  01000001 = 65 = A in ASCII

Сейчас популярен unicode, потому что он биг бой, до 4 млрд всевозможных символов 2^32 (4 294 967 296), чтобы отобразить любой человеческий
язык, существующий или будущий

Uniceode is using base-16 or hexadecimal system. U+1F602
U+ have no math impact, its just a convention to say that this is a Unicode char.

colors re represented through RGB 0-255


ЧТО В ИТОГЕ ТО? как так выходит, что 72, 73 и 33 = HI!, но также это и какой-то RGB цвет?

Все зависит от контекста, если это текстовое сообщение, то текст, если фотошоп, то цве, если калькулятор, то сиволы сложения, цифры и т.д.
и тут уже программисты кодом говорят что и как интерпритировать.

еще пример занятный - видосы и фотки становятся все жирнее по размеру, потому что и кол-во пикселей увеличивается, т.е кач-во

или как представить музыку? как минимум через три числа? 1 для ноты, 2 для длительности, 3 для громкости ну и т.д.

или фильмы мульы - как множество картинок, fps blahblah

в общем и целом вот как все вообще работает, просто ВСЕ:

input - {Algorithm(step-by-step-instruction)} - output
code eto implementation of algorithms, t.e instructions
arguments - {function} - return value - ewe odin primer

Важно не просто что-то сваять, а хорошо и эффективно задизайнить.
например поиск в тлфной книге - binary search(log2n, т.к. мы постоянно делим на 2), а не линейный поиск и все такое.

functions, conditions, boolean expressions, loops.   Data and instruction on what do do with it

functional programming 
"""



