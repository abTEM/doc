# {py:mod}`abtem.scan`

```{py:module} abtem.scan
```

```{autodoc2-docstring} abtem.scan
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseScan <abtem.scan.BaseScan>`
  - ```{autodoc2-docstring} abtem.scan.BaseScan
    :summary:
    ```
* - {py:obj}`CustomScan <abtem.scan.CustomScan>`
  - ```{autodoc2-docstring} abtem.scan.CustomScan
    :summary:
    ```
* - {py:obj}`GridScan <abtem.scan.GridScan>`
  - ```{autodoc2-docstring} abtem.scan.GridScan
    :summary:
    ```
* - {py:obj}`LineScan <abtem.scan.LineScan>`
  - ```{autodoc2-docstring} abtem.scan.LineScan
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_coordinate <abtem.scan.validate_coordinate>`
  - ```{autodoc2-docstring} abtem.scan.validate_coordinate
    :summary:
    ```
* - {py:obj}`validate_scan <abtem.scan.validate_scan>`
  - ```{autodoc2-docstring} abtem.scan.validate_scan
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`ScanWithSampling <abtem.scan.ScanWithSampling>`
  - ```{autodoc2-docstring} abtem.scan.ScanWithSampling
    :summary:
    ```
````

### API

`````{py:class} BaseScan(in_place: bool = False, distributions: tuple[str, ...] = ())
:canonical: abtem.scan.BaseScan

Bases: {py:obj}`abtem.transform.ReciprocalSpaceMultiplication`

```{autodoc2-docstring} abtem.scan.BaseScan
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.scan.BaseScan.__init__
```

````{py:property} ensemble_shape
:canonical: abtem.scan.BaseScan.ensemble_shape
:type: tuple[int, ...]

````

````{py:method} get_positions(*args, **kwargs) -> numpy.ndarray
:canonical: abtem.scan.BaseScan.get_positions
:abstractmethod:

```{autodoc2-docstring} abtem.scan.BaseScan.get_positions
```

````

````{py:property} limits
:canonical: abtem.scan.BaseScan.limits
:abstractmethod:

```{autodoc2-docstring} abtem.scan.BaseScan.limits
```

````

````{py:method} match_probe(probe: abtem.waves.Probe | abtem.prism.s_matrix.BaseSMatrix)
:canonical: abtem.scan.BaseScan.match_probe
:abstractmethod:

```{autodoc2-docstring} abtem.scan.BaseScan.match_probe
```

````

````{py:property} num_positions
:canonical: abtem.scan.BaseScan.num_positions
:type: int

```{autodoc2-docstring} abtem.scan.BaseScan.num_positions
```

````

````{py:property} shape
:canonical: abtem.scan.BaseScan.shape
:abstractmethod:
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.scan.BaseScan.shape
```

````

`````

`````{py:class} CustomScan(positions: numpy.ndarray | typing.Sequence = (0.0, 0.0), squeeze: bool = False)
:canonical: abtem.scan.CustomScan

Bases: {py:obj}`abtem.scan.BaseScan`

```{autodoc2-docstring} abtem.scan.CustomScan
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.scan.CustomScan.__init__
```

````{py:method} add_to_plot(ax, **kwargs)
:canonical: abtem.scan.CustomScan.add_to_plot

```{autodoc2-docstring} abtem.scan.CustomScan.add_to_plot
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

````{py:method} match_probe(probe: abtem.waves.Probe | abtem.prism.s_matrix.BaseSMatrix)
:canonical: abtem.scan.CustomScan.match_probe

```{autodoc2-docstring} abtem.scan.CustomScan.match_probe
```

````

````{py:property} positions
:canonical: abtem.scan.CustomScan.positions

```{autodoc2-docstring} abtem.scan.CustomScan.positions
```

````

````{py:property} shape
:canonical: abtem.scan.CustomScan.shape

````

`````

`````{py:class} GridScan(start: typing.Union[float, typing.Tuple[float, float], ase.Atom] = (0.0, 0.0), end: tuple[float, float] | ase.Atom | None = None, gpts: int | tuple[int, int] | None = None, sampling: float | tuple[float, float] | None = None, endpoint: bool | tuple[bool, bool] = False, fractional: bool = False, potential: abtem.potentials.iam.BasePotential | ase.Atoms | None = None)
:canonical: abtem.scan.GridScan

Bases: {py:obj}`abtem.core.grid.HasGrid2DMixin`, {py:obj}`abtem.scan.BaseScan`

```{autodoc2-docstring} abtem.scan.GridScan
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.scan.GridScan.__init__
```

````{py:method} add_to_plot(ax, alpha: float = 0.33, facecolor: str = 'r', edgecolor: str = 'r', **kwargs)
:canonical: abtem.scan.GridScan.add_to_plot

```{autodoc2-docstring} abtem.scan.GridScan.add_to_plot
```

````

````{py:property} end
:canonical: abtem.scan.GridScan.end
:type: tuple[float, float] | None

```{autodoc2-docstring} abtem.scan.GridScan.end
```

````

````{py:property} endpoint
:canonical: abtem.scan.GridScan.endpoint
:type: tuple[bool, bool]

```{autodoc2-docstring} abtem.scan.GridScan.endpoint
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

````{py:method} match_probe(probe: abtem.waves.Probe | abtem.prism.s_matrix.BaseSMatrix)
:canonical: abtem.scan.GridScan.match_probe

```{autodoc2-docstring} abtem.scan.GridScan.match_probe
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
```

````

`````

`````{py:class} LineScan(start: tuple[float, float] | ase.Atom = (0.0, 0.0), end: tuple[float, float] | ase.Atom | None = None, gpts: int | None = None, sampling: float | None = None, endpoint: bool = True, fractional: bool = False, potential: abtem.potentials.iam.BasePotential | ase.Atoms | None = None)
:canonical: abtem.scan.LineScan

Bases: {py:obj}`abtem.scan.BaseScan`

```{autodoc2-docstring} abtem.scan.LineScan
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.scan.LineScan.__init__
```

````{py:method} add_margin(margin: float | tuple[float, float])
:canonical: abtem.scan.LineScan.add_margin

```{autodoc2-docstring} abtem.scan.LineScan.add_margin
```

````

````{py:method} add_to_axes(*args, **kwargs)
:canonical: abtem.scan.LineScan.add_to_axes

```{autodoc2-docstring} abtem.scan.LineScan.add_to_axes
```

````

````{py:method} add_to_plot(ax, width: float = 0.0, **kwargs)
:canonical: abtem.scan.LineScan.add_to_plot

```{autodoc2-docstring} abtem.scan.LineScan.add_to_plot
```

````

````{py:property} angle
:canonical: abtem.scan.LineScan.angle

```{autodoc2-docstring} abtem.scan.LineScan.angle
```

````

````{py:method} at_position(center: tuple[float, float] | ase.Atom, extent: float = 1.0, angle: float = 0.0, gpts: int | None = None, sampling: float | None = None, endpoint: bool = True)
:canonical: abtem.scan.LineScan.at_position
:classmethod:

```{autodoc2-docstring} abtem.scan.LineScan.at_position
```

````

````{py:property} direction
:canonical: abtem.scan.LineScan.direction

```{autodoc2-docstring} abtem.scan.LineScan.direction
```

````

````{py:property} end
:canonical: abtem.scan.LineScan.end
:type: tuple[float, float] | None

```{autodoc2-docstring} abtem.scan.LineScan.end
```

````

````{py:property} endpoint
:canonical: abtem.scan.LineScan.endpoint
:type: bool

```{autodoc2-docstring} abtem.scan.LineScan.endpoint
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
```

````

````{py:method} get_positions(chunks: int | None = None, lazy: bool = False) -> numpy.ndarray
:canonical: abtem.scan.LineScan.get_positions

````

````{py:property} gpts
:canonical: abtem.scan.LineScan.gpts
:type: int | None

```{autodoc2-docstring} abtem.scan.LineScan.gpts
```

````

````{py:property} limits
:canonical: abtem.scan.LineScan.limits
:type: typing.Tuple[typing.Optional[typing.Tuple[float, float]], typing.Optional[typing.Tuple[float, float]]]

````

````{py:method} match_probe(probe: abtem.waves.Probe | abtem.prism.s_matrix.BaseSMatrix)
:canonical: abtem.scan.LineScan.match_probe

```{autodoc2-docstring} abtem.scan.LineScan.match_probe
```

````

````{py:property} metadata
:canonical: abtem.scan.LineScan.metadata

````

````{py:property} sampling
:canonical: abtem.scan.LineScan.sampling
:type: float | None

```{autodoc2-docstring} abtem.scan.LineScan.sampling
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
```

````

`````

````{py:data} ScanWithSampling
:canonical: abtem.scan.ScanWithSampling
:value: >
   None

```{autodoc2-docstring} abtem.scan.ScanWithSampling
```

````

````{py:function} validate_coordinate(coordinate: float | tuple[float, float] | ase.Atom | None, potential: abtem.potentials.iam.BasePotential | ase.Atoms | None = None, fractional: bool = False) -> tuple[float, float] | None
:canonical: abtem.scan.validate_coordinate

```{autodoc2-docstring} abtem.scan.validate_coordinate
```
````

````{py:function} validate_scan(scan: typing.Optional[typing.Sequence | numpy.ndarray | BaseScan], probe: abtem.waves.Probe | None = None) -> BaseScan
:canonical: abtem.scan.validate_scan

```{autodoc2-docstring} abtem.scan.validate_scan
```
````
