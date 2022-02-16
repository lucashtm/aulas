age = int(input('Type your age: '))
country = input('Type your country: ')

max_age = -1
message_1 = ''
message_2 = ''
if country == 'brazil':
  max_age = 18
  message_1 = 'Vc e menor de idade'
  message_2 = 'Pode lamaber uma loirinha'
elif country == 'usa':
  max_age = 21
  message_1 = 'Youre underaged'
  message_2 = 'You can drink caipirina'

if age < max_age:
  print(message_1)
elif max_age > 0:
  print(message_2)
else:
  print('Invalid country')
