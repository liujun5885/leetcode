class Menu:
    menu_id = None
    menu_type = ""  # CATEGORY, ENTREE or OPTION
    name = ""
    price = 0.0
    linked_items = []

    def __init__(self, menu_id=None, menu_type=None, name=None, price=None, linked_item_ids=None):
        self.menu_id = menu_id
        self.menu_type = menu_type
        self.name = name
        self.price = price
        self.linked_item_ids = linked_item_ids or []
        self.linked_items = []


class MenuStream:
    def __init__(self):
        self.iter = iter(
            ['4', 'ENTREE', 'Spaghetti', '10.95', '2', '3', '', '1', 'CATEGORY', 'Pasta', '4', '5', '', '2', 'OPTION',
             'Meatballs', '1.00', '', '3', 'OPTION', 'Chicken', '2.00', '', '5', 'ENTREE', 'Lasagna', '12.00', '', '6',
             'ENTREE', 'Caesar Salad', '9.75', '3', ''])

    def next_line(self):
        return next(self.iter, None)


class MenuParser:
    id_vs_menus = {}

    def initiate(self, stream):
        params = []

        line = stream.next_line()
        while line is not None:
            if line != '':
                params.append(line)
            else:
                if params[1] == 'CATEGORY':
                    params_dict = {
                        "menu_id": params[0],
                        "menu_type": params[1],
                        "name": params[2],
                        "price": None,
                        "linked_item_ids": params[3:],
                    }
                else:
                    params_dict = {
                        "menu_id": params[0],
                        "menu_type": params[1],
                        "name": params[2],
                        "price": params[3],
                        "linked_item_ids": params[4:],
                    }
                self.id_vs_menus[params[0]] = Menu(**params_dict)
                params = []

            line = stream.next_line()

        for k, v in self.id_vs_menus.items():
            for i in v.linked_item_ids:
                v.linked_items.append(self.id_vs_menus[i])

        return [i for i in self.id_vs_menus.values()]

    def encode(self, menu_list):
        output = []
        for i in menu_list:
            if i.menu_type == 'CATEGORY':
                output.extend([i.menu_id, i.menu_type, i.name])
            else:
                output.extend([i.menu_id, i.menu_type, i.name, i.price])
            for j in i.linked_items:
                output.append(j.menu_id)

            output.append("")
        return output


if __name__ == '__main__':
    stream = MenuStream()
    print(MenuParser().encode((MenuParser().initiate(stream))))
