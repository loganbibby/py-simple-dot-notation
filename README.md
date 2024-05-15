# Simple Dot Notation
Very simple dot notation implementation for Python

## Usage

```python
from simpledot import SimpleDotNotation

dot = SimpleDotNotation({
  "foo": "bar",
  "bar": {
    "foobar": "barfoo"
  }
})

print(dot.foo)  # bar
print(dot.bar)  # SimpleDotNotation instance
print(dot.bar.value())  # {"foobar": "barfoo"}
print(dot.get("bar").value())  # {"foobar": "barfoo"}
print(dot.bar.foobar)  # barfoo
print(dot.get("bar.foobar")  # barfoo
```
