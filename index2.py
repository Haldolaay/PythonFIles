import PyPDF2  # pdf library
import re  # regular expression library
import csv  # scv file library
import json  # didn't use this in this code - didn't delete becuase I might need to use later
import numpy as np  # this dependince is needed for pandas to work
import pandas as pd  # pd is just to save time
import smartsheet  # smartsheet-python-sdk
# this code will create a panda dataframe from the list we got from csv file
# then it'll call the smartsheet, compare the telphone column with the list we got
# then it'll merge the result in a new column in smartsheet data frame,
# this code will not push anything to smartsheet
# this file can be used without accessing anything from new.py, this file is a standalone file


def write_to_csv(list):  # creating a csv file

    with open('result.csv', 'w', newline='') as f:
        # writer is from csv library - delimiter is for new lines
        writer = csv.writer(f, delimiter='\n')
        writer.writerow(list)


def getting_numbers_out_of_PDF():
    # looks for xxxxxxxxxx or xxx-xxx-xxxx that is prefixed by WTN
    regex = re.compile(r'(?<=WTN) \d{3}-\d{3}-\d{4}|(?<=WTN) \d{10}')
    result = []  # list of all the numbers
    pdfFileObj = open('bill.PDF', 'rb')  # opening a file
    # using the Pypdf2 to read through the file
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # this loop will get all the numebers needed to a result list
    # number of all the pages - will be used for a loop
    numberOfPages = pdfReader.getNumPages()
    text = ""
    for i in range(numberOfPages):
        text += pdfReader.getPage(i).extractText()
    result += re.findall(regex, text)
    pdfFileObj.close()  # getting rid of the pointer
    return result


# function that reads the columns and rows from the smartsheet and populate the datafram, basic nested loop for a 2d array
def simple_sheet_to_dataframe(sheet):
    col_names = [col.title for col in sheet.columns]
    rows = []
    for row in sheet.rows:
        cells = []
        for cell in row.cells:
            cells.append(cell.value)
        rows.append(cells)
    data_frame = pd.DataFrame(rows, columns=col_names)
    return data_frame


def dataFrame_Creation(mylist):

    # trying out pandas:

    access_token = ''  # temp access token for smartsheets
    smartsheet_client = smartsheet.Smartsheet(
        access_token)  # accessing our smartsheet
    phone_call_analysis = simple_sheet_to_dataframe(
        smartsheet_client.Sheets.get_sheet())  # grabing a specific sheet from my account using the sheet number
    newlist = []  # this array is gonna contain the numbers -
    for i in mylist:  # this loop will get rid of spaces
        j = i.replace(' ', '')
        newlist.append(j)
    newFrame = pd.DataFrame(newlist)  # creating a new dataframe
    # creating a new column in the list for testing
    newFrame['phoneList'] = newlist
    outcome = phone_call_analysis.merge(
        newFrame, left_on='Telephone Number_Centrix', right_on='phoneList', how='outer')  # comparing and sorting and creating a new dataframe
    # outer join is to show all the rows even the ones that didn't match
    # left join is to grap everything from the phon_call_anlysis datafram and only the phonlistcolumn from the other dataframe
    # right is the opposite - grabbing everything from the newFrame and only the telephone number_centrix from the phon_call_analysis dataframe
    # inner join only shows the common rows after checking and sorting
    return outcome


# main code:----------------------------------------------------------------
# result will not be used till the end of the program - it is there to grab the initial values - name should be changed later
result = getting_numbers_out_of_PDF()
print(len(result))  # testing
# casting to a dictonary to get rid of duplicates then recasting it to a list
mylist = list(dict.fromkeys(result))

print(len(mylist))  # testing
write_to_csv(mylist)  # calling a write function to write to a scv

outcome = dataFrame_Creation(mylist)  # returning a datafrme
# creating a csv file ( .to_csv is a pandas function)
outcome.to_csv('outcome.csv')
# main code end-------------------------------------------------------------

# with open('result.CSV', 'w')as f:
#     f.write(str(mylist))
