class averager(object):
    def __init__(self, npts_average):
        self.data = []
        self.number_of_data_points = 0
        self.npts_average = npts_average

    def add_data(self, datapoint):
        self.data.append(datapoint)
        self.number_of_data_points += 1

        if self.number_of_data_points > self.npts_average:
            self.remove_first_point()

    def remove_first_point(self):
        self.data.pop(0)
        self.number_of_data_points -= 1

    def running_mean(self):
        return sum(self.data) / self.number_of_data_points
