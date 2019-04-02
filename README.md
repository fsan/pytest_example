# Run all tests
``` python -m pytest tests ```

# Run unit tests
``` python -m pytest tests/unit ```

# Run functional tests
``` python -m pytest tests/functional/ ```

# Generate pytest-bdd py structure from feature
- Generate feature
[Pytest-bdd documentation](https://pypi.org/project/pytest-bdd/)

- Example
``` tests/functional/features/authentication ```

- Generating  skeleton
``` pytest-bdd generate tests/functional/features/authentication > tests/functional/test_authentication.py ```

- Advanced test generation 
``` PYTHONPATH=$PYTHONPATH:$(pwd) py.test --generate-missing --feature tests/functional/features/authentication ```

