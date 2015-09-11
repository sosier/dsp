[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> **Actual Distribution of Children per Household:**

>>![Actual Distribution of Children per Household Chart]
(https://github.com/sosier/dsp/blob/master/img/KIHactualChart.png?raw=true)

>>**Code:**
>>```python
resp = chap01soln.ReadFemResp()
kidsInHouse = resp.numkdhh
kidsInHousePMF = thinkstats2.Pmf(kidsInHouse, "actual")

>>thinkplot.PrePlot(1)
thinkplot.Hist(kidsInHousePMF, align="center", width=0.75)
thinkplot.Config(xlabel="kids in household", ylabel="%", axis=[-0.5, 5.5, 0, 0.5])
```

>> **Actual vs. Observed Distribution of Children per Household:**

>> ![Actual vs. Observed Distribution of Children per Household Chart]
(https://github.com/sosier/dsp/blob/master/img/KIHactual+observedChart.png?raw=true)

>>**Code:**
>>```python
observedKidsInHousePMF = BiasPmf(kidsInHousePMF, "observed")

>>thinkplot.PrePlot(2)
thinkplot.Hist(kidsInHousePMF, align="right", width=0.35)
thinkplot.Hist(observedKidsInHousePMF, align="left", width=0.35)
thinkplot.Config(xlabel="kids in household", ylabel="%", axis=[-0.5, 5.5, 0, 0.5])
```

>>**Means:**

>>Actual | Observed
:---: | :---:
~1.0 kids | ~2.4 kids

>>**Code:**
>>```python
def PMFmean(pmf):
    mean = 0
    for x,p in pmf.Items():
        mean += x*p
        
>>     return mean

>>actualMean = PMFmean(kidsInHousePMF)
observedMean = PMFmean(observedKidsInHousePMF)

>>print("Actual Mean: %s" % str(actualMean))
print("Observed Mean: %s" % str(observedMean))
```

>>_Note:
The way the term "biased" is used in this chapter/exercise is a little misleading, which is why I use "observed" instead. The "biased" approach is a completley valid approach; it just answers a different question._

>>_For example, in this exercise the "actual" question is: **How many children are in the average household?** This includes **all** households, which is why it is important to include those with no children._

>>_The "biased" approach answers the question: **How many siblings does the average child have?** (Note: we would subract 1 from our results so as to not count the respondent as a sibling.) In this case we don't care about households with no children, because you if you're a child in a household with no children, you don't exist._

>>_Ultimatley the difference is in which population we care about (households vs. children). To say one is more valid than the other is incorrect. It just depends on the question of interest._
