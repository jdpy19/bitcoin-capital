import sys
import random
import itertools
import time

def generate_input(length, n=0):
  x = list(f'{random.randint(0, 2**length - 1):08b}')
  while n > 0:
    x[random.randint(0, len(x)-1)] = 'X'
    n -= 1
  return ''.join(x)

def generate_combinations(input_str):
  input_list = list(input_str)
  indices = [i for i, x in enumerate(input_list) if x == 'X']
  set_result(input_list, indices, 0, '0')
  set_result(input_list, indices, 0, '1')
    
def set_result(input_list, indices, depth, value):
  input_list[indices[depth]] = value
  if depth == len(indices)-1:
    print(''.join(input_list))
  else:
    set_result(input_list, indices, depth+1, '0')
    set_result(input_list, indices, depth+1, '1')
  
if __name__ == '__main__':
  if sys.argv[1] == 'random':
    x = generate_input(100, 20)
  else:
    x = sys.argv[1]
  print(f'Input: {x}')
  generate_combinations(x)