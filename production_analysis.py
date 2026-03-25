def calculate_totals(expected_output, actual_output):
  if len(expected_output) != len(actual_output):
    print("Lists must have same length")
    return None
  total_expected = 0
  total_output = 0

  for n in range(len(expected_output)):
    if not isinstance(expected_output[n], (int, float)) or not isinstance(actual_output[n], (int, float)):
      print("Data must be only numbers")
      return None
    if expected_output[n] < 0 or actual_output[n] < 0:
      print("Numbers must be higher than 0")
      return None
    total_expected += expected_output[n]
    total_output += actual_output[n]
  return total_expected, total_output

def count_days_below_target(expected_output, actual_output, target):
  days_below = 0

  for n in range(len(expected_output)):
    performance = (actual_output[n]/expected_output[n]) *100
    if performance < target:
      days_below += 1
  return days_below

def get_worst_day(expected_output, actual_output):
  worst = actual_output[0] - expected_output[0] 

  for n in range(len(expected_output)):
    difference = actual_output[n] -expected_output[n]
    if difference < worst:
      worst = difference
  return worst
  
def get_best_day(expected_output, actual_output):
  best = actual_output[0] - expected_output[0]

  for n in range(len(expected_output)):
    difference = actual_output[n] -expected_output[n]
    if difference > best:
      best = difference
  return best

def check_status(performance, target):
  if performance >= target:
    return "On Track"
  return "Off Track"

expected_output = [1000, 1100, 1050, 1200, 1150]
actual_output   = [950, 1150, 1000, 1250, 1100]
target = 95

result = calculate_totals(expected_output, actual_output)

if result is not None:
  total_expected, total_output = result
  performance = (total_output/total_expected) *100

  print(f'===== WEEKLY PRODUCTION REPORT =====\n\n Total expected: {total_expected} \n Total actual: {total_output}\n Overall performance: {round(performance,2)}\n\n Days below target: {count_days_below_target(expected_output, actual_output, target)}\n Worst day deviation: {get_worst_day(expected_output, actual_output)}\n Best day deviation: {get_best_day(expected_output, actual_output)}\n \n Final status: {check_status(performance, target)}')


