import os
with open(os.getcwd() + '/day7/input.txt') as f:
    input = f.read().splitlines()
    input.append('$ EOF')

    filesystem = []
    currentDir = -1
    directory = ''
    inode = -1
    for l, commandLine in enumerate(input):
        token = commandLine.split()
        if token[0] == '$':
            if directory != '':
                inode += 1
                filesystem.append(directory)
                currentDir = inode
                directory = ''
            command = token[1]
            if command == 'cd':
                argument = token[2]
                if argument == '..':
                    currentDir = filesystem[currentDir]['parent']
                    dirName = filesystem[currentDir]['dirName']
                else:
                    parentDir = currentDir
                    dirName = argument
            elif command == 'ls':
                directory = {'dirName':dirName,'parent':parentDir, 'files':[], 'dirs':[], 'total_size':0}
        elif token[0] == 'dir':
            subdir = token[1]
            directory['dirs'].append(subdir)
        else:
            size = int(token[0])
            file = token[1]
            directory['files'].append((file,size))
            directory['total_size'] += size
            # percolate file size up the tree
            pdir = directory['parent']
            while True:
                if pdir == -1: break
                filesystem[pdir]['total_size'] += size
                pdir = filesystem[pdir]['parent']

directory_sum = 0

discSpace = 70000000
usedDiscSpace = filesystem[0]['total_size']
unusedDiscSpace = discSpace - usedDiscSpace

unusedRequired  = 30000000
spaceToFree = unusedRequired - unusedDiscSpace

best_delete_size = discSpace
delete_dir = ''

for directory_inode, directory in enumerate(filesystem):
    dir_size = directory['total_size']
    if dir_size <= 100000:
        directory_sum += dir_size
    if dir_size >= spaceToFree:
        if dir_size < best_delete_size:
            best_delete_size = dir_size
            delete_dir = directory['dirName']

# Part 1
print(directory_sum)

# Part 2
print(best_delete_size)


