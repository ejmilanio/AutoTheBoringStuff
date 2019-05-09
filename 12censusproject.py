###---------------------------------------###
#           Ch. 12 Census Project           #
###---------------------------------------###
"""
Progam will...


    -Read Data from the Excel Spreadsheet.
    -Counts the number of census tracts in each county
    -Counts the total population of each country
    -Prints the results

"""
#! python3

import openpyxl, pprint, os
print('Opening workbook....')

wb = openpyxl.load_workbook('C:\\Users\\ejmil\\AppData\\Local\\Programs\\Python\\Python37-32\\censuspopdata.xlsx')
sheet = wb.get_sheet_by_name('Population by Census Tract')
countyData = {}

# Calculate all the tract and population data and store it in a data structure.
print('Reading rows...')
for row in range(2, sheet.max_row +1):
    # Each row in the spreadsheet has data for one census tract.
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

# Make sure the key for this state exists          
    countyData.setdefault(state, {})
# Make sure the key for this county in this state exitsts.
    countyData[state].setdefault(county, {'tracts': 0, 'pop': 0})

# Each row represents one census tract, so incrememnt by one
    countyData[state][county]['tracts'] += 1
# Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)



# Write the data structure to a text file with the .py extension using the pprint module

print('Writing results...')
resultFile = open('12census2010.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
resultFile.close()
print('Done.')




