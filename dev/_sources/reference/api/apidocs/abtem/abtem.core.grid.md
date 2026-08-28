# {py:mod}`abtem.core.grid`

```{py:module} abtem.core.grid
```

```{autodoc2-docstring} abtem.core.grid
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Grid <abtem.core.grid.Grid>`
  - ```{autodoc2-docstring} abtem.core.grid.Grid
    :parser: rst
    :summary:
    ```
* - {py:obj}`HasGrid2DMixin <abtem.core.grid.HasGrid2DMixin>`
  - ```{autodoc2-docstring} abtem.core.grid.HasGrid2DMixin
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`adjusted_gpts <abtem.core.grid.adjusted_gpts>`
  - ```{autodoc2-docstring} abtem.core.grid.adjusted_gpts
    :parser: rst
    :summary:
    ```
* - {py:obj}`coordinate_grid <abtem.core.grid.coordinate_grid>`
  - ```{autodoc2-docstring} abtem.core.grid.coordinate_grid
    :parser: rst
    :summary:
    ```
* - {py:obj}`disk_meshgrid <abtem.core.grid.disk_meshgrid>`
  - ```{autodoc2-docstring} abtem.core.grid.disk_meshgrid
    :parser: rst
    :summary:
    ```
* - {py:obj}`disk_meshgrid_iter <abtem.core.grid.disk_meshgrid_iter>`
  - ```{autodoc2-docstring} abtem.core.grid.disk_meshgrid_iter
    :parser: rst
    :summary:
    ```
* - {py:obj}`polar_spatial_frequencies <abtem.core.grid.polar_spatial_frequencies>`
  - ```{autodoc2-docstring} abtem.core.grid.polar_spatial_frequencies
    :parser: rst
    :summary:
    ```
* - {py:obj}`real_space_grid <abtem.core.grid.real_space_grid>`
  - ```{autodoc2-docstring} abtem.core.grid.real_space_grid
    :parser: rst
    :summary:
    ```
* - {py:obj}`spatial_frequencies <abtem.core.grid.spatial_frequencies>`
  - ```{autodoc2-docstring} abtem.core.grid.spatial_frequencies
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_gpts <abtem.core.grid.validate_gpts>`
  - ```{autodoc2-docstring} abtem.core.grid.validate_gpts
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`T <abtem.core.grid.T>`
  - ```{autodoc2-docstring} abtem.core.grid.T
    :parser: rst
    :summary:
    ```
* - {py:obj}`U <abtem.core.grid.U>`
  - ```{autodoc2-docstring} abtem.core.grid.U
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} Grid(...)
:canonical: abtem.core.grid.Grid

Bases: {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.core.grid.Grid
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.grid.Grid.__init__
:parser: rst
```

````{py:method} check_is_defined(...)
:canonical: abtem.core.grid.Grid.check_is_defined

```{autodoc2-docstring} abtem.core.grid.Grid.check_is_defined
:parser: rst
```

````

````{py:method} check_match(...)
:canonical: abtem.core.grid.Grid.check_match

```{autodoc2-docstring} abtem.core.grid.Grid.check_match
:parser: rst
```

````

````{py:property} dimensions
:canonical: abtem.core.grid.Grid.dimensions
:type: int

```{autodoc2-docstring} abtem.core.grid.Grid.dimensions
:parser: rst
```

````

````{py:property} endpoint
:canonical: abtem.core.grid.Grid.endpoint
:type: tuple[bool] | tuple[bool, bool] | tuple[bool, ...]

```{autodoc2-docstring} abtem.core.grid.Grid.endpoint
:parser: rst
```

````

````{py:property} extent
:canonical: abtem.core.grid.Grid.extent
:type: tuple[float, ...] | None

```{autodoc2-docstring} abtem.core.grid.Grid.extent
:parser: rst
```

````

````{py:property} gpts
:canonical: abtem.core.grid.Grid.gpts
:type: tuple[int, ...] | None

```{autodoc2-docstring} abtem.core.grid.Grid.gpts
:parser: rst
```

````

````{py:method} match(...)
:canonical: abtem.core.grid.Grid.match

```{autodoc2-docstring} abtem.core.grid.Grid.match
:parser: rst
```

````

````{py:property} reciprocal_space_sampling
:canonical: abtem.core.grid.Grid.reciprocal_space_sampling
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.core.grid.Grid.reciprocal_space_sampling
:parser: rst
```

````

````{py:method} round_to_power(...) -> tuple[int, ...]
:canonical: abtem.core.grid.Grid.round_to_power

```{autodoc2-docstring} abtem.core.grid.Grid.round_to_power
:parser: rst
```

````

````{py:property} sampling
:canonical: abtem.core.grid.Grid.sampling
:type: tuple[float, ...] | None

```{autodoc2-docstring} abtem.core.grid.Grid.sampling
:parser: rst
```

````

````{py:method} spatial_frequencies()
:canonical: abtem.core.grid.Grid.spatial_frequencies

```{autodoc2-docstring} abtem.core.grid.Grid.spatial_frequencies
:parser: rst
```

````

`````

````{py:exception} GridUndefinedError()
:canonical: abtem.core.grid.GridUndefinedError

Bases: {py:obj}`Exception`

```{autodoc2-docstring} abtem.core.grid.GridUndefinedError
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.grid.GridUndefinedError.__init__
:parser: rst
```

````

`````{py:class} HasGrid2DMixin
:canonical: abtem.core.grid.HasGrid2DMixin

```{autodoc2-docstring} abtem.core.grid.HasGrid2DMixin
:parser: rst
```

````{py:property} extent
:canonical: abtem.core.grid.HasGrid2DMixin.extent
:type: tuple[float, float] | None

```{autodoc2-docstring} abtem.core.grid.HasGrid2DMixin.extent
:parser: rst
```

````

````{py:property} gpts
:canonical: abtem.core.grid.HasGrid2DMixin.gpts
:type: tuple[int, int] | None

```{autodoc2-docstring} abtem.core.grid.HasGrid2DMixin.gpts
:parser: rst
```

````

````{py:property} grid
:canonical: abtem.core.grid.HasGrid2DMixin.grid
:type: abtem.core.grid.Grid

```{autodoc2-docstring} abtem.core.grid.HasGrid2DMixin.grid
:parser: rst
```

````

````{py:method} match_grid(...)
:canonical: abtem.core.grid.HasGrid2DMixin.match_grid

```{autodoc2-docstring} abtem.core.grid.HasGrid2DMixin.match_grid
:parser: rst
```

````

````{py:property} reciprocal_space_sampling
:canonical: abtem.core.grid.HasGrid2DMixin.reciprocal_space_sampling
:type: tuple[float, float]

```{autodoc2-docstring} abtem.core.grid.HasGrid2DMixin.reciprocal_space_sampling
:parser: rst
```

````

````{py:property} sampling
:canonical: abtem.core.grid.HasGrid2DMixin.sampling
:type: tuple[float, float] | None

```{autodoc2-docstring} abtem.core.grid.HasGrid2DMixin.sampling
:parser: rst
```

````

`````

````{py:data} T
:canonical: abtem.core.grid.T
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.core.grid.T
:parser: rst
```

````

````{py:data} U
:canonical: abtem.core.grid.U
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.core.grid.U
:parser: rst
```

````

````{py:function} adjusted_gpts(...) -> tuple[tuple[float, ...], tuple[int, ...]]
:canonical: abtem.core.grid.adjusted_gpts

```{autodoc2-docstring} abtem.core.grid.adjusted_gpts
:parser: rst
```
````

````{py:function} coordinate_grid(...) -> tuple[numpy.ndarray, ...]
:canonical: abtem.core.grid.coordinate_grid

```{autodoc2-docstring} abtem.core.grid.coordinate_grid
:parser: rst
```
````

````{py:function} disk_meshgrid(...) -> numpy.ndarray
:canonical: abtem.core.grid.disk_meshgrid

```{autodoc2-docstring} abtem.core.grid.disk_meshgrid
:parser: rst
```
````

````{py:function} disk_meshgrid_iter(...)
:canonical: abtem.core.grid.disk_meshgrid_iter

```{autodoc2-docstring} abtem.core.grid.disk_meshgrid_iter
:parser: rst
```
````

````{py:function} polar_spatial_frequencies(...) -> tuple[numpy.ndarray, numpy.ndarray]
:canonical: abtem.core.grid.polar_spatial_frequencies

```{autodoc2-docstring} abtem.core.grid.polar_spatial_frequencies
:parser: rst
```
````

````{py:function} real_space_grid(...)
:canonical: abtem.core.grid.real_space_grid

```{autodoc2-docstring} abtem.core.grid.real_space_grid
:parser: rst
```
````

````{py:function} spatial_frequencies(...)
:canonical: abtem.core.grid.spatial_frequencies

```{autodoc2-docstring} abtem.core.grid.spatial_frequencies
:parser: rst
```
````

````{py:function} validate_gpts(...) -> tuple[int, ...]
:canonical: abtem.core.grid.validate_gpts

```{autodoc2-docstring} abtem.core.grid.validate_gpts
:parser: rst
```
````
