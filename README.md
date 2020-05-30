# Proyecto Final HPC (Método Monte Carlo para calcular el valor de π )

## Desarrolladores

- Joshua Sánchez Álvarez - jsanch90@eafit.edu.co - Universidad EAFIT
- Juan Pablo Zapata Raigoza - jzapat90@eafit.edu.co - Universidad EAFIT
- Miguel Angel Ortíz Arboleda - mortiza3@eafit.edu.co - Universidad EAFIT

## Desarrollo

Para desarrollar este proyecto se utilizó el lenguaje de programación [Python](https://www.python.org/). Se implemento el algoritmo de Monte Carlo en 3 maneras distintas, en forma secuencial, paralela con OpenMP (threads) y paralela con MPI. Para las implementaciones de OpenMP y MPI en Python se utilizaron las siguientes bibliotecas:

- OpenMP: Se usó la biblioteca [pymp](https://github.com/classner/pymp)
- MPI: Se usó la biblioteca [mpi4py](https://bitbucket.org/mpi4py/mpi4py/src/master/)

## Compilación y ejecución

### Monte Carlo secuencial
Para ejecutar el método secuencialmente se debe ejecutar el archivo [montecarlo_serial.py](https://github.com/jpzapata99/Proyecto4_Topicos_Telematica/blob/master/montecarlo_serial.py) de la siguiente manera: 
```ssh
 $ python montecarlo_serial.py --n_points <numero de puntos a generar>
  ```
  Ejemplo:
  ```ssh
 $ python montecarlo_serial.py --n_points 10000
 pi was estimated as: 3.136424
  ```

### Monte Carlo paralelo OpenMP (pymp)
Inicialmente se debe instalar la biblioteca ```pymp``` de la siguiente manera:
```ssh
$ pip install pymp-pypi
```
Luego debemos ejecutar el archivo [montecarlo_parallel.py](https://github.com/jpzapata99/Proyecto4_Topicos_Telematica/blob/master/montecarlo_parallel.py) de la siguiente manera:

  ```ssh
 $ python montecarlo_parallel.py --n_points <numero de puntos a generar> --n_threads <numero de hilos a crear>
  ```

Ejemplo:
 ```ssh
 $ python montecarlo_parallel.py --n_points 10000 --n_threads 4
 pi was estimated as: 3.141114
  ```

### Monte Carlo paralelo MPI (mpi4py)
Antes de ejecutar el algoritmo debemos instalar la biblioteca ```mpi4py``` de la siguiente manera:

```ssh
$ pip install mpi4py
```

Luego debemos ejecutar el archivo [montecarlo_mpi.py](https://github.com/jpzapata99/Proyecto4_Topicos_Telematica/blob/master/montecarlo_mpi.py) de la siguiente manera:

```ssh
mpiexec -np <numero de procesos a crear> python montecarlo_mpi.py --n_points <numero de puntos a generar>
```
Ejemplo:
```ssh
mpiexec -np 4 python montecarlo_mpi.py --n_points 10000
pi was estimated as: 3.141462
```
## Análisis de resultados

### Comparación de los distintos métodos
![](https://github.com/jpzapata99/Proyecto4_Topicos_Telematica/blob/master/graficos/tiempo_vs_cantidadPuntos.png)

![](graficos/tiempo_vs_cantidadPuntos.png)
