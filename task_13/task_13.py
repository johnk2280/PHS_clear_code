# 6.1. Работа с массивом без прямой индексации:

# было:
for i in range(len(arr)):
    do_something(arr[i])

# стало:
for el in arr:
    do_something(el)

# 6.2. Работа с массивом без прямой индексации используюя словарь:

# было:
arr = [obj_1, obj_2, obj_3]
# some code
do_something(arr[0])
# some code
do_something(arr[1])
# some code
do_something(arr[2])
# some code

# стало:
widgets = {
    'orders_widget': obj_1,
    'contracts_widget': obj_2,
    'reports_widget': obj_3,
}

# some code
do_something(widgets.get('orders_widget'))
# some code
do_something(widgets.get('contracts_widget'))
# some code
do_something(widgets.get('reports_widget'))
# some code

# 6.2. Работа с массивом без прямой индексации используюя модуль collections:
# было:
arr = [obj_1, obj_2, obj_3]
# some code
do_something(arr[0])
# some code
do_something(arr[1])
# some code
do_something(arr[2])
# some code


# стало:
import collections

incoming_objects = collections.deque(obj_1, obj_2, obj_3)
# some code
do_something(incoming_objects.popleft())
# some code
do_something(incoming_objects.popleft())
# some code
do_something(incoming_objects.popleft())
# some code
