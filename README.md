# Run all tests
``` python -m pytest tests ```

or

``` PYTHONPATH=$PYTHONPATH:$(pwd) pytest ```


# Run unit tests
``` python -m pytest tests/unit/ ```

# Run functional tests
``` python -m pytest tests/functional/ ```

# Run Coverate test
``` python -m pytest --cov=. tests/ ```

# Run tests distributed/parallel
``` python -m pytest --cov=. tests/ -n 4 ```

# Run only modified tests but not commited to git 
``` python -m pytest --picked ```

# Run with all options
``` python -m pytest --cov=. tests/ -n 4 --picked ```

# Run with benchmark
``` python -m pytest --benchmark-compare ```

# Generate pytest-bdd py structure from feature
- Generate feature
[Pytest-bdd documentation](https://pypi.org/project/pytest-bdd/)

- Example
``` tests/functional/features/authentication ```

- Generating  skeleton
``` pytest-bdd generate tests/functional/features/authentication > tests/functional/test_authentication.py ```

- Advanced test generation 
``` PYTHONPATH=$PYTHONPATH:$(pwd) py.test --generate-missing --feature tests/functional/features/authentication ```

