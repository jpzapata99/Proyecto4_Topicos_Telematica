# PCAM - PROYECTO 4 TÓPICOS EN TELEMÁTICA

### Introducción

El objetivo de este documento es realizar una explicación exhaustiva del proceso de creación de los 3 algoritmos con los cuales se calcula el valor de phi mediante el método de Montecarlo.

La fórmula y el funcionamiento del método se pueden ver representadas en el siguiente algoritmo:

##### Algoritmo secuencial

El método consiste en generar N puntos aleatorios dentro del intervalo [0, 1] para los ejes X e Y y cuente cuántos de estos puntos caen dentro de un círculo o radio 1 y se centran en (0,0) que se llaman M. Finalmente se retorna el número de puntos que se situaron al interior del circulo.
```python
def mccount(n):
  count = 0
  for _ in range(n):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    if (x * x + y * y) < 1:
      count += 1
  return count
```
Luego calcula pi usando la siguiente fórmula: π=(4.0∗M)/N siendo N el número puntos que se situaron en el circulo hallado en el método anterior.
```python
count = mccount(npoints);
pi = 4.0 * count / npoints;
print("pi was estimated as:", pi)
```
Y así es como se estima el número pi se forma secuencial.

##### Algoritmo pararelizado con OpenMP

Para la parelización del algoritmo en el lenguaje de programación Python decidimos utilizar la librería *pymp* la cual está soportado y se basa en el framework OMP.
A diferencia del algoritmo secuencial el algoritmo paralelizado utiliza hilos de ejecución con el fin de que cada uno de estos ejecute una iteración del ciclo, realice el respectivo cálculo de la formula y finalmente almacene el resultado de dicho calculo en una memoria compartida representada en un arreglo de numpy. Como se puede ver este método recibe la cantidad de hilos que desea utilizar por medio del parametro t, luego se utilizará este en el método Parallel de pymp para inicializar cada uno de los hilos que dicta el parametro, posteriormente, estos hilos son utilizados en la declaración del ciclo for para ejecutar el bloque de código dentro de este.
```python
def mccount(n,t):
  res = pymp.shared.array((n,), dtype='uint8')
  count = 0
  with pymp.Parallel(t) as p:
    for index in p.range(0,n):
      x = random.uniform(0.0, 1.0)
      y = random.uniform(0.0, 1.0)
      if (x * x + y * y) < 1:
        res[index] = 1
    return res
```
Una vez realizada toda la ejecución que halla los puntos dentro del circulo, el contenido del arreglo resultante es sumado para que finalmente se pueda calcular el valor de pi por medio de la formula inicialmente mostrada.
```python
  count = np.sum(mccount(npoints,nthreads))
  pi = 4.0 * count / npoints;
  print("pi was estimated as:", pi)
```
##### Algoritmo pararelizado con MPI
Para el algoritmo realizado con el framework MPI utilizamos la libreria *mpi4py* que trae todas las funciones del framework nativo de MPI. El algoritmo realizado con MPI utilizada distintos nodos(procesadores) para ejecutar el algoritmo de manera pararelizada mejorando así su perfomance ya que divide la cantidad de puntos a calcular para cada uno de los procesadores disponibles.
Ya en el código, primeramente se inicializa todo el contexto de MPI por medio del comando *MPI.COMM_WORLD*,  se obtiene el nodo actual por medio de la función *Get_rank()*, y se obtiene tambien el número de nodos disponibles por medio del método *Get_size()*
```python
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()
```
Ahora, se realiza el particionamiento de puntos que van a corresponder a cada uno de los procesadores disponibles y se calculan los puntos aleatorios que se ubican dentro del circulo por medio de la función mccount.
```python
n = int(npoints / size)
count = mccount(n)
```
Los procesadores distintos al procesador master se van a encargar de calcular los puntos y enviarselos a este nodo principal por medio del método *comm.send()*, luego, el nodo principal recibe cada uno de los conjuntos de puntos por medio del método *comm.recv* y aplica la formula para hallar el valor de pi. Finalmente se cierra el contexto MPI por medio del comando *MPI.Finalize()*.
```python
if rank != 0:
    comm.send(count, dest=0, tag=0)
else:
    for i in range(1, size):
      data = comm.recv(source=i, tag=0)
      count += data
    pi = 4.0 * count / npoints;
    print("pi was estimated as:", pi)

  MPI.Finalize()
```
