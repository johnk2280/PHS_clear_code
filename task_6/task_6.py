add_data() - upload_file_data()  # загрузи данные из файла
read() - get_file_data()  # получи данные из файла
read_context_file() - get_file_data()  # получи данные из файла
get_data() - get_page_data()  # получи данные страницы
check_file_upload() - get_upload_status()  # получи статус загрузки данных (True / False)
get_products_from_file() - get_products(file)  # получить данные товаров из файла
get_uploaded_products_files() - get_files_to_upload()  # получить файлы для загрузки товаров из них
total_quantity_of_goods_row() - get_products_quantity_row()  # получи строку с указнием общего количества товаров
get_total_quantity_of_goods() - get_products_quantity()  # получи общее количество товаров
total_basket_price() - get_price()  # без указания basket, т.к. данный метод используется для экземпляра класса Basket
reduce_the_number_of_products() - reduce_products_quantity()  # уменьши количество товаров
_create_table() - _create_orders_table()  # создай таблицу заказов
