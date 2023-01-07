->Data types in python
#LIST in python
 ->It is a ordered collection of datypes.
 ->Represented by->[]
 ->Lists are used to store multiple items in a single variable.
 ->Lists are one of 4 built-in data types in Python.
 ->They are mutable(changable).
 ->Lists are ordered.
 ->Lists allow duplicate values.
  #Examples
  #printing the list,same data type.
  list = ["apple", "mango", "cherry"]
  print(list)
  #using constructor
  list = list(("apple", "mango", "cherry")) 
  print(list)
  o/p:['apple', 'mango', 'cherry']
  #operations on list  
  #printing the index value
  name="snehith"
  print(name.index("h"))
  o/p:3
  #changing the values
  mylist=[5,67.89,"python","yes",3,5,6]
  mylist[-3]=True
  print("List after updation",mylist)
  o/p:List after updation [5, 67.89, 'python', 'yes', True, 5, 6]
   
  #printing only certain values
  print(mylist[2:4])
  o/p:['python', 'yes']
   
  # Appending element to list
  mylist.append(2)
  print("Appending values to the list",mylist)
  o/p: Appending values to the list [5, 67.89, 'python', 'yes', True, 5, 6, 2]
   
  c=["hi",10,9]
  # Extending the list(adding more than one element to list)
  mylist.extend(c)
  print("extending values of list",mylist)
  o/p:extending values of list [5, 67.89, 'python', 'yes', True, 5, 6, 2, 'hi', 10, 9]
   
  # Inserting values(not in order)
  mylist.insert(7,11)
  print("List after insertion",mylist)
  o/p:List after insertion [5, 67.89, 'python', 'yes', True, 5, 6, 11, 2, 'hi', 10, 9]
   
  # Deleting a certain values by giving it's index
  del mylist[0]
  print("List after deleting the values",mylist)
  o/p: List after deleting the values [67.89, 'python', 'yes', True, 5, 6, 11, 2, 'hi', 10, 9]
   
  # Removing a value directly
  mylist.remove("hi")
  print("List after removing values",mylist)
  o/p:List after removing values [67.89, 'python', 'yes', True, 5, 6, 11, 2, 10, 9]
     
  # deleting entire list
  del mylist
  print(mylist)  
  o/p:   NameError: name 'mylist' is not defined   #list got deleted
  
  
  #TUPLES in python
  ->Tuples are used to store multiple items in a single variable.
  ->Tuple is one of 4 built-in data types in Python.
  ->It is an ordered collection.
  ->They are immutable.
  ->Represented using->()
  ->Tuples allow duplicates since they are indexed.
  #Examples
  #printing the tuple
  mytuple = ("tiger","Lion")
  print(mytuple)
  o/p:('tiger', 'Lion')
   
  #Length of tuple
  print(len(mytuple))
  o/p:2
   
  #When you create a tuple with only 1 item you need to place a , after it otherwise it will not be cosidered as tuple.
  mytuple = ("snehith",)
  print(type(mytuple))
  <class 'tuple'>
  #NOT a tuple
  mytuple = ("snehith")
  print(type(mytuple))
  <class 'str'>

  
  #DICTIONARIES in python
  
