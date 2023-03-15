import argparse
import csv
import statistics

def load('data.csv'):
    with open('data.csv', 'r') as file:
        csv_reader = csv.reader(file)
        header = next(csv_reader)
        data = [row for row in csv_reader]
    return header, data

def count(header, data):
    return len(data)

def mean(header, data, column):
    column_index = header.index(column)
    column_data = [float(row[column_index]) for row in data]
    return statistics.mean(column_data)

def filter_data(header, data, column, value):
    column_index = header.index(column)
    filtered_data = [row for row in data if row[column_index] == value]
    return header, filtered_data

def sort_data(header, data, column):
    column_index = header.index(column)
    sorted_data = sorted(data, key=lambda x: float(x[column_index]))
    return header, sorted_data

def std_dev(header, data, column):
    column_index = header.index(column)
    column_data = [float(row[column_index]) for row in data]
    return statistics.stdev(column_data)

def main():
    parser = argparse.ArgumentParser(description='CSV Tool')
    parser.add_argument('filename', type=str, help='CSV file to process')
    parser.add_argument('--count', action='store_true', help='Count the number of rows')
    parser.add_argument('--mean', type=str, help='Calculate the mean of a numeric column')
    parser.add_argument('--filter', nargs=2, metavar=('column', 'value'), help='Filter rows where a column matches a value')
    parser.add_argument('--sort', type=str, help='Sort rows by a numeric column')
    parser.add_argument('--std-dev', type=str, help='Calculate the standard deviation of a numeric column')

    args = parser.parse_args()

    header, data = load(args.filename)

    if args.count:
        result = count(header, data)
        print(f'Count: {result}')

    if args.mean:
        result = mean(header, data, args.mean)
        print(f'Mean of {args.mean}: {result}')

    if args.filter:
        header, filtered_data = filter_data(header, data, args.filter[0], args.filter[1])
        print(f'Filtered data: {filtered_data}')

    if args.sort:
        header, sorted_data = sort_data(header, data, args.sort)
        print(f'Sorted data: {sorted_data}')

    if args.std_dev:
        result = std_dev(header, data, args.std_dev)
        print(f'Standard deviation of {args.std_dev}: {result}')

if __name__ == '__main__':
    main()
