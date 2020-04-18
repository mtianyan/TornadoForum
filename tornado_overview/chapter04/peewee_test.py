from peewee import ModelUpdate
from chapter04.models.model import Supplier, Goods
from chapter04.data import supplier_list, goods_list


def save_model():
    for data in supplier_list:
        supplier = Supplier()
        supplier.name = data["name"]
        supplier.address = data["address"]
        supplier.phone = data["phone"]

        supplier.save()

    for data in goods_list:
        good = Goods(**data)
        good.save()


def query_model():
    # 获取某一条数据
    # good = Goods.get(Goods.id==1)
    good = Goods.get_by_id(2)
    good = Goods[2]

    # select 返回的是modelselect对象
    # 获取所有数据
    # select price from goods
    goods = Goods.select(Goods.name, Goods.price)
    for good in goods:
        print(good.price)
    print("*"*30)
    # select * from goods where price > 100
    goods = Goods.select().where(Goods.price > 100)
    for good in goods:
        print(good.price)
    print("*"*30)
    # select * from goods where price>100 and click_num>200 &
    # select * from goods where price>100 or click_num>200 |
    goods = Goods.select().where((Goods.price > 100) | (Goods.click_num > 200))
    for good in goods:
        print(good.price)
    print("*"*30)
    # select * from goods where name like "%飞天"
    goods = Goods.select().where(Goods.name.contains("飞天"))
    for good in goods:
        print(good.name)
    print("*"*30)
    goods = Goods.select().where(Goods.id << [2, 3]) # 等价 goods = Goods.select().where((Goods.id == 1) | (Goods.id == 3))
    for good in goods:
        print(good.id, good.name)
    print("*"*30)
    goods = Goods.select().where((Goods.id == 1) | (Goods.id == 3))
    for good in goods:
        print(good.name)
    print("*"*30)
    goods = Goods.select().where((Goods.id.in_([1, 3])))
    for good in goods:
        print(good.id, good.name)
    print("*" * 30)
    # select * from goods where price>click_num
    goods = Goods.select().where(Goods.price > Goods.click_num)
    for good in goods:
        print(good.id, good.name, good.price, good.click_num)
    print("*" * 30)
    # 排序 select * from goods order by price desc
    goods = Goods.select().order_by(Goods.price.asc())
    for good in goods:
        print(good.id, good.name, good.price, good.click_num)
    print("*" * 30)
    goods = Goods.select().order_by(-Goods.price)
    for good in goods:
        print(good.id, good.name, good.price, good.click_num)
    print("*" * 30)
    # 分页
    goods = Goods.select().order_by(Goods.price).paginate(2, 2)
    print("分页")
    for good in goods:
        print(good.price)


def update_model():
    try:
        good = Goods.get_by_id(2)
        good.click_num += 1
        good.save()
        good.delete_instance()
    except Goods.DoesNotExist:
        pass
    # delete from goods where price>150
    Goods.delete().where(Goods.price > 150).execute()

    # update click_num=100 where id =1
    # Goods.update(click_num=Goods.click_num+1).where(Goods.id==1).execute()


if __name__ == "__main__":
    # save_model()
    # query_model()
    update_model()
