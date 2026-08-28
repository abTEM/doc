# {py:mod}`abtem.scan`

```{py:module} abtem.scan
```

```{autodoc2-docstring} abtem.scan
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseScan <abtem.scan.BaseScan>`
  - ```{autodoc2-docstring} abtem.scan.BaseScan
    :parser: rst
    :summary:
    ```
* - {py:obj}`CustomScan <abtem.scan.CustomScan>`
  - ```{autodoc2-docstring} abtem.scan.CustomScan
    :parser: rst
    :summary:
    ```
* - {py:obj}`GridScan <abtem.scan.GridScan>`
  - ```{autodoc2-docstring} abtem.scan.GridScan
    :parser: rst
    :summary:
    ```
* - {py:obj}`LineScan <abtem.scan.LineScan>`
  - ```{autodoc2-docstring} abtem.scan.LineScan
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_coordinate <abtem.scan.validate_coordinate>`
  - ```{autodoc2-docstring} abtem.scan.validate_coordinate
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_scan <abtem.scan.validate_scan>`
  - ```{autodoc2-docstring} abtem.scan.validate_scan
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ScanWithSampling <abtem.scan.ScanWithSampling>`
  - ```{autodoc2-docstring} abtem.scan.ScanWithSampling
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BaseScan(...)
:canonical: abtem.scan.BaseScan

Bases: {py:obj}`abtem.transform.ReciprocalSpaceMultiplication`

```{autodoc2-docstring} abtem.scan.BaseScan
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.scan.BaseScan.__init__
:parser: rst
```

````{py:property} ensemble_shape
:canonical: abtem.scan.BaseScan.ensemble_shape
:type: tuple[int, ...]

````

````{py:method} get_positions(...) -> numpy.ndarray
:canonical: abtem.scan.BaseScan.get_positions
:abstractmethod:

```{autodoc2-docstring} abtem.scan.BaseScan.get_positions
:parser: rst
```

````

````{py:property} limits
:canonical: abtem.scan.BaseScan.limits
:abstractmethod:

```{autodoc2-docstring} abtem.scan.BaseScan.limits
:parser: rst
```

````

````{py:method} match_probe(...)
:canonical: abtem.scan.BaseScan.match_probe
:abstractmethod:

```{autodoc2-docstring} abtem.scan.BaseScan.match_probe
:parser: rst
```

````

````{py:property} num_positions
:canonical: abtem.scan.BaseScan.num_positions
:type: int

```{autodoc2-docstring} abtem.scan.BaseScan.num_positions
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.scan.BaseScan.shape
:abstractmethod:
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.scan.BaseScan.shape
:parser: rst
```

````

`````

`````{py:class} CustomScan(...)
:canonical: abtem.scan.CustomScan

Bases: {py:obj}`abtem.scan.BaseScan`

```{autodoc2-docstring} abtem.scan.CustomScan
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.scan.CustomScan.__init__
:parser: rst
```

````{py:method} add_to_plot(...)
:canonical: abtem.scan.CustomScan.add_to_plot

```{autodoc2-docstring} abtem.scan.CustomScan.add_to_plot
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.scan.CustomScan.ensemble_axes_metadata

````

````{py:method} get_positions() -> numpy.ndarray
:canonical: abtem.scan.CustomScan.get_positions

````

````{py:property} limits
:canonical: abtem.scan.CustomScan.limits

````

````{py:method} match_probe(...)
:canonical: abtem.scan.CustomScan.match_probe

```{autodoc2-docstring} abtem.scan.CustomScan.match_probe
:parser: rst
```

````

````{py:property} positions
:canonical: abtem.scan.CustomScan.positions

```{autodoc2-docstring} abtem.scan.CustomScan.positions
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.scan.CustomScan.shape

````

`````

`````{py:class} GridScan(...)
:canonical: abtem.scan.GridScan

Bases: {py:obj}`abtem.core.grid.HasGrid2DMixin`, {py:obj}`abtem.scan.BaseScan`

```{autodoc2-docstring} abtem.scan.GridScan
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.scan.GridScan.__init__
:parser: rst
```

````{py:method} add_to_plot(...)
:canonical: abtem.scan.GridScan.add_to_plot

```{autodoc2-docstring} abtem.scan.GridScan.add_to_plot
:parser: rst
```

````

````{py:method} commensurate(...) -> abtem.scan.GridScan
:canonical: abtem.scan.GridScan.commensurate
:classmethod:

```{autodoc2-docstring} abtem.scan.GridScan.commensurate
:parser: rst
```

````

````{py:property} end
:canonical: abtem.scan.GridScan.end
:type: tuple[float, float] | None

```{autodoc2-docstring} abtem.scan.GridScan.end
:parser: rst
```

````

````{py:property} endpoint
:canonical: abtem.scan.GridScan.endpoint
:type: tuple[bool, bool]

```{autodoc2-docstring} abtem.scan.GridScan.endpoint
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.scan.GridScan.ensemble_axes_metadata

````

````{py:property} ensemble_shape
:canonical: abtem.scan.GridScan.ensemble_shape

````

````{py:method} get_positions() -> numpy.ndarray
:canonical: abtem.scan.GridScan.get_positions

````

````{py:property} limits
:canonical: abtem.scan.GridScan.limits

````

````{py:method} match_probe(...)
:canonical: abtem.scan.GridScan.match_probe

```{autodoc2-docstring} abtem.scan.GridScan.match_probe
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.scan.GridScan.shape
:type: tuple[int, int]

````

````{py:property} start
:canonical: abtem.scan.GridScan.start
:type: tuple[float, float] | None

```{autodoc2-docstring} abtem.scan.GridScan.start
:parser: rst
```

````

`````

`````{py:class} LineScan(...)
:canonical: abtem.scan.LineScan

Bases: {py:obj}`abtem.scan.BaseScan`

```{autodoc2-docstring} abtem.scan.LineScan
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.scan.LineScan.__init__
:parser: rst
```

````{py:method} add_margin(...)
:canonical: abtem.scan.LineScan.add_margin

```{autodoc2-docstring} abtem.scan.LineScan.add_margin
:parser: rst
```

````

````{py:method} add_to_axes(...)
:canonical: abtem.scan.LineScan.add_to_axes

```{autodoc2-docstring} abtem.scan.LineScan.add_to_axes
:parser: rst
```

````

````{py:method} add_to_plot(...)
:canonical: abtem.scan.LineScan.add_to_plot

```{autodoc2-docstring} abtem.scan.LineScan.add_to_plot
:parser: rst
```

````

````{py:property} angle
:canonical: abtem.scan.LineScan.angle

```{autodoc2-docstring} abtem.scan.LineScan.angle
:parser: rst
```

````

````{py:method} at_position(...)
:canonical: abtem.scan.LineScan.at_position
:classmethod:

```{autodoc2-docstring} abtem.scan.LineScan.at_position
:parser: rst
```

````

````{py:property} direction
:canonical: abtem.scan.LineScan.direction

```{autodoc2-docstring} abtem.scan.LineScan.direction
:parser: rst
```

````

````{py:property} end
:canonical: abtem.scan.LineScan.end
:type: tuple[float, float] | None

```{autodoc2-docstring} abtem.scan.LineScan.end
:parser: rst
```

````

````{py:property} endpoint
:canonical: abtem.scan.LineScan.endpoint
:type: bool

```{autodoc2-docstring} abtem.scan.LineScan.endpoint
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.scan.LineScan.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_shape
:canonical: abtem.scan.LineScan.ensemble_shape

````

````{py:property} extent
:canonical: abtem.scan.LineScan.extent
:type: float | None

```{autodoc2-docstring} abtem.scan.LineScan.extent
:parser: rst
```

````

````{py:method} get_positions(...) -> numpy.ndarray
:canonical: abtem.scan.LineScan.get_positions

````

````{py:property} gpts
:canonical: abtem.scan.LineScan.gpts
:type: int | None

```{autodoc2-docstring} abtem.scan.LineScan.gpts
:parser: rst
```

````

````{py:property} limits
:canonical: abtem.scan.LineScan.limits
:type: typing.Tuple[typing.Optional[typing.Tuple[float, float]], typing.Optional[typing.Tuple[float, float]]]

````

````{py:method} match_probe(...)
:canonical: abtem.scan.LineScan.match_probe

```{autodoc2-docstring} abtem.scan.LineScan.match_probe
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.scan.LineScan.metadata

````

````{py:property} sampling
:canonical: abtem.scan.LineScan.sampling
:type: float | None

```{autodoc2-docstring} abtem.scan.LineScan.sampling
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.scan.LineScan.shape
:type: tuple[int]

````

````{py:property} start
:canonical: abtem.scan.LineScan.start
:type: tuple[float, float] | None

```{autodoc2-docstring} abtem.scan.LineScan.start
:parser: rst
```

````

`````

````{py:data} ScanWithSampling
:canonical: abtem.scan.ScanWithSampling
:value: >
   None

```{autodoc2-docstring} abtem.scan.ScanWithSampling
:parser: rst
```

````

````{py:function} validate_coordinate(...) -> tuple[float, float] | None
:canonical: abtem.scan.validate_coordinate

```{autodoc2-docstring} abtem.scan.validate_coordinate
:parser: rst
```
````

````{py:function} validate_scan(...) -> BaseScan
:canonical: abtem.scan.validate_scan

```{autodoc2-docstring} abtem.scan.validate_scan
:parser: rst
```
````
