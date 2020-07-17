# create the planets.txt
solar = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
file = open('planets.txt', 'w', encoding='utf-8')
for i in solar:
    file.write(i + '\n')

file.close()