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

for name in nama_sheet: 

    print(f'sedang ngeprint {name}')
    df = pd.read_excel('data.xlsx', sheet_name=name, index=False)

    # print(df.columns)
    x = df['Frekuensi (KHz)'].values
    y = df['Suhu (°C)'].values

    pl.plot(y,x)
    pl.xlabel('Suhu')
    pl.ylabel('Frekuensi')
    pl.title(name)
    pl.savefig(f'./img/{name}.png')
    pl.show() 


xls = pd.ExcelFile('data.xlsx')
d51 = pd.read_excel(xls,'D5 P9 L6')
d52 = pd.read_excel(xls,'D5 P9 L8')
d53 = pd.read_excel(xls,'D5 P9 L10')
d651 = pd.read_excel(xls,'d6.5 p9 L6')
d652 = pd.read_excel(xls,'d6.5 p9 L8')
d653 = pd.read_excel(xls,'d6.5 p9 L10')
cl1 = pd.read_excel(xls,'CL L8 P7.5 D5')
cl2 = pd.read_excel(xls,'CL L8 P7.5 D6.5')
cl3 = pd.read_excel(xls,'CL L8 P7.5 D8')

kumpulan = [d51,d52,d53,d651,d652,d653,cl1,cl2,cl3]


cmap = pl.get_cmap('gnuplot')
colors = [cmap(i) for i in np.linspace(0, 1, 9)]


for i, dat in enumerate(kumpulan[:3]): 
    pl.plot('Waktu', 'Suhu (°C)', data=dat, color=colors[i],label=nama_sheet[i])
    pl.xlabel('Waktu(S)')
    pl.ylabel('Suhu')
pl.legend(loc='upper left')
pl.title('D5')
pl.savefig('./img/D5.png')
pl.show()


for i, dat in enumerate(kumpulan[2:5]): 
    pl.plot('Waktu', 'Suhu (°C)', data=dat, color=colors[i], label=nama_sheet[i+3])
    pl.xlabel('Waktu(S)')
    pl.ylabel('Suhu')
pl.legend(loc='upper left')
pl.title('D6.5')
pl.savefig('./img/D65.png')
pl.show()


for i, dat in enumerate(kumpulan[5:-1]): 
    pl.plot('Waktu', 'Suhu (°C)', data=dat, color=colors[i], label=nama_sheet[i+6])
    pl.xlabel('Waktu(S)')
    pl.ylabel('Suhu')
pl.legend(loc='upper left')
pl.title('CL')
pl.savefig('./img/CL.png')
pl.show()