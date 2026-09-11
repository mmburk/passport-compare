import sys

if len(sys.argv) > 1:
    content = sys.stdin.read()
    with open(sys.argv[1], 'w', encoding='utf-8') as f:
        f.write(content)
    print('Successfully wrote ' + sys.argv[1])
