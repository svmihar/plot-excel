import pandas as pd 
import matplotlib.pylab as pl 
import numpy as np
import itertools



nama_sheet = [
    'D5 P9 L6', 
    'D5 P9 L8',
    'D5 P9 L10',

    'd6.5 p9 L6',
    'd6.5 p9 L8',
    'd6.5 p9 L10',

    'CL L8 P7.5 D5', 
    'CL L8 P7.5 D6.5', 
    'CL L8 P7.5 D8'
]

# for name in nama_sheet: 

#     print(f'sedang ngeprint {name}')
#     df = pd.read_excel('data.xlsx', sheet_name=name, index=False)

#     # print(df.columns)
#     x = df['Frekuensi (KHz)'].values
#     y = df['Suhu (°C)'].values

#     plt.plot(y,x)
#     plt.xlabel('Suhu')
#     plt.ylabel('Frekuensi')
#     plt.title(name)

#     plt.show() 


# plt.gca().set_color_cycle(['red', 'green', 'blue', 'yellow'])


xls = pd.ExcelFile('data.xlsx')
d51 = pd.read_excel(xls,'D5 P9 L6')
waktu = d51['Waktu'].values
suhu51 = d51['Suhu (°C)'].values

d52 = pd.read_excel(xls,'D5 P9 L8')
Waktu52 = d52['Waktu'].values
suhu52 = d52['Suhu (°C)'].values


d53 = pd.read_excel(xls,'D5 P9 L10')
Waktu53 = d53['Waktu'].values
suhu53 = d53['Suhu (°C)'].values


d651 = pd.read_excel(xls,'d6.5 p9 L6')
Waktu651 = d651['Waktu']
suhu651 = d651['Suhu (°C)'].values

d652 = pd.read_excel(xls,'d6.5 p9 L8')
Waktu652 = d652['Waktu']
suhu652 = d652['Suhu (°C)'].values

d653 = pd.read_excel(xls,'d6.5 p9 L10')
Waktu653 = d653['Waktu']
suhu653 = d653['Suhu (°C)'].values

cl1 = pd.read_excel(xls,'CL L8 P7.5 D5')
Waktucl1 = cl1['Waktu']
suhucl1 = cl1['Suhu (°C)']

cl2 = pd.read_excel(xls,'CL L8 P7.5 D6.5')
Waktucl2 = cl2['Waktu']
suhucl2 = cl2['Suhu (°C)']

cl3 = pd.read_excel(xls,'CL L8 P7.5 D8')
Waktucl3 = cl3['Waktu']
suhucl3 = cl3['Suhu (°C)']

kumpulan = [d51,d52,d53,d651,d652,d653,cl1,cl2,cl3]


mark = itertools.cycle(('b','g','m','c','m','y','k','r'))


cmap = pl.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, 9)]


for i, dat in enumerate(kumpulan[:3]): 
    pl.plot('Waktu', 'Suhu (°C)', data=dat, color=colors[i],label=nama_sheet[i])
pl.legend(loc='upper left')
pl.title('D5')
pl.show()


for i, dat in enumerate(kumpulan[2:5]): 
    pl.plot('Waktu', 'Suhu (°C)', data=dat, color=colors[i], label=nama_sheet[i+3])
pl.legend(loc='upper left')
pl.title('D6.5')
pl.show()


for i, dat in enumerate(kumpulan[5:-1]): 
    pl.plot('Waktu', 'Suhu (°C)', data=dat, color=colors[i], label=nama_sheet[i+6])
pl.legend(loc='upper left')
pl.title('CL')
pl.show()