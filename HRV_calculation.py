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
        self.rounded_sdsd = 0
        self.rounded_sd1 = 0
        self.rounded_sd2 = 0

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

    def sdsd(self):
        pp_array = []
        i = 0
        first_value = 0
        second_value = 0
        while i < len(self.dataset) - 1:
            pp_array.append(int(self.dataset[i + 1]) - int(self.dataset[i]))
            i += 1
        i = 0
        while i < len(pp_array) - 1:
            first_value += float(pp_array[i] ** 2)
            second_value += float(pp_array[i])
            i += 1
        first = first_value / (len(pp_array) - 1)
        second = (second_value / (len(pp_array))) ** 2
        self.rounded_sdsd = round((first - second) ** (1 / 2), 0)
        return int(self.rounded_sdsd)

    def sd1(self):
        self.rounded_sd1 = round(((self.rounded_sdsd ** 2) / 2) ** (1 / 2), 0)
        return int(self.rounded_sd1)

    def sd2(self):
        self.rounded_sd2 = round(((2 * (self.rounded_sdnn ** 2)) - ((self.rounded_sdsd ** 2) / 2)) ** (1 / 2), 0)
        return int(self.rounded_sd2)


test1 = Calculator(test_data1)
mean_PPI1 = test1.mean_ppi()
print(f'mean PPI1 = {mean_PPI1} ms')
mean_HR1 = test1.mean_hr()
print(f'mean HR1 = {mean_HR1} bpm')
SDNN1 = test1.sdnn()
print(f'SDNN1 = {SDNN1} ms')
RMSSD1 = test1.rmssd()
print(f'RMSSD1 = {RMSSD1} ms')
SDSD1 = test1.sdsd()
print(f'SDSD1 = {SDSD1}')
SD1_1 = test1.sd1()
print(f'SD1_1 = {SD1_1}')
SD2_1 = test1.sd2()
print(f'SD2_1 = {SD2_1}')

print('')

test2 = Calculator(test_data2)
mean_PPI2 = test2.mean_ppi()
print(f'mean PPI2 = {mean_PPI2} ms')
mean_HR2 = test2.mean_hr()
print(f'mean HR2 = {mean_HR2} bpm')
SDNN2 = test2.sdnn()
print(f'SDNN2 = {SDNN2} ms')
RMSSD2 = test2.rmssd()
print(f'RMSSD2 = {RMSSD2} ms')
SDSD2 = test2.sdsd()
print(f'SDSD2 = {SDSD2}')
SD1_2 = test2.sd1()
print(f'SD1_1 = {SD1_2}')
SD2_2 = test2.sd2()
print(f'SD2_1 = {SD2_2}')
