[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> Simple answer, **yes** the numbers are uniform. As evidence see:

>>**Random PMF:**

>>![Random PMF Chart]
(https://github.com/sosier/dsp/blob/master/img/randomPMF.png?raw=true)

>>**Random CDF:**

>>![Random CDF Chart]
(https://github.com/sosier/dsp/blob/master/img/randomCDF.png?raw=true)

>>**Code:**
```python
def genRandom(n):
    randomList = []
    for i in range(n):
        randomList.append(random.random())
        
>>     return randomList
        
>>randomList = genRandom(1000)
randomPMF = thinkstats2.Pmf(randomList, label="random")

>>thinkplot.PrePlot(1)
thinkplot.Hist(randomPMF, align="center", width=0.001)
thinkplot.Config(xlabel="number", ylabel="%", axis=[0, 1, 0, 0.0011])

>>randomCDF = thinkstats2.Cdf(randomPMF, label="random")

>>thinkplot.PrePlot(1)
thinkplot.Cdf(randomCDF, label="random")
thinkplot.Show(xlabel="number", ylabel="CDF")
```
