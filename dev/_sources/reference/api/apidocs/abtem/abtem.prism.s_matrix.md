# {py:mod}`abtem.prism.s_matrix`

```{py:module} abtem.prism.s_matrix
```

```{autodoc2-docstring} abtem.prism.s_matrix
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseSMatrix <abtem.prism.s_matrix.BaseSMatrix>`
  - ```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix
    :parser: rst
    :summary:
    ```
* - {py:obj}`CompressedSMatrixArray <abtem.prism.s_matrix.CompressedSMatrixArray>`
  - ```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray
    :parser: rst
    :summary:
    ```
* - {py:obj}`SMatrix <abtem.prism.s_matrix.SMatrix>`
  - ```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix
    :parser: rst
    :summary:
    ```
* - {py:obj}`SMatrixArray <abtem.prism.s_matrix.SMatrixArray>`
  - ```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BaseSMatrix
:canonical: abtem.prism.s_matrix.BaseSMatrix

Bases: {py:obj}`abtem.waves.BaseWaves`

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix
:parser: rst
```

````{py:property} base_axes_metadata
:canonical: abtem.prism.s_matrix.BaseSMatrix.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} device
:canonical: abtem.prism.s_matrix.BaseSMatrix.device

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.device
:parser: rst
```

````

````{py:method} dummy_probes(...) -> abtem.waves.Probe
:canonical: abtem.prism.s_matrix.BaseSMatrix.dummy_probes

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.dummy_probes
:parser: rst
```

````

````{py:attribute} ensemble_axes_metadata
:canonical: abtem.prism.s_matrix.BaseSMatrix.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]
:value: >
   None

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.ensemble_axes_metadata
:parser: rst
```

````

````{py:attribute} ensemble_shape
:canonical: abtem.prism.s_matrix.BaseSMatrix.ensemble_shape
:type: tuple[int, ...]
:value: >
   None

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.ensemble_shape
:parser: rst
```

````

````{py:property} interpolation
:canonical: abtem.prism.s_matrix.BaseSMatrix.interpolation
:abstractmethod:

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.interpolation
:parser: rst
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.prism.s_matrix.BaseSMatrix.semiangle_cutoff
:abstractmethod:
:type: float

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.semiangle_cutoff
:parser: rst
```

````

````{py:property} wave_vectors
:canonical: abtem.prism.s_matrix.BaseSMatrix.wave_vectors
:abstractmethod:
:type: numpy.ndarray

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.wave_vectors
:parser: rst
```

````

````{py:property} window_extent
:canonical: abtem.prism.s_matrix.BaseSMatrix.window_extent
:abstractmethod:

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.window_extent
:parser: rst
```

````

````{py:property} window_gpts
:canonical: abtem.prism.s_matrix.BaseSMatrix.window_gpts
:abstractmethod:

```{autodoc2-docstring} abtem.prism.s_matrix.BaseSMatrix.window_gpts
:parser: rst
```

````

`````

`````{py:class} CompressedSMatrixArray(...)
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray

Bases: {py:obj}`abtem.prism.s_matrix.BaseSMatrix`, {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.__init__
:parser: rst
```

````{py:property} blend_angle
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.blend_angle
:type: float | None

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.blend_angle
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.ensemble_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.ensemble_shape
:parser: rst
```

````

````{py:property} interpolation
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.interpolation
:type: tuple[int, int]

````

````{py:property} max_batch_expansion
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.max_batch_expansion
:type: int | str

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.max_batch_expansion
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.metadata
:type: dict

````

````{py:property} rank
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.rank
:type: int

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.rank
:parser: rst
```

````

````{py:method} reduce(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.reduce

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.reduce
:parser: rst
```

````

````{py:method} scan(...)
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.scan

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.scan
:parser: rst
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.semiangle_cutoff
:type: float

````

````{py:property} sigma
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.sigma
:type: numpy.ndarray

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.sigma
:parser: rst
```

````

````{py:property} singular_values
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.singular_values
:type: numpy.ndarray

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.singular_values
:parser: rst
```

````

````{py:property} u
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.u
:type: numpy.ndarray

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.u
:parser: rst
```

````

````{py:property} vh_dense
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.vh_dense
:type: numpy.ndarray

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.vh_dense
:parser: rst
```

````

````{py:property} wave_vectors
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.wave_vectors
:type: numpy.ndarray

```{autodoc2-docstring} abtem.prism.s_matrix.CompressedSMatrixArray.wave_vectors
:parser: rst
```

````

````{py:property} window_extent
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.window_extent
:type: tuple[float, float]

````

````{py:property} window_gpts
:canonical: abtem.prism.s_matrix.CompressedSMatrixArray.window_gpts
:type: tuple[int, int]

````

`````

`````{py:class} SMatrix(...)
:canonical: abtem.prism.s_matrix.SMatrix

Bases: {py:obj}`abtem.prism.s_matrix.BaseSMatrix`, {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.__init__
:parser: rst
```

````{py:property} base_shape
:canonical: abtem.prism.s_matrix.SMatrix.base_shape
:type: tuple[int, int, int]

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.base_shape
:parser: rst
```

````

````{py:property} blend_angle
:canonical: abtem.prism.s_matrix.SMatrix.blend_angle
:type: float | str | None

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.blend_angle
:parser: rst
```

````

````{py:method} build(...) -> abtem.prism.s_matrix.SMatrixArray | abtem.prism.s_matrix.CompressedSMatrixArray
:canonical: abtem.prism.s_matrix.SMatrix.build

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.build
:parser: rst
```

````

````{py:property} downsample
:canonical: abtem.prism.s_matrix.SMatrix.downsample
:type: str | bool

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.downsample
:parser: rst
```

````

````{py:property} downsampled_gpts
:canonical: abtem.prism.s_matrix.SMatrix.downsampled_gpts
:type: tuple[int, int]

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.downsampled_gpts
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.prism.s_matrix.SMatrix.ensemble_axes_metadata

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.prism.s_matrix.SMatrix.ensemble_shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.ensemble_shape
:parser: rst
```

````

````{py:property} interpolation
:canonical: abtem.prism.s_matrix.SMatrix.interpolation
:type: tuple[int, int]

````

````{py:property} max_batch_expansion
:canonical: abtem.prism.s_matrix.SMatrix.max_batch_expansion
:type: int | str

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.max_batch_expansion
:parser: rst
```

````

````{py:property} max_rank
:canonical: abtem.prism.s_matrix.SMatrix.max_rank
:type: int | None

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.max_rank
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.prism.s_matrix.SMatrix.metadata

````

````{py:method} multislice(...)
:canonical: abtem.prism.s_matrix.SMatrix.multislice

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.multislice
:parser: rst
```

````

````{py:property} position_quantization
:canonical: abtem.prism.s_matrix.SMatrix.position_quantization
:type: int | None

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.position_quantization
:parser: rst
```

````

````{py:property} potential
:canonical: abtem.prism.s_matrix.SMatrix.potential
:type: abtem.potentials.iam.BasePotential

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.potential
:parser: rst
```

````

````{py:method} reduce(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.prism.s_matrix.SMatrix.reduce

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.reduce
:parser: rst
```

````

````{py:method} round_gpts_to_interpolation() -> abtem.prism.s_matrix.SMatrix
:canonical: abtem.prism.s_matrix.SMatrix.round_gpts_to_interpolation

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.round_gpts_to_interpolation
:parser: rst
```

````

````{py:method} scan(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.prism.s_matrix.SMatrix.scan

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.scan
:parser: rst
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.prism.s_matrix.SMatrix.semiangle_cutoff
:type: float

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.semiangle_cutoff
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.prism.s_matrix.SMatrix.shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.shape
:parser: rst
```

````

````{py:property} store_on_host
:canonical: abtem.prism.s_matrix.SMatrix.store_on_host
:type: bool

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.store_on_host
:parser: rst
```

````

````{py:property} tilt
:canonical: abtem.prism.s_matrix.SMatrix.tilt

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.tilt
:parser: rst
```

````

````{py:property} tolerance
:canonical: abtem.prism.s_matrix.SMatrix.tolerance
:type: float

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.tolerance
:parser: rst
```

````

````{py:method} transition_potential_scan(...)
:canonical: abtem.prism.s_matrix.SMatrix.transition_potential_scan

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.transition_potential_scan
:parser: rst
```

````

````{py:property} upsample
:canonical: abtem.prism.s_matrix.SMatrix.upsample
:type: bool

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.upsample
:parser: rst
```

````

````{py:property} wave_vectors
:canonical: abtem.prism.s_matrix.SMatrix.wave_vectors
:type: numpy.ndarray

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.wave_vectors
:parser: rst
```

````

````{py:property} window_extent
:canonical: abtem.prism.s_matrix.SMatrix.window_extent

````

````{py:property} window_gpts
:canonical: abtem.prism.s_matrix.SMatrix.window_gpts

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.window_gpts
:parser: rst
```

````

`````

`````{py:class} SMatrixArray(...)
:canonical: abtem.prism.s_matrix.SMatrixArray

Bases: {py:obj}`abtem.prism.s_matrix.BaseSMatrix`, {py:obj}`abtem.array.ArrayObject`

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.__init__
:parser: rst
```

````{py:method} copy_to_device(...) -> abtem.prism.s_matrix.SMatrixArray
:canonical: abtem.prism.s_matrix.SMatrixArray.copy_to_device

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.copy_to_device
:parser: rst
```

````

````{py:property} device
:canonical: abtem.prism.s_matrix.SMatrixArray.device

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.device
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.prism.s_matrix.SMatrixArray.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.prism.s_matrix.SMatrixArray.ensemble_shape
:type: tuple[int, int]

````

````{py:method} from_array_and_metadata(...)
:canonical: abtem.prism.s_matrix.SMatrixArray.from_array_and_metadata
:abstractmethod:

````

````{py:property} interpolation
:canonical: abtem.prism.s_matrix.SMatrixArray.interpolation
:type: tuple[int, int]

````

````{py:property} metadata
:canonical: abtem.prism.s_matrix.SMatrixArray.metadata
:type: dict

````

````{py:method} multislice(...) -> abtem.prism.s_matrix.SMatrixArray
:canonical: abtem.prism.s_matrix.SMatrixArray.multislice

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.multislice
:parser: rst
```

````

````{py:property} periodic
:canonical: abtem.prism.s_matrix.SMatrixArray.periodic
:type: tuple[bool, bool]

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.periodic
:parser: rst
```

````

````{py:method} rechunk(...)
:canonical: abtem.prism.s_matrix.SMatrixArray.rechunk

````

````{py:method} reduce(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.prism.s_matrix.SMatrixArray.reduce

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.reduce
:parser: rst
```

````

````{py:method} scan(...)
:canonical: abtem.prism.s_matrix.SMatrixArray.scan

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.scan
:parser: rst
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.prism.s_matrix.SMatrixArray.semiangle_cutoff
:type: float

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.semiangle_cutoff
:parser: rst
```

````

````{py:property} storage_device
:canonical: abtem.prism.s_matrix.SMatrixArray.storage_device

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.storage_device
:parser: rst
```

````

````{py:property} wave_vectors
:canonical: abtem.prism.s_matrix.SMatrixArray.wave_vectors
:type: numpy.ndarray

````

````{py:property} waves
:canonical: abtem.prism.s_matrix.SMatrixArray.waves
:type: abtem.waves.Waves

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.waves
:parser: rst
```

````

````{py:property} window_extent
:canonical: abtem.prism.s_matrix.SMatrixArray.window_extent
:type: tuple[float, float]

````

````{py:property} window_gpts
:canonical: abtem.prism.s_matrix.SMatrixArray.window_gpts
:type: tuple[int, int]

````

````{py:property} window_offset
:canonical: abtem.prism.s_matrix.SMatrixArray.window_offset
:type: tuple[float, float]

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.window_offset
:parser: rst
```

````

`````
