import lsfc

xy,R,sigma=lsfc(x,y).findit()
print("center is",xy )
print("radius is " ,R)
print("error is ", sigma)
lsfc(x,y).showit()