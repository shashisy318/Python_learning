'''WAP find whether a student is failed or pass. 
it requires 40% overall and 33% in each subject. there are 3 subjects'''

sub1 = int(input("Enter marks of first subject : "))
sub2 = int(input("Enter marks of second subject : "))
sub3 = int(input("Enter marks of third subject : "))

Total_marks = sub1+sub2+sub3
total_percentage = (Total_marks/300)*100

if(sub1>=33 and sub2>=33 and sub3>=33 and total_percentage >=40):
    print(f"You are Pass with {total_percentage}%")
else: 
    print(f"You are Fail with {total_percentage}%")