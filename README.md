# Gregorian calendar date checker =)

### Features:
- CI (Github actions)
    - Virtual environment with dependencies lock (poetry) 
    - Code formatter (black)
    - Linter (flake8)
    - Tests (pytest)
- Docker image

### Installation & Usage:
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

### Next steps:
- [ ] Extract methods from app.py for parse user input with tests (for better coverage)
  - [ ] Add code coverage level
  - [ ] Improve it
- [ ] Rewrite from datetime.strptime to custom realization (for better performance)
  - [ ] Measure speed
  - [ ] Improve it
    - [ ] Fix day count for each month
    - [ ] Calculate leap years
    - [ ] Extend supported years
- [ ] Extend linter checks and formatter:
  - [ ] Add import sort with isort
  - [ ] Add deadcode analysis with vulture
  - [ ] Add flake8 plugins relevant for project
