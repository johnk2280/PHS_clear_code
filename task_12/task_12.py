# Время связывания переменных

# 1. Максимально раннее связывание, во время написания кода.

def get_data():
    a = 0
    b = 0
    # some code
    for i in range(10):
        a += i
        b = a + i

    return b


# 2. Связывание по ссылке
from datetime import date

TODAY = date.today()
# some code
created_at = TODAY


# 3. Связывание во время выполнения программы

def get_user(request):
    # some code
    user = User.objects.get(pk=request.user.pk)
    return user
