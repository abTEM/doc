# {py:mod}`abtem.ebsd.detectors`

```{py:module} abtem.ebsd.detectors
```

```{autodoc2-docstring} abtem.ebsd.detectors
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BackscatterDetector <abtem.ebsd.detectors.BackscatterDetector>`
  - ```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`small_angle_error <abtem.ebsd.detectors.small_angle_error>`
  - ```{autodoc2-docstring} abtem.ebsd.detectors.small_angle_error
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BackscatterDetector(...)
:canonical: abtem.ebsd.detectors.BackscatterDetector

Bases: {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.__init__
:parser: rst
```

````{py:property} base_shape
:canonical: abtem.ebsd.detectors.BackscatterDetector.base_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.base_shape
:parser: rst
```

````

````{py:property} directions
:canonical: abtem.ebsd.detectors.BackscatterDetector.directions
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.directions
:parser: rst
```

````

````{py:property} gpts
:canonical: abtem.ebsd.detectors.BackscatterDetector.gpts
:type: typing.Optional[int]

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.gpts
:parser: rst
```

````

````{py:property} is_grid
:canonical: abtem.ebsd.detectors.BackscatterDetector.is_grid
:type: bool

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.is_grid
:parser: rst
```

````

````{py:property} max_angle
:canonical: abtem.ebsd.detectors.BackscatterDetector.max_angle
:type: typing.Optional[float]

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.max_angle
:parser: rst
```

````

````{py:property} max_scattering_angle
:canonical: abtem.ebsd.detectors.BackscatterDetector.max_scattering_angle
:type: float

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.max_scattering_angle
:parser: rst
```

````

````{py:method} reciprocal_sampling(...) -> float
:canonical: abtem.ebsd.detectors.BackscatterDetector.reciprocal_sampling

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.reciprocal_sampling
:parser: rst
```

````

````{py:method} transverse_wave_vectors(...) -> numpy.ndarray
:canonical: abtem.ebsd.detectors.BackscatterDetector.transverse_wave_vectors

```{autodoc2-docstring} abtem.ebsd.detectors.BackscatterDetector.transverse_wave_vectors
:parser: rst
```

````

`````

````{py:function} small_angle_error(...) -> float
:canonical: abtem.ebsd.detectors.small_angle_error

```{autodoc2-docstring} abtem.ebsd.detectors.small_angle_error
:parser: rst
```
````
