# Сортировка пузырьком
# во время итерации сравниваются 2 рядом стоящие числа. слева - меньшее, справа - большее
# каждая итерация показывает нам наибольшее число справа
# пузырек - потому что каждую внешнюю итерацию будет справа наибольшее число
lst = [23, 100, 45, 65, 1, 32, 12, 2]
count = 0
for iteration in range(len(lst) - 1):  # n-1, так как последний и так ясен пень будет
    for twist in range(len(lst) - 1 - iteration):  # повороты внутри итерации
        if lst[twist] > lst[twist + 1]:
            lst[twist], lst[twist + 1] = lst[twist + 1], lst[twist]
            count += 1
    print(lst, end=" ")
print()
print(*lst)

# %% Есть несколько видов сортировки: сортировка вставкой, пузырьком и выборкой (insert sort, choice sort, bubble sort) - они все квадратичные O(n^2) в максимале
# Также есть сортировка подсчётом, если есть узкий домен значений. Не требует подсчёта всех чисел из исходных данных
# 31232312441242315122109412590125 - можем разделить на 10 цифр и находить, сколько раз встречались через lst[0] * 10 and +=1

# Сортировка подсчётом O(N) in terms of time and O(M) in terms of different digits

# Инвариант цикла всегда есть: он показывает, каким образом мы облегчаем нашу следующую итерацию.

lst = [13, 31, 11, 12, 43, 22, 145, 2, 1231]


# Рассмотрим сначала сортировку пузрьком
def bubble_sort(inp):
    for iteration_depth in range(len(inp) - 1):
        for iteration_width in range(len(inp) - 1 - iteration_depth):
            if inp[iteration_width] > inp[iteration_width + 1]:
                inp[iteration_width], inp[iteration_width + 1] = inp[iteration_width + 1], inp[iteration_width]
    return inp


# Теперь сортировка выборкой
def choice_sort(inp):
    lst_answer = list()
    while len(inp) != 1:
        min_index = 0
        min_digit = inp[min_index]
        for i in range(1, len(inp)):
            if min_digit > inp[i]:
                min_index = i
                min_digit = inp[min_index]
        lst_answer.append(inp.pop(min_index))
    lst_answer.append(inp.pop())
    return lst_answer


# Теперь сортировка вставкой
def insert_sort(inp):
    for top in range(1, len(inp)):
        key = top
        while key > 0 and inp[key - 1] > inp[key]:
            inp[key], inp[key - 1] = inp[key - 1], inp[key]
            key -= 1
    return inp


def test_func(lst):
    result = sorted(lst)
    print(bubble_sort(lst) == result)
    print(insert_sort(lst) == result)
    print(choice_sort(lst) == result)
    print("The end")


test_func(lst)
# %%

# %% Алгоритм циклического сдвига вправо и влево
lst = [1, 2, 3, 4, 5]


def move_left(inp):
    temp = inp[0]  # на хранение
    for i in range(len(inp) - 1):  # на одну меньше
        # print(f"Before: {inp}")
        inp[i] = inp[i + 1]  # не трогаем последнюю
        # print(f"After{inp}")
    inp[-1] = temp
    return inp


def move_right(inp):
    temp = inp[-1]
    for i in range(len(inp) - 2, -1, -1):  # до 0
        inp[i + 1] = inp[i]  # не трогаем начальную
    inp[0] = temp
    return inp


def test_func(lst):
    lst_1 = list(lst)
    print(move_right(lst_1), "as right")
    lst_2 = list(lst)
    print(move_left(lst_2), "as left")


test_func(lst)

# %% слияние списков
# мини списки уже отсортированы
# основа - это указатели, которые по умолчанию равны первым элементам
# если число больше, то указатель сдвигается вправо
# [1, 4, 6, 12]
#   |
# [2, 3, 4, 15]
lst_1 = [12, 14, 16, 22, 23, 65]
lst_2 = [13, 14, 15, 17, 21, 25, 45, 100]
lst_3 = []
i = j = 0  # указатели
while i < len(lst_1) and j < len(lst_2):
    if lst_1[i] >= lst_2[j]:
        lst_3.append(lst_2[j])
        j += 1
    else:
        lst_3.append(lst_1[i])
        i += 1
if i != len(lst_1) - 1:
    lst_3 += lst_1[i:]
else:
    lst_3 += lst_2[j:]
print(lst_3)
print()


# %% Сортировка слиянием
# разбиваем по len//2 и так делаем до тех пор, пока длина не станет равна 1
# затем слияние отсортированных списков по 1 элементу применяем (выше алгоритм) через указатели

def merge_twi_list(lst_1, lst_2):
    lst_3 = []
    i = j = 0  # указатели
    while i < len(lst_1) and j < len(lst_2):
        if lst_1[i] >= lst_2[j]:
            lst_3.append(lst_2[j])
            j += 1
        else:
            lst_3.append(lst_1[i])
            i += 1
    while i < len(lst_1):
        lst_3.append(lst_1[i])
        i += 1
    while j < len(lst_2):
        lst_3.append(lst_2[j])
        j += 1
    return lst_3


def merge_sort(s):
    if len(s) == 1:
        return s
    middle = len(s) // 2
    left = merge_sort(s[:middle])  # с самого начала - возрат из рекурсии по базовому случаю
    right = merge_sort(s[middle:])  # это тоже
    return merge_twi_list(left, right)


print(merge_sort([13, 24, 3, 2, 132, 22]))
print(merge_sort([13, 24, 3, 2]))
merge_sort([13, 24, 3, 2])


# %% Быстрая сортировка - через рекурсию
# выбирае опорный элемень. Слева - меньше опортного, справа - больше опорного
# список из одного элемента или пустой список уже отсортирован
def fast_search(s):
    if len(s) <= 1:
        return s
    stable = s[0]
    left = list(filter(lambda x: x < stable, s))
    center = list(filter(lambda x: x == stable, s))  # если есть одинаковые числа = опорному числу (8 8 8)
    right = list(filter(lambda x: x > stable, s))
    return fast_search(left) + center + fast_search(right)


print(fast_search([13, 22, 1, 15, 17, 15, 3, 10223, 7]))


# %% Stack - LIFO - тарелки
# ПСП - правильная скобочная последовательность

def psp(s):
    stack = []
    is_good = True
    for element in s:
        if element in "({[":
            stack.append(element)
        else:
            if not stack:  # if len(stack) == 0
                is_good = False
                break
            open_brackets = stack.pop()
            if open_brackets == '(' and element == ')':
                continue
            elif open_brackets == "{" and element == '}':
                continue
            elif open_brackets == "[" and element == ']':
                continue
            is_good = False
            break
    if len(stack) == 0 and is_good == True:
        print("YES")
    else:
        print("NO")


psp("(){}[]")
psp("{(})")
psp("{()}")

# %% Грокаем алгоритмы. Сложность алгоритмов показывает худший случай нахождения
# %% 5 видов алгоритмов: 0(log(n)) - логарифмическое время. Бинарный поиск
# O(n) - линейное время. Простой поиск
# 0(n*log(n)) - эффективный алгоритм сортировки (быстрая сортировка)
# 0(n^2) - медленные алгоритмы сортировки (сортировкавыбором).
# O(n!) - очень медленные алгоритмы. (задача о коммивояжере)

# %% Реализуем бинарный поиск, который имеет алгоритмическую сложность 0(logn)
# особенность в том, что изначально список должен быть отсортирован
# отсекаем сразу же по половине каждую итерацию
lst = [2, 4, 12, 421, 555, 1000, 2000]


def binary_search(lst, fact):
    min = 0
    max = len(lst) - 1
    iter_number = 0

    while max >= min:  # пока они не сойдутся
        iter_number += 1
        middle = (max + min) // 2
        if fact == lst[middle]:
            return (lst[middle], iter_number)

        if fact > lst[middle]:
            min = middle + 1
            continue

        if fact < lst[middle]:
            max = middle - 1
            continue
        return None


print(binary_search(lst, 2000))
# %% # Массивы и связанный список
# Массивы в питоне. Чтение o(1), запись и удаление o(n). Сохраняются целым пластом в памяти
# Связанные списки чтение o(n), удаление и запись o(1) благодаря ссылочной целостности между элементами связанного списка
# o(1) - постоянно
# Сортировки выбором (n^2) - тупо

lst = [2, 4, 1, 1232, 11, 253, 22]
new_lst = []


def myfunc(lst):
    for element in range(len(lst) - 1):  # смотрим внешнюю хуйню
        min_number = lst[0]  # обнуляем
        min_index = 0  # обнуляем
        for i in range(1, len(lst)):  # смотрим внутреннюю фигню
            if min_number > lst[i]:
                min_number = lst[i]  # в конце каждого цикла у нас будет минимальный элемент
                min_index = i
        new_lst.append(lst.pop(min_index))  # только один элемент добавится. Нужно повторить n раз
    new_lst.append(lst.pop())
    print(new_lst)


myfunc(lst)


# %% Рекурсия.
# Базовый и рекурсивный случай. Стек вызовов и передача управления внешней функции стека на один слой ниже/выше
# Состояние функции, которые не находятся на внешнем слое, замораживаются

def recursion(n):
    if n == 1:
        return 1
    return recursion(n - 1) * n


print(recursion(5))

# %%
print(min(10, 10))
# %%
a = ''' в Рекурсии каждый вызов замораживает состояние вызова
Разделяй и властвуй - основа на определении базового случае, к которому нужно стремиться и поэтапное уменьшение задачи (
в основном, через рекурсию) для приближения к базовому случаю

Алгоритм Архимеда: a, b = max(a,b) % min(a,b), min(a,b) и так до тех пор, пока a or b !=0. Задача с полем

Быстрый поиск - уже делал, смотри ранее.
Средний и лучший случай для быстрой сотрировки - одно и то же. Средний случай и есть лучший случай.

'''


def arhimed(a, b):
    if min(a, b) == 0:
        return max(a, b)
    return arhimed(max(a, b) % min(a, b), min(a, b))


print(f"Наибольший общий делитель: {arhimed(1020, 40)}")

# %% Быстрый поиск
# Базовый случай для рекурсии в случае применения метода "Разделяй и властвуй" является длина массива 1 или 0
# Выбираем в качестве опорного случайный элемент
lst = [2, 31, 1, 12, 21, 123412, 7, 35, 3, 2, 2, 2]
from random import randint


def fast_search(lst):
    if len(lst) <= 1:
        return lst
    else:
        digit = randint(0, len(lst) - 1)  # both included
        return fast_search(list(filter(lambda x: x < lst[digit], lst))) + list(
            filter(lambda x: x == lst[digit], lst)) + fast_search(list(filter(lambda x: x > lst[digit], lst)))


print(fast_search(lst))
# %% В среднем, быстрая сортировка лучше сортировки слиянием!


# %% Хеш-таблица - это неупорядоченная коллекция, в которой элементы, проходя через хэш-функцию получают индекс размещения в массиве
# имеющий константное значение изъятия относительно длины данной структуры данных
# .get .pop and etc
# По сути хеш-таблица - это объединение массива с хеш-функцией
# Коллизии нежелательны (это когда на один индекс массива приходится несколько значений) и создаётся связанный список
# Обеспечение быстрого доступа, вставки, удаления
# В среднем и лучшем случае О(1 - моментальное чтение, в худшем 0(н) - если все элементы находятся внутри связанного списка
# Хорош для кеширования (DNS, например)
# Для обнаружения дубликатов тоже норм (на выборах)
# Коэффициент заполнения выше 0.7 -> пора увеличивать размер массива 2 раза (коэф.заполнения - отношение элементов на размер массива)

# %% Поиск в ширину и графы!
# Граф - это отношения через ребра и узлы
# Направленный граф (стрелка смотрит только в одну сторону) и ненаправленный граф (стрелка смотрит в обе стороны)
# Дерево - это направленный граф, в котором нет рёбер, указывающих в обратном направлении
# Поиск в ширину - это алгоритм с графами, который определяет,
# 1) есть ли маршрут вообще до желаемого!
# 2) Показывает кратчайший маршрут
# PS. Проверка на то, что данный человек уже был, иначе возникнет цикл

# В алгоритме поиск в ширину используется FIFO (first in - first out. Структура - двусторонняя очередь deque)
# Алгоритмическа сложность алгоритма - Nузлов + Cребер + O(1)обработка из словаря => O(N+C)
# Поиск в ширину только для невзвешенных графов

# 1) Запишем имена людей
graph = {}
graph["you"] = ["alica", "bob", "jane"]
graph["alica"] = ["Mikhail", "Andei", "Debil"]
graph["bob"] = ["Mikhail", "Andrei", "Dovin"]
graph["jane"] = ["Mikhail", "Andrei", "bob"]
graph["Mikhail"] = []
graph["Andei"] = []
graph["Andrei"] = []
graph["Debil"] = []
graph["Dovin"] = []

print(graph)

from collections import deque
from random import randint


def search_in_width(graph):
    my_deque = deque()
    checked_list = []
    my_deque += graph["you"]
    checked_list.append("you")
    while my_deque:  # it has at least 1 element или все элементы не равны []. [] - означает по сути пропуск/отсутствие
        selected_item = my_deque.popleft()
        if selected_item in checked_list:
            continue
        else:
            if if_mango():
                return f"We have found this person. His name is {selected_item}"
            else:
                checked_list.append(selected_item)
                my_deque += graph[selected_item]

    return f"We can't find an appropriate human-being"


def if_mango():
    randomik = randint(1, 10)
    if randomik == 5:
        return True
    else:
        return False


print(search_in_width(graph))

# %
# %%
a = '''
Алгоритм Дейкстры - это обход взвешенного ациклического графа (без ненаправленного и направленного в обе стороны взвешенного графа
Работает только с положительными весами
Вычисляет кратчайший путь во взвешенном графе'''

# Создадим граф, создадим хеш-таблицу весов и хеш-таблицу родительских связей, которые будут показывать кратчайший взвешенный промежуточный и финальный путь
# Алгоритм состоит из следующих шагов:
#   1) Определяем, если есть необработанные узлы
#   2) Находим ближайший маршрут от родительского узла до смежных, обновляев таблицу весов и родителей
#   3) Находим расстояние до смежных узлов. Если это расстояние между того, которое в таблице - то заменяем стоимость и родителя
#   4) После обработки всех узлов помечаем данные опорный узел как пройденный
#   5) Заходим в таблицу стоимости и переходим к наилегчайшему маршруту и повторяем шаги 2-4 до тех пор, пока узлы все не пройдены

graph = {}
graph["you"] = {}
graph["you"]["A"] = 6
graph["you"]["B"] = 2
graph["you"]["A"] = {}
graph["you"]["A"]["End"] = 1
graph["you"]["B"] = {}
graph["you"]["B"]["A"] = 3
graph["you"]["B"]["End"] = 5
graph["you"]["End"] = {}
print(graph)

# Создадим граф стоимости (веса)
cost = {}
cost["A"] = 6
cost["B"] = 2
cost["End"] = float('infinity')
print(cost)

parents = {}
parents["A"] = "you"
parents["B"] = "you"
parents["End"] = float("infinity")
print(parents)

checked = []


# Напишем формулу поиска минимального узла
def deisktra(graph, cost, parents, checked):
    node = min_price(cost, checked)
    while node:  # пока там вообще что-то есть   None -> False
        for key, value in graph["you"][node].items():
            if graph["you"][node][key] + cost[node] < cost[key]:
                cost[key] = graph["you"][node][key] + cost[node]
                parents[key] = node
        checked.append(node)
        node = min_price(cost, checked)
    return f"Answer is {parents}, with the price is {cost['End']}"


def min_price(cost, checked):
    least_size = float("infinity")
    least_node = None
    for key, value in cost.items():
        if not key in checked:
            if value < least_size:
                least_size = value
                least_node = key
    return least_node


print(deisktra(graph, cost, parents, checked))
# %%
graph = {}
graph["you"] = ["alica", "bob", "jane"]
graph["alica"] = ["Mikhail", "Andei", "Debil"]
graph["bob"] = ["Mikhail", "Andrei", "Dovin"]
graph["jane"] = ["Mikhail", "Andrei", "bob"]
graph["Mikhail"] = []
graph["Andei"] = []
graph["Andrei"] = []
graph["Debil"] = []
graph["Dovin"] = []

print(graph)

from collections import deque
from random import randint


def my_func(graph):
    checked_list = []
    my_deque = deque()
    my_deque += graph["you"]

    while my_deque:
        person = my_deque.popleft()
        if person in checked_list:
            continue
        elif checked_apple():
            return f" WE have found our friend - {person}!"
        else:
            my_deque += graph[person]
    return "We can't found the apple"


def checked_apple():
    digit = randint(1, 10)
    if digit == 5:
        return True
    return False


print(my_func(graph))
# %%
graph = {}
graph["you"] = {}
graph["you"]["A"] = 6
graph["you"]["B"] = 2
graph["you"]["A"] = {}
graph["you"]["A"]["End"] = 1
graph["you"]["B"] = {}
graph["you"]["B"]["A"] = 3
graph["you"]["B"]["End"] = 5
graph["you"]["End"] = {}
print(graph)

# Создадим граф стоимости (веса)
cost = {}
cost["A"] = 6
cost["B"] = 2
cost["End"] = float('infinity')
print(cost)

parents = {}
parents["A"] = "you"
parents["B"] = "you"
parents["End"] = None
print(parents)


def deisktra(graph, cost, parents):
    checked = []
    node = minimal(cost, checked)
    while node:
        for key, value in graph["you"][node].items():
            new_value = cost[node] + value
            if new_value < cost[key]:
                cost[key] = new_value
                parents[key] = node
        checked.append(node)
        node = minimal(cost, checked)
    return f"The full price is {cost['End']}. Parents are {parents}"


def minimal(cost, checked):
    minimum_cost = float("infinity")
    minimum_node = None
    for key, value in cost.items():
        if key in checked:
            continue
        if value < minimum_cost:
            minimum_cost = value
            minimum_node = key
    return minimum_node


print(deisktra(graph, cost, parents))


# %%
def my():
    b = 12
    c = [1, 2, 3]
    you(b, c)
    print(b)
    print(c)


def you(b, c):
    b += 2
    c.append(
        132113123123)  # изменяемыйц объект, вызываемый в друго функции, сохраняет ссылочную целостность с пронтсранством имён из основной части
    # МОЖЕМ ПЕРЕДАТЬ НЕЗИМЕНЯЕМЫЙ ОБЪЕКТ ТОЛЬКО ЧЕРЕЗ RETURN


my()
# %%
b = 12
c = [1, 2, 3]


def my():  # невозможно и в параметрах, и в глобале указать одинаковые переменные
    # global b, c

    # b += 2
    c.append(
        132113123123)  # изменяемым объектам не нужно разрешение в виде передачи параметра из-за ссылочной целостности
    print("During", b, c)


print("До", b, c)

my()
print("after", b, c)
# %%
a = 3
b = [1, 2, 3]


class Tom:
    c = 3
    d = [1, 2, 3]

    def __init__(self):
        self.d = "Abra"

    def __str__(self):
        return f"{a, b, Tom.c, Tom.d, self.d}"


tom = Tom()
print(tom)
# %%
a = 3
b = [1, 2, 3]
c = 3
d = [1, 2, 3]
print(id(b) == id(d), id(a) == id(c), b == d)  # у неизменяемых объектов одинаковые id
# У изменяемых объектов проходят по итерации и сравнивают каждый элемент
e = "str"
f = "str"
print(id(e) == id(f))  # -> True - неизменяемый объект

# %% NP-полные задачи (задача о коммивояжере или о покрытии множества) - нельзя решить абсолютно точно
# Прибегаем к приближенному алгоритму
# Жадные алгоритмы прибегают к оптимально-локальному исходу

# Решим задачу о покрытии множества
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

# Эта задача является NP-полной, поэтому приходим к тому, что выберем станцию с максимальным количеством станций, которые нужны, а затем так делаем до тех пор, пока все не закончатся
states_needed = set(['id', 'nv', 'ut', 'wa', 'id', 'mt', 'or', 'nv', 'ca', 'nv', 'ut', 'ca', 'az'])
final_stations = set()


def find_best_station():
    global states_needed
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states in stations.items():
            covered = states_needed & states
            if len(states_covered) < len(covered):
                states_covered = covered
                best_station = station
        final_stations.add(best_station)
        states_needed -= states_covered


find_best_station()
print(final_stations)


# %%

# %% Алгоритм K ближайших соседей для задач классификации и регрессии
# Оптимальным количеством K ближайших соседей является sqrt(n)
# Извлечение признаков для работы алгоритма - это представления признаков в виде матрицы

# %% Алгоритм со степенью

def pwr(a, n):
    if n == 1:
        return a
    elif n % 2 == 0:  # через каждый шаг у нас будет кратная степень, из-за чего общее количество итераций будет равно log2(N) a^10 = (a**2)^5
        return pwr(a ** 2, n // 2)
    return pwr(a, n - 1) * a  # n^10 = n^9 * n


print(pwr(10, 3))
# %% Особенность питона
for i, j in [1, 2], [3, 4], [5, 6]:
    print(i, j)


# %%
# Генерация перестановки
def generate_numbers(n, m,
                     prefix=None):  # m размерность наших переменных, n - количество цифр, длина которых должна быть
    prefix = prefix or []
    if m == 0:
        print(*prefix)
        return
    for digit in range(n):  # всегда из каждого узла будет исходить по 2 ветви
        prefix.append(digit)
        generate_numbers(n, m - 1,
                         prefix)  # создаём новую ветвь для поиска в глубину. Тип по правилам Шерлока: зашёл в дом - открыл вазу - открыл ячейку - закрыл ячейку - закрыл вазу
        prefix.pop()  # удаляем последний элемент, чтобы вернуться назад на одну ноду наверх


# Таким образом проходим по каждой ноде, перебирая значения
generate_numbers(2, 2)


# %% Генерация перестановки - повторение
def generate_numbers(n, m, prefix=None):
    prefix = prefix or []  # if prefix is None: prefix = []
    if m == 0:
        print(*prefix)
        return

    for digit in range(n):
        prefix.append(digit)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


generate_numbers(3, 2)


# %% Перестановка чисел
def unique_checker(i, prefix):
    if i in prefix:
        return True
    return False


def generate_permutation(n, m=-1, prefix=None):
    if m == -1:
        m = n

    prefix = prefix or []
    if m == 0:
        print(prefix)
        return

    for i in range(1, n + 1):
        if unique_checker(i, prefix):
            continue
        prefix.append(i)
        generate_permutation(n, m - 1, prefix)
        prefix.pop()


generate_permutation(2)

# %% Cортировка слиянием

def merge(a: list, b: list) -> list:
    c = []
    i = j = 0
    while len(a) > i and len(b) > j:
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    while len(a) > i:
        c.append(a[i])
        i += 1
    while len(b) > j:
        c.append(b[j])
        j += 1
    return c


def merge_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left = merge_sort(lst[:middle])
    right = merge_sort(lst[middle:])
    answer = merge(left, right)
    return answer


lst = [1, 33231, 12321, 2231, 11, 23, 4, 123214]
print(merge_sort(lst))
# %% Быстрая сортировка
barrier = 0


def quick_sort(lst: list) -> list:
    if len(lst) <= 1:
        return lst
    left = list(filter(lambda x: x < lst[barrier], lst))
    middle = list(filter(lambda x: x == lst[barrier], lst))
    right = list(filter(lambda x: x > lst[barrier], lst))
    return quick_sort(left) + middle + quick_sort(right)


lst = [1, 33231, 12321, 2231, 11, 23, 4, 123214]
c = quick_sort(lst)


# %% Проверка, отсортирован ли массив
def checked_list(lst: list, ascending=True) -> list:
    s = 2 * int(ascending) - 1
    flag = True
    for i in range(len(lst) - 1):
        if s * lst[i] > s * lst[i + 1]:
            flag = False
            break
    return flag


print(checked_list(c))


# %% Бинарный поиск (условие - список уже отсортирован)

def binary_search(lst, guess):
    start = 0
    end = len(lst) - 1
    while end >= start:
        middle = (end + start) // 2
        if lst[middle] == guess:
            return middle
        elif lst[middle] < guess:
            start = middle + 1
            continue
        else:
            end = middle - 1
            continue
    return None


print(binary_search(c, 12321))


# %% Оптимизация фибоначчи
def fibonacchi(n):
    lst = [0, 1] + [0] * (n - 1)
    print(lst)

    for i in range(2, n + 1):
        lst[i] = lst[i - 1] + lst[i - 2]  # обращение по o(1)
    print(lst[n])


fibonacchi(8)


# %%
# задачи с кузнечиками о шансах решаются также
# если есть какие-то клетки, в которые нельзя наступать, то убираем их

def count_trajectiores(n, allowed: list):
    k = [0, 1, int(allowed[2])] + [0] * (n - 3)  # int(True) = 1 int(False) = 0

    for i in range(3, n + 1):
        if allowed[i]:
            k[i] = k[i - 1] + k[i - 2] + k[i - 3]


# %% Допрыгать за минимальную стоимость

def price_cost(n, price: list):
    c = [float('-inf'), price[1], price[1] + price[2]] + [0] * n - 3
    for i in range(3, len(price) + 1):
        c[i] = min(price[i - 1], price[i - 2]) + price[i]  # выбор из двух мин + наша цена


# %% Алгоритм подчсёта длины общей последовательности
# Целевая функция, что если элементы равны, то +1 от прошлого i-1 j-1, если не равны, то максимум из i-1 j and i j-1

def lcs(a, b):
    f = [[0] * (len(b) + 1) for i in range(len(a) + 1)]  # для первых чисел добавляем 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = 1 + f[i - 1][j - 1]
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
    return f[-1]


f = lcs([1, 2, 32, 321224, 5], [1, 4, 3, 4, 5])
print("Наибольшая длина общей подпоследовательности:", f[-1][-1])
# %% Нахождение  пути наибольшей длины возрастающей числовой подпоследовательности
def back_path(a, b, f):
    ans = []
    i = len(a)
    j = len(b)

    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1]:
            ans.append(a[i - 1])  # -1 от длины
            i -= 1
            j -= 1
        elif f[i - 1][j] == f[i][j]:
            i -= 1
        else:
            j -= 1
    return ans[::-1]


print(back_path(['a', 'b', 'c', 'd', 'e'], ['a', 'b', 'd', 'c', 'e'], f))

#%% О наибольшей возрастающей последовательности
def lcs(a, b):
    f = [[0] * (len(b) + 1) for i in range(len(a) + 1)]  # для первых чисел добавляем 0
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                f[i][j] = 1 + f[i - 1][j - 1]
            else:
                f[i][j] = 0
    return f

f = lcs([1, 2, 3,  32, 321224, 5], [1, 2, 3, 4, 5, 6])
print("Наибольшая длина общей подпоследовательности:", f)
#%% Редакционное расстояние Левенштейна
# Целевая функция: a[i-1]==b[j-1] -> F[i-1][j-1]
# min(F[i-1][j], F[i][j-1], F[i-1][j-1])
# Крайний случай: F[0][j] = j, F[i][0] = i, F[0][0] = 0
def levistein_distance(a, b):
    f = [[(i+j) if i * j == 0 else 0 for j in range(0, len(b) + 1)] for i in range(0, len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i-1] == b[j-1]:
                f[i][j] = f[i-1][j-1]
            else:
                f[i][j] = 1 + min(f[i-1][j], f[i][j-1], f[i-1][j-1])
    return f[-1][-1]

print(levistein_distance("hello", "lo"))

#%% Стек ПСП
def psp(string):
    lst = []
    for element in string:
        if element in ["(", "["]:
            lst.append(element)
            continue
        else:
            top_stack = lst.pop()
            if top_stack:
                if top_stack == "[" and element == "]":
                    continue
                elif top_stack == "(" and element == ")":
                    continue
                else:
                    return False
            else:
                return False
    if lst:
        return False
    return True

print(psp("([])"))
print(psp("()[]()"))
print(psp("([([([])])])"))
print(psp("([([()])]]"))
#%% Обратная польская нотация (reversed polish notation)
# Алгоритм вычисления выражений в постфиксной нотации
# [5, 2, 7, *, +] -> 5 + 2 * 7
# В питоне нельзя int сравнивать со строкой на вхождение. 5 in "hello" -> error (not false but error) -> нужно преобразовывать в list

def rpn(lst):
    stack = []
    for element in lst:
        if not element in ["*", "/", "+", "-", "%"]:
            stack.append(element)
        else:
            right_element = stack.pop()
            left_element = stack.pop()
            if element == "+":
                stack.append(left_element + right_element)
            elif element == "-":
                stack.append(left_element - right_element)
            elif element == '*':
                stack.append(left_element * right_element)
            else:
                stack.append(left_element / right_element)
    return stack.pop()

print(rpn([5, 2, 7, '*', '+']))
#%%
#%% heap

class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    def lift_up(self, i):
        while i != 0 and self.values[i] < self.values[(i-1) // 2]:
            self.values[i], self.values[(i-1) // 2] = self.values[(i-1) // 2], self.values[i]
            i = (i-1) // 2

    def lift_down(self, i):
         #количество родителей, у которых есть хотя бы один ребёнок
        while 2*i+1 < self.size:
            j = i
            if self.values[i] > self.values[i*2+1]:
                j = 2*i+1
            if self.values[i*2+2] and self.values[j] > self.values[i*2+2]: # либо поменяется, либо нет
                j = 2*i+2
            if i == j: # одной неизменичивыой итерации по детям достаточно!
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j

    def insert(self, x): # вставляем в конец, пропихивая вверх по родителям (n-1) // 2
        self.values.append(x)
        self.size += 1
        self.lift_up(self.size - 1)

    def extract_min(self):
        tmp = self.values[0]
        self.values[0] = self.values.pop()
        self.size -= 1
        self.lift_down(0)
        return tmp
#%% heapify_sort
def heapify_sort(arr):
    heap = Heap()
    for element in arr:
        heap.insert(element)
    print(heap.values)
    return heap

def get_sorted_heap(heap):
    arr = []
    while heap.size:
        arr.append(heap.extract_min())
    return arr

print(get_sorted_heap(heapify_sort([4, 2, 1, 14, 15, 12321, 11111])))

#%%
# Списки смежности
# {key:{values}, ...}
# m - размер графа, n - порядок

m, n = [int(x) for x in input().split()]
graph = {}

for i in range(m):
    v1, v2 = input().split()
    for e1, e2 in (v1, v2), (v2, v1): # если граф неориентированный, то должно быть симметрично относительно главной диагонали
        if e1 not in graph:
            graph[e1] = {e2}
        else:
            graph[e1].add(e2)




# %%
# Поиск графа в глубину (поиск в ширину через deque)
# Поиск в глубину через стек

graph = {'A': ['B', 'C'],

         'B': ['C', 'D'],

         'C': ['D'],

         'D': ['C'],

         'E': ['F'],

         'F': ['C']}


def find_path(graph, start, end, path=[]):
    path = path + [start]  # для будущего
    if start == end:
        return path

    if not start in graph:
        return None

    for node in graph[start]:
        if not node in path:  # от циклов
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath


print(find_path(graph, "A", "D"))
#%% поиск в глубину (поиск в ширину всегда ищет наикратчайший путь из-за за того, что действует по-уровнего)

visited = [False] * (n+1)
ans = []
def dfs(start, graph, visited, ans):
    visited[start] = True
    for neighbour in graph[start]:
        if not visited[neighbour]:
            dfs(neighbour, graph, visited, ans)
    ans.append(start)


#%% Поиск в ширину
n, m = map(int, input().split())
graph = {i: set() for i in range(n)} #список смежности
for i in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].add(v2)
    graph[v2].add(v1)

from collections import deque
distances = [None] * n
start_vertex = 0
distances[start_vertex] = 0
parents = [None] * n
queue = deque([start_vertex])
while queue:
    current_vertex = queue.popleft()
    for neighbour in graph[current_vertex]:
        if not distances[neighbour]: # проверка на то, был ли обработан ранее
            queue.append(neighbour)
            parents[neighbour] = current_vertex
            distances[neighbour] = distances[current_vertex] + 1

#%% Дополнение - определение маршрута (восстановление пути)
end_vertex = 9
path = [end_vertex]
parent = parents[end_vertex]
while parent is not None:
    path.append(parent)
    parent = parents[parent]
path = path[::-1]


# мб в таких задачах проще сначала всё просчитать, хотя обход в ширину наименьший! (у невзвешенного графа) по количеству шагов
#%% Задача с конём
# Идея задачи в том, чтобы построить все клетки и указать в них всевозможные ходы, чтобы потом выбрать
from collections import deque

letters = 'abcdefgh'
numbers = '12345678'
graph = dict()
for i in letters:
    for j in numbers:
        graph[i+j] = set()

# Теперь проверим, есть ли соседи, для того чтобы сделать ход
for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j] # "a4"
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            graph[v1].add(letters[i+2] + numbers[j+1])
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            graph[v1].add(letters[i+1] + numbers[j+2])
        if 0 <= i + 2 < 8 and 0 <= j - 1 < 8:
            graph[v1].add(letters[i+2] + numbers[j-1])
        if 0 <= i + 1 < 8 and 0 <= j - 2 < 8:
            graph[v1].add(letters[i+1] + numbers[j-2])
        if 0 <= i - 1 < 8 and 0 <= j - 2 < 8:
            graph[v1].add(letters[i-1] + numbers[j-2])
        if 0 <= i - 2 < 8 and 0 <= j - 1 < 8:
            graph[v1].add(letters[i-2] + numbers[j-1])
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            graph[v1].add(letters[i-2] + numbers[j+1])
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            graph[v1].add(letters[i-1] + numbers[j+2])
print(graph)
start_vertex = 'd4'
end_vertex = 'f7'
queue = deque([start_vertex]) # можно начать и с конца, так даже будет быстрее (меньше возможных шагов в начале поиска)
distances = {v: None for v in graph}
distances[start_vertex] = 0
parents = {v: None for v in graph}
while queue:
    current_vertex = queue.popleft()
    for neighbour in graph[current_vertex]:
        if distances[neighbour] is None: # хранить неподходящие шаги можно в dict - parents and distances
            queue.append(neighbour)
            distances[neighbour] = distances[current_vertex] + 1
            parents[neighbour] = current_vertex

path = [end_vertex]
parent = parents[end_vertex]
while parent is not None:
    path.append(parent)
    parent = parents[parent]

print(path[::-1])
print(distances)
#%%
print(path[::-1])
#%%

#%% Повторение шахмат
# Всё-таки надо выполнить полный обход в ширину, а затем уже отбирать

letters = 'abcdefgh'
numbers = '12345678'
graph = dict()
for l in letters:
    for n in numbers:
        graph[l+n] = set()

# Сделаем все шаги коня
for i in range(8):
    for j in range(8):
        v1 = letters[i] + numbers[j] # "a4"
        if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
            graph[v1].add(letters[i+2] + numbers[j+1])
        if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
            graph[v1].add(letters[i+1] + numbers[j+2])
        if 0 <= i + 2 < 8 and 0 <= j - 1 < 8:
            graph[v1].add(letters[i+2] + numbers[j-1])
        if 0 <= i + 1 < 8 and 0 <= j - 2 < 8:
            graph[v1].add(letters[i+1] + numbers[j-2])
        if 0 <= i - 1 < 8 and 0 <= j - 2 < 8:
            graph[v1].add(letters[i-1] + numbers[j-2])
        if 0 <= i - 2 < 8 and 0 <= j - 1 < 8:
            graph[v1].add(letters[i-2] + numbers[j-1])
        if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
            graph[v1].add(letters[i-2] + numbers[j+1])
        if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
            graph[v1].add(letters[i-1] + numbers[j+2])

# Теперь начнём обход в ширину
parents = {v: None for v in graph}
distances = {v: None for v in graph}
start_vertex = 'd4'
end_vertex = 'e2'
distances[start_vertex] = 0
queue = deque([start_vertex])
while queue:
    current_vertex = queue.popleft()
    for neighbour in graph[current_vertex]:
        if distances[neighbour] is None:
            distances[neighbour] = distances[current_vertex] + 1
            queue.append(neighbour)
            parents[neighbour] = current_vertex

path = [end_vertex]
parent = parents[end_vertex]
while parent is not None:
    path.append(parent)
    parent = parents[parent]
print(path[::-1])

# Алгоритм:
# 1) Обходим по всем буквам цифрам шахматной фигуры, создавай dict и set в значениях, куда мы будем складывать всевозможные ходы
# 2) добавляем всевозможные ходы
# 3) создаём dict (в случае с цифрами lst) родителей и distance
# 4) по проверке distance понимаем, обходили ли мы этот узел
# 5) path по обратному пути от родителей от end_vertex until start_vertex, который в своё поле родитель имеет None

#%% Алгоритм дейстры - в ширину, но во взвешенном графе. Требования - положительные веса О(n^2)
# В поиске в ширину было O(m+n)
# Поиск кратчайших путей от исходной вершины ко всем остальным в пределах компоненты связности

# 1) Предполагаем, что расстояние до всех бесконечность
# 2) Добавляем в очередь всех тех, у кого расстояние получилось меньше (if distances[neighbour] is None: не используем по ВСЕМ ходим)


# Восставление пути от обратного. если сумма 14, а прошлое ребро 2, то должно быть 12. => выбираем эту вершину
# 3 варианта Дейкстры: с очередью (с приоритетом и без, то  есть чистой и грязной очередью), без очереди

graph = {}
m = int(input("Число рёбер"))
for i in range(m):
    v1, v2, weight = input("Введите первую, вторую, вес:").split()
    if v1 not in graph:
        graph[v1] = {v2: weight}
    else:
        graph[v1][v2] = weight

start_vertex = "A"
path = {} # словарь кратчайших путей
path[start_vertex] = 0
queue = deque([start_vertex])
while queue:
    current_vertex = queue.popleft()
    for neighbour in graph[current_vertex]:   # {A: {B:3, C:2}, B: ..}
        if neighbour not in path or graph[current_vertex] + graph[current_vertex][neighbour] < path[neighbour]:
            path[neighbour] = graph[current_vertex] + graph[current_vertex][neighbour]
            queue.append(neighbour)

5#%% Алгоритм Дейкстры (норм)
# v2 and v3 are both related to the v1
# Составим граф вида {v1:{v2:cost, v3:cost}, v2:{v4:cost}}
from collections import deque
graph = {}
parents = {} # {v2: v1}
cost = {}
m = int(input("Число рёбер"))
for i in range(m):
    v1, v2, weight = input("Введите первую, вторую, вес:").split()
    if v1 not in graph:
        graph[v1] = {v2: float(weight)}
    else:
        graph[v1][v2] = float(weight)
    parents[v2] = v1

# Добавим в cost начальные поля
start, finish = input("Напиши через пробел букву СТАРТА и ФИНИША").split() #B D
# добавим в начальный список стоимость прямых соседей старта
cost[start] = 0

queue = deque([start])
while queue:
    current_vertex = queue.popleft()
    if current_vertex not in graph: # если конечная точка без ребёр из неё
        break
    for neighbour in graph[current_vertex]:
        if neighbour not in cost or cost[current_vertex] + graph[current_vertex][neighbour] < cost[neighbour]:
            cost[neighbour] = cost[current_vertex] + graph[current_vertex][neighbour]
            parents[neighbour] = current_vertex
            queue.append(neighbour)# грязная очередь (без приоритетов)

# Теперь восстановим путь
path = [finish]
parent = parents[finish]
while parent != start:
    path.append(parent)
    parent = parents[parent]
path.append(start)
print("Путь составил: ", len(path), "шагов. Стоимостью:", cost[finish])
print("Путь:", *path)






#%% Двоичные деревья
