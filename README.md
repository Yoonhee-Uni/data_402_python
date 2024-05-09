# Python Fundamentals
## Learning Objectives
- basic data types in Python
- perform basic mathematical operations on different number types
- build and manipulate string variables
### 1. Variable Declaration
To define a variable we can use the assignment operator.
- `Apple_device = 'Mac pro'`
### 2. Strings
Strings can be declared with with single or double quotes. Multiline strings can be declared using ''' or """
We can use string interpolation by declaring an f-string:

```
teacher = "Luke"
greeting = f"Hello there, {teacher}!"

>>> Hello there, Luke!
```

### 3. Slice Operator
The slice operator is a convenient way to create a subsection of a string. It can take up to three colon separated values [start:stop:step].
```
alphabet = 'abcdefghijklmnopqrstuvwzyz'

alphabet[9] # 'j'

alphabet[9:] # 'jklmnopqrstuvwzyz'

alphabet[9:11] # 'jk' N.B. stop is exclusive

alphabet[:2] # 'ab'

alphabet[9:20:2] # 'jlnprt' takes alternating chars
```
We can take slices of lists, strings and tuples.

### 4. Numbers
Integers, floating point and complex numbers fall under the Python numbers category. They are defined as `int`, `float` and `complex`classes. When working with variables we can use the `type` function to inspect it's data type.
```commandline
num_int = 14

num_float = 17.32

num_complex = 5+3j


type(num_int) # <class 'int'>

type(num_float) # <class 'float'>

type(num_complex) # <class 'complex'>

```

### 5. Booleans
A boolean, `True` or `False`, is defined by the `bool` class. We can create expressions which evaluate or coerce to a boolean. This is particularly helpful for control flow logic and test assertions.

The equality operator `==` checks if two values are the equivalent. The expression will evaluate to either `True` or `False`.

Logic operators allow us to expand on our comparison checks.

`and` - True if both the operands are true.

`or` - True if either of the operands is true.

`not` - True if operand is false.

```commandline
x = True
y = False

x and y # False

x or y # True

not x # False
```
## Collections
### 1. Lists
A `list` is an ordered collections of elements. They are mutable. Each element can be accessed, removed and updated by looking up their index. Lists allow for duplicate members.
```commandline
my_favourite_things = ['raindrops on roses', 'whiskers on kittens', 'bright copper kettles', 'warm woollen mittens']

my_favourite_things[2] # 'bright copper kettles'

len(my_favourite_things) # 4
```
Lists come with some built in methods which allow us to mutate the sequence. For example:

`append` - add new element to the end of the list

`pop` - remove the last element from the list

`sort` - sorts the list alphanumerically.

### 2. Dictionaries
Dictionaries are an **ordered** (as of Python 3.7), **mutable** collection of data stored in `key:value` pairs. Dictionaries allow for quick look up using the assigned key, meaning that all keys must be unique. Keys are free to be of any immutable data type.
```commandline
teacher = {
    'name': 'Luke',
    'age': 25,
    'interests': ['coffee','docker','lamsip']
}

teacher['age'] # 25

teacher['interests'] = ['coffee','docker','lamsip']
```
Dictionaries are compared by value. The following expression `dict_1 == dict_2 `would evaluate to `True` for two different, but identical looking dictionaries.

### 3. Tuples
A Tuple is an ordered collection of items, similar to a List. However, tuples are **immutable** meaning they can not be modified after creation. Tuples are often used in place of lists when we want to protect our data for being over-written. Their collection literal is defined within a set of parentheses `()` with comma separated elements. **Tuple unpacking** allows us to declare variables which match the position of the members within the tuple for easier referencing.

```commandline
my_tuple = (2, 'toupée', 'toucan', ['💊','💊'] )

# tuple unpacking
num, false_hair, bird, two_pills = my_tuple

print(two_pills) # ['💊','💊']
```
Tuples are implicitly returned from functions which return multiple values.

### 4. Sets
Sets are collection of **unique immutable data types.** Sets are **mutable** however are unordered so indexing has no meaning. In order to access an element within a set we must use the built in methods.
```commandline
my_set = {1, 3}

# add an element
my_set.add(2) # {1, 2, 3}

# add multiple elements

my_set.update([2, 3, 4]) # {1, 2, 3, 4}


# discard an element
my_set.discard(4)  # {1, 3, 5, 6}
```

## Control Flow
### 1. Conditional Logic

We can employ `if`...`elif`...`else` statements to specify a block of code to execute depending on whether an expression evaluates or coerces to `True`.
```commandline
paula_chocolate = 4
luke_chocolate = 6

if paula_chocolate > luke_chocolate:
    print('Paula has more chocolate')
elif paula_chocolate < luke_chocolate:
    print('Luke has more chocolate')
else:
    print('Both got same amount')

print('play again?')

# Luke has more chocolate
# play again?
```

## Loop
A Python for loop is utilized to iterate through any `iterable` object, such as a `list`, `string`, or `tuple`.
```commandline

fishes = [
    {'name': 'Dory', 'feed': False},
    {'name': 'Nemo', 'feed': True},
    {'name': 'Gill', 'feed': True},
    {'name': 'Bloat', 'feed': False},
    {'name': 'Peach', 'feed': True},
    {'name': 'Bubbles', 'feed': True},
    {'name': 'deb', 'feed': False}
    ]

for blub in fishes:
    if blub['feed']:
        food(blub)
print('all hungry blub fed!')

```

Iterating over a dictionary allows us to access its keys. We can utilize the built-in methods of dictionaries to modify this behavior.
```commandline
 fish = { 'name': 'Dory',
              'feed': False,
              'Colour':'Blue',
              'age': 2
            }
 
 for key, value in fish.items():
    print(f'key:{key}, value: {value}')
    
# 'key: name, value: Dory'
# 'key: feed, value: False'
# 'key: colour, value: Blue'
# 'key: age, value: 2' 
```

## Functions
Python can be used in different ways. Functional programming is one style where we focus on making small, testable functions. We define functions like this:
```commandline
def hello_new_bee(name):
    return 'Welcome to Data Enginnering ' + name
```
1. `def`: This keyword is used to define a function.
2. `hello_new_bee`: This is the name of the function.
3. `(name):` This is the parameter the function expects to receive when it's called. It represents the name of the person being welcomed.
4. `return`: This keyword is used to specify the value that the function should output.
5. `Welcome to Data Engineering `: This is a string literal that forms the beginning of the greeting message.
6. `+`: This is the concatenation operator, used to join strings together.
7. `name`: This is the parameter received by the function, representing the name of the person being welcomed. It's concatenated with the greeting message.

### Positional Arguments vs Keyword Arguments

When we create functions, we can set up placeholders called parameters. These placeholders are like empty slots where we'll put values when we use the function. The names we give to these placeholders don't really affect how the function works, but it's a good idea to use names that describe what they're for. When we call the function, the order in which we provide values decides which placeholder gets which value. These placeholders are called positional arguments because their position matters. Every positional argument needs to have a value when we call the function, or else the function won't work correctly.

```commandline
def minus(a,b,c):
    return a-b-c

total = minus(100-9-8)  # returns 83
```

We can make functions more flexible by giving them optional arguments. With keyword arguments, we don't have to worry about the order in which we provide them; instead, we assign them to specific names. If we don't provide a value for an optional argument, the function will use a default value that we set. Using keyword arguments can sometimes make the code easier to read and understand compared to just listing all the arguments.
```
def product_name(name = "pen pineapple apple pen"):
    return 'We have good product called: ' + name

product_name('run out of ink pen') # 'We have good product called: run out of ink pen '
product_name() # 'We have good product called: pen pineapple apple pen '
```