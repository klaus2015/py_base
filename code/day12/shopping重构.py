dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

class CommodityInfo:
    """
        创建商品信息类
    """
    def __init__(self):
        self.commodity_info = dict_commodity_info


class CommodityManagerController:
    """
        商品管理控制器,负责业务逻辑处理.
    """

    def __init__(self):
        self.list_order = []

    def settlement(self):
        """
            结算
        """
        # self.print_orders()
        total_price = self.calculate_total_price()
        self.paying(total_price)

    def paying(self,total_price):
        """
            支付过程
        :param total_price: 需要支付的价格
        """
        while True:
            money = float(input("总价%d元，请输入金额：" % total_price))
            if money >= total_price:
                print("购买成功，找回：%d元。" % (money - total_price))
                self.list_order.clear()
                break
            else:
                print("金额不足.")

    def calculate_total_price(self):
        """
            计算总价格
        """
        total_price = 0
        for order in self.list_order:
            commodity = dict_commodity_info[order["cid"]]
            total_price += commodity["price"] * order["count"]
        return total_price

    def print_orders(self):
        """
            打印订单
        """
        for order in self.list_order:
            commodity = dict_commodity_info[order["cid"]]
            print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], order["count"]))

    def buying(self):
        """
            购买
        """
        self.print_commodity_info()

        self.create_order()

        print("添加到购物车。")

    def create_order(self):
        """
            创建订单
        """
        cid = self.input_commodity_id()
        count = int(input("请输入购买数量："))
        order = {"cid": cid, "count": count}
        self.list_order.append(order)

    def input_commodity_id(self):
        """
            获取商品订单
        """
        while True:
            cid = int(input("请输入商品编号："))
            if cid in dict_commodity_info:
                break
            else:
                print("该商品不存在")
        return cid

    def print_commodity_info(self):
        """
            打印商品信息
        """
        for key, value in dict_commodity_info.items():
            print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))

class CommodityManagerView:
    """
        商品管理器视图
    """
    def __init__(self):
        self.__manager = CommodityManagerController()


    def __display_menu(self):
        print("1)购买")
        print("2)打印订单")
        print("3)结算")

    def __select_menu(self):
        item = input("请输入：")
        if item == "1":
            self.buy()
        elif item == "2":
            self.out_put()
        elif item == "3":
            self.sett()

    def main(self):
        """
            界面视图入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def buy(self):
        """
            购买
        """
        self.__manager.buying()

    def out_put(self):
        self.__manager.print_orders()


    def sett(self):
        """
            结算
        """
        self.__manager.settlement()

view = CommodityManagerView()
view.main()