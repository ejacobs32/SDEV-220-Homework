""" 
Name: M02 Lab - Case Study if, else, and while
By: Enoch E Jacobs

Description: Takes test scores from the user and returns a score. 

Variables: 
    l_name = student last name (string)
    f_name = student first name (string)
    gpa = student grade point average (float)
"""


#start the main loop.
while True:
    #ask for last name, or break if zzz is entered. 
    l_name = input("Please enter the student's last name, or \"ZZZ\" to quit: ")
    if l_name.upper() == "ZZZ": break
    #ask for first name. 
    f_name = input("Please enter the student's first name: ")
    #ask for gpa and check if it is actually a float. 
    try: gpa = float(input("Please enter the student's GPA: "))
    except: 
        print("\nNot a valid input...\n")
        continue

    #display a message based on what the GPA score is.
    if gpa >= 3.5: print(f"\n{f_name} {l_name} has made the Dean's List with a GPA of {gpa}!\n")
    elif gpa >= 3.25: print(f"\n{f_name} {l_name} has made the Honor Roll with a GPA of {gpa}.\n")
    else: print(f"\n{f_name} {l_name} has a GPA of {gpa}.\n")

#program ends with this main loop.