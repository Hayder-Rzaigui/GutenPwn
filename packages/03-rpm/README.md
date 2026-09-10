## Caminho 3 - RPM (RHEL/Fedora/Rocky/Alma)

Empacotamento via `rpmbuild` usando o spec em `packages/03-rpm/gutenpwn.spec`.

### Pré-requisitos

```bash
sudo dnf install rpm-build python3-devel python3-setuptools rpmdevtools
```

### Build

```bash
./packages/03-rpm/build.sh
```

Saídas:

- `~/rpmbuild/RPMS/noarch/gutenpwn-<versao>-1*.noarch.rpm`
- `~/rpmbuild/SRPMS/gutenpwn-<versao>-1*.src.rpm`

