def calc_letter_grade(y,needs_string_to_float=False):
    if needs_string_to_float==True:
        if y.strip()=='':
            x=0
    x=float(y)
    if x>=97.5:
        return 'A+'
    elif x>=92.5: 
        return 'A'
    elif x>=89.5:
        return 'A-'
    elif x>=87.5:
        return 'B+'
    elif x>=82.5:
        return 'B'
    elif x>=79.5: 
        return 'B-'
    elif x>=77.5:
        return 'C+'
    elif x>=72.5: 
        return 'C'
    elif x>=69.5:
        return 'C-'
    elif x>=59.5:
        return 'D'
    else:
        return 'F'
