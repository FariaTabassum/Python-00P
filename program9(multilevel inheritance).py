class level1:
    def first(self):
        print('code')


class level2(level1):  # inherit level1
    def second(self):
        print('with')


class level3(level2):  # inherit level2
    super.first()
    super.second()
    def third(self):
        print('harry')


obj = level3()
# obj.first()
# obj.second()
obj.third()
