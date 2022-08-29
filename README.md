# Divisible

[![Run Tests](https://github.com/DucNgn/divisible/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/DucNgn/divisible/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/divisible.svg)](https://badge.fury.io/py/divisible)


Great python package for all your hmm-is-this-number-divisible-by-this-number needs!

### Installation:

```
pip install divisible
## --- OR ---
poetry add divisible
```
**Voilà**, done.

### Usage
```
from divisible import is_divisible

is_divisible(200, 25) # --> True
```

Now supports is_even and is_odd, wow.

```
from divisible import is_odd

is_odd(200) # --> False
```

```
from divisible import is_even

is_even(200) # --> True
```
