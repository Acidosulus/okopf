
def delete_from_string_between_substrings(lc_source: str, lc_from: str, lc_to: str):    # удаляет подстроку из строки ограниченную начальной и конечной подстрокой
    l = lc_source.find(lc_from)
    r = lc_source.find(lc_to)
    if l > -1 and r > -1: return lc_source[:l] + lc_source[r + 1:-1]
    else: return lc_source

def file_to_str(file_path:str):         # считывает текстовый файл в строку
    with open(file_path, "r", encoding="utf-8") as myfile:
        data = ' '.join(myfile.readlines())
    myfile.close()
    return data


def prepare_for_csv_non_list (pc_value):     # подготовка к записи в csv, списки преобразуются к строке с разделителями пробелами
    if type(pc_value) =="<class 'str'>":
        return prepare_str(pc_value)
    else:       #if type(pc_value) == "<class 'list'>"
        lc = ''
        for i in pc_value:
            lc = lc + ' ' + prepare_str(i)
        return lc.strip()
    return pc_value


def prepare_for_csv_list(pc_value):     # подготовка к записи в csv, списки преобразуются в список с разделителями точка с запятой и экранируются кавычками
    if type(pc_value) == "<class 'str'>":
        return prepare_str(pc_value)
    else: #if type(pc_value) == "<class 'list'>"
        lc = ''
        ln_counter = 0
        for i in pc_value:
            ln_counter=ln_counter+1
            if ln_counter != 1: lc_comma = ';'
            else: lc_comma = ''
            lc = lc + lc_comma + prepare_str(i)
        return '"'+lc.strip()+'"'

def prepare_str(pc_value:str):  #удаляет из будущего параметра CSV недопустимые символы
    return pc_value.replace('"','').replace(';',' ').replace('\n',' ').replace('\t',' ')

def sx(source_string='', left_split='', right_split='', index=1):
    # print(source_string + ' '+left_split + ' '+ right_split)
    # print(index)
    # star_position = 0
    # print('')
    # print(source_string.count(left_split))
    if source_string.count(
            left_split) < index:  # если требуется вхождение с большим номером чем имеется в исходной строке
        return ""
    lc_str = source_string
    for i in range(0, index):  # range(1,source_string.count(left_split)):
        lc_str = lc_str[lc_str.find(left_split) + len(left_split):len(lc_str)]
        # print(lc_str)
    # print(lc_str[0:lc_str.find(right_split)])
    return lc_str[0:lc_str.find(right_split)]

# print (   sx('123abc321cba123abc321cba','a','1',1)  )
# print (   sx('123abc321cba123abc321cba','a','c',2)  )
# print (   sx('123abc321cba123abc321cba','a','c',3)  )


# price = Price()
# price.add_good('','name','descr', 'price', 'proc', 'link_on_site', 'link_on_pictures','size','color')
# price.write_to_csv('list.csv')
# print (price.goods)


class Price:
    def __init__(self):
        #print('Инициализация')
        self.good = ['ID товара', 'наименование', 'описание', 'цена', 'орг %', 'ccылка на товар на сайте поставщика',
                     'ссылки на Фото', 'размер']
        self.goods = [self.good]

    def add_good(self, id, name, descr, price, procent, link_on_site, link_on_pictures, size):
        self.goods.append([id, name, descr, price, procent, link_on_site, link_on_pictures, size])

    def write_to_csv(self, file_name):
        file = open(file_name, mode='w', encoding='cp1251')
        for gd in self.goods:
            lc_str = ''
            for col in gd:
                #if col != None:
                #    file.write(col + ';')
                #else:
                #    file.write(';')
                if col != None:
                    lc_str = lc_str + col + ';'
                else:
                    lc_str = lc_str + ';'
            file.write((lc_str+'|').replace(';|', '').replace('|', '') + '\n')
        file.close()




