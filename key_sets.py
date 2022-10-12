import csv

## pull max scores from webassign csv file

file_to_list=[]

with open('webassign.csv') as open_file:
    reader=csv.reader(open_file, quotechar='"')
    for row in reader:
        file_to_list.append(row)

## this is how many assignments to drop

quiz_default_num_drops=1
webassign_default_num_drops=2

## this is how many assignments to grade

num_webassign=9


## maximum scores


####### Gradescope Keys ########

num_quiz=5

#### quizzes
quiz_keys=[]
quiz_max_score_keys=[]

base_string='Quiz'

for i in range(num_quiz):
    quiz_keys.append(base_string+' '+str(i+1))
    quiz_max_score_keys.append(base_string+' '+str(i+1)+' - Max Points')


#### exams

midterm1_written_key='Midterm 1'
midterm1_written_max_points_key=midterm1_written_key+' - Max Points'
midterm2_written_key='Midterm 2'
midterm2_written_max_points_key=midterm2_written_key+' - Max Points'
final_written_key='Final'
final_written_max_points_key=final_written_key+' - Max Points'

midterm1_webassign_key='Midterm 1 Part A: Webassign Portion'
midterm1_webassign_max_points=float(file_to_list[6][14])

#midterm2_webassign_key='Midterm 2'
#final_webassign_key='Final'

####### WebAssign Keys ########


webassign_keys=file_to_list[4][5:5+num_webassign]
webassign_max_score_list=file_to_list[6][5:5+num_webassign]

for i in range(len(webassign_max_score_list)):
    webassign_max_score_list[i]= float(webassign_max_score_list[i])


#print(webassign_keys)
#print('')
#print('')
#print(webassign_max_score_keys)



####### Blackboard Keys ########

#copy these from the bb grades file after you have downloaded it

bb_quiz_avg_key='Quiz Average [Total Pts: 100 Score] |3877452'
bb_webassign_key='WebAssign Average [Total Pts: 100 Score] |3877453'
bb_midterm1_webassign_key='Midterm 1 WebAssign Score [Total Pts: 100 Score] |3877454'
bb_midterm1_written_key='Midterm 1 Written Score [Total Pts: 100 Score] |3877455'
bb_midterm1_key='Midterm 1 Score [Total Pts: 100 Score] |3877456'
bb_midterm2_webassign_key='Midterm 2 WebAssign Score [Total Pts: 100 Score] |3877457'
bb_midterm2_written_key='Midterm 2 Written Score [Total Pts: 100 Score] |3877458'
bb_midterm2_key='Midterm 2 Score [Total Pts: 100 Score] |3877459'
bb_final_webassign_key='Final WebAssign Score [Total Pts: 100 Score] |3877460'
bb_final_written_key='Final Written Score [Total Pts: 100 Score] |3877461'
bb_final_key='Final Exam Score [Total Pts: 100 Score] |3877463'
bb_overall_course_grade_key='Overall Numerical Average [Total Pts: 100 Score] |3877464'
bb_letter_grade_key='Overall Letter Grade [Total Pts: 100 Score] |3877465'

