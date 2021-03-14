# Gregorian calendar date checker =)

Features:
- CI (Github actions)
    - Virtual environment with dependencies lock (poetry) 
    - Code formatter (black)
    - Linter (flake8)
    - Tests (pytest)
- Docker image

Easy way to check it:
- `make docker_app` for working with app
- `make docker_test` for run tests

Otherwise:
- install python (3.9+)
- install poetry (1.1.4+)
- `poetry install --no-dev`
- `make app`

For developing:
- `poetry install`
- write some code here
- `make test`

In case of installation\configuration problems:
- [MacOs guide to python on MacOS](
  https://medium.com/@briantorresgil/definitive-guide-to-python-on-mac-osx-65acd8d969d0
  )
