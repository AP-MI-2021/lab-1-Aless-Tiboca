'''
Returneaza true daca n este prim si false daca nu.
'''
def is_prime(n):
  n = int(n)
  if n <= 2:
    return True
  for i in range(2, int(n/2)):
    if (n % i) == 0:
      return False
  return True    
  
  
'''
Returneaza produsul numerelor din lista lst.
'''
def get_product(lst):
  prod = 1
  for i in lst:
    prod *= i
  return prod
  
'''
Returneaza CMMDC a doua numere x si y folosind primul algoritm.
'''
def get_cmmdc_v1(x, y):
  while y!=0:
   aux = x%y
   x = y
   y = aux
  return x  
  
  
'''
Returneaza CMMDC a doua numere x si y folosind al doilea algoritm.
'''
def get_cmmdc_v2(x, y):
  if x == 0:
    return y
  else:
    return get_cmmdc_v2(y, x % y)  
  
  
def main():
  print("Doriti sa verificati primalitatea unui numar?")
  ras = input("y/n\n")
  if ras == 'y':
    n = input("Dati un numar:")
    int(n)
    if is_prime(n) == True:
      print("Numarul este prim")
    else: 
      print("Numarul nu este prim")
  print("Doriti sa faceti produsul unui sir de numere?")
  ras = input("y/n\n")
  if ras == 'y':
    lst = []
    n = int(input("Dati lungimea sirului:"))
    print("Scrieti numerele:\n")
    for i in range(0,n):
      aux = int(input())
      lst.append(aux)
    print("Produsul numerelor este:", get_product(lst))   
  print("Doriti sa aflati cmmdc a doua numere?")
  ras = input("y/n\n")
  if ras == 'y':
    print("Dati numerele:")
    x = int(input())
    y = int(input())
    print("Cmmdc al celor doua numere este:",get_cmmdc_v1(x, y))
        


if __name__ == '__main__':
  main()
