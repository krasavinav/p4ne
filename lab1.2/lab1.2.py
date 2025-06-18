from cProfile import label

from matplotlib import pyplot
from openpyxl import load_workbook


def getvalue(x):
    return x.value


wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']
years = list(map(getvalue, sheet['A'][1:]))
temp = list(map(getvalue, sheet['C'][1:]))
act = list(map(getvalue, sheet['D'][1:]))

pyplot.plot(years, temp, label="относительная емпература")
pyplot.plot(years, act, label="активность Солнца")

pyplot.xlabel('Годы')
pyplot.ylabel('температура и активность Солнца')
pyplot.legend()

pyplot.show()