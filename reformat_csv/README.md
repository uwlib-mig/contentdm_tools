# Transform tabular data from format A to format B
Using Python

## Details about this use case
The use case is converting tabular data from one format (FORMAT A) to another (FORMAT B). A spreadsheet will be used to edit metadata values in FORMAT A, which is as follows.

### FORMAT A
- `cdmnumber` is an identifier for the row (no two rows will have the same `cdmnumber` value)
- some rows have values in more columns than others
- some rows in the edited spreadsheet will be blank and need to be skipped over during processing

#### input example
| cdmnumber | Title | Printer | Keyword | Date |
|---|---|---|---|---|
| 001 | The Boat Book | Nautical Printers | Boats | 2022 |
| 001-01 | Page 1 | | | |
| 001-02 | Page 2 | | | |
| | | | | |
| 002 | The Car Book | Automotive Printers | Cars | 2021 |
| 002-01 | Page 1 | | | |
| 002-02 | Page 2 | | | |

### FORMAT B
Edited metadata will be handed off for loading into the collection, and I was provided with a required tabular format for this, which is as follows.

- I assume that the headers are *not* needed but are provided here for ease of understanding.
- I'm including all fields, even those with value ""

#### output example
| cdmnumber | value | field |
|---|---|---|
| 001 | The Boat Book | Title |
| 001 | Nautical Printers | Printer |
| 001 | Boats | Keyword |
| 001 | 2022 | Date |
| 001-01 | Page 1 | Title |
| 001-01 | | Printer |
| 001-01 | | Keyword |
| 001-01 | | Date |
| 001-02 | Page 2 | Title |
| 001-02 | | Printer |
| 001-02 | | Keyword |
| 001-02 | | Date |
| 002 | The Car Book | Title |
| 002 | Automotive Printers | Printer |
| 002 | Cars | Keyword |
| 002 | 2021 | Date |
| 002-01 | Page 1 | Title |
| 002-01 | | Printer |
| 002-01 | | Keyword |
| 002-01 | | Date |
| 002-02 | Page 2 | Title |
| 002-02 | | Printer |
| 002-02 | | Keyword |
| 002-02 | | Date |

## REQUIREMENTS FOR INPUT SPREADSHEETS
1.  Input file must be CSV UTF-8
2.  `cdmnumber`must be the leftmost column
3. header row must not contain duplicates
4.  header row must not contain blank cells between headers


## RESOURCES

### Modules, methods, functions, operations, built-in types, ...
*All links here are for v3.8 docs*

- Built-in functions > [open()](https://docs.python.org/3.8/library/functions.html#open)
- [csv — CSV File Reading and Writing](https://docs.python.org/3.8/library/csv.html#module-csv)
    - csv module > functions > [csv.reader](https://docs.python.org/3.8/library/csv.html#csv.reader)
    - csv module > functions > [csv.writer](https://docs.python.org/3.8/library/csv.html#csv.writer)
      csv.writer > methods > [csvwriter.writerow](https://docs.python.org/3.8/library/csv.html#csv.csvwriter.writerow)
- [More on lists](https://docs.python.org/3.8/tutorial/datastructures.html#more-on-lists) (methods for the list data type)
  - list.index()
  - list.append()
- Operations for dictionaries > [update()](https://docs.python.org/3.8/library/stdtypes.html?highlight=update#dict.update)
- [Sequence types](https://docs.python.org/3.8/library/stdtypes.html?highlight=update#sequence-types-list-tuple-range) [common sequence operations](https://docs.python.org/3.8/library/stdtypes.html?highlight=update#common-sequence-operations) 
  - len(sequence)
  - sequence[index]
- Built-in types > [ranges](https://docs.python.org/3.8/library/stdtypes.html?highlight=range#ranges)

### Tutorials
- Real Python > [Reading and Writing CSV Files in Python](https://realpython.com/python-csv/)
  - Read [Parsing CSV Files With Python’s Built-in CSV Library](https://realpython.com/python-csv/#parsing-csv-files-with-pythons-built-in-csv-library)

### My notes
- All my scratch code and notebook files from work on this are available [here](https://github.com/briesenberg07/notebooks_001/tree/67b8913fa5ea6684ff960e366e26b5abd5e29a5b/202205_csv)
