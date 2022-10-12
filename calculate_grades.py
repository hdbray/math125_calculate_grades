import csv
import subprocess
from datetime import date
import key_sets as ks
import write_file_indices as wfi
import email_script
import convert_to_letter_grade as lg
import convert_to_dict as cd


### file names 

today=date.today()
date_str=today.strftime('%m_%d_%y')

bb_grades_file='bb_gc.csv'
gs_grades_file='gs.csv'
webassign_grades_file='restructured_webassign.csv'
new_file='graded_files/'+date_str+'_graded_'+bb_grades_file
email_file='email_files/'+date_str+'_email_script.csv'

### list names 

bb_grades_list=[]
gs_grades_list=[]
webassign_grades_list=[]
email_script_list=[['Email','Name','Body']]



## functions

def string_to_float(string):
    if string=='' or string=='NS' or string=='ND':
        return 0
    else:
        return float(string)

def remove_drops(list_name,num_drops):
    for i in range(num_drops):
        list_name.remove(min(list_name))
    return list_name


# this function takes a student dictionary of scores and the designated
# keys of interest and creates a list for the computed average, with a
# conditional for the case of connect

def key_set_to_list(student_entry_dict,key_set):
    #student_entry_dict is a dictionary 
    #key_set is a set of keys that you want to use to form a list of grades
    #for computing their averages

    scores_list=[]

    for key in key_set:
        scores_list.append(string_to_float(student_entry_dict[key]))
    return scores_list

    
def calc_assignment_average(name_pair, student_scores, num_drops, assmt_type, max_points,  extra_credit=0):

    # add extra drops for certain students
#    num_drops+=added_drops(name_pair,assmt_type)

    avg_scores=[]

    # scores list with drops 
    if type(max_points)==list:
        for i in range(len(max_points)):
            avg_scores.append(student_scores[i]/max_points[i])
        percentage=0

    else: 

        for score in student_scores:
            avg_scores.append(score/max_points)


    new_student_scores=remove_drops(avg_scores, num_drops)
    total_score=sum(new_student_scores)+extra_credit
    num_graded_assignments=len(new_student_scores)

    average=total_score/num_graded_assignments

    percentage=100*average

    return percentage

def calc_overall_score(quiz_avg,webassign_avg,midterm1, midterm2,final):

    option1=.15*quiz_avg+.2*webassign_avg+.2*midterm1+.2*midterm2+.25*final

    option2=option1

    return max(option1, option2)


### end functions
### start calculating the grades


### read the files and make lists

def calculate_grades(check_names=True, write_email=False):
    gs_grades_list_of_dicts=cd.file_to_dict(gs_grades_file,'Last Name')
    webassign_grades_list_of_dicts=cd.file_to_dict(webassign_grades_file,'Last Name')
    bb_grades_list=cd.file_to_list(bb_grades_file,'Last Name','Last Name')

    email_list=[['Name', 'Email', 'Body']]

#### now we are calculating the grades for real 

    
    for i in range(0,len(gs_grades_list_of_dicts)):
        gs_student_row_dict=gs_grades_list_of_dicts[i]
        webassign_student_row_dict=webassign_grades_list_of_dicts[i]


        ##the indexing is off because the list of dicts does not include the
        ##headers
        i+=1
    
        first_name=gs_student_row_dict['First Name']
        last_name=gs_student_row_dict['Last Name']
        name_pair=(last_name,first_name)
    
        # for writing the email
        student_name=first_name+' '+last_name
        student_email=gs_student_row_dict['Email']

        # extra credit
    
#        extra_credit_list=key_set_to_list(gs_student_row_dict,ks.extra_credit_keys)
#        total_extra_credit=sum(xc for xc in extra_credit_list)
    
        # quiz grades
    
        quiz_grades_list=key_set_to_list(gs_student_row_dict,ks.quiz_keys)
        quiz_max_score_list=key_set_to_list(gs_student_row_dict,ks.quiz_max_score_keys)
        
        quiz_avg=calc_assignment_average(name_pair, quiz_grades_list, ks.quiz_default_num_drops, 'quiz', quiz_max_score_list)


        # webassign grades
    
        webassign_grades_list=key_set_to_list(webassign_student_row_dict,ks.webassign_keys)
#        webassign_max_grades_list=key_set_to_list(webassign_student_row_dict,ks.webassign_max_score_keys)
        
        webassign_avg=calc_assignment_average(name_pair, webassign_grades_list, ks.webassign_default_num_drops, 'webassign', ks.webassign_max_score_list)

#        webassign_avg=0


        # test grades
    
        midterm1_written=string_to_float(gs_student_row_dict[ks.midterm1_written_key])
        midterm1_written_max_points=string_to_float(gs_student_row_dict[ks.midterm1_written_max_points_key])
        midterm1_written=100*midterm1_written/midterm1_written_max_points

        midterm1_webassign=100*string_to_float(webassign_student_row_dict[ks.midterm1_webassign_key])/(ks.midterm1_webassign_max_points)

        midterm1=.25*midterm1_webassign+.75*midterm1_written

        midterm2_written=midterm1_written
        midterm2_webassign=midterm1_webassign

        final_written=midterm1_written
        final_webassign=midterm1_webassign


        midterm2=.25*midterm2_webassign+.75*midterm2_written
        final=.25*final_webassign+.75*final_written




    
        # overall course grade and letter grade
    
        overall_score=calc_overall_score(quiz_avg, webassign_avg, midterm1, midterm2, final)
    
        letter_grade=lg.calc_letter_grade(overall_score)
    
        # add everything to the bb_grades_list  
    
        bb_grades_list[i][wfi.target_quiz_avg_index]=quiz_avg
        bb_grades_list[i][wfi.target_webassign_avg_index]=webassign_avg
        bb_grades_list[i][wfi.target_midterm1_index]=midterm1
        bb_grades_list[i][wfi.target_midterm1_written_index]=midterm1_written
        bb_grades_list[i][wfi.target_midterm1_webassign_index]=midterm1_webassign
        bb_grades_list[i][wfi.target_midterm2_index]=midterm2
        bb_grades_list[i][wfi.target_midterm2_written_index]=midterm2_written
        bb_grades_list[i][wfi.target_midterm2_webassign_index]=midterm2_webassign
        bb_grades_list[i][wfi.target_final_index]=final
        bb_grades_list[i][wfi.target_final_written_index]=final_written
        bb_grades_list[i][wfi.target_final_webassign_index]=final_webassign

    
        bb_grades_list[i][wfi.target_overall_course_grade_index]=overall_score
        bb_grades_list[i][wfi.target_letter_grade_index]=letter_grade
    
        if write_email==True:
            email_list.append(['','',''])
            email_list[i][0]=student_name
            email_list[i][1]=student_email

            body=email_script.write_email(student_name, overall_score, letter_grade, quiz_avg, webassign_avg, midterm1_webassign, midterm1_written, midterm1)

#
            email_list[i][2]=body
            
    
    
    # now write the updated bb_grades_list to the new_file csv 
    
    with open(new_file, 'w+') as write_file:
        write=csv.writer(write_file)
        write.writerows(bb_grades_list)
    
    # open the new csv with your default program (mine is excel). note that it
    # will not update so you have to close the old one before running the
    # script
    
    subprocess.run(['open', new_file], check=True)
#    
#    ### check that the names match up in the two different files 
#    
    if check_names==True:
        print('''

Checking whether the names match up in the Blackboard and Gradescope files.
Any mismatches will be printed below.

    ''')
        for i in range(len(gs_grades_list_of_dicts)):
            if gs_grades_list_of_dicts[i]['Last Name']!=bb_grades_list[i+1][0]:
                print('GS: '+gs_grades_list_of_dicts[i]['Last Name']+' --- BB: '+bb_grades_list[i+1][0]+' at line '+str(i)) 

        print('')
        print('')

        for i in range(len(gs_grades_list_of_dicts)):
            if gs_grades_list_of_dicts[i]['Last Name']!=webassign_grades_list_of_dicts[i]['Last Name']:
                print('GS: '+gs_grades_list_of_dicts[i]['Last Name']+' --- WebAssign: '+webassign_grades_list_of_dicts[i]['Last Name']+' at line '+str(i)) 

        print('')
        print('')



    if write_email==True:
        with open(email_file, 'w+') as write_file:
            write=csv.writer(write_file)
            write.writerows(email_list)

        subprocess.run(['open', email_file], check=True)
#    

print('')
print('the check names feature is not working')
print('')
print('also the webassign names need to be checked with the other spreadsheets')


#calculate_grades()

# calculate grades and check names
calculate_grades(True)

# just calculate grades, without checking names
#calculate_grades(False)

# calculate grades, check names, and write email
calculate_grades(True,True)



