# 1. Информативные комментарии
def find_subs(s, subs):
    """Функция поиска подстроки в строке"""

    for i in range(len(s) - len(subs) + 1):
        for j in range(len(subs)):
            if subs[j] != s[i + j]:
                break
            if j == len(subs) - 1:
                return i
    return -1


# 2. Представление намерений
# Протестируем функцию вставки не вызывая изменение размера буффера.
@pytest.mark.parametrize('range_limit, index, item, expected_result', [
    (0, 0, '4', ['4']),
    (10, 3, 117, [0, 1, 2, 117, 3, 4, 5, 6, 7, 8, 9]),
    (11, 10, '16', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, '16', 10]),
    (12, 12, '12', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, '12']),
    (13, 0, None, [None, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]),
    (14, 7, False, [0, 1, 2, 3, 4, 5, 6, False, 7, 8, 9, 10, 11, 12, 13]),
    (15, 15, True, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, True])
])
def test_insert__buffer_not_resized(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert [el for el in a_arr] == expected_result


# Протестируем функцию вставки при этом вызовем изменение размера буфера:
@pytest.mark.parametrize('range_limit, index, item, expected_result', [
    (17, 3, 117, [1, 2, 3, 117] + [i for i in range(4, 17)]),
    (18, 10, '16', [i for i in range(1, 11)] + ['16'] + [i for i in range(11, 18)]),
    (19, 12, '12', [i for i in range(1, 13)] + ['12'] + [i for i in range(13, 19)]),
    (20, 0, None, [None] + [i for i in range(1, 20)]),
    (21, 7, False, [i for i in range(1, 8)] + [False] + [i for i in range(8, 21)]),
    (22, 16, True, [i for i in range(1, 17)] + [True] + [i for i in range(17, 22)]),
    (65, 64, 0.5, [i for i in range(1, 65)] + [0.5])
])
def test_insert__buffer_resized(range_limit, index, item, expected_result):
    a_arr = DynArray()
    for i in range(1, range_limit):
        a_arr.append(i)

    a_arr.insert(index, item)
    assert [el for el in a_arr] == expected_result

    # 3. Прояснение
    # Комментарии расшифровывают код операции, указанной в условии задачи
    if command[0] == "1":  # Добавить строку
        if be_chang == True:
            list_chang = list_chang[-1:]
            list_redo = []
        S_current += command[2:]
        list_chang.append(S_current)
        be_chang = False


# 4. Предупреждения о последствиях
# Не запускайте подбор гиперпараметров по сетке это займет несколько часов!!!

# 5. Усиление
# в качестве key поступают строки! всегда возвращает корректный индекс слота!
class NativeDictionary:
    def hash_fun(self, key):
        if self.size == 0:
            return None
        b = key.encode("utf-8")
        sum_b = 0
        for i in range(len(b)):
            sum_b += b[i]
        return sum_b % self.size

# 6. Комментарии TODO
# TODO: добавить меодели для contracts и orders
# TODO: в следующей версии здесь будет логика подсчета затрат
