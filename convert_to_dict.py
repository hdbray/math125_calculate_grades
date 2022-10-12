import csv

### function which sorts a list of lists by a particular column, while
### fixing the first row of headers

def alphabetize_list(list_name, column_header):

    headers=list_name[0]

    ### identify the correct index

    index=0

    for i in range(len(headers)):
        if headers[i]==column_header:
            index=i
            break

    ### alphabetize list

    sorted_list=[]

    sorted_list.append(headers)

    names_for_sorting=list_name[1:]

    names_for_sorting.sort(key=lambda a: a[index].lower())

    sorted_list.extend(names_for_sorting)

    return sorted_list

### function which reads a csv file and creates a dictionary

def file_to_dict(file_name,alphabetize_header='',optional_first_header=''):

    file_to_list=[]
    
    # open file and write to a list
    
    with open(file_name) as open_file:
        reader=csv.reader(open_file, quotechar='"')
        for row in reader:
            file_to_list.append(row)

    # identify headers


    ### alphabetize gradescope list
    if alphabetize_header!='':
        file_to_list=alphabetize_list(file_to_list,alphabetize_header)

    
    # convert to dict

    headers=file_to_list[0]
    
    file_to_list_of_dicts=[]
    
    # fair warning, if you open the csv file with excel it will add a weird
    # symbol to the top left entry in the headers. so the optional argument
    # helps with that

    if optional_first_header!='':
        headers[0]=optional_first_header
    
    for i in range(len(file_to_list)):
        file_to_list_of_dicts.append({})
        for j in range(len(headers)):
            file_to_list_of_dicts[i][headers[j]]=file_to_list[i][j]

    return file_to_list_of_dicts[1:] 
            # the list slicing removes the rows of the list which just have
            # headers or other nonsense

def file_to_list(file_name,alphabetize_header='',optional_first_header=''):

    file_to_list=[]
    
    # open file and write to a list
    
    with open(file_name) as open_file:
        reader=csv.reader(open_file, quotechar='"')
        for row in reader:
            file_to_list.append(row)

    if alphabetize_header!='':
        file_to_list=alphabetize_list(file_to_list,alphabetize_header)

    if optional_first_header!='':
        file_to_list[0][0]=optional_first_header

    return file_to_list
    

