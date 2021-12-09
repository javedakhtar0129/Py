'''if an applicant has high income AND good credit,
   Eligible for loan'''
has_high_income = True
has_high_credit = False

if has_high_income and has_high_credit:
    print("Eligible for load")
else:
    print("Not")


if has_high_income or has_high_credit :
    print("Eligible for load")
else:
    print("Not")

# not operator change the value of your variable
if has_high_income and not has_high_credit:
    print("Eligible for load")
else:
    print("Not")



