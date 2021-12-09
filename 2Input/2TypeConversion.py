birth_year = input('What is your birth year: ')
print(type(birth_year))
age = 2021 - int(birth_year)
print(type(age))
# This will produce error because birth year is string
print(age)

weight = input('What is your weight in KG? ')
pounds = 0.45 * float(weight)
print(type(pounds))
print(type(weight))
print(pounds)


