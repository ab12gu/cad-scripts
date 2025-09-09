# CAD Scripts

Scripts/Code that I wrote to develop 3d models

## Options

1. Build123d
    - Python
2. OpenSCAD
    - Domain specific language, ".scad", called OpenSCAD

## Getting started with Build123d

**Note:** the `requirements.txt`, which contains all packages project depends on

I'm going to try out a new python manager, UV.

### Installation

Install [uv](https://github.com/astral-sh/uv):
```
$ brew install uv
```

Install dependencies
```
$ uv pip install build123d
```

To install dependencies
```
$ uv install
```

### Dependencies

Create a `uv.lock` file, locks exact versions of all dependencies and sub-dependencies

```
$ uv lock
```

In contrast, `pyproject.toml` is the current state of dependencies, not used in reinstallation

To list all dependencies
```
$ uv pip list
```

### Virtual Environment

Create a virtual environment if one does not exit in folder:
```
$ uv venv my-name
```

Activate environment
```
$ source .venv/bin/activate
```

Run file with temprorary environment
```
$ uv run python3 example.py
```

## Getting started with OpenSCAD


