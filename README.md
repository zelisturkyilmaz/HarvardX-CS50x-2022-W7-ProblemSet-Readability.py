# CS50's Introduction to Computer Science
## HarvardX - CS50x
### Week 7 Problem Set - Readability.py
<hr>


### Assignment and Requirements:
Write and execute the program that prompts the user for a text and determines its reading level using ```Coleman-Liau index```.

For example, if user types in a line of text from Dr. Seuss, the program should behave as follows:

```
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

#### Coleman-Liau index:
```
index = 0.0588 * L - 0.296 * S - 15.8
```

where ```L``` is the average number of letters per 100 words in the text, and ```S``` is the average number of sentences per 100 words in the text.

#### Compiling And Execution:

To run a program we wrote in Python, we’ll only need to run:

```Python
$ python readability.py
```
```python``` is the name of a program called an interpreter, which reads in our source code and translates it to code that our CPU can understand, line by line.
