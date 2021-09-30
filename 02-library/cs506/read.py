def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    
    file = open(csv_file_path, 'r')

    matrix = []

    # read each line
    for line in file:
        whole_line = line.split(',') #separate values with commas

        for i in range(len(whole_line)):
            term = whole_line[i]

            if term[0] == '"' and term[-1] == '"':
                whole_line[i] = term[1:-1]
            else:
                whole_line[i] = float(whole_line[i])

        # insert into matrix
        matrix.append(whole_line)

    file.close()

    return matrix
