# {py:mod}`abtem.ebsd.measurements`

```{py:module} abtem.ebsd.measurements
```

```{autodoc2-docstring} abtem.ebsd.measurements
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EBSDPatternImages <abtem.ebsd.measurements.EBSDPatternImages>`
  - ```{autodoc2-docstring} abtem.ebsd.measurements.EBSDPatternImages
    :parser: rst
    :summary:
    ```
* - {py:obj}`ReferencePatternImages <abtem.ebsd.measurements.ReferencePatternImages>`
  - ```{autodoc2-docstring} abtem.ebsd.measurements.ReferencePatternImages
    :parser: rst
    :summary:
    ```
* - {py:obj}`SphericalPattern <abtem.ebsd.measurements.SphericalPattern>`
  - ```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} EBSDPatternImages(...)
:canonical: abtem.ebsd.measurements.EBSDPatternImages

Bases: {py:obj}`abtem.measurements.Images`

```{autodoc2-docstring} abtem.ebsd.measurements.EBSDPatternImages
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.measurements.EBSDPatternImages.__init__
:parser: rst
```

````{py:property} base_axes_metadata
:canonical: abtem.ebsd.measurements.EBSDPatternImages.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} detector_array
:canonical: abtem.ebsd.measurements.EBSDPatternImages.detector_array

```{autodoc2-docstring} abtem.ebsd.measurements.EBSDPatternImages.detector_array
:parser: rst
```

````

`````

`````{py:class} ReferencePatternImages(...)
:canonical: abtem.ebsd.measurements.ReferencePatternImages

Bases: {py:obj}`abtem.measurements.Images`

```{autodoc2-docstring} abtem.ebsd.measurements.ReferencePatternImages
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.measurements.ReferencePatternImages.__init__
:parser: rst
```

````{py:property} base_axes_metadata
:canonical: abtem.ebsd.measurements.ReferencePatternImages.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

`````

````{py:exception} SparseProjectionWarning()
:canonical: abtem.ebsd.measurements.SparseProjectionWarning

Bases: {py:obj}`UserWarning`

```{autodoc2-docstring} abtem.ebsd.measurements.SparseProjectionWarning
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.measurements.SparseProjectionWarning.__init__
:parser: rst
```

````

`````{py:class} SphericalPattern(...)
:canonical: abtem.ebsd.measurements.SphericalPattern

Bases: {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.__init__
:parser: rst
```

````{py:property} array
:canonical: abtem.ebsd.measurements.SphericalPattern.array
:type: numpy.ndarray | dask.array.core.Array

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.array
:parser: rst
```

````

````{py:method} bin(...) -> abtem.ebsd.measurements.ReferencePatternImages
:canonical: abtem.ebsd.measurements.SphericalPattern.bin

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.bin
:parser: rst
```

````

````{py:property} centrosymmetric
:canonical: abtem.ebsd.measurements.SphericalPattern.centrosymmetric
:type: typing.Optional[bool]

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.centrosymmetric
:parser: rst
```

````

````{py:method} compute(...) -> abtem.ebsd.measurements.SphericalPattern
:canonical: abtem.ebsd.measurements.SphericalPattern.compute

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.compute
:parser: rst
```

````

````{py:method} concatenate(...) -> abtem.ebsd.measurements.SphericalPattern
:canonical: abtem.ebsd.measurements.SphericalPattern.concatenate
:classmethod:

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.concatenate
:parser: rst
```

````

````{py:property} directions
:canonical: abtem.ebsd.measurements.SphericalPattern.directions
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.directions
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.ebsd.measurements.SphericalPattern.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.ebsd.measurements.SphericalPattern.ensemble_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.ensemble_shape
:parser: rst
```

````

````{py:method} from_zarr(...) -> abtem.ebsd.measurements.SphericalPattern
:canonical: abtem.ebsd.measurements.SphericalPattern.from_zarr
:classmethod:

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.from_zarr
:parser: rst
```

````

````{py:property} hemisphere
:canonical: abtem.ebsd.measurements.SphericalPattern.hemisphere
:type: str

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.hemisphere
:parser: rst
```

````

````{py:method} interpolate(...) -> abtem.ebsd.measurements.ReferencePatternImages
:canonical: abtem.ebsd.measurements.SphericalPattern.interpolate

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.interpolate
:parser: rst
```

````

````{py:method} interpolate_directions(...) -> numpy.ndarray
:canonical: abtem.ebsd.measurements.SphericalPattern.interpolate_directions

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.interpolate_directions
:parser: rst
```

````

````{py:property} is_lazy
:canonical: abtem.ebsd.measurements.SphericalPattern.is_lazy
:type: bool

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.is_lazy
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.ebsd.measurements.SphericalPattern.metadata
:type: dict

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.metadata
:parser: rst
```

````

````{py:property} northern
:canonical: abtem.ebsd.measurements.SphericalPattern.northern
:type: abtem.ebsd.measurements.SphericalPattern

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.northern
:parser: rst
```

````

````{py:method} project(...) -> abtem.ebsd.measurements.EBSDPatternImages
:canonical: abtem.ebsd.measurements.SphericalPattern.project

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.project
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.ebsd.measurements.SphericalPattern.show

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.show
:parser: rst
```

````

````{py:property} southern
:canonical: abtem.ebsd.measurements.SphericalPattern.southern
:type: abtem.ebsd.measurements.SphericalPattern

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.southern
:parser: rst
```

````

````{py:method} to_emsoft(...) -> None
:canonical: abtem.ebsd.measurements.SphericalPattern.to_emsoft

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.to_emsoft
:parser: rst
```

````

````{py:method} to_zarr(...) -> None
:canonical: abtem.ebsd.measurements.SphericalPattern.to_zarr

```{autodoc2-docstring} abtem.ebsd.measurements.SphericalPattern.to_zarr
:parser: rst
```

````

`````
