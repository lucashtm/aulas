# Logical Operators

# and

True and True == True

True and False == False

False and True == False

False and False == False

# or

True or True == True

True or False == True

False or True == True

False or False == False

# not

not False == True

not True == False

# Comparison operators


3 > 7 == False

3 < 7 == True

4 >= 4 == True
4 > 4 or 4 == 4 == True

3 <= 3 == True

5 == 6 == False

5 != 5 == False

# Conditionals

reactor = 4 > 5

jobs = 7

gust_intensity = 10.5
threshold = 100


if reactor and gust_intensity*jobs < threshold:
  print('Jorge')
