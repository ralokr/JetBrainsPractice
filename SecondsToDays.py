seconds = [86400, 1028397, 8372891, 219983, 865779330, 3276993204380912]

days = [x // (24*60*60) for x in seconds]

print(days)