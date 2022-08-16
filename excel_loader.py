import pandas as pd

def dict_to_excel(filename:str, dictonary:dict):
    with pd.ExcelWriter(filename) as excel_file:
        for sheet, data in dictionary.items():
            data.to_excel(excel_file, sheet_name=sheet)

def get_sheet():
    file_name = input("""
Enter the name of the file you would like to read
        """)
    file_name += ".xlsx"
    sheet_name = input("""
Enter the sheet you want to load from the file
        """)
    return pd.read_excel(file_name, sheet_name)

def main():
    print(get_sheet())

if __name__ == '__main__':
    main()