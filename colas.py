from queue import Queue as Cola
import random
def generar_nros_al_azar(cantidad:int,desde:int,hasta:int)->Cola[int]:
    c = Cola()
    for i in range(cantidad):
        c.put(random.randint(desde,hasta))
    return c


def mostrar_cola(c:Cola)->None:
    while not c.empty():
        elem  = c.get()
        print(elem)
        print("--------")

def cantidad_elementos(c:Cola)->int:
    cantidad = 0
    c_auxiliar = Cola()
    while not  c.empty():
        cantidad+=1
        c_auxiliar.put(c.get())
    while not c_auxiliar.empty():
        c.put(c_auxiliar.get())
    return cantidad

def buscar_el_maximo(c:Cola)->int:
    c_auxiliar = Cola()
    current_max = c.get()
    c_auxiliar.put(current_max)
    while not c.empty():
        elem  = c.get()
        if elem>current_max:
            current_max = elem
        c_auxiliar.put(elem)
    while not c_auxiliar.empty():
        c.put(c_auxiliar.get())
    return current_max

def buscar_nota_minima(c:Cola[tuple[str,int]])->tuple[str,int]:
    c_auxiliar:Cola = Cola()
    current:tuple[str,int]  = c.get()
    c_auxiliar.put(current)
    while not c.empty():
        elem = c.get()
        if(elem[1]<current[1]):
            current = elem
        c_auxiliar.put(elem)
    while not c_auxiliar.empty():
        c.put(c_auxiliar.get())
    return current

def intercalar(p1:Cola,p2:Cola)->Cola:
    p = Cola()
    while not p1.empty():
        p.put(p1.get())
        p.put(p2.get())
    return p

def pertenece(l:list,e:int)->bool:
    for i in range(len(l)):
        if l[i]==e:
            return True
    return False

def armar_secuencia_de_bingo()->Cola[int]:
    numeros = Cola()
    aux = []
    cantidad_numeros = 0
    while cantidad_numeros < 100:
        elem = random.randint(0,99)
        if not pertenece(aux,elem):
            aux.append(elem)
            numeros.put(elem)
            cantidad_numeros+=1
    return numeros

def jugar_carton_bingo(carton:list[int],bolillero:Cola[int])->int:
    jugadas = 0
    aciertos = 0
    bolillero_aux = Cola()
    while not bolillero.empty():
                bolilla = bolillero.get()
                bolillero_aux.put(bolilla)
                if(aciertos!=len(carton)):
                    jugadas+=1
                if (pertenece(carton,bolilla)):
                    aciertos+=1
    while not bolillero_aux.empty():
        bolillero.put(bolillero_aux.get())
    
    return jugadas
                    
def n_pacientes_urgentes(c:Cola[tuple[(int,str,int)]])->int:
    pacientes_urgentes = 0
    c_auxiliar = Cola()
    while not c.empty():
        elem:tuple[(int,str,int)] = c.get()
        if(elem[0]<=3):
            pacientes_urgentes+=1
    while not c_auxiliar.empty():
        c.put(c_auxiliar.get())
    return pacientes_urgentes

def atencion_al_cliente(c:Cola[tuple[str,int,bool,bool]])->Cola[tuple[str,int,bool,bool]]:
    cola_orden_atencion = Cola()
    c_aux = Cola()
    cola_prioridad = Cola()
    cola_cuenta_bancaria_preferencial = Cola()
    cola_resto_clientes = Cola()
    while not c.empty():
        data_cliente = c.get()
        c_aux.put(data_cliente)
        if(data_cliente[3]):
            cola_prioridad.put(data_cliente)
        elif (data_cliente[2]):
            cola_cuenta_bancaria_preferencial.put(data_cliente)
        else:
            cola_resto_clientes.put(data_cliente)
    while not cola_prioridad.empty():
        cola_orden_atencion.put(cola_prioridad.get())
    while not cola_cuenta_bancaria_preferencial.empty():
        cola_orden_atencion.put(cola_cuenta_bancaria_preferencial.get())
    while not cola_resto_clientes.empty():
        cola_orden_atencion.put(cola_resto_clientes.get())
    while not c_aux.empty():
        c.put(c_aux.get())
    return cola_orden_atencion

cola_banco = Cola()
elementos = [("Maximo Tietze",46499706,False,False),("Marcelo Tietze",342342342,False,False),("Maximo Luan",123123123,False,True),("Maximo as",123123,False,True),("Maximo gff",123123,True,True)]
for elemento in elementos:
    cola_banco.put(elemento)




