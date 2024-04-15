
from entities.sin import SystemIdentificationNumber


def main():
    sin = SystemIdentificationNumber()
    print(sin)
    print(sin.decrypt())


if __name__ == '__main__':
    main()
