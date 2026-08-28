# {py:mod}`abtem.core.utils`

```{py:module} abtem.core.utils
```

```{autodoc2-docstring} abtem.core.utils
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CopyMixin <abtem.core.utils.CopyMixin>`
  - ```{autodoc2-docstring} abtem.core.utils.CopyMixin
    :parser: rst
    :summary:
    ```
* - {py:obj}`EqualityMixin <abtem.core.utils.EqualityMixin>`
  - ```{autodoc2-docstring} abtem.core.utils.EqualityMixin
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`array_row_intersection <abtem.core.utils.array_row_intersection>`
  - ```{autodoc2-docstring} abtem.core.utils.array_row_intersection
    :parser: rst
    :summary:
    ```
* - {py:obj}`ensure_list <abtem.core.utils.ensure_list>`
  - ```{autodoc2-docstring} abtem.core.utils.ensure_list
    :parser: rst
    :summary:
    ```
* - {py:obj}`expand_dims_to_broadcast <abtem.core.utils.expand_dims_to_broadcast>`
  - ```{autodoc2-docstring} abtem.core.utils.expand_dims_to_broadcast
    :parser: rst
    :summary:
    ```
* - {py:obj}`flatten_list_of_lists <abtem.core.utils.flatten_list_of_lists>`
  - ```{autodoc2-docstring} abtem.core.utils.flatten_list_of_lists
    :parser: rst
    :summary:
    ```
* - {py:obj}`get_data_path <abtem.core.utils.get_data_path>`
  - ```{autodoc2-docstring} abtem.core.utils.get_data_path
    :parser: rst
    :summary:
    ```
* - {py:obj}`get_dtype <abtem.core.utils.get_dtype>`
  - ```{autodoc2-docstring} abtem.core.utils.get_dtype
    :parser: rst
    :summary:
    ```
* - {py:obj}`insert_empty_axis <abtem.core.utils.insert_empty_axis>`
  - ```{autodoc2-docstring} abtem.core.utils.insert_empty_axis
    :parser: rst
    :summary:
    ```
* - {py:obj}`interleave <abtem.core.utils.interleave>`
  - ```{autodoc2-docstring} abtem.core.utils.interleave
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_broadcastable <abtem.core.utils.is_broadcastable>`
  - ```{autodoc2-docstring} abtem.core.utils.is_broadcastable
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_scalar <abtem.core.utils.is_scalar>`
  - ```{autodoc2-docstring} abtem.core.utils.is_scalar
    :parser: rst
    :summary:
    ```
* - {py:obj}`itemset <abtem.core.utils.itemset>`
  - ```{autodoc2-docstring} abtem.core.utils.itemset
    :parser: rst
    :summary:
    ```
* - {py:obj}`label_to_index <abtem.core.utils.label_to_index>`
  - ```{autodoc2-docstring} abtem.core.utils.label_to_index
    :parser: rst
    :summary:
    ```
* - {py:obj}`normalize_axes <abtem.core.utils.normalize_axes>`
  - ```{autodoc2-docstring} abtem.core.utils.normalize_axes
    :parser: rst
    :summary:
    ```
* - {py:obj}`number_to_tuple <abtem.core.utils.number_to_tuple>`
  - ```{autodoc2-docstring} abtem.core.utils.number_to_tuple
    :parser: rst
    :summary:
    ```
* - {py:obj}`safe_ceiling_int <abtem.core.utils.safe_ceiling_int>`
  - ```{autodoc2-docstring} abtem.core.utils.safe_ceiling_int
    :parser: rst
    :summary:
    ```
* - {py:obj}`safe_equality <abtem.core.utils.safe_equality>`
  - ```{autodoc2-docstring} abtem.core.utils.safe_equality
    :parser: rst
    :summary:
    ```
* - {py:obj}`safe_floor_int <abtem.core.utils.safe_floor_int>`
  - ```{autodoc2-docstring} abtem.core.utils.safe_floor_int
    :parser: rst
    :summary:
    ```
* - {py:obj}`tuple_range <abtem.core.utils.tuple_range>`
  - ```{autodoc2-docstring} abtem.core.utils.tuple_range
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`T <abtem.core.utils.T>`
  - ```{autodoc2-docstring} abtem.core.utils.T
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} CopyMixin
:canonical: abtem.core.utils.CopyMixin

```{autodoc2-docstring} abtem.core.utils.CopyMixin
:parser: rst
```

````{py:method} copy() -> typing.Self
:canonical: abtem.core.utils.CopyMixin.copy

```{autodoc2-docstring} abtem.core.utils.CopyMixin.copy
:parser: rst
```

````

`````

````{py:class} EqualityMixin
:canonical: abtem.core.utils.EqualityMixin

```{autodoc2-docstring} abtem.core.utils.EqualityMixin
:parser: rst
```

````

````{py:data} T
:canonical: abtem.core.utils.T
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.core.utils.T
:parser: rst
```

````

````{py:function} array_row_intersection(a, b)
:canonical: abtem.core.utils.array_row_intersection

```{autodoc2-docstring} abtem.core.utils.array_row_intersection
:parser: rst
```
````

````{py:function} ensure_list(x)
:canonical: abtem.core.utils.ensure_list

```{autodoc2-docstring} abtem.core.utils.ensure_list
:parser: rst
```
````

````{py:function} expand_dims_to_broadcast(arr1: numpy.ndarray | dask.array.core.Array, arr2: numpy.ndarray | dask.array.core.Array, match_dims: typing.Optional[tuple[tuple[int, ...], tuple[int, ...]]] = None, broadcast: bool = False) -> tuple[numpy.ndarray | dask.array.core.Array, numpy.ndarray | dask.array.core.Array]
:canonical: abtem.core.utils.expand_dims_to_broadcast

```{autodoc2-docstring} abtem.core.utils.expand_dims_to_broadcast
:parser: rst
```
````

````{py:function} flatten_list_of_lists(lst: list[list]) -> list
:canonical: abtem.core.utils.flatten_list_of_lists

```{autodoc2-docstring} abtem.core.utils.flatten_list_of_lists
:parser: rst
```
````

````{py:function} get_data_path(file: str) -> str
:canonical: abtem.core.utils.get_data_path

```{autodoc2-docstring} abtem.core.utils.get_data_path
:parser: rst
```
````

````{py:function} get_dtype(complex: bool = False) -> numpy.dtype
:canonical: abtem.core.utils.get_dtype

```{autodoc2-docstring} abtem.core.utils.get_dtype
:parser: rst
```
````

````{py:function} insert_empty_axis(match_axis1, match_axis2)
:canonical: abtem.core.utils.insert_empty_axis

```{autodoc2-docstring} abtem.core.utils.insert_empty_axis
:parser: rst
```
````

````{py:function} interleave(l1: list | tuple, l2: list | tuple) -> list | tuple
:canonical: abtem.core.utils.interleave

```{autodoc2-docstring} abtem.core.utils.interleave
:parser: rst
```
````

````{py:function} is_broadcastable(*shapes: tuple[int, ...]) -> bool | tuple[int, ...]
:canonical: abtem.core.utils.is_broadcastable

```{autodoc2-docstring} abtem.core.utils.is_broadcastable
:parser: rst
```
````

````{py:function} is_scalar(value) -> typing.TypeGuard[float | int | numpy.floating | numpy.integer]
:canonical: abtem.core.utils.is_scalar

```{autodoc2-docstring} abtem.core.utils.is_scalar
:parser: rst
```
````

````{py:function} itemset(arr: numpy.ndarray, args: int | slice | typing.Sequence[int], item: typing.Any) -> None
:canonical: abtem.core.utils.itemset

```{autodoc2-docstring} abtem.core.utils.itemset
:parser: rst
```
````

````{py:function} label_to_index(labels: numpy.ndarray, max_label: typing.Optional[int] = None, min_label: int = 0)
:canonical: abtem.core.utils.label_to_index

```{autodoc2-docstring} abtem.core.utils.label_to_index
:parser: rst
```
````

````{py:function} normalize_axes(axes: tuple[int, ...] | int, shape: tuple[int, ...]) -> tuple[int, ...]
:canonical: abtem.core.utils.normalize_axes

```{autodoc2-docstring} abtem.core.utils.normalize_axes
:parser: rst
```
````

````{py:function} number_to_tuple(value: abtem.core.utils.T | tuple[abtem.core.utils.T, ...], dimension: typing.Optional[int] = None) -> tuple[abtem.core.utils.T, ...]
:canonical: abtem.core.utils.number_to_tuple

```{autodoc2-docstring} abtem.core.utils.number_to_tuple
:parser: rst
```
````

````{py:function} safe_ceiling_int(n: float, tol: int = 7) -> int
:canonical: abtem.core.utils.safe_ceiling_int

```{autodoc2-docstring} abtem.core.utils.safe_ceiling_int
:parser: rst
```
````

````{py:function} safe_equality(a, b, exclude: tuple[str, ...] = ()) -> bool
:canonical: abtem.core.utils.safe_equality

```{autodoc2-docstring} abtem.core.utils.safe_equality
:parser: rst
```
````

````{py:function} safe_floor_int(n: float, tol: int = 7) -> int
:canonical: abtem.core.utils.safe_floor_int

```{autodoc2-docstring} abtem.core.utils.safe_floor_int
:parser: rst
```
````

````{py:function} tuple_range(length: int, offset: int = 0) -> tuple[int, ...]
:canonical: abtem.core.utils.tuple_range

```{autodoc2-docstring} abtem.core.utils.tuple_range
:parser: rst
```
````
