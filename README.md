# LeetCode

[![Unittest - Python](https://github.com/kuntelin/leetcode/actions/workflows/unitest-python.yaml/badge.svg)](https://github.com/kuntelin/leetcode/actions/workflows/unitest-python.yaml)

## update python virtual environment with `uv`

```bash
uv sync

```

## run unittest

```bash
uv run pytest .

```

## run unittest with logging level `debug`

```bash
uv run pytest . --log-cli-level debug

```

## run unittest in specify folder

```bash
uv run pytest 001-containers-duplicate

```
