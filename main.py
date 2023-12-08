import db
import warnings
import NameDB


warnings.filterwarnings("ignore")

connection = db.MongoDB()
name_db = NameDB.namedb.get_name_db()
db = connection.create_db(name_db)
collection = connection.cr_coll(db, NameDB.namedb.get_name_tb())


list1 = list(map(int, input("Введите элементы первого списка через пробел: ").split()))
list2 = list(map(int, input("Введите элементы второго списка через пробел: ").split()))
n1 = len(list1) // 2
n2 = len(list2) // 2


def split_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]

def prin():
    sublists_list1 = split_list(list1, n1)
    sublists_list2 = split_list(list2, n2)
    data = [
        {'sublists_list': sublists_list1},
        {'sublists_list': sublists_list2}
    ]
    connection.ins_data(collection, data)
    connection.exp_to_ex(collection)
    print("Подсписки первого списка: ", sublists_list1)
    print("Подсписки второго списка: ", sublists_list2)
    return


print(prin())
