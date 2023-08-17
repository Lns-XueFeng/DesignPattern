"""
Create time: 2023.08.17
Author: Lns-XueFeng
Goal: To master the common design pattern
"""


# 外观模式
# 外部与一个子系统的通信必须通过一个统一的外观对象进行，为子系统中的一组接口提供一个一致的界面
# 外观模式定义了一个高层接口，这个接口使得这一子系统更加容易使用，外观模式又称为门面模式，它是一种对象结构型模式


# 步骤1：定义子系统，即三个子元件：一个警报器，一个喷水器，一个自动拨打电话的装置
class AlarmSender:
    def run(self, msg):
        return "产生了高温告警: {}".format(msg)


class WaterSprinker:
    def run(self):
        return "洒水降温"


class Dialer:
    def run(self, name, phone):
        return "拨打值班人：{} 电话: {}".format(name, phone)


# 步骤二：定义外观类，封装子系统的操作
class EmergencyFacade:
    def __init__(self):
        self.alarm = AlarmSender()
        self.water = WaterSprinker()
        self.dialer = Dialer()

    def run(self, name, phone, msg):
        data = []
        data.append(self.alarm.run(msg))
        data.append(self.water.run())
        data.append(self.dialer.run(name, phone))
        return data


name = "Bruce"
phone = "210-123456"
msg = "高温告警，请立即处理"
emergency = EmergencyFacade()
resp = emergency.run(name, phone, msg)
print(resp)