#Calculate Average of 5 Marks#
#without looping#

mark1 = float(input("\nMark 1: "))
mark2 = float(input("Mark 2: "))
mark3 = float(input("Mark 3: "))
mark4 = float(input("Mark 4: "))
mark5 = float(input("Mark 5: "))

TotalMark = mark1 + mark2 + mark3 + mark4 + mark5
AverageMark = TotalMark / 5.0

print("\nTotal Mark: ", TotalMark , "\nAverage Mark: ", AverageMark)

if(AverageMark >= 80):
    print("Excellent");
elif (AverageMark > 70 and AverageMark <= 79):
    print("Good");
elif (AverageMark > 50 and AverageMark <= 59):
    print("Pass");
else:
    print("Fail")

