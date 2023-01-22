class Guy:
    def __init__(self, x, y):
        self.xpos = x
        self.ypos = y
        pass

    def update(self, x):

        self.xpos = self.xpos + x

if __name__ == '__main__':
    guy1 = Guy(1, 2)
    guy2 = Guy(2, 3)

    orig_x2 = guy2.xpos
    orig_x1 = guy1.xpos

    guy1.update(orig_x2)
    print(orig_x1)
    print(guy1.xpos)


