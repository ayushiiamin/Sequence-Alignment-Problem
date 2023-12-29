import sys
from resource import *
import time
import psutil

# constants
delta = 30
alpha = [
    [0, 110, 48, 94],
    [110, 0, 118, 48],
    [48, 118, 0, 110],
    [94, 48, 110, 0]
]
index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}

def process_memory():
  process = psutil.Process()
  memory_info = process.memory_info()
  memory_consumed = int(memory_info.rss/1024)
  return memory_consumed

def time_wrapper(str1, str2):
  start_time = time.time()
  opt_val, opt1, opt2 = sequence_alignment_basic(str1,str2)
  end_time = time.time()
  time_taken = (end_time - start_time)*1000
  return time_taken, opt_val, opt1, opt2

def clean_data(data):
  str1 = data[0].strip()
  lst1 = []

  i = 1
  while i < len(data):
    if data[i].strip().isnumeric():
      lst1.append(int(data[i].strip()))
    elif data[i].strip() == "":
      i += 1
      continue
    else:
      break
    i += 1

  str2 = data[i].strip()
  i += 1
  lst2 = []
  
  while i < len(data):
    if data[i].strip().isnumeric():
      lst2.append(int(data[i].strip()))
    elif data[i].strip() == "":
      i += 1
      continue
    else:
      break
    i += 1
  
  return str1, lst1, str2, lst2

def validate_len(generated_list_len, orig_len, lst_len):
  assert generated_list_len == (2**lst_len * orig_len)

def generate_string(s, lst):
  orig_len = len(s)
  lst_len = len(lst)

  for index in lst:
    s = s[:index+1] + s + s[index+1:]

  validate_len(len(s), orig_len, lst_len)
  return s

def sequence_alignment_basic(str1, str2):
  m, n = len(str1), len(str2)
  dp = [[0 for j in range(n + 2)] for i in range(m + 2)]

  # base case
  for i in range(1, m+2):
    dp[i][0] = i * delta
  
  for j in range(1, n+2):
    dp[0][j] = j * delta
  
  # recurrence
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      alpha_i_j = alpha[index[str1[i-1]]][index[str2[j-1]]]
      dp[i][j] = min(
          alpha_i_j + dp[i-1][j-1],
          delta + dp[i-1][j],
          delta + dp[i][j-1]
      )
  
  # value of optimal soln at dp[m][n]
  # Optimal solution
  opt1 = ""
  opt2 = ""

  i = m
  j = n

  while i >= 1 and j >= 1: 
    alpha_i_j = alpha[index[str1[i-1]]][index[str2[j-1]]]
    if dp[i][j] == dp[i-1][j-1] + alpha_i_j:
      # mismatch or exact match
      opt1 += str1[i-1]
      opt2 += str2[j-1]
      i -= 1
      j -= 1
    elif dp[i][j] == delta + dp[i-1][j]:
      # str1 not matched
      opt2 += "_"
      opt1 += str1[i-1]
      i -= 1

    elif dp[i][j] == delta + dp[i][j-1]:
      # str2 not matched
      opt1 += "_"
      opt2 += str2[j-1]
      j -= 1
  
  # if i > 0:
  #   remaining_str = str1[:i]
  #   opt1 += remaining_str[::-1]
  #   opt2 += '_' * i

  # elif j > 0:
  #   remaining_str = str2[:j]
  #   opt2 += remaining_str[::-1]
  #   opt1 += '_' * j

  while j > 0:
  # only str1 remains and all _ in str2
    opt2 += str2[j-1]
    opt1 += "_"
    j -= 1

  while i > 0:
  # only str2 remains and all _ in str1
    opt1 += str1[i-1]
    opt2 += "_"
    i -= 1

  opt1 = opt1[::-1]
  opt2 = opt2[::-1]

  return dp[m][n], opt1, opt2



if __name__ == "__main__":

  input_file_path = sys.argv[1]
  output_file_path = sys.argv[2]
  
  # read data
  f = open(input_file_path, 'r')
  data = f.readlines()
  f.close()

  # clean data
  str1, lst1, str2, lst2 = clean_data(data)

  # generate_strings
  str1 = generate_string(str1, lst1)
  str2 = generate_string(str2, lst2)
  m = len(str1)
  n = len(str2)

  # calling seq alignment
  time_taken, opt_val, opt1, opt2 = time_wrapper(str1, str2)
  memory_taken = process_memory()

  # writing output file
  fout = open(output_file_path, "w")
  fout.write(str(opt_val) + "\n")
  fout.write(opt1 + "\n")
  fout.write(opt2 + "\n")
  fout.write(str(time_taken) + "\n")
  fout.write(str(memory_taken) + "\n")
  fout.close()
