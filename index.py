Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myword=["cat","dog","fish","cow"]
>>> myword.index(cat)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    myword.index(cat)
NameError: name 'cat' is not defined
>>> myword.index("cat")
0
>>> myword.index("dog")
1
>>> myword.index("fish")
2
>>> myword.index("cow")
3
>>> ("my name is {}"). format("Esther")
'my name is Esther'
>>> {0:20,1:10}.clear format
SyntaxError: invalid syntax
>>> {0:20,1:10}. format
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    {0:20,1:10}. format
AttributeError: 'dict' object has no attribute 'format'
>>> {0:20,1:10}.clear format("word","lemma")
SyntaxError: invalid syntax
>>> {0:20,1:10}. format("word","lemma")
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    {0:20,1:10}. format("word","lemma")
AttributeError: 'dict' object has no attribute 'format'
>>> {0:20},{1:10}. format("word","lemma")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    {0:20},{1:10}. format("word","lemma")
AttributeError: 'dict' object has no attribute 'format'
>>>  '{0:20}{1:10}'. format("word","lemma")
 
SyntaxError: unexpected indent
>>> '{0:20}{1:10}'. format("word","lemma")
'word                lemma     '
>>> '{0:20}{1:10}'. format("word","past participle")
'word                past participle'
>>> '{0:20}{1:10}'. format('word','past tense')
'word                past tense'
>>> myword=["buy","bought","wear","wore","sink","sank"]
>>> myword2=["bought","wore","sank"]
>>> myword3=["buy","wear","sink"]
>>> '{0:20}{1:20}.format("word","past tense")
SyntaxError: EOL while scanning string literal
>>> "{0:20}{1:20}".format("myword3","myword3")
'myword3             myword3             '
>>> "{0:20}{1:20}".format("myword3","myword2")
'myword3             myword2             '
>>> 
