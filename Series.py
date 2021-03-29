#Pandas Series
#A Pandas Series is like a column in a table.
#series is a one-dimensional array holding data of any type
#Create  a simple pandas series from a list
#Example 1
import pandas as pd
a=[2,3,4,5,6]
myvar=pd.Series(a)
print(myvar)
#Example 2
import pandas as pd
a=[1,7,9,10]
myvar=pd.Series(a)
print(myvar)
#Lables
#example 1
import pandas as pd
a=[1,2,3,4,5]
myvar=pd.Series(a)
print(myvar)
#lable
print(myvar[2])
#Create labels
#Example 1
import pandas as pd
a=[1,5,3]
myvar=pd.Series(a,index=["x","y","z"])
print(myvar)
#Example 2
import pandas as pd
a=[1,2,3,4,5]
myvar=pd.Series(a,index=["p","q","r","s","t"])
print(myvar)
#return the value of t
print(myvar["t"])
#Key/values  objects as series
#Example 1
import pandas as pd
calories={"day1":400,"day2":300,"day3":200}
myvar=pd.Series(calories)
print(myvar)
#Example 2
import pandas as pd
Item={"Chicken":4,"sabji":3,"biryani":3,"bread":4}
myvar=pd.Series(Item,index=["sabji","bread"])
print(myvar)
#DataFrames
#Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
#Example 1
import pandas as pd
data={
    "calories":[460,400,340],
    "duration":[50,45,60]
}
myvar=pd.Series(data)
mychar=pd.DataFrame(data)
print(myvar)
print(mychar)


