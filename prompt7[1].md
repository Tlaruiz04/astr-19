```python
import numpy as np
import matplotlib.pyplot as plt
```


```python
x = np.linspace(0, 1, 100)
```


```python
def exp_func(x):
    return np.exp(x)
```


```python
y = exp_func(x)
```

## Plot X vs. Y


```python
plt.plot(x,y)
plt.xlabel('Time [milliseconds]')
plt.ylabel('Awesomeness')
plt.title('Exponential Growth of Awesomeness Over Time')
plt.grid(True)
plt.show()
```


    
![png](output_5_0.png)
    



```python

```
