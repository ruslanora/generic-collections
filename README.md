# generic-collections

Generic collections in Python.

# Requirements

- Python>=v3.12

# Collections

- [HashTable](./src/datastructpy/hash_table.py)
- [LinkedList](./src/datastructpy/linked_list.py)
- [PriorityQueue](./src/datastructpy/priority_queue.py)
- [Queue](./src/datastructpy/queue.py)
- [Stack](./src/datastructpy/stack.py)

# Project

## Getting Started

`cd` to the project directory, and create a virtual environment by running:

```sh
make venv
```

Activate the environment by running:

```sh
source venv/bin/activate
```

Install all dependencies by running:

```sh
make install
```

Integrate pre-commit and pre-push hooks by running:

```sh
make hooks
```

To test a new hook, run the following command:

```sh
make test-hook # all

# OR

make test-hook hook=<id> # specific hook
```

## Package Management

To install a new package, run the following command:

```sh
make install name=<package_name>
```

To uninstall a package, run the following command:

```sh
make uninstall nanme=<package_name>
```

> **Important**: These commands run pipdeptree under the hood to generate or update the requirements-lock.txt file. Please, rely on these commands to manage packages.

## Testing, linting, formatting

### pylint

The project follows the [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html), and uses `pylint` to check if the code follows the guide.

To analyze the entire codebase, run the following command:

```sh
make smell
```

To analyze a specific file, run the following command:

```sh
make smell file=./path/to/file.py
```

To lint the code, run the following command:

```sh
make lint
```

### black

The project uses `black` as a code formatter.

To check the format of the entire codebase, run the following command:

```sh
make check-format
```

To check a specific file, run the following command:

```sh
make check-format file=./path/to/file.py
```

To format the code, run one of the following commands:

```sh
make format # formats all

# OR

make format file=./path/to/file.py # formats a specific file
```

### mypy

The project relies on `mypy` for type checking.

To check the types, run one of the following commands:

```sh
make check-types # checks all files

# OR

make check-types file=./path/to/file.py # checks a specific file
```

### unittest

The project uses the `unittest` framework. To execute all tests, run the following command:

```sh
make test
```

To execute a specific testcase, run the following command:

```sh
make test file=./path/to/file.py
```

# License

[MIT License](LICENSE)
