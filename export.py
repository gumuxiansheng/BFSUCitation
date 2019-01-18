import xlwt

wb = xlwt.Workbook(encoding='utf-8', style_compression=0)
ws = wb.add_sheet('export', cell_overwrite_ok=True)

colNames = ['AU', 'TI', 'SO', 'VL', 'IS', 'BP', 'EP', 'DI', 'PD', 'PY', 'AB', 'ZR', 'TC', 'ZB', 'Z8', 'ZS',
            'Z9', 'SN', 'EI', 'UT']
for i in range(0, colNames.__len__()):
    ws.write(0, i, colNames[i])

with open('./data/savedrecsOmega.txt', 'r') as f:
    row_i = 0
    col_j = 0
    item = ''
    shouldAddRow = False
    for row in f:

        if row.startswith('PT'):
            shouldAddRow = True
            continue
        if row.startswith('AU') or row.startswith('TI')\
            or row.startswith('SO') or row.startswith('VL') or row.startswith('IS') or row.startswith('BP')\
                or row.startswith('EP') or row.startswith('DI') or row.startswith('PD') or row.startswith('PY')\
                or row.startswith('AB') or row.startswith('ZR') or row.startswith('TC') or row.startswith('ZB')\
                or row.startswith('Z8') or row.startswith('ZS') or row.startswith('Z9') or row.startswith('SN')\
                or row.startswith('EI') or row.startswith('UT'):
            if item != '':
                ws.write(row_i, col_j, item)
            if shouldAddRow:
                row_i += 1
                shouldAddRow = False
            col_j = colNames.index(row[0:2])
            item = row[3:]
        elif row.startswith('   '):
            item += row[2:]
        elif row.startswith('EF') and item != '':
            ws.write(row_i, col_j, item)

wb.save('./data/savedrecsOmega.xls')
