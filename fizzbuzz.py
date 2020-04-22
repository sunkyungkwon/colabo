##fizzbuzz using list comprehension

fbz = ["fizz"*(i%3==0)+"buzz"*(i%5==0)
       if i%3==0 or i%5==0
       else i
       for i in range(1,101)
]

print(fbz)
