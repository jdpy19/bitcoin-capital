import sys
import random
import itertools

def generate_input(length, n=0):
  x = list(f'{random.randint(0, 2**length - 1):08b}')
  while n > 0:
    x[random.randint(0, len(x)-1)] = 'X'
    n -= 1
  return ''.join(x)

def generate_combinations(input_str):
  input_list = list(input_str)
  indices = [i for i, x in enumerate(input_list) if x == 'X']
  for combo in itertools.product([0, 1], repeat=len(indices)):
    print_result(input_list, zip(indices, combo))
    

def print_result(input_list, iterator):
  for (i, x) in iterator:
    input_list[i] = str(x)
  print(f''.join(input_list))
  
if __name__ == '__main__':
  if sys.argv[1] == 'random':
    x = generate_input(10, 3)
  else:
    x = sys.argv[1]
  print(f'Input: {x}')
  generate_combinations(x)
