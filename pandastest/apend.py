import  pandas as pd

df=pd.DataFrame(data={"a":1,"B":3},index=range(1))
se=pd.Series(data={"a":1,"B":2})
df=df.append(se,ignore_index=True)
print(df)