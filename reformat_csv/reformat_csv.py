# v007.004

import csv

# function to convert CSV data
def convert(file_in, file_out):
    with open(file_in, encoding = 'utf-8-sig', errors = 'ignore', newline = '') as file_in:
        reader = csv.reader(file_in)
        datarows = 0
        emptyrows = 0
        unknown_condition = 0
        headers = {}
        endrow = 'NOTSET' # set below
        with open(file_out, encoding = 'utf-8-sig', mode = 'w', newline = '') as file_out:
            writer = csv.writer(file_out, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
            newheaders = ['cdmnumber', 'value', 'field'] # hard-code headers
            writer.writerow(newheaders)
            for row in reader:
                if datarows == 0: # for header row
                    for cell in row:
                        if cell != '':
                            header = {row.index(cell): cell}
                            headers.update(header)
                        else: # no empty cells allowed in the middle of the headers row!
                            pass
                    datarows += 1
                    endrow = len(headers)
                elif datarows > 0 and row[0] != '': # for data, note that leftmost column must be cdmnumber, every row must have cdmnumber
                    for cell in range(1, endrow): # don't process first column
                        newrow = [] # each cell becomes a new row
                        newrow.append(row[0]) # get cdmnumber
                        newrow.append(row[cell]) # get value / list[index]
                        newrow.append(headers[cell]) # get header / dict[key] header keys must be integers to match using the cell index
                        writer.writerow(newrow)
                    datarows += 1
                elif datarows > 0 and row[0] == '': # for empty rows
                    emptyrows += 1
                    pass
                else:
                    unknown_condition += 1
                    pass
    
    # brief report - might be good to make this a separate func
    print(f"{endrow} header columns in data")
    print(headers) # improve header output
    print(f"{datarows - 1} rows containing data were processed") # don't count header
    if emptyrows == 1:
        print(f"{emptyrows} empty row was skipped")
    elif emptyrows > 1:
        print(f"{emptyrows} empty rows were skipped")
    else:
        pass
    if unknown_condition > 0:
        if unknown_condition == 1:
            print(f"A mysterious unknown condition was met {unknown_condition} time")
        elif emptyrows > 1:
            print(f"A mysterious unknown condition was met {unknown_condition} times")
        else:
            pass
    else:
        pass

file_in = input("Enter filepath for the input CSV file: ")
file_out = input("Enter filepath for an output CSV file to write: ")
convert(file_in, file_out)

# some kind of testing option would be good, testing would be good for input and output:
    # input: 
        # check for empty header columns
        # check for duplicate header columns
    # output:
        # use randint to display a random input row and output rows?
