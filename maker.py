filename = 'journal.txt'
with open(filename, 'w') as f:
    f.write('This file was created by a Python script!\n')
    f.write('Victory Odingo is mastering the terminal.')
print(f'Successfully created {filename}!')
