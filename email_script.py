
def write_email(student_name, course_grade, letter_grade, quiz_avg, webassign_avg, midterm1_webassign, midterm1_written, midterm1):

    course_grade=round(course_grade,2)
    quiz_avg=round(quiz_avg,2)
    webassign_avg=round(webassign_avg,2)
    midterm1_webassign=round(midterm1_webassign,2)
    midterm1_written=round(midterm1_written,2)
    midterm1=round(midterm1,2)

    email_opener='''Dear %s, 

This email is reporting on your current course grade for Math 125. Your
course grade is %s, which corresponds to a letter grade of %s. 
    ''' % (student_name, course_grade, letter_grade)

    email_score_overview='''
Your score is calculated using the following formula, as outlined in the
syllabus, assuming you get the same scores on midterm 2 and the final as
you did for midterm 1:

+ .2 x (WebAssign average = %s)
+ .15 x (quiz average  = %s)
+ .65 x (midterm 1 = %s)

where midterm 1 = .25*(midterm 1 part A: webassign percentage) +
.75*(midterm 1 part B: written percentage) = .25*%s + .75* %s.
    ''' % (webassign_avg, quiz_avg, midterm1, midterm1_webassign,midterm1_written) 

    additional_calculation_remarks='''
These scores are also posted to Blackboard.  You are encouraged to double
check that these averages are correct, and that the final calculation is
correct, and report any concerns or discrepancies to me. Extra credit has
not been incorporated at this stage.  

These scores were calculated with 1 quiz drop and 2 WebAssign drops. These
drops will increase at future progress reports to be proportional
to the agreed upon drops of 5 WebAssign homeworks and 4 quizzes based on
the portion of the semester completed.

Your Midterm 1 written score and feedback are available on Gradescope. 
'''

    additional_support='''
If you wish to improve your grade, there are many resources available to
you. The LAs have added resources on background material such as algebra to
Blackboard under the 'Other Resources' Tab on the left-hand side. Office
hours and the tutoring center are also available to you. The LAs also will
continue to provide model solutions to worksheet problems before major
assessments. 

Your LA Andy says: Good job on making it halfway! Discrete is very unique
type of math, one that you've likely not seen before. It takes time to get
used to thinking in this new way, so don't beat yourself up if you don't
get it right away! Remember that the Professor and us LA's are here
literally only for your benefit. Office hours get boring when students
don't stop by. So good luck, and make sure you use your resources!

Your LA Eileen says: Congrats on making it halfway through the semester!
Discrete math is tricky and it"s okay (and normal) to be confused about the
material. I encourage you all to use that confusion to foster curiosity by
experimenting with practice problems and asking questions. Keep pushing
through until you've made it to the end of finals. You got this!
        '''
    if course_grade<70:
        additional_support+='''
Based on your overall numerical average, it seems you are struggling with
the course. The LAs and I want to support you. We hope you will please come
talk with us about ways you can improve.
        '''

    email_signature='''

Best,

Professor Harry Bray
    '''

    email_body=email_opener+email_score_overview+additional_calculation_remarks+additional_support+ email_signature

    return email_body

