def front_times(str, n):
  first_len = 3
  if first_len > len(str):
    first_len = len(str)
  first = str[:first_len]
  
  result = ""
  for i in range(n):
    result = result + first
  return result