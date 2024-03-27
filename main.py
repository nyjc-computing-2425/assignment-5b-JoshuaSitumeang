# Part 1
    # Type your code below
def read_csv(filename):
    """
    takes in a filename and processes its contents
    
    Parameter
    ----------
    filename: str
      name of a file
    
    Returns
    ---------
    tuple
      tuple in the format (header, data)
    """
    data = []
    with open(filename, 'r') as f:
        header = f.readline().strip()
        for line in f:
            record = line.strip().split(",")
            record[0] = int(record[0])
            record[3] = int(record[3])
            data.append(record)

       #f.close() is called automatically

    return header, data

read_csv('pre-u-enrolment-by-age.csv')


# Part 2
def filter_gender(enrolment_by_age, sex):
    """
    filter data according to enrolment_by_age and sex

    Parameter
    ----------
    filename: str
        name of a file

    Returns
    ---------
    tuple
        tuple in the format [year, age, enrolment_jc]
    """
    # Type your code below
    filtered_data = []
    for rec in enrolment_by_age:
        if rec[2] == sex:
            filtered_data.append([rec[0], rec[1], rec[3]])

    return filtered_data


# Part 3
def sum_by_year(enrolment):
    """
    adds up total enrolment for each year, regardless of age

    Parameter
    ---------
    filename: int
        name of a file

    Returns
    ---------
    tuple
        tuple in the format [year, total_enrolment]
    """
    # Type your code below
    year_list = []
    sum_list = []
    sum = 0
    year_list.append(enrolment_data[0][0])
    for rec in enrolment_data:
        year = rec[0]
        if year not in year_list:
            year_list.append(year)
            sum_list.append(sum)
            sum = 0

        sum += rec[2]

    sum_list.append(sum)

    enrolment_by_year = []
    for i in range(len(year_list)):
        enrolment_by_year.append([year_list[i], sum_list[i]])

    return enrolment_by_year


# Part 4
def write_csv(filename, header, data):
    """
    Convert data to CSV format and return the number of lines written

    Parameter
    ---------
    filename: csv
        name of a file

    Returns
    file 
        file in the csv format
    """
    # Type your code below
    with open(filename, 'w') as f:
        output = f'{rec[0]},{rec[1]}\n'
        f.write(output)

        count += 1



# TESTING
# You can write code below to call the above functions
# and test the output

print(read_csv('pre-u-enrolment-by-age.csv'))