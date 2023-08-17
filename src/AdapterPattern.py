"""
Create time: 2023.08.17
Author: Lns-XueFeng
Goal: To master the common design pattern
"""


# 适配器模式
# 所谓适配器模式是指是一种接口适配技术，它可通过某个类来使用另一个接口与之不兼容的类，运用此模式，两个类的接口都无需改动
# 适配器模式主要应用于希望复用一些现存的类，但是接口又与复用环境要求不一致的情况，比如在需要对早期代码复用一些功能等应用上很有实际价值
class Computer:  # 旧组件
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "the {} computer".format(self.name)

    def execute(self):
        return "executes a program"


class Synthesizer:  # 新组件
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "the {} synthesizer".format(self.name)

    def play(self):
        return "is playing an electronic song"


class Human:  # 新组件
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{} the human".format(self.name)

    def speak(self):
        return "says hello"


# 对于原来的老系统来说，所有动作函数均使用 Obj.execute() 来执行
# 对于调用者来说，新系统的组件 Synthesizer.play() 和 Human.speak() 是不存在的
# 必须像调用 Computer.execute() 一样使用 Synthesizer.execute() 和 Human.execute() 来调用原系统中对象的执行函数
# 在不改变 Synthesizer 和 Human 类的前提下，为了让新组件去适应（兼容）旧系统的情况，我们可以使用适配器模式来解决
class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)


def main():
    objects = [Computer("Asus")]
    synth = Synthesizer("moog")
    objects.append(Adapter(synth, dict(execute=synth.play)))
    human = Human("Bob")
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print("{} {}".format(str(i), i.execute()))
        print("type is {}".format(type(i)))