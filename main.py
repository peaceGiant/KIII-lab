from functions import *

if __name__ == '__main__':
  init_dist = init_distribution()
  scaled_dist = scale_distribution(init_dist)
  print("This is the scaled distribution")
  print(scaled_dist)
  