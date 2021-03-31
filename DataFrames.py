#Pandas Dataframes
#Example 1
import pandas as pd
data={
    "calories":[140,78,90],
    "time":[60,40,20]
}
myvar=pd.DataFrame(data)
print(myvar)
#Example 2
import pandas as pd
food={
    "weight":[1,2,3,4],
    "price":[100,233,678,789]
}
df=pd.DataFrame(food)
print(myvar)
#Locate Row -Pandas use the "loc" attribute to return one or more specified row.
print(myvar.loc[1])
print(myvar.loc[[0,1]])
print(df.loc[[0,2]])
#Named indexes
#Example 1
import pandas as pd
books={
    "quantity":[25,67,90],
    "price":[60,78,98]
}
df=pd.DataFrame(books,index=["physics","chemistry","maths"])
print(df)
myvar=pd.DataFrame(data,index=["day1","day2","day3"])
print(myvar)
#Located named indexes
print(df.loc["chemistry"])
print(myvar.loc["day3"])
