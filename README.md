# UniAcco
In this implementation, we use the argparse module to handle command-line arguments. The load function reads the CSV file into memory and returns the header and data as separate variables. The other functions perform the specified operations on the data and return the results.

We also added support for additional commands, such as sort and std-dev. The sort function sorts the data by a specified numeric column. The std_dev function calculates the standard deviation of a specified numeric column.

We can run the tool by specifying the CSV file to process and any desired commands as arguments. For example, to count the number of rows in a file named "data.csv", we would run: python csv_tool.py data.csv --count
