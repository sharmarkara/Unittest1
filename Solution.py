import pandas as pd
import datetime
import calendar
from datetime import datetime
from collections import OrderedDict


def Solution(d):
  day_number_name= {0:'Mon', 1:'Tue', 2:'Wed', 3:'Thu', 4:'Fri', 5:'Sat',6:'Sun'}
  day_number=list(day_number_name.keys())

  d1={}
  for i in d:
    k = datetime.strptime(i, "%Y-%m-%d").weekday()
    j=day_number[k]
    if j in d1.keys():
      d1[j]=d1[j]+d[i]
    else:
      d1[j]=d[i]
  d1=dict(sorted(d1.items()))
  if len(d1)==7:
      day_value=list(d1.values())
      day_name=list(day_number_name.values())
      return dict(zip(day_name,day_value))
  else:
     day_n=list(d1.keys())
     for i in range(7):
       if i not in day_n:
         d1[i]=(d1[day_n[i-2]]+d1[day_n[i]])//2
         day_n=list(d1.keys())
     d1=dict(sorted(d1.items()))
     day_value=list(d1.values())
     day_name=list(day_number_name.values())
     return dict(zip(day_name,day_value))
       


d={'2020-01-01':4,'2020-01-02':4,'2020-01-03':6,'2020-01-04':8,'2020-01-05':2,'2020-01-06':-6,'2020-01-07':2,'2020-01-08':-2}
D={'2020-01-01':6,'2020-01-04':12,'2020-01-05':14,'2020-01-06':2,'2020-01-07':4}
print(Solution(d))
print(Solution(D))