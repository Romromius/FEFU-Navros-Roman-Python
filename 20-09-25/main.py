import math

with open('input.txt', 'r') as f:
    text = f.read()
    text = text.split('\n')

def one(K):
    K = int(K)
    return math.ceil(1000 * math.log(K, 2)) / 1000

def two(K):
    K = int(K)
    i = 1
    while True:
        if 2**i >= K:
            return i
        i += 1


def main():
    print()
    for i in text:
        print('Мощность:', i)
        print('Действительные биты:', one(i))
        print('Целые биты:', two(i))
        print()

if __name__ == '__main__':
    main()
