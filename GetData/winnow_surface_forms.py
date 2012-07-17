"""
Filter out unwanted entities from the surface forms database
Keep if
    len > 3 characters
    number of words == 1
"""
import sys

def error():
        print 'winnow_surface_forms.py: ERROR: Please provide the surface forms to URIs database in plain text format'
        print 'Exiting now.'
        sys.exit()

def winnow(filename):
    file_out = open('winnowed_surface_forms.txt', 'w')
    with open(filename, 'r') as file_in:
        for line in file_in:
            items = line.strip().split()
            item = items[0]
            if len(item) > 3 and item.count(' ') == 0:
                file_out.write(item + '\n')

    file_out.close()

def main():
    if len(sys.argv) != 2:
        error()
    winnow(sys.argv[1])

if __name__ == '__main__':
    main()
