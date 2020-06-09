cells = list(input())
line_text = ''
separator = '|'
print('---------')

for i in range(0,len(cells)):
  if i % 3 == 0:
    line_text = line_text + ' ' + cells[i]
    line_text = separator + line_text
  elif ((i+1) % 3) == 0:
    line_text = line_text + ' ' + cells[i] + ' ' + separator
    print(line_text + '\n')
    line_text = ''
  else:
    line_text = line_text + ' ' + cells[i]

print('---------')