# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Both lists and tuples are sequences of items, but lists are mutable, while tuples are immutable (meaning items in lists can be changed or extended whereas item in a tuple can't, e.g. `aList[0]=1` is legeal whereas `aTuple[0]=1` is *__NOT__* legal).

>>Since dictionaries require immutable keys, a tuple can be a key, but a list can't.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Both lists and set are mutable sequences of items, however sets are unique, unordered sequences of items whereas lists can have duplicates and be sorted. For example:
```
aList = [0,0,1,2,3,3,4,5,"a","a","b","b"]
aSet = set(aList)
#aSet returns {0,1,2,3,4,5,"a","b"} (though not necessarily in that order)
```

>>The items in a set are required to be hashable, which makes it quicker to find elements in a set than a list.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` is essentially a shorter way of writing a function for one-time use. It is commonly used in functional programming with functions that accept function(s) as arguments. These commonly include: `map`, `filter`, `reduce`, and `sorted`.

>>For example, used with `sorted` `lambda` provides an easier way to sort complex objects:
```
listOfTuples = [("Apple", "Red", 1.23), ("Banana", "Yellow", 0.90), ("Cantaloupe", "Tan", 5.00)]
listOfTuples = sorted(listOfTuples, key=lambda fruit: fruit[2]) #Sort by price
#Returns [("Banana", "Yellow", 0.90), ("Apple", "Red", 1.23), ("Cantaloupe", "Tan", 5.00)]
```

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE  

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





