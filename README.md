# least_square_fit_circle

```python
x=[  -33.0889,   -32.1011,   -72.4388,  -115.8   ,  -170.532 ,
        -172.55  ,  -257.768 ,  -362.111 ,  -497.552 ,  -656.519 ,
        -814.409 , -1007.85  ]
y=[  -2.12004,   -2.05388,   -4.87116,   -8.18968,  -12.832  ,
        -13.0126 ,  -21.1943 ,  -32.7992 ,  -50.461  ,  -75.1209 ,
       -103.938  , -145.071  ]

xy,R,sigma=lsfc(x,y).findit()
print("center is",xy )
print("radius is " ,R)
print("error is ", sigma)
lsfc(x,y).showit()

```



![alt text](download.png)


