l = []
def dict1():
    d = {"key1":"value1", "name":"simmi", "surname":"singh", "email":"simmisingh@gmail.com", "ph no.":"9110940835"}
    for i in d.items():
        l.append(i)
    
    result = l
    print(result)
d1 = dict1()