class cell_rect:
    def __init__(self, xmin, xmax, ymin, ymax, labelname):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.labelname = labelname

    def __str__(self):
        return self.xmin, self.xmax, self.ymin, self.ymax, self.labelname