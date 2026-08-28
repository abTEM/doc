# {py:mod}`abtem.tilt`

```{py:module} abtem.tilt
```

```{autodoc2-docstring} abtem.tilt
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AxisAlignedBeamTilt <abtem.tilt.AxisAlignedBeamTilt>`
  - ```{autodoc2-docstring} abtem.tilt.AxisAlignedBeamTilt
    :parser: rst
    :summary:
    ```
* - {py:obj}`BaseBeamTilt <abtem.tilt.BaseBeamTilt>`
  -
* - {py:obj}`BeamTilt <abtem.tilt.BeamTilt>`
  - ```{autodoc2-docstring} abtem.tilt.BeamTilt
    :parser: rst
    :summary:
    ```
* - {py:obj}`BeamTilt2D <abtem.tilt.BeamTilt2D>`
  - ```{autodoc2-docstring} abtem.tilt.BeamTilt2D
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`precession_tilts <abtem.tilt.precession_tilts>`
  - ```{autodoc2-docstring} abtem.tilt.precession_tilts
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_tilt <abtem.tilt.validate_tilt>`
  - ```{autodoc2-docstring} abtem.tilt.validate_tilt
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`TiltType <abtem.tilt.TiltType>`
  - ```{autodoc2-docstring} abtem.tilt.TiltType
    :parser: rst
    :summary:
    ```
* - {py:obj}`TiltType2D <abtem.tilt.TiltType2D>`
  - ```{autodoc2-docstring} abtem.tilt.TiltType2D
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} AxisAlignedBeamTilt(tilt: abtem.tilt.TiltType = 0.0, direction: str = 'x')
:canonical: abtem.tilt.AxisAlignedBeamTilt

Bases: {py:obj}`abtem.distributions.DistributionFromValues`

```{autodoc2-docstring} abtem.tilt.AxisAlignedBeamTilt
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.tilt.AxisAlignedBeamTilt.__init__
:parser: rst
```

````{py:property} direction
:canonical: abtem.tilt.AxisAlignedBeamTilt.direction
:type: str

```{autodoc2-docstring} abtem.tilt.AxisAlignedBeamTilt.direction
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.tilt.AxisAlignedBeamTilt.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.tilt.AxisAlignedBeamTilt.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.tilt.AxisAlignedBeamTilt.metadata

```{autodoc2-docstring} abtem.tilt.AxisAlignedBeamTilt.metadata
:parser: rst
```

````

````{py:property} tilt
:canonical: abtem.tilt.AxisAlignedBeamTilt.tilt
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.tilt.AxisAlignedBeamTilt.tilt
:parser: rst
```

````

`````

`````{py:class} BaseBeamTilt(distributions: tuple[str, ...] = ())
:canonical: abtem.tilt.BaseBeamTilt

Bases: {py:obj}`abtem.transform.WavesToWavesTransform`

````{py:method} apply(waves: abtem.waves.Waves, max_batch: int | str = 'auto') -> abtem.waves.Waves
:canonical: abtem.tilt.BaseBeamTilt.apply

```{autodoc2-docstring} abtem.tilt.BaseBeamTilt.apply
:parser: rst
```

````

`````

`````{py:class} BeamTilt(tilt: tuple[float, float] | abtem.distributions.BaseDistribution | numpy.ndarray)
:canonical: abtem.tilt.BeamTilt

Bases: {py:obj}`abtem.tilt.BaseBeamTilt`

```{autodoc2-docstring} abtem.tilt.BeamTilt
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.tilt.BeamTilt.__init__
:parser: rst
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.tilt.BeamTilt.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.tilt.BeamTilt.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.tilt.BeamTilt.metadata

```{autodoc2-docstring} abtem.tilt.BeamTilt.metadata
:parser: rst
```

````

````{py:property} tilt
:canonical: abtem.tilt.BeamTilt.tilt
:type: tuple[float, float] | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.tilt.BeamTilt.tilt
:parser: rst
```

````

`````

`````{py:class} BeamTilt2D(tilt_x: abtem.distributions.BaseDistribution, tilt_y: abtem.distributions.BaseDistribution)
:canonical: abtem.tilt.BeamTilt2D

Bases: {py:obj}`abtem.tilt.BaseBeamTilt`

```{autodoc2-docstring} abtem.tilt.BeamTilt2D
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.tilt.BeamTilt2D.__init__
:parser: rst
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.tilt.BeamTilt2D.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_shape
:canonical: abtem.tilt.BeamTilt2D.ensemble_shape
:type: tuple[int, int]

````

````{py:property} metadata
:canonical: abtem.tilt.BeamTilt2D.metadata

````

````{py:property} shape
:canonical: abtem.tilt.BeamTilt2D.shape
:type: tuple[int, int]

````

````{py:property} tilt_x
:canonical: abtem.tilt.BeamTilt2D.tilt_x
:type: abtem.distributions.BaseDistribution | float

```{autodoc2-docstring} abtem.tilt.BeamTilt2D.tilt_x
:parser: rst
```

````

````{py:property} tilt_y
:canonical: abtem.tilt.BeamTilt2D.tilt_y
:type: abtem.distributions.BaseDistribution | float

```{autodoc2-docstring} abtem.tilt.BeamTilt2D.tilt_y
:parser: rst
```

````

`````

````{py:data} TiltType
:canonical: abtem.tilt.TiltType
:value: >
   None

```{autodoc2-docstring} abtem.tilt.TiltType
:parser: rst
```

````

````{py:data} TiltType2D
:canonical: abtem.tilt.TiltType2D
:value: >
   None

```{autodoc2-docstring} abtem.tilt.TiltType2D
:parser: rst
```

````

````{py:function} precession_tilts(precession_angle: float, num_samples: int, min_azimuth: float = 0.0, max_azimuth: float = 2 * np.pi, endpoint: bool = False)
:canonical: abtem.tilt.precession_tilts

```{autodoc2-docstring} abtem.tilt.precession_tilts
:parser: rst
```
````

````{py:function} validate_tilt(tilt: abtem.tilt.TiltType2D) -> BeamTilt | BeamTilt2D | AxisAlignedBeamTilt
:canonical: abtem.tilt.validate_tilt

```{autodoc2-docstring} abtem.tilt.validate_tilt
:parser: rst
```
````
