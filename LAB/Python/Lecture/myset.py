#set use {}
#set is modifiable (add,edit,and delete)
# set is unordered(the items does not retain its position)
#set is  not indexed (Do not have 0,1,2,3,4....)
#set does not allo duplicates



x = {10,20,30, 10,40,50, 20, 60,70}
print(x)
#1)Numbers are not in the same order as it was created
#2)duplicate numbers are missing


#selection and indexing
#since set is so indexed you cannot retreive the values using [] SyntaxError
#only way is to use for loop
for i in x:
    print(i)


#modifiable
fruits = {"apple", "orange", "mango"}
print(fruits)
fruits.add("durian") #add at a random place
print(fruits)


#to delete an item in the set
fruits.remove("orange")
print(fruits)
#pop => randomly removes an item in the set
fruits.pop()
print(fruits)

#if you want to update an item
#1) remove the item
#2) add the new item

fruits = ["apple", "orange", "apple", "mango", "banana", "apple"]
uniquefruits = set (fruits)
print(uniquefruits) #print set() you will get unique item but not in order

overseafruits = {"apple", "orange", "mango", "banana", "grapes"}
localfruits = {"durian", "rambutan", "cempedak", "banana", "mangosteen"}
print(overseafruits.union(localfruits))
print(overseafruits.intersection(localfruits))
print(overseafruits.difference(localfruits))
print(localfruits.difference(overseafruits))


favoriteFruits = {"durian", "rambutan", "mangosteen"}
print(favoriteFruits.issubset(localfruits))
print(localfruits.issuperset(favoriteFruits))
print(favoriteFruits.isdisjoint(overseafruits))

# #list, tuple, set ,dictionaries
# print (range(1,10))

# for x in range(1,11):
#     while x != 9:
#         mukt = x*5
#         print(mukt)
#         break

emailcontent = """The Collatz conjecture says that for every n that is a positive integer, a sequence created with the function above will 
eventually fall to the number one. Thus, these numbers are sometimes called hailstone numbers.
This is because hailstones are formed when raindrops get carried upward by updrafts into the colder areas of the atmosphere and freeze. 
They will continue to do so until they get so heavy that they fall to the ground.Like hailstones, sequences created by the Collatz conjecture problem
will often get higher and then lower, but eventually will fall to the ground resulting in the final number in the sequence being 1."""

words = emailcontent.split()
print(len(words))
print(words)

uniquewords = set(words)
print(len(uniquewords))
print(uniquewords)

cleanwords = []
for word in words:
    word = word.replace(",", "")
    word = word.replace(",", "")
    word = word.lower()
    cleanwords.append(word)

uniquewords = set(words)
print(len(cleanwords))
print(cleanwords)
# print(uniquewords)s
print("="*200)

commonwords = {"is", "or", "so", "by", "how", "when", "it", "on", "the", "into", "a", "to ", "is",}

uniquewords = uniquewords.difference(commonwords)
print(uniquewords)
