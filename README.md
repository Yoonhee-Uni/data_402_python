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