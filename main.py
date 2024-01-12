"""
Este programa executa o arquivo analysis.py para encontrar as figuras
Autor: Luis Villon
"""


def main() -> None:
    with open("analysis.py") as f:
        exec(f.read())


if __name__ == '__main__':
    main()
