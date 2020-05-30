import sys, getopt
import random 

def mccount(n):
  count = 0
  for _ in range(n):
    x = random.uniform(0.0, 1.0)
    y = random.uniform(0.0, 1.0)
    if (x * x + y * y) < 1:
      count += 1
  return count

def main():
  npoints = 0
  try:
    opts, args = getopt.getopt(sys.argv[1:],"n",["n_points="])
  except getopt.GetoptError:
    print("Usage: python montecarlo_serial.py -n <# points>")
    sys.exit(2)

  for o,a in opts:
    if o in ("-n","--n_points"):
      print("number of points: ",a)
      npoints = int(a)

  count = mccount(npoints);
  pi = 4.0 * count / npoints;
  print("pi was estimated as:", pi)


if __name__ == "__main__":
    main()
