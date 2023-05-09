test_data1 = [1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000, 1100, 1000,
              1100, 1000, 1100]

test_data2 = [828, 836, 852, 760, 800, 796, 856, 824, 808, 776, 724, 816, 800, 812, 812, 812, 756, 820, 812, 800]


class Calculator:
    def __init__(self, dataset):
        self.dataset = dataset
        self.rounded_ppi = 0
        self.rounded_hr = 0
        self.rounded_sdnn = 0
        self.rounded_rmssd = 0

    def mean_ppi(self):
        sum_ppi = 0
        for i in self.dataset:
            sum_ppi += i
        self.rounded_ppi = round(sum_ppi / len(self.dataset), 0)
        return int(self.rounded_ppi)

    def mean_hr(self):
        self.rounded_hr = round(60 * 1000 / self.rounded_ppi, 0)
        return int(self.rounded_hr)

    def sdnn(self):
        summary = 0
        for i in self.dataset:
            summary += (i - self.rounded_ppi) ** 2
        sdnn = (summary / (len(self.dataset) - 1)) ** (1 / 2)
        self.rounded_sdnn = round(sdnn, 0)
        return int(self.rounded_sdnn)

    def rmssd(self):
        i = 0
        summary = 0
        while i < len(self.dataset) - 1:
            summary += (self.dataset[i + 1] - self.dataset[i]) ** 2
            i += 1
        self.rounded_rmssd = round((summary / (len(self.dataset) - 1)) ** (1 / 2), 0)
        return int(self.rounded_rmssd)


test1 = Calculator(test_data1)
mean_PPI1 = test1.mean_ppi()
print(f'mean PPI1 = {mean_PPI1} ms')
mean_HR1 = test1.mean_hr()
print(f'mean HR1 = {mean_HR1} bpm')
SDNN1 = test1.sdnn()
print(f'SDNN1 = {SDNN1} ms')
RMSSD1 = test1.rmssd()
print(f'RMSSD1 = {RMSSD1} ms')

print('')

test2 = Calculator(test_data2)
mean_PPI2 = test2.mean_ppi()
print(f'mean PPI2 = {mean_PPI2} ms')
mean_HR2 = test2.mean_hr()
print(f'mean HR2 = {mean_HR2} bpm')
SDNN2 = test2.sdnn()
print(f'SDNN2 = {SDNN2} ms')
RMSSD2 = test2.rmssd()
print(f'RMSSD1 = {RMSSD2} ms')
