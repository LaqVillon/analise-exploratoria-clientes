"""
Este programa executa o arquivo analysis.py para encontrar as figuras
Autor: Luis Villon
"""


# import subprocess
# import os
# from contextlib import chdir


def main() -> None:
    # os.chdir("/media/luis/sdc3-arq-ubu/GITHUB-PROJECT/Visualizacoes-análise-exploratória")
    with open("analysis.py") as f:
        exec(f.read())
    # subprocess.run(["python", "src/analysis.py"])
    # os.system(f'python {"src/analysis.py"}')


if __name__ == '__main__':
    main()
