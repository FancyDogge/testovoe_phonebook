"""
Компуктеру, чтобы найти что-то в памяти, придется смотреть ячейки по одной за раз.

бла-бла, тут про BigO

Классы(структуры/struct)

typedef struct
{
    string name;
    string number;
} person;


                                    SORTING

            selection sort - 

проходим массив в поисках наименьшего числа и запоминаем его, пусть жто будет curr_small
также нам понадобится curr_index(я так думаю), чтобы увеличивать его на +1 после каждой сортировки.
меняем индексами наше текущее наименьшее число с числом с нулевым индексом.
первое число отсортированно
можно начать поиск следующего наименьшего числа, которое будет > уже отсортированных.
поэтому каждый раз после сортировки мы начинаем с индекса +1, т.к. отметаем по одному числу.

(n-1)+(n-2)+(n-3)+...+1 // кол-во проходов, оценка алгоритма
можно свести к этой формуле
n(n-1)/2 (кстати, где-то я ее уже юзал, в задачке какой-то, популярная тема)
=
(n^2 - n)/2
=
n^2/2 - n/2
В BigO имеет значение только наибольший жлемент, т.е. растущий с наибольшей скоростью 
все остальное отметается, даже если мы буквально делим остающийся n^2 на 2
так что сложность этого алгоритма - O(n^2)


            bubble sort -

Repeat n (или n-1) times
    For i from 0 to n-2
        If numbers[i] and numbers[i+2] out of order
            Swap them
    If no swaps
        Quit

(n-1)x(n-1)
=
n^2 - 1n -1n +1
=
n^2 -2n + 1

BigO(n^2)  (algorithmically or asymptptically)
and Omega time(best case) - O(n) if checks for no swaps


            Recursion

void draw(int n) //к марио проблем
{
    //to not go negative
    if (n <= 0)
    {
        return;
    }

    // print pyramid of height n - 1
    draw(n - 1)

    //Print one more row
    for (int = 0; i < n; i++)
    {
        printf("#")
    }
    printf("\n")
}



            merge sort -

If only one num
    Quit
Else
    Sort left half of numbers
    sort right half of numbers
    Merge sorted halves


It takes more space for allocating arrays but less time cmplexity

n log n - bigo
n log n - omega
"""