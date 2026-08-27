# {py:mod}`abtem.core.utils`

```{py:module} abtem.core.utils
```

```{autodoc2-docstring} abtem.core.utils
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CopyMixin <abtem.core.utils.CopyMixin>`
  - ```{autodoc2-docstring} abtem.core.utils.CopyMixin
    :summary:
    ```
* - {py:obj}`EqualityMixin <abtem.core.utils.EqualityMixin>`
  - ```{autodoc2-docstring} abtem.core.utils.EqualityMixin
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`number_to_tuple <abtem.core.utils.number_to_tuple>`
  - ```{autodoc2-docstring} abtem.core.utils.number_to_tuple
    :summary:
    ```
* - {py:obj}`itemset <abtem.core.utils.itemset>`
  - ```{autodoc2-docstring} abtem.core.utils.itemset
    :summary:
    ```
* - {py:obj}`is_broadcastable <abtem.core.utils.is_broadcastable>`
  - ```{autodoc2-docstring} abtem.core.utils.is_broadcastable
    :summary:
    ```
* - {py:obj}`safe_equality <abtem.core.utils.safe_equality>`
  - ```{autodoc2-docstring} abtem.core.utils.safe_equality
    :summary:
    ```
* - {py:obj}`array_row_intersection <abtem.core.utils.array_row_intersection>`
  - ```{autodoc2-docstring} abtem.core.utils.array_row_intersection
    :summary:
    ```
* - {py:obj}`safe_floor_int <abtem.core.utils.safe_floor_int>`
  - ```{autodoc2-docstring} abtem.core.utils.safe_floor_int
    :summary:
    ```
* - {py:obj}`safe_ceiling_int <abtem.core.utils.safe_ceiling_int>`
  - ```{autodoc2-docstring} abtem.core.utils.safe_ceiling_int
    :summary:
    ```
* - {py:obj}`ensure_list <abtem.core.utils.ensure_list>`
  - ```{autodoc2-docstring} abtem.core.utils.ensure_list
    :summary:
    ```
* - {py:obj}`insert_empty_axis <abtem.core.utils.insert_empty_axis>`
  - ```{autodoc2-docstring} abtem.core.utils.insert_empty_axis
    :summary:
    ```
* - {py:obj}`normalize_axes <abtem.core.utils.normalize_axes>`
  - ```{autodoc2-docstring} abtem.core.utils.normalize_axes
    :summary:
    ```
* - {py:obj}`expand_dims_to_broadcast <abtem.core.utils.expand_dims_to_broadcast>`
  - ```{autodoc2-docstring} abtem.core.utils.expand_dims_to_broadcast
    :summary:
    ```
* - {py:obj}`tuple_range <abtem.core.utils.tuple_range>`
  - ```{autodoc2-docstring} abtem.core.utils.tuple_range
    :summary:
    ```
* - {py:obj}`interleave <abtem.core.utils.interleave>`
  - ```{autodoc2-docstring} abtem.core.utils.interleave
    :summary:
    ```
* - {py:obj}`flatten_list_of_lists <abtem.core.utils.flatten_list_of_lists>`
  - ```{autodoc2-docstring} abtem.core.utils.flatten_list_of_lists
    :summary:
    ```
* - {py:obj}`label_to_index <abtem.core.utils.label_to_index>`
  - ```{autodoc2-docstring} abtem.core.utils.label_to_index
    :summary:
    ```
* - {py:obj}`get_data_path <abtem.core.utils.get_data_path>`
  - ```{autodoc2-docstring} abtem.core.utils.get_data_path
    :summary:
    ```
* - {py:obj}`get_dtype <abtem.core.utils.get_dtype>`
  - ```{autodoc2-docstring} abtem.core.utils.get_dtype
    :summary:
    ```
* - {py:obj}`is_scalar <abtem.core.utils.is_scalar>`
  - ```{autodoc2-docstring} abtem.core.utils.is_scalar
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`T <abtem.core.utils.T>`
  - ```{autodoc2-docstring} abtem.core.utils.T
    :summary:
    ```
````

### API

````{py:data} T
:canonical: abtem.core.utils.T
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.core.utils.T
```

````

````{py:function} number_to_tuple(value: abtem.core.utils.T | tuple[abtem.core.utils.T, ...], dimension: typing.Optional[int] = None) -> tuple[abtem.core.utils.T, ...]
:canonical: abtem.core.utils.number_to_tuple

```{autodoc2-docstring} abtem.core.utils.number_to_tuple
```
````

````{py:function} itemset(arr: numpy.ndarray, args: int | slice | typing.Sequence[int], item: typing.Any) -> None
:canonical: abtem.core.utils.itemset

```{autodoc2-docstring} abtem.core.utils.itemset
```
````

````{py:function} is_broadcastable(*shapes: tuple[int, ...]) -> bool | tuple[int, ...]
:canonical: abtem.core.utils.is_broadcastable

```{autodoc2-docstring} abtem.core.utils.is_broadcastable
```
````

`````{py:class} CopyMixin
:canonical: abtem.core.utils.CopyMixin

```{autodoc2-docstring} abtem.core.utils.CopyMixin
```

````{py:method} copy() -> typing.Self
:canonical: abtem.core.utils.CopyMixin.copy

```{autodoc2-docstring} abtem.core.utils.CopyMixin.copy
```

````

`````

````{py:function} safe_equality(a, b, exclude: tuple[str, ...] = ()) -> bool
:canonical: abtem.core.utils.safe_equality

```{autodoc2-docstring} abtem.core.utils.safe_equality
```
````

````{py:class} EqualityMixin
:canonical: abtem.core.utils.EqualityMixin

```{autodoc2-docstring} abtem.core.utils.EqualityMixin
```

````

````{py:function} array_row_intersection(a, b)
:canonical: abtem.core.utils.array_row_intersection

```{autodoc2-docstring} abtem.core.utils.array_row_intersection
```
````

````{py:function} safe_floor_int(n: float, tol: int = 7) -> int
:canonical: abtem.core.utils.safe_floor_int

```{autodoc2-docstring} abtem.core.utils.safe_floor_int
```
````

````{py:function} safe_ceiling_int(n: float, tol: int = 7) -> int
:canonical: abtem.core.utils.safe_ceiling_int

```{autodoc2-docstring} abtem.core.utils.safe_ceiling_int
```
````

````{py:function} ensure_list(x)
:canonical: abtem.core.utils.ensure_list

```{autodoc2-docstring} abtem.core.utils.ensure_list
```
````

````{py:function} insert_empty_axis(match_axis1, match_axis2)
:canonical: abtem.core.utils.insert_empty_axis

```{autodoc2-docstring} abtem.core.utils.insert_empty_axis
```
````

````{py:function} normalize_axes(axes: tuple[int, ...] | int, shape: tuple[int, ...]) -> tuple[int, ...]
:canonical: abtem.core.utils.normalize_axes

```{autodoc2-docstring} abtem.core.utils.normalize_axes
```
````

````{py:function} expand_dims_to_broadcast(arr1: numpy.ndarray | dask.array.core.Array, arr2: numpy.ndarray | dask.array.core.Array, match_dims: typing.Optional[tuple[tuple[int, ...], tuple[int, ...]]] = None, broadcast: bool = False) -> tuple[numpy.ndarray | dask.array.core.Array, numpy.ndarray | dask.array.core.Array]
:canonical: abtem.core.utils.expand_dims_to_broadcast

```{autodoc2-docstring} abtem.core.utils.expand_dims_to_broadcast
```
````

````{py:function} tuple_range(length: int, offset: int = 0) -> tuple[int, ...]
:canonical: abtem.core.utils.tuple_range

```{autodoc2-docstring} abtem.core.utils.tuple_range
```
````

````{py:function} interleave(l1: list | tuple, l2: list | tuple) -> list | tuple
:canonical: abtem.core.utils.interleave

```{autodoc2-docstring} abtem.core.utils.interleave
```
````

````{py:function} flatten_list_of_lists(lst: list[list]) -> list
:canonical: abtem.core.utils.flatten_list_of_lists

```{autodoc2-docstring} abtem.core.utils.flatten_list_of_lists
```
````

````{py:function} label_to_index(labels: numpy.ndarray, max_label: typing.Optional[int] = None, min_label: int = 0)
:canonical: abtem.core.utils.label_to_index

```{autodoc2-docstring} abtem.core.utils.label_to_index
```
````

````{py:function} get_data_path(file: str) -> str
:canonical: abtem.core.utils.get_data_path

```{autodoc2-docstring} abtem.core.utils.get_data_path
```
````

````{py:function} get_dtype(complex: bool = False) -> numpy.dtype
:canonical: abtem.core.utils.get_dtype

```{autodoc2-docstring} abtem.core.utils.get_dtype
```
````

````{py:function} is_scalar(value) -> typing.TypeGuard[float | int | numpy.floating | numpy.integer]
:canonical: abtem.core.utils.is_scalar

```{autodoc2-docstring} abtem.core.utils.is_scalar
```
````
