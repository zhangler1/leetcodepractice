import re
import pandas as pd
data=pd.read_csv("PFI_10-19.csv")
print(data["Awardee"])
demo=[a.strip() for a in open("demo数据",encoding="utf-8")]

df=pd.read_csv("大学排序后名称")
targets=[a.strip(" |\"|\'|\n") for a in df["university"]]

stopwords=[a.strip(" |\"|\'|\n") for a in open("stopwords",encoding="utf-8")]

a=".+?"
print(data.loc[3,"Awardee"])

from 心阳.permute生成全排列  import Solution
for target in targets:
    print(target,"-----------------------")

    b = [a.join( per) for per in Solution().permute(["\\b"+a[0:5] for a in re.split(" |,", target) if (str(a) not in stopwords)])]
    print(b)
    for patern in b:
        for i,text in enumerate(data["Awardee"]):
            if re.search(patern,text):

                data.loc[i,"chanegedname"]=target
                print(re.search(patern,text).group())

data.to_csv("Newdata.csv",decimal="\t")