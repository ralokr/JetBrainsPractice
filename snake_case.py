input_word = input()
output_word = ''

for i in input_word:
    if i.isupper():
        output_word = output_word + i.replace(i,'_' + i.lower())
    else:
        output_word += i

print(output_word)