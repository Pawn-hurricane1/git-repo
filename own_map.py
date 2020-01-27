def own_map(func, *lists):
       ans = []
       if len(lists) > 0:
           minimum=len(lists[0])
           #print(lists[0])
           #print(len(lists))
           for i in range (len(lists)):
               if minimum>len(lists[i]):
                   minimum=len(lists[i]);
           print(minimum)
           for i in range(minimum):
              ans.append(func(*[l[i] for l in lists]))
       return ans
def func(*argvs):
    sum=0;
    for i in argvs:
        sum+=i;
    return sum;



