#Pandas is a python library used for working with data sets.
#Getting start with python
#Example 1
import pandas
mydataset = {
 'cars': ["BMW", "Volvo", "Ford"],
 'passings': [3, 7, 2]
}
myvar = pandas.DataFrame(mydataset)
print(myvar)
#Example 2
import pandas as pd
mydataset={
    'Fruits':["Litchi","Orange","Mango","Guava"],
    'Price':[100,90,78,98]
}
myvar=pandas.DataFrame(mydataset)
print(myvar)
#checking pandas version(__version__)
import pandas as pd
print(pd.__version__)
