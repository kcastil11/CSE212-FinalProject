def intersection(names1, names2):
    """
    Purpose: Use intersection to make a new set.
    Return: New intersected set.
    """
    return names1 & names2

def union(names1, names2):
    """
    Purpose: union to make a new set.
    Return: New unioned set.
    """
    return names1 | names2

def add_names_to_sets(list_of_names1, list_of_names2):
    """
    Purpose: Add all of the names from 
    list 1 into the Apple users set and then add
    all of the names from list 2 into the 
    Samsung users set.


    Return: return a tuple containing both update
    sets.
    """
    apple_set = set()
    samsung_set = set()

    for i in range(len(list_of_names1)):
        usuario = list_of_names1[i]
        apple_set.add(usuario)

    for i in range(len(list_of_names2)):
        usuario = list_of_names2[i]
        samsung_set.add(usuario)

    return (apple_set, samsung_set)

def remove_name_from_sets(value, union_set):
    """
    Purpose: Remove user from list. 
    Return: The updated set.
    """
    union_set.remove(value)
    return union_set


apple_users = ["Roberto Carlos", "Claude Makelele", "Romario Souza", "Ronaldo", "Guti", "Luis Figo", "Iker Casillas", "Sergio Ramos", "Zidane", "Arbeloa", "Beckham"]
samsung_users = ["Roberto Carlos", "Ronaldo", "Cassano", "Maldinni", "Raul", "Fabbio", "Gravessen", "Benzema", "Ozil", "Zidane", "Arbeloa", "Beckham"]
print("=================== Test 1 ===================")
print()
# Result: Since sets are unordered they will show a different result everytime. Make sure the corresponding sets contains the correct users.
phone_user_sets = add_names_to_sets(apple_users, samsung_users) 

print(intersection(phone_user_sets[0], phone_user_sets[1])) # Result: Contain names 'Zidane', 'Beckhams', 'Arbeloa', 'Roberto Carlos', 'Ronaldo'
print()

total_users = union(phone_user_sets[0], phone_user_sets[1])
print(total_users)   # Result: 'Romario Souzas', 'Arbeloa', 'Iker Casillas', 'Roberto Carlos', 'Benzema', 'Sergio Ramos', 'Guti', 'Zidane', 'Beckham', 'Fabbio', 'Gravessen', 'Cassano', 
                        # 'Maldinni', 'Luis Figo', 'Ozil', 'Ronaldo', 'Claude makelele', 'Raul'


print("\n Roberto Carlos now has been using a different kind of phone. Please remove him from the Apple and Samsung platforms.")
name = input("Please enter the name that you would like to remove from the phone users(Apple & Samsung)> ") 
print(remove_name_from_sets(name, total_users)) #  Result: Contain names: 'Romario Souza', 'Arbeloa', 'Iker Casillas', 'Roberto Carlos', 'Benzema', 'Sergio Ramos', 'Guti', 'Zidane',
                                                    # 'Beckham', 'Fabbio', 'Gravessen', 'Cassano', 'Maldinni', 'Luis Figo', 'Ozil', 'Ronaldo', 'Claude makelele', 'Raul' 
                                                
