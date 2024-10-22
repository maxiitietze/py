
import random

def divide_a_todos (lista: list,e:int)->bool:
        for i in range (len(lista)):
                if lista[i] % e != 0 :
                    return False
        return True

def suma_total(lista:list)->int:
        suma = 0
        for item in lista:
                suma+=item
        return suma

def maximo (lista:list)->int:
        act_max=lista[0]
        for elem in lista:
                if act_max < elem:
                        act_max=elem
        return act_max

def minimo (lista:list)->int:
       act_min=lista[0]
       for elem in lista:
        if act_min>elem:
                act_min= elem
        return act_min

def ordenados (lista:list)->bool:
        for i in range (len(lista)-1):
                if(lista[i]>lista[i+1]):
                        return False
        return True


def pos_maximo(lista:list)->int:
        act_max = lista[0]
        act_pos = 0
        for i in range (len(lista)):
               if act_max<lista[i]:
                      act_max=lista[i]
                      act_pos=i
        return act_pos


def pos_minimo (lista:list)->int:
         act_min:int = lista[0]
         act_pos:int = 0
         for i in range (len(lista)):
                if act_min>lista[i]:
                        act_min = lista[i]
                        act_pos = i
         return act_pos

def longitud_palabra(lista:list)->bool:
        for elem in lista:
               if (len(elem)>7):
                        return True
        return False

def palindromo(texto:str)->bool:
       for i in range (int(len(texto)/2)):
           if(texto[i]!=texto[len(texto)-(i+1)]):
                  return False
       return True 

def es_vocal(palabra:chr)->bool:
        vocales = ["a","e","i","o","u"]
        for i in range (len(vocales)):
               if  (vocales[i] == palabra):
                        return True
        return False 

def vocales_distintas(palabra:str)->bool:
       vocales = []
       for elem in palabra:
              if es_vocal(elem) and not pertenece(vocales,elem):
                vocales.append(elem)
        
       return len(vocales)>=3

def convertir_string(lista:list)->int:
       contatenacion=""
       cant_digitos_impares=0
       for elem in lista:
                contatenacion+=str(elem)
       for i in contatenacion:
              if(int(i)%2!= 0):
                     cant_digitos_impares+=1
       return cant_digitos_impares
        
def todas_letras_distintas(palabra:str)->bool:
       for i in range (len(palabra)):
            for j in range (i+1,len(palabra)-1):
                if palabra[i] == palabra[j+1]:
                    return False    
       return True

def ceros_en_posiciones_pares(lista:list)->list:
          for i in range (len(lista)):
               if ((i+1) % 2 ==0):
                    lista[i]=0
          return lista


def borrar_posiciones_pares_dos(lista:list)->list:
    lista_nueva=[]
    for i in range (1,len(lista)+1):
        if(i %2 == 0):
            lista_nueva.append(0)
        else:
            lista_nueva.append(lista[i-1])
        
    return lista_nueva
                
def es_vocal(caracter:chr)->bool:
     vocales = ["a","e","i","o","u"]
     for vocal in vocales:
        if caracter == vocal:
         return True
     return False

def borrar_vocales(palabra:str)->str:
        cadena =""
        for caracter in palabra:
             if not es_vocal(caracter):
                    cadena+=caracter
        return cadena

def reemplaza_vocales(lista:list)->list:
        new_list=[]
        for caracter in lista:
         if not es_vocal(caracter):
          new_list.append(caracter)
         else:
          new_list.append("_")
        return new_list


def da_vuelta_str(lista:list)->list:
        lista_2 = []
        for i in range (len(lista),0,-1):
                lista_2.append(lista[i-1])
        return lista_2

def pertenece (lista:list,e:chr)->bool:
     for item in lista:
          if item == e:
              return True
     return False

def eliminar_repetidos(lista:list)->list:
     lista_sin_repetidos=[]
     for item in lista:
        if not pertenece(lista_sin_repetidos,item):
             lista_sin_repetidos.append(item)
     return lista_sin_repetidos

def matriz_vacia(matriz:list[list[int]])->bool:
     return matriz == [[]]

def primer_fila_vacia(fila:list[int])->bool:
     return len(fila)==0

def matriz_valida(matriz:list[list[int]])->bool:
     for i in range(len(matriz)-1):
          if len(matriz[i])!=len(matriz[i+1]):
               return False
     return not (matriz_vacia(matriz)) and not primer_fila_vacia(matriz[0]) and True

def ordenados(fila:list[int])->bool:
     for i in range(len(fila)-1):
          if fila[i]>fila[i+1]:
               return False
     return True

def filas_ordenadas(matriz:list[list[int]])->bool:
     for fila in matriz:
          if not ordenados(fila):
               return False
     return True


def columnas_ordenadas(matriz:list[list[int]])->bool:
     for i in range (len(matriz)):
          fila_actual= []
          for j in range(len(matriz)):
               fila_actual.append(matriz[j][i])
          if not ordenados(fila_actual):
               return False
     return True

def transponer(matriz:list[list[int]])->list[list[int]]:
     matriz_transpuesta = []
     for i in range(len(matriz)-1):
          matriz_transpuesta.append(columna(matriz,i+1))
     return matriz_transpuesta

def obtener_fila(matriz:list[list[int]],fila=int)->list[int]:
     for i in range(len(matriz)):
      if i+1== fila:
          return matriz[i]

def columna(matriz:list[list[int]],columna:int)->list[int]:
     fila_columna = []
     for i in range (len(matriz)):
          for j in range(len(matriz[i])):
               if(columna==j+1):
                    fila_columna.append(matriz[i][j])
     return fila_columna


def iguales (fila:list[int])->bool:
     for i in range(len(fila)-1):
          if(fila[i]!=fila[i+1]):
               return False
     return True

def obtener_diagonal(matriz:list[list[int]])->list[int]:
     diagonal = []
     for i in range(len(matriz)):
          for j in range(len(matriz[i])):
               if(j==i):
                    diagonal.append(matriz[i][j])
     return diagonal

def obtener_diagonal_inversa(matriz:list[list[int]])->list[int]:
     diagonal_inversa=[]
     for i in range(len(matriz)):
          for j in range(len(matriz[i])-1-i,len(matriz[i])-i):
               diagonal_inversa.append(matriz[j][i])
     return diagonal_inversa


def ta_te_ti(matriz:list[list[int]]):
     for i in range(3):
          fila_actual = obtener_fila(matriz,i+1)
          columna_actual = columna(matriz,i+1)
          if(iguales(fila_actual) or iguales(columna_actual)):
               if(fila_actual[0]== "X" or columna_actual[0]):
                    return 1
               else:
                    return 0
                    
     diagonal_principal = obtener_diagonal(matriz)
     diagonal_secundaria = obtener_diagonal_inversa(matriz)
     if (iguales(diagonal_principal) or iguales(diagonal_secundaria)):
          if(diagonal_principal[0] or diagonal_secundaria[0]=="X"):
                    return 1
          else:
                    return 0

     return 2

def notas_mayores_a_cuatro(notas:list)->bool:
     for nota in notas:
            if nota < 4:
                return False
     return True

def calcular_promedio(notas:list)->int:
     suma_notas=0
     for nota in notas:
          suma_notas+=nota
     return (suma_notas/len(notas))

def aprobado(notas:list)->int:
      if(notas_mayores_a_cuatro(notas) and calcular_promedio(notas)>=7):
          return 1
      elif (notas_mayores_a_cuatro(notas)and calcular_promedio(notas)>=4 and calcular_promedio(notas)<7):
           return 2
      elif (not notas_mayores_a_cuatro(notas) or calcular_promedio(notas)<4):
           return 3

def nombres_alumnos()->list:
     lista_alumnos=[]
     alumno=input("ingrese nombre de alumno:")
     while(alumno!="listo"):
            lista_alumnos.append(alumno)
            alumno=input("ingrese nombre de alumno:")
     return lista_alumnos


cartas = [1,2,3,4,5,6,7,10,11,12]
eleccion = random.choice(cartas)
sumatoria  = 0
historial_cartas = []
print("tu carta es:",eleccion)
historial_cartas.append(eleccion)
seguir_jugando = input("sacas otra carta:")
while(seguir_jugando == "SI"):
        if(sumatoria>=10):
                sumatoria+=0.5
        else:
                sumatoria+=eleccion
        eleccion = random.choice(cartas)
        historial_cartas.append(eleccion)

        print("tu carta es:",eleccion)
        seguir_jugando = input("sacas otra carta:")

if(sumatoria>7.5):
        print("Has perdido")
else:
        print("Has ganado")

print("Las cartas con las que terminaste el juego son:")
for carta in historial_cartas:
        print(carta)
        
def estudiantes()->list[str]:
    estudiantes:list[str] = []
    estudiante = input("ingrese estudiante:")
    while(estudiante!="LISTO" and estudiante!=""):
     estudiantes.append(estudiante)
     estudiante = input("ingrese estudiante:")
    return estudiantes


def monedero()->list[(chr,int)]:
   historial:list[(chr,int)] =[]
   monedero = 0
   movimiento = input("ingrese que movimiento quiere hacer:")
   while(movimiento!="X"):
        if(movimiento=="C"):
            carga = int(input("ingrese monto a cargar:"))
            monedero += carga
            historial.append(("C",carga))
        elif movimiento == "D":
            retiro = int(input("ingrese cantidad a retirar:"))
            monedero-=retiro
            historial.append(("D",retiro))
        movimiento = input("ingrese que movimiento quiere hacer:")


   return historial

def suma_cartas(carta:float)->float:
    if carta>= 10:
        return 0.5
    else: 
        return carta


def juego():
    opciones = [1,2,3,4,5,6,7,10,11,12]
    primer_carta=random.choice(opciones)
    sumatoria_cartas = suma_cartas(primer_carta)
    print("tu primer carta es:",primer_carta)
    eleccion = input("deseas sacar otra carta:")
    while(eleccion!="NO"):
        carta = random.choice(opciones)
        print("tu carta es:",carta)
        sumatoria_cartas+=suma_cartas(carta)
        if(sumatoria_cartas>7.5):
            print("has perdido")
            return sumatoria_cartas
        elif(sumatoria_cartas==7.5):
            print("has ganado")
            return sumatoria_cartas
        else:
            eleccion = input("deseas sacar otra carta:")
    return sumatoria_cartas

def green_password(password:str)->bool:
     len_password = len(password)
     mayuscula = False
     minuscula  = False
     numero = False
     for caracter in password:
        if caracter.isupper():
           mayuscula = True
        elif caracter.islower():
            minuscula = True
        elif caracter.isnumeric():
            numero = True
     return (len_password>8 and mayuscula and minuscula and numero)

def red_password(password:str)->bool:
    return len(password)<5

def armar_password()->str:
 password = input("ingrese su contraseña:")
 if(green_password(password)):
     return "VERDE"
 elif (red_password(password)):
     return "ROJO"
 else:
     return "AMARILLO"


