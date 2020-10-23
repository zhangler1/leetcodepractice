import pandas as pd
import re
stopwords=[a.strip("\n") for a in open("stopwords",encoding="utf-8")]
print(stopwords)
uni_name=pd.read_excel("university_name.xlsx")
uni=[a for a in uni_name["university"]]

uni.sort(key=lambda x: len([a for a in re.split(" |,",x) if a not in stopwords]))
print(uni)
print(uni_name)

uni_name["university"]=uni
uni_name.to_csv("大学排序后名称")
