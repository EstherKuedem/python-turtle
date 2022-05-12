Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import nltk
>>> 
>>> from nltk.stem import PorterStemmer, LancasterStemmer
>>> from nltk.stem import WordNetLemmatizer
>>> wn = WordNetLemmatizer
>>> ps = PorterStemmer
>>> ls = LancasterStemmer
>>> ps.stem"storage"
SyntaxError: invalid syntax
>>>  wn = WordNetLemmatizer
>>> ps = PorterStemmer
>>> ls = LancasterStemmer
SyntaxError: unexpected indent
>>> wn = WordNetLemmatizer()
>>> ps = PorterStemmer()
>>> ls = LancasterStemmer()
>>> ps.stem("storage")
'storag'
>>> ls.stem("storage")
'stor'
>>> wn.lemmatize("storage" ,pos='a')
'storage'
>>> wn.lemmatize("kindly" ,pos='n')
'kindly'
>>> wn.lemmatize("kindly" ,pos='r')
'kindly'
>>> wn.lemmatize("kindly" ,pos='v')
'kindly'
>>> wn.lemmatize("kindly" ,pos='a')
'kindly'
>>> wn.lemmatize("greatness" ,pos='n')
'greatness'
>>> wn.lemmatize("greatness" ,pos='r')
'greatness'
>>> wn.lemmatize("greatness" ,pos='v')
'greatness'
>>>  wn.lemmatize("greatness" ,pos='a')
 
SyntaxError: unexpected indent
>>> wn.lemmatize("greatness" ,pos='a')
'greatness'
>>> wn.lemmatize("doing" ,pos='n')
'doing'
>>> 
