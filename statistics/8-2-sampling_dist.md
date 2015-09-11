[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> **Sampling Distribution (lamda = 2, n = 10):**

>>![Sampling Distribution at lamda = 2, n = 10 Chart]
(https://github.com/sosier/dsp/blob/master/img/LSamplingDist.png?raw=true)

>>**Code:**
```python
def plotSamplingDist(dist, label=""):
    thinkplot.Cdf(thinkstats2.Cdf(dist), label=label)
    thinkplot.Show(xlabel="Sample Mean", ylabel="CDF")

>>plotSamplingDist(dist, "n=%d" % n)
```

>> **Sampling Statistics:**
- _**Mean Error L :**_ ~0.23
- _**90% Confidence Intreval:**_ ~1.3 - 3.7

>>**Code:**
```python
n = 10
lam = 2

>>def EstimateExpo(lam=2, n=10, iters=1000):
    """Evaluates L and Lm as estimators of the exponential parameter.

>>     n: sample size
    iters: number of iterations
    """
    means = []
    medians = []
    for _ in range(iters):
        xs = np.random.exponential(1.0/lam, n)
        L = 1 / np.mean(xs)
        Lm = math.log(2) / np.median(xs)
        means.append(L)
        medians.append(Lm)

>>     print('rmse L', estimation.RMSE(means, lam))
    print('rmse Lm', estimation.RMSE(medians, lam))
    print('mean error L', estimation.MeanError(means, lam))
    print('mean error Lm', estimation.MeanError(medians, lam))

>>     cdf = thinkstats2.Cdf(means)
    ci = cdf.Percentile(5), cdf.Percentile(95)
    print('confidence interval', ci)
    
>>     return means
    
>>dist = EstimateExpo(lam, n)
```

>> **Experiment Repeated for Various n-sizes - L Mean Error by n-size:**

>>![Mean Error L by n-size Chart]
(https://github.com/sosier/dsp/blob/master/img/stdErrorByN.png?raw=true)

>>**Code:**
```python
ns = [x*10 for x in range(1, 16)]

>>def EstimateMultExpo(ns, lam=2, n_iters=10, iters=1000):
    """Evaluates L and Lm as estimators of the exponential parameter.

>>     ns: list of sample sizes
    iters: number of iterations
    """
    stdErrors = []
    
>>     for n in ns:
        n_stdErrors = []
        
>>         # Iterates a few times for each n as well, 
        # so that the final curve is a little smoother
        for _ in range(n_iters):
            means = []
            medians = []
            for _ in range(iters):
                xs = np.random.exponential(1.0/lam, n)
                L = 1 / np.mean(xs)
                Lm = math.log(2) / np.median(xs)
                means.append(L)
                medians.append(Lm)

>>             n_stdErrors.append(estimation.MeanError(means, lam))

>>         stdErrors.append(np.mean(n_stdErrors))
            
>>     return stdErrors

>>stdErrors = EstimateMultExpo(ns, lam)

>>thinkplot.Plot(ns, stdErrors, label="")
thinkplot.Show(xlabel="n-size", ylabel="Mean Error L")
```
