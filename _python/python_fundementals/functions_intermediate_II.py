x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#Update Values in Dictionaries and Lists
x[1][0]= 15
students[0]={"last_name": "Bryant"}
sports_directory["soccer"][0]="Andres"
z[0]["y"]= 30

#Iterate Through a List of Dictionaries
#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value

def iterateDictionary(x):
    for i in x:
        print(f"first_name - {i['first_name']}, last_name - {i['last_name']}")

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 

#Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary

def iterateDictionary2(key, list):
    for i in list:
        print(f"{i[key]}")

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#Iterate Through a Dictionary with List Values
#Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, 
#and then prints the associated values within each key's list

def  printInfo(some_dict):
    keyList = list(some_dict.keys())
    for i in range(len(keyList)):
        print(f"{len(some_dict[keyList[i]])} {str.upper(keyList[i])}")
        for j in range(len(some_dict[keyList[i]])):
            print(f"{some_dict[keyList[i]][j]}")


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)