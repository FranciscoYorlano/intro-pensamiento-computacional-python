def fibonnacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonnacci(n-1) + fibonnacci(n-2)


def main():
    n = int(input('Elige un número: '))

    fibonnacci(n)


if __name__ == '__main__':
    main()
