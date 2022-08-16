def process_rates():
    import xlwings as xw
    import pandas as pd

    with xw.App() as app:
        wb = xw.books.open(r'datasets/rates_copy.xlsx')

        #set variable for sheet with rates data
        rates_sheet = wb.sheets[0]

        #load rates data into pandas
        rates_df = rates_sheet.range('A1').options(pd.DataFrame,
                                               expand="table").value

        #calculate correlations between rates
        corrs = rates_df.corr()

        #Add report sheet
        report_sheet = wb.sheets.add()

        #insert correlations
        report_sheet.range("A1").value = corrs

        #insert line chart of original data 
        chart = report_sheet.charts.add(left=200, top=10)
        chart.set_source_data(rates_sheet.range('A1').expand())
        chart.chart_type = 'line'
        chart.name = "Exchange Rates"

        #save chart & close workbook
        wb.save("rates_report.xlsx")
        wb.close()


def main():
    process_rates()

if __name__ == '__main__':
    main()