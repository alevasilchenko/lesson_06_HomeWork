# -*- coding: utf-8 -*-


# ГИПОТЕЗА
#
# Предположим, что мы занимаемся разработкой компьютерных моделей динамики подземных вод. К этой сфере имеют
# непосредственное отношение и разработка месторождений полезных ископаемых, и проектирование водозаборов, и проблемы,
# связанные с утечкой ядовитых промышленных отходов и многое другое. Кроме того, это имеет самое непосредственное
# отношение к моей нынешней профессии, в которой я специализируюсь, правда, не как разработчик, а в качестве
# пользователя уже разработанного в США пакета прикладных программ.
#
# Итак, допустим, для наших целей был ранее создан класс GroundWaterBaseModel, реализующий базовую модель потока
# подземных вод и находящийся в модуле base_class. Со временем стало очевидным, что имеющихся атрибутов и методов
# в этом классе недостаточно для "полного счастья" разработчика. И мы попросили программиста написать новый класс,
# который, во-первых, ОБЯЗАТЕЛЬНО должен наследоваться от базового класса, и, во-вторых, включить в себя два
# дополнительных атрибута и метод, которые существенно облегчат наши дальнейшие разработки.
#
# Задействованный нами программист, вроде бы, выполнил задание, создав новый класс GroundWaterModelWithOutFlow и
# поместив его в модуль inherited_class, но, с другой стороны, поленился написать для нас подробную документацию,
# сочтя это для себя крайне неинтересным занятием (кстати, Ваш покорный слуга, пишущий эти строки, испытывает огромное
# удовольствие, когда подробно комментирует как свои, пока ещё весьма скромные, наработки, так и чужой код, в котором
# получается разобраться).
#
# Чтобы получить детальное представление о том классе, который мы получили "в наследство" от строптивого программиста,
# мы создадим объект этого класса с параметрами по умолчанию и с помощью методов интроспекции исследуем его. Для этого
# мы написали специальную функцию, в которую передаём созданный объект, и возвращаем словарь с данными об объекте.


import inspect
from inherited_class import GroundWaterModelWithOutFlow
from base_class import GroundWaterBaseModel


def introspection_info(obj):

    introspection_dict = {}  # создаём пустой словарь

    # помещаем в словарь тип переданного объекта
    type_obj = type(obj)
    introspection_dict['type'] = type_obj

    # проверяем, является ли объект наследником базового класса (согласно требованию ТЗ)
    if isinstance(obj, GroundWaterBaseModel):
        introspection_dict['base_class'] = f'наследуется от требуемого класса {GroundWaterBaseModel.__name__}'
    else:
        introspection_dict['base_class'] = '!!! не наследуется от требуемого класса !!!'

    # генерируем списковую сборку со всеми атрибутами объекта и помещаем её в словарь
    all_attributes_obj = [attr for attr in dir(obj)]
    introspection_dict['all_attributes'] = all_attributes_obj

    # на основе предыдущего списка генерируем списковую сборку со всеми системными атрибутами объекта,
    system_attributes_obj = [attr for attr in all_attributes_obj if attr.startswith('__')]
    introspection_dict['system_attributes'] = system_attributes_obj

    # а также списковую сборку со всеми пользовательскими атрибутами объекта
    user_attributes_obj = [attr for attr in all_attributes_obj if not attr.startswith('__')]
    introspection_dict['user_attributes'] = user_attributes_obj

    # на основе предыдущего списка создаём отдельный список, собственно, атрибутов
    only_attributes_obj = [attr for attr in user_attributes_obj if not inspect.ismethod(getattr(obj, attr))]
    introspection_dict['only_attributes'] = only_attributes_obj

    # и "параллельный" список типов пользовательских атрибутов
    type_only_attributes_obj = [type(getattr(obj, attr)) for attr in only_attributes_obj]
    introspection_dict['type_attributes'] = type_only_attributes_obj

    # по аналогии, создаём список пользовательских методов,
    only_methods_obj = [attr for attr in user_attributes_obj if inspect.ismethod(getattr(obj, attr))]
    introspection_dict['only_methods'] = only_methods_obj

    # а также "параллельный" список с их исходным кодом (для наглядности исследования)
    code_only_methods_obj = [inspect.getsource(getattr(obj, attr)) for attr in only_methods_obj]
    introspection_dict['source_methods'] = code_only_methods_obj

    # наконец, получаем информацию о модуле, к которому объект принадлежит
    module_obj = inspect.getmodule(obj)
    introspection_dict['module'] = module_obj

    return introspection_dict


groundwater_model = GroundWaterModelWithOutFlow()  # создаём экземпляр разработанного класса

introspection_result = introspection_info(groundwater_model)  # исследуем его

print(f"\nРЕЗУЛЬТАТЫ ИНТРОСПЕКЦИИ ОБЪЕКТА")
print(f"\nТип объекта: {introspection_result['type']}, {introspection_result['base_class']}")
print(f"\nПолный перечень атрибутов:\n{introspection_result['all_attributes']}")
print(f"\nПеречень системных атрибутов:\n{introspection_result['system_attributes']}")
print(f"\nПеречень пользовательских атрибутов:\n{introspection_result['user_attributes']}")
print(f"\nПеречень собственно атрибутов и их тип:")
for i in range(len(introspection_result['only_attributes'])):
    print(f"{introspection_result['only_attributes'][i]:20}, {introspection_result['type_attributes'][i]}")
print(f"\nПеречень пользовательских методов и их исходный код:\n")
for i in range(len(introspection_result['only_methods'])):
    print(f"{introspection_result['only_methods'][i]}")
    print(f"{introspection_result['source_methods'][i]}")
print(f"Модуль, к которому объект принадлежит: {introspection_result['module']}")
