my_dict = {'Buonorotti' : 1475, 'Leonardo' : 1452, 'Hamingway' : 1899, 'Victor Hugo' : 1802, 'Dostoevskii' : 1821}
print(my_dict)
print("Date of birth one's guy is :", my_dict['Buonorotti'])
my_dict['Lenin'] = 1870
my_dict['Chaikovskiy'] = 1840
print(my_dict)
del_key = my_dict.pop('Leonardo')
print(my_dict)
print("Existing person's date of birth: ", del_key)

my_set = {'firestarter', "baby's got a temper", 2009, None, False, (True + True), None, "firestarter"}
print(my_set)
my_set.add(1961)
my_set.add('Liam Howlett')
my_set.remove(None)
print(my_set)