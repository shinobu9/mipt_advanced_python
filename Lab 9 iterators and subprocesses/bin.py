класс BinTree:
    def __init__(само:
        себя. пуск = Нет
        себя. длина = 0
        себя. последний = Нет

    def __iter__(a):
        проходить

    def insert_into_tree(self, value): # добавление в дерево

        если сам . start is None: # проверка на содержание корневого элемента
            себя. start = Узел(значение)
            себя. длина = 1
        еще:
            себя. ток = сам . начало
            while True: # добавление в узел
                если сам . текущий. value == value: # проверка на равенство
                    ломать
                элиф само . текущий. value > value: # если value < значения в узле, то добавляем элемент влево
                    если сам . текущий. слева == Нет:
                        себя. текущий. left = Узел(значение)
                        ломать
                    еще:
                        себя. ток = сам . текущий. налево
                else: # если значение > значения в узле, то добавляем элемент вправо
                    если сам . текущий. справа == Нет:
                        себя. текущий. right = Узел(значение)
                        ломать
                    еще:
                        себя. ток = сам . текущий. направо
            себя. длина += 1

    def __len__(само:
        вернуть себя. длина

    def __iter__(self): # список для обхода в глубину

        узел = само . начало
        стек = []
        результат = []
        в то время как узел или стек:
            в то время как узел:
                стек. добавить(узел)
                результат. добавить(узел)
                узел = узел. налево

            если стек:
                узел = стек. поп()
                узел = узел. направо
        вернуть итер(результат)

    def __str__(само:
        линии = само . build_tree(само . начало, 0, Ложь, '-')[0]
        возврат '\n' + '\n'. join((строка. rstrip() для строки в строках))

    @статический метрод
    def build_tree(корень, curr_index, индекс=Ложь, разделитель = '-'):

        если корень — Нет:
            возврат [], 0, 0, 0

        линия1 = []
        линия2 = []
        если индекс:
            node_repr = '{}{}{}'. формат(curr_index, разделитель, корень. ценность)
        еще:
            node_repr = str(корень. ценность)

        new_root_width = gap_size = лен(node_repr)

        # левая и правая части и их размеры
        l_box, l_box_width, l_root_start, l_root_end = \
            БинТри. build_tree(корень. слева, 2 * curr_index + 1, индекс, разделитель)
        r_box, r_box_width, r_root_start, r_root_end = \
            БинТри. build_tree(корень. справа, 2 * curr_index + 2, индекс, разделитель)
        если l_box_width > 0:
            l_root = (l_root_start + l_root_end) // 2 + 1
            линия1. добавить(' ' * (l_root + 1))
            линия1. добавить('_' * (l_box_width - l_root))
            строка2. добавить(' ' * l_root + '/')
            строка2. добавить(' ' * (l_box_width - l_root))
            new_root_start = l_box_width + 1
            gap_size += 1
        еще:
            new_root_start = 0

        линия1. добавить(node_repr)
        строка2. добавить(' ' * new_root_width)

        # добавляет пробелы
        если r_box_width > 0:
            r_root = (r_root_start + r_root_end) // 2
            линия1. добавить('_' * r_root)
            линия1. добавить(' ' * (r_box_width - r_root + 1))
            строка2. добавить(' ' * r_root + '\\')
            строка2. добавить(' ' * (r_box_width - r_root))
            gap_size += 1
        new_root_end = new_root_start + new_root_width - 1

        # объеденяет левую и правую часть
        gap = ' ' * gap_size
        new_box = [''. присоединиться(строка 1), ''. соединение(строка2)]
        для i в диапазоне(макс(лен(l_box), лен(r_box))):
            l_line = l_box[i] если i < len(l_box) else ' ' * l_box_width
            r_line = r_box[i] если i < len(r_box) else ' ' * r_box_width
            new_box. добавить(l_line + пробел + r_line)

        возврат new_box, лен(new_box[0]), new_root_start, new_root_end


class Node: # Узел, который содержит информацию о левом и правом потомке + величину, которую кладем

    def __init__(self, value, lft=None, rght=None):
        себя. значение = значение
        себя. левый = lft
        себя. справа = rght

    def get_value(само:
        вернуть себя. ценность

    def get_right(само:
        вернуть себя. направо

    def get_left(само:
        вернуть себя. налево

    def __str__(само:
        возврат str(само . get_value())


дерево = БинТри()

для i в диапазоне(10):
    value = int(вход())
    дерево. insert_into_tree(значение)
печать(дерево)
для i в дереве:
    печать(i)