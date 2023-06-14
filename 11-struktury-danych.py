#names_list = []
#names_list.append("Bruno")
#names_list.append("Kacper")

#person = ("Bruno", "Żychowski", 19)
#print(person)

#names_list.sort(reverse=True)

#names_list[0]

#names_list.clear("Bruno")
#print(names_list)

#for name in names_list:
#    print(name)

#print(len(names_list))

#names_set = {"Bruno", "Kacper", "Bruno"}

#names_set.remove("Bruno")
#names_set.remove("Bruno")
#print(names_set)

names_set = set()

names_set.add("Bruno")
names_set.add("Kacper")

name_set2 = {"Mariusz", "Tytus", "Bruno"}

name_set3 = names_set.difference(name_set2)

for name in names_set:
    print(name)