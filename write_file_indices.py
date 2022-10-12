import csv 
import convert_to_dict as cd
import key_sets as ks

## write file indices

bb_grades_file='bb_gc.csv'


bb_grades_list=cd.file_to_list(bb_grades_file,'Last Name')

headers=bb_grades_list[0]

for i in range(len(headers)):
    if headers[i]==ks.bb_quiz_avg_key:
        target_quiz_avg_index=i
    elif headers[i]==ks.bb_webassign_key:
        target_webassign_avg_index=i
        # midterm1
    elif headers[i]==ks.bb_midterm1_written_key:
        target_midterm1_written_index=i
    elif headers[i]==ks.bb_midterm1_webassign_key:
        target_midterm1_webassign_index=i
    elif headers[i]==ks.bb_midterm1_key:
        target_midterm1_index=i
        # midterm 2
    elif headers[i]==ks.bb_midterm2_written_key:
        target_midterm2_written_index=i
    elif headers[i]==ks.bb_midterm2_webassign_key:
        target_midterm2_webassign_index=i
    elif headers[i]==ks.bb_midterm2_key:
        target_midterm2_index=i
        # final
    elif headers[i]==ks.bb_final_written_key:
        target_final_written_index=i
    elif headers[i]==ks.bb_final_webassign_key:
        target_final_webassign_index=i
    elif headers[i]==ks.bb_final_key:
        target_final_index=i

    elif headers[i]==ks.bb_overall_course_grade_key:
        target_overall_course_grade_index=i
    elif headers[i]==ks.bb_letter_grade_key:
        target_letter_grade_index=i

