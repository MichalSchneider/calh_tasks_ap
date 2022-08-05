"""
Zaaimplementuj funkcję generującą even_numbers(n: int) zwracającą kolejne liczby parzyste,
nie podzielne przez 3 do wartości maksymalnej, włącznie podanej jako argument
funkcji na przykład:
    - even_numbers(7) powinna zwracać kolejno: [2, 4]
    - even_numbers(15) powinna zwracać kolejno: [2, 4, 8, 10, 14]
"""


def even_numbers(n):

    for number in range(n+1):
        if number > 0 and number % 2 == 0 and number % 3 != 0:
            yield