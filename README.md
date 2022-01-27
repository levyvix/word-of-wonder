# Word of Wonders Bot

Este programa gera possiveis palavras para o jogo **Word of Wonders**.


## Instalação

```bash
git clone https://github.com/levyvix/word-of-wonder
```

## Como usar

Para obter ajuda:

```bash
python wow.py --help
```

Para usar o programa:
```bash
python wow.py -w [Palavra] -n [Número de palavras] -m [Máscara]
``` 

Exemplo:
```bash
python wow.py -w "CASA" -n 4 -m "_AS_"
```

Saída: (Todas as combinações onde a máscara está presente)
```bash
CASA
CASA
AASC
AASC
```
