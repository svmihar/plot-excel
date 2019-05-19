import okay
import pandas as pd
import matplotlib.pylab as pl
import numpy as np 

if __name__ == "__main__":
    print("""
    Choose:
    1. many line in 1 figure
    2. one line
    """)
    choice = input("> ")
    print(choice)
    if choice == '1':
        print('you choose 1.')
        print('insert excel filename (don\'t for get the .xlsx in the end)')
        excel = input('> ')
        xls = pd.ExcelFile(excel)
        print(f'there are {len(xls.sheet_names)} sheets')
        print('choose sheet name')
        for i, name in enumerate(xls.sheet_names):
            print(f'{i}. {name}')
        i_sheet_name = int(input('> '))
        sheet_name = xls.sheet_names[i_sheet_name]
        df = pd.read_excel(xls, sheet_name)
        
        kolom = df.columns
        for i, fitur in enumerate(kolom): 
            print(f'{i}. {fitur}')
        print('\nChoose x: ')
        i_x = int(input('> '))

        for i, fitur in enumerate(kolom): 
            print(f'{i}. {fitur}')
        print('\nChoose y:')
        i_y = int(input('> '))


        okay.plot_this(excel=excel,x=kolom[i_x], y=kolom[i_y], sheetname=sheet_name)

