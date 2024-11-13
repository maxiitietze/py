from queue import LifoQueue as Pila 
import random

def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Pila[int]:
   pila = Pila()
   for i in range(cantidad):
      pila.put(random.randint(desde,hasta))
   return pila

def mostrar_pila(pila:Pila[int]):
   pila_aux =Pila()
   while not pila.empty():
      val  = pila.get()
      pila_aux.put(val)
      print(val)
      print("-----")
   while not pila_aux.empty():
      pila.put(pila_aux.get())

def cantidad_elementos(pila:Pila)->int:
   cantidad_elementos = 0
   pila_auxiliar = Pila()
   while not pila.empty():
      cantidad_elementos+=1
      pila_auxiliar.put(pila.get())
   while not pila_auxiliar.empty():
      pila.put(pila_auxiliar.get())
   return pila

def buscar_maximo(pila:Pila[int])->int:
   pila_auxiliar = Pila()
   current_max = pila.get()
   pila_auxiliar.put(current_max)
   while not (pila.empty()):
      elem = pila.get()
      pila_auxiliar.put(elem)
      if(elem>current_max):
         current_max = elem
   while not pila_auxiliar.empty():
      pila.put(pila_auxiliar.get())
   return current_max

def buscar_nota_maxima(p:Pila[tuple[(str,int)]]):
   elemento:tuple[(str,int)] = p.get()
   pila_aux = Pila()
   current_max  = elemento[1]
   pila_aux.put(elemento)
   while not p.empty():
      elem = p.get()
      if(elem[1]>current_max):
         current_max = elem[1]
      pila_aux.put(elem)
   while not pila_aux.empty():
      pila.put(pila_aux.get())
   return current_max

def intercala(p1:Pila,p2:Pila)->Pila:
   pila_aux1 = Pila()
   pila_aux2 = Pila()
   pila_intercalada = Pila()
   while not p1.empty():
      pila_aux1.put(p1.get())
   while not p2.empty():
      pila_aux2.put(p2.get())
   while not pila_aux1.empty():
      pila_intercalada.put(pila_aux1.get())
      pila_intercalada.put(pila_aux2.get())          
   return pila_intercalada


def pertenece(l:list,s:chr)->bool:
   for i in range(len(l)):
      if l[i]==s:
         return True
   return False


def evaluar_expresion(s:str)->float:
   operando = ["0","1","2","3","4","5","6","7","8","9","10"]
   operadores = ["+","-","/","*"]
   p = Pila()
   for i in range(len(s)):
      if pertenece(operando,s[i]):
         p.put(int(s[i]))
      if pertenece(operadores,s[i]):
         n1 = p.get()
         n2 = p.get()
         if(s[i]=="+"):
            p.put(int(n1+n2))
         elif (s[i]=="-"):
            p.put(int(n1-n2))
         elif(s[i]=="/"):
            p.put(int(n1/n2))
         else:
            p.put(int(n1*n2))

   return p.get()

   
   


pila = Pila()
pila2 = Pila()
nros2 = [4,5,6]
nros = [1,2,3]
for elemento in nros:
   pila.put(elemento)

for elementos in nros2:
   pila2.put(elementos)
