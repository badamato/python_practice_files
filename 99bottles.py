def line(num_bottles):
  current = num_bottles
  next = num_bottles - 1

  if current > 1 or current == 0:
    first_part = "%d bottles of beer on the wall %d bottles of beer, take one down, pass it around, " % (current, current)
  else:
    first_part = "%d bottle of beer on the wall %d bottle of beer, take one down, pass it around, " % (current, current)

  if next > 1 or next == 0:
    second_part = "%d bottles of beer on the wall" % (next)
  else:
    second_part = "%d bottle of beer on the wall" % (next)

  result = first_part + second_part

  return result


def song(number_of_lines):
  lines_of_song = []
  for i in range(number_of_lines, 0, -1):
    lines_of_song.append(line(i))

  return lines_of_song

def main():
  print(song(99))

main()