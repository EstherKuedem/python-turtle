Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> from nltk.tokenize import regexp_toknize
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from nltk.tokenize import regexp_toknize
ImportError: cannot import name 'regexp_toknize' from 'nltk.tokenize' (C:\Users\VISION\AppData\Local\Programs\Python\Python38-32\lib\site-packages\nltk\tokenize\__init__.py)
>>> from nltk.tokenize import regexp_tokenize
>>> sent1 = "I am a mondragon.becai"
>>> sent = "I choose to make the best of my time.I choose to put my education first
SyntaxError: EOL while scanning string literal
>>> 
>>> regexp_tokenize(sent,"[+]")
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    regexp_tokenize(sent,"[+]")
NameError: name 'sent' is not defined
>>> regexp_tokenize(sent,"[]")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    regexp_tokenize(sent,"[]")
NameError: name 'sent' is not defined
>>> 

>>> 


>>> 


>>> 

>>> 


>>> 


>>> 

>>> 


>>> 


>>> 

>>> 
