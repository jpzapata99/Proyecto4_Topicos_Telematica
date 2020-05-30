import sys, getopt
import random
import pymp
import numpy as np

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

def main():
  npoints = 10
  nthreads = 1
  try:
    opts, args = getopt.getopt(sys.argv[1:],"n:t",["n_points=","n_threads="])
  except getopt.GetoptError:
    print("Usage: python montecarlo_serial.py -n <# points>")
    sys.exit(2)

  for o,a in opts:
    if o in ("-n","--n_points"):
      npoints = int(a)
    if o in ("-t","--n_threads"):
      nthreads = int(a)
  
  count = np.sum(mccount(npoints,nthreads))

  pi = 4.0 * count / npoints;
  print("pi was estimated as:", pi)

if __name__ == "__main__":
  main()
