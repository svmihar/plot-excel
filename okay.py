import argparse, itertools
import pandas as pd
import matplotlib.pylab as pl
import numpy as np 


def plot_this(excel=None, x=None, y=None,sheetname=None, sty='seaborn'):
    pl.style.use(sty)
    fig, ax = pl.subplots(figsize=(6, 6))

    print(f'you are now searching for page {sheetname} in {excel}')
    xls = pd.ExcelFile(excel)
    df = pd.read_excel(xls,sheetname)
    ax.plot(x,y,data=df)
    ax.set_title(sheetname)
    ax.set_xlabel(x)
    ax.set_ylabel(y)
    ax.legend()
    pl.show()


def multiplot(excel, jumlah_line,x,y, sty='seaborn'):
    pl.style.use(sty)
    print(f'you are now trying to plot {jumlah_line} lines inside one fig')
    jumlah_line = int(jumlah_line)
    
    xls = pd.ExcelFile(excel)
    kumpulan = []
    sn = xls.sheet_names
    for i,name  in enumerate(sn): 
        print(f'{i}. {name}')
    
    print('pilih sheet yang akan di anuin')
    pilihan_sheet = []
    for i in range(jumlah_line):
        pilihan = input(f'sheet{i}> ')
        pilihan_sheet.append(sn[int(pilihan)])

    for i in pilihan_sheet: 
        kumpulan.append(pd.read_excel(xls, i))

    for i, dat in enumerate(kumpulan): 
        pl.plot(x,y,data=dat, label=pilihan_sheet[i])
        pl.xlabel(x)
        pl.ylabel(y)
    pl.legend(loc='best')
    pl.show()
