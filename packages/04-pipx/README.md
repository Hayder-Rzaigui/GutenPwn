## Caminho 4 - pipx (implementado por último)

Este é o caminho recomendado para uso operacional isolado (sem poluir Python do sistema).

### Instalação do pipx

```bash
python -m pip install --user pipx
python -m pipx ensurepath
```

### Instalar GutenPwn

Publicado no PyPI:

```bash
pipx install gutenpwn
```

A partir do checkout local:

```bash
pipx install --editable .
```

### Extras opcionais

```bash
pipx inject gutenpwn shodan censys scikit-learn
```

### Validar

```bash
gutenpwn --version
gutenpwn --help
```

