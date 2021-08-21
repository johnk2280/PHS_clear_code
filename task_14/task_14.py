# 3. Если вы раньше делали комментарии к коду, найдите 5 мест, где эти комментарии были излишни,
# удалите их и сделайте сам код более наглядным.

# 3.1.
# было:
def matrix_creating(n):
    """
    Функция создания матрицы смежности ненаправленного графа.
    Возвращаемая данной функцией матрица является симметричной относительно диагональной линии,
    идущей от верхнего левого угла к правому нижнему.
    """

    matrix = [[0 if j == i else 1 for j in range(n)] for i in range(n)]
    return matrix


# стало
def get_undirected_graph_adjacency_matrix(rows_number: int) -> list:
    return [[0 if j == i else 1 for j in range(rows_number)] for i in range(rows_number)]


# 3.2.
#  было:
def graph_creating(n):
    """
    Функция создания списка смежности графа.
    Данная функция возвращает словарь множеств начиная с 1.
    Список смежности генерируется по числу вершин (в нашем случае - друзей).
    В качестве ключа принимается номер вершины (друга), в качестве значения - множество смежных вершин (соседей).
    Вместо множества можно использовать список.
    Так как при малом количестве вершин, это не влияет на 'O-большое' (время выполнения алгоритма).
    """

    graph = {i: {j for j in range(1, n + 1) if j != i} for i in range(1, n + 1)}
    return graph


# стало:
def get_graph_adjacency_list(vertex_number: int) -> dict:
    return {
        i: {j for j in range(1, vertex_number + 1) if j != i} for i in range(1, vertex_number + 1)
    }


# 3.3.
# было:
def handshake_counting(obj):
    """
    Функция подсчета рукопожатий каждого друга со всем остальными.
    На вход поступает матрица, либо словарь.
    В функции имеется проверка на список/словарь.
    В зависимости от типа объекта производится подсчет суммы следующи методом:
    а) для словаря (списка смежности) считается количество смежных вершин (соседей);
    б) для матрицы смежности - сумма ребер для каждой вершины.
    """
    total_sum = 0

    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key in obj.keys():
                total_sum += len(obj[key])
        else:
            for el in obj:
                total_sum += sum(el)

    return total_sum // 2


# стало:
def get_handshakes_number(friends: dict) -> int:
    handshakes: int = 0
    if hasattr(friends, '__iter__'):
        if hasattr(friends, 'items'):
            for other_friend in friends.keys():
                handshakes += len(friends.get(other_friend))
        else:
            for other_friend in friends:
                handshakes += sum(other_friend)
    return handshakes // 2


# 3.4.
# было:
class MyDate:
    """Инициализация метода класса"""

    def __init__(self, date):
        self.date = date

    @classmethod
    def set_date(cls):
        """Метод создает из строки формата "dd-mm-yyyy" список со значениями типа int [dd, mm, yyyy].
        Если введены все числа, метод возвращает спиок, в противном случае False.
        """
        try:
            return list(map(int, MyDate(incoming_date).date.split('-')))
        except ValueError:
            return False

    @staticmethod
    def check_date():
        """Метод проверяет дату на валидность. Если дата валидна, возвращает True, в противном случае False."""
        temp_list = MyDate(incoming_date).set_date()
        try:
            if temp_list[1] == 2 and temp_list[0] > 29:
                return False
            elif 1 <= temp_list[0] <= 31 and 1 <= temp_list[1] <= 12 and 0 <= temp_list[2] <= 2099:
                return True
        except:
            return False

    def __str__(self):
        """Метод выводит на печать в нужном нам виде"""
        date_list = MyDate.set_date()
        return f'Date {date_list[0]}.{date_list[1]}.{date_list[2]} is valid' \
            if MyDate.check_date() and MyDate.set_date() else f'Date {incoming_date} is not valid'


# стало:
class MyNewDate:
    def __init__(self, date: str):
        self.date: str = date

    @classmethod
    def set_date(cls) -> dict:
        try:
            date: list = list(map(int, MyDate(incoming_date).date.split('-')))
            return {
                'dd': date[0],
                'mm': date[1],
                'yyyy': date[2]
            }
        except ValueError as e:
            return str(e)

    @staticmethod
    def check_date() -> bool:
        date: dict = MyDate(incoming_date).set_date()
        try:
            if date['mm'] == 2 and date['dd'] > 29:
                return False
            elif 1 <= date['dd'] <= 31 and 1 <= date['mm'] <= 12 and 0 <= date['yyyy'] <= 2099:
                return True
        except:
            return False

    def __str__(self):
        date: dict = MyDate.set_date()
        return f'Date {date["dd"]}.{date["mm"]}.{date["yyyy"]} is valid' \
            if MyDate.check_date() and MyDate.set_date() else f'Date {incoming_date} is not valid'
