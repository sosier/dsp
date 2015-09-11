[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>>**~34%** of US males are between 5'10" and 6'1"

>>**Code:**
```python
mu = 178  # in cm
sigma = 7.7  # in cm
dist = scipy.stats.norm(loc=mu, scale=sigma)

>>def heightToCm(feet, inches):
    inchesPerFoot = 12
    inches += feet * inchesPerFoot
    
>>     cmPerInch = 2.54
    return inches * cmPerInch

>>lowerBound = heightToCm(5, 10)
upperBound = heightToCm(6, 1)

>>def percentInRange(dist, upperBound, lowerBound):
    return dist.cdf(upperBound) - dist.cdf(lowerBound)

>>print(percentInRange(dist, upperBound, lowerBound))
```
