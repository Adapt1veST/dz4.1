class Xz:
   def __init__(self, data):
    self.data = data
   def __iter__(self):
    for pc in self.data:
     yield pc

int = Xz([1, 2, 3, 4, 5])

for pc in int:
   print(pc)


def ok():    
  prew = cur = 1      
  elements = [0, 1, 1]      
  for t in range(100):            
      oke = prew + cur            
      prew = cur            
      cur = oke            
      elements.append(cur)      
  print(elements)

def speed_test():  
  import time 
  t0 = time.time()  
  ok()  
  t1 = time.time()  
  total = t1 - t0  
  print(total)