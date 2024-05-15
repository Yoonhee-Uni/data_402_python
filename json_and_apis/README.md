# JSON

### what does it stand for?
-   JSON stands for JavaScript Object Notation
-   JSON is a lightweight format for storing and transporting data
-   JSON is often used when data is sent from a server to a web page
-   JSON is "self-describing" and easy to understand

### What is it used for?

-   Transmitting data between a client and a server in web applications
-   Storing structured data in configuration files
- Logging data
- Data storage in various applications and programming languages

### Why use JSON?

The JSON format is syntactically similar to the code for creating JavaScript objects. Because of this, a JavaScript program can easily convert JSON data into JavaScript objects.

Since the format is text only, JSON data can easily be sent between computers, and used by any programming language.

- JavaScript has a built in function for converting JSON strings into JavaScript objects:

`JSON.parse()`

- JavaScript also has a built in function for converting an object into a JSON string:

`JSON.stringify()`
```
You can receive pure text from a server and use it as a JavaScript object.

You can send a JavaScript object to a server in pure text format.

You can work with data as JavaScript objects, with no complicated parsing and translations.
```

### What is it written in?
- JSON arrays are written inside square brackets. 
Just like in JavaScript, an array can contain objects:

```
"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]
```
### What data types can it store/use?
- Strings
- Numbers (integers and floats)
- Booleans (true or false)
- Arrays (ordered lists of values)
- Objects (unordered collections of key-value pairs)
- null (represents an empty value or absence of value)

```commandline
'{"name":"John", "age":30, "car":null}'

Strings
- {"name":"John"}

Numbers
- {"age":30}

Objects
- {"employee":{"name":"John", "age":30, "city":"New York"}}

Arrays
- {"employees":["John", "Anna", "Peter"]}

null
- {"middlename":null}
```

It defines an object with 3 properties:
- name
- age
- car
- Each property has a value.

If you parse the JSON string with a JavaScript program, you can access the data as an object:
```
let personName = obj.name;
let personAge = obj.age;
```

JSON values cannot be one of the following data types:
- a function
- a date
- undefined

### What is the JSON syntax for:
JSON syntax is derived from JavaScript object notation syntax:

- Data is in name/value pairs
- Data is separated by commas
- Curly braces hold objects
- Square brackets hold arrays

JSON Data - A Name and a Value - JSON names require double quotes.
`"name":"John"`

The JSON format is almost identical to JavaScript objects.
In JSON, keys must be strings, written with double quotes:

```
JSON
{"name":"John"}
```

Objects
- Because JSON syntax is derived from JavaScript object notation, very little extra software is needed to work with JSON within JavaScript.
- With JavaScript you can create an object and assign data to it, like this:
```
person = {name:"John", age:31, city:"New York"};

person.name     # returns John
person["name"]  # returns John
person.name = "Gilbert"     # modified  person name to Gilbert
person["name"] = "Gilbert"  # modified  person name to Gilbert
```

