import argparse, itertools
import pandas as pd
import matplotlib.pylab as pl
import numpy as np 

parser = argparse.ArgumentParser()
parser.add_argument("excel")
parser.add_argument("sheetname")
parser.add_argument("x")
parser.add_argument("y")

arg = parser.parse_args()

# print(arg.excel, arg.sheetname)

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




if __name__ == "__main__":
    plot_this(arg.excel,x=arg.x, y=arg.y, sheetname=arg.sheetname)