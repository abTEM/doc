# {py:mod}`abtem.ebsd.geometry`

```{py:module} abtem.ebsd.geometry
```

```{autodoc2-docstring} abtem.ebsd.geometry
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EBSDGeometry <abtem.ebsd.geometry.EBSDGeometry>`
  - ```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`bunge_rotation <abtem.ebsd.geometry.bunge_rotation>`
  - ```{autodoc2-docstring} abtem.ebsd.geometry.bunge_rotation
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} EBSDGeometry(...)
:canonical: abtem.ebsd.geometry.EBSDGeometry

Bases: {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.__init__
:parser: rst
```

````{py:property} azimuthal_angle
:canonical: abtem.ebsd.geometry.EBSDGeometry.azimuthal_angle
:type: float

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.azimuthal_angle
:parser: rst
```

````

````{py:property} camera_tilt
:canonical: abtem.ebsd.geometry.EBSDGeometry.camera_tilt
:type: float

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.camera_tilt
:parser: rst
```

````

````{py:property} detector_distance
:canonical: abtem.ebsd.geometry.EBSDGeometry.detector_distance
:type: float

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.detector_distance
:parser: rst
```

````

````{py:property} detector_to_sample
:canonical: abtem.ebsd.geometry.EBSDGeometry.detector_to_sample
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.detector_to_sample
:parser: rst
```

````

````{py:property} directions
:canonical: abtem.ebsd.geometry.EBSDGeometry.directions
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.directions
:parser: rst
```

````

````{py:property} pattern_center
:canonical: abtem.ebsd.geometry.EBSDGeometry.pattern_center
:type: tuple[float, float]

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.pattern_center
:parser: rst
```

````

````{py:property} pixel_size
:canonical: abtem.ebsd.geometry.EBSDGeometry.pixel_size
:type: float

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.pixel_size
:parser: rst
```

````

````{py:method} rotated_directions(...) -> numpy.ndarray
:canonical: abtem.ebsd.geometry.EBSDGeometry.rotated_directions

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.rotated_directions
:parser: rst
```

````

````{py:property} sample_tilt
:canonical: abtem.ebsd.geometry.EBSDGeometry.sample_tilt
:type: float

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.sample_tilt
:parser: rst
```

````

````{py:property} scintillator_coordinates
:canonical: abtem.ebsd.geometry.EBSDGeometry.scintillator_coordinates
:type: tuple[numpy.ndarray, numpy.ndarray]

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.scintillator_coordinates
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.ebsd.geometry.EBSDGeometry.shape
:type: tuple[int, int]

```{autodoc2-docstring} abtem.ebsd.geometry.EBSDGeometry.shape
:parser: rst
```

````

`````

````{py:function} bunge_rotation(...) -> numpy.ndarray
:canonical: abtem.ebsd.geometry.bunge_rotation

```{autodoc2-docstring} abtem.ebsd.geometry.bunge_rotation
:parser: rst
```
````
