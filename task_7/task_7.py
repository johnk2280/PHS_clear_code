from abc import ABC, abstractmethod


# 3.1. Сделайте в своём коде три примера наглядных методов-фабрик.
class WidgetFactory(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_data_from_widget_forms(self):
        pass

    @abstractmethod
    def save(self, widget_forms_data):
        pass

    @abstractmethod
    def show_widget(self):
        pass

    @abstractmethod
    def hide_widget(self):
        pass


# 3.2. Если вы когда-нибудь использовали интерфейсы или абстрактные классы,
# напишите несколько примеров их правильного именования
class CompanyDepartmentFactory(ABC):
    pass


class OfficeEquipmentFactory(ABC):
    pass


class WidgetFactory(ABC):
    pass
