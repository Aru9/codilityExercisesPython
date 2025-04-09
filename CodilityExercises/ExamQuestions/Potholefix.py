def solution(s):
  """
  Calculates the number of "holes" in a string based on a specific pattern.

  Args:
    s: The input string.

  Returns:
    The number of "holes" counted.
  """
  holes = 0
  i = 0
  while i < len(s):
    if s[i] == 'X':
      holes += 1
      i += 3  # Increment by 3 to skip the 'X' and the next two characters
    else:
      i += 1  # Move to the next character if it's not 'X'
  return holes