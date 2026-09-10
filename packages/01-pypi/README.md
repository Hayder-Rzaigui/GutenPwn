## Caminho 1 - PyPI / Wheel

Publica o GutenPwn para instalação via `pip`.

### Objetivo

- gerar `sdist` + `wheel`
- validar instalação local
- publicar em TestPyPI e PyPI

### Build local

Linux/macOS:

```bash
./packages/01-pypi/build.sh
```

Windows:

```powershell
.\packages\01-pypi\build.ps1
```

### Publicação

```bash
python -m twine upload --repository testpypi dist/*
python -m twine upload dist/*
```

### Instalação do usuário final

```bash
pip install gutenpwn
pip install "gutenpwn[full]"
```

