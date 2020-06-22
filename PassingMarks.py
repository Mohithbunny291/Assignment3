# !/passing marks of a subject is 35/


print("Total subjects are 3")

print("Enter 3 subjects markes one after the other\n")

sub1 = int(input("Subject 1 markes:\n"))

if (sub1 <= 100):

	sub2 = int(input("Subject 2 markes:\n"))

	if (sub2 <= 100):

		sub3 = int(input("Subject 3 markes:\n"))

		if (sub3 <= 100):

			print("Sum of Subjects is :" , sub1 + sub2 + sub3)

			if sub1 + sub2 + sub3 == 300:

				print("Student is outstanding")
				exit()

			if sub1 and sub2 and sub3 >= 35:
	
				print("Student is pass")

			else:

				print("Student is fail")