xx = ['ki']
ff = 'lo'


class ff():
    def __init__(self):
        self.a = 6

    def k(self):
        self.a += 1
        print(self.a)

    def b(self):
        self.a += 2
        print(self.a)

    def __del__(self):
        print('over')


q = ff()
q.k()
