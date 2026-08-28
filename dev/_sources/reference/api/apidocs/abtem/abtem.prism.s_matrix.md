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

````{py:method} dummy_probes(scan: abtem.scan.BaseScan = None, ctf: abtem.transfer.CTF = None, plane: str = 'entrance', downsample: bool = True, **kwargs) -> abtem.waves.Probe
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

`````{py:class} SMatrix(semiangle_cutoff: float, energy: float, potential: ase.Atoms | abtem.potentials.iam.BasePotential = None, gpts: int | tuple[int, int] = None, sampling: float | tuple[float, float] = None, extent: float | tuple[float, float] = None, interpolation: int | tuple[int, int] = 1, downsample: bool | str = 'cutoff', device: str = None, store_on_host: bool = False)
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

````{py:method} build(lazy: bool = None, max_batch: int | str = 'auto', bound: bool = None) -> abtem.prism.s_matrix.SMatrixArray
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

````{py:property} metadata
:canonical: abtem.prism.s_matrix.SMatrix.metadata

````

````{py:method} multislice(potential=None, lazy: bool = None, max_batch: int | str = 'auto')
:canonical: abtem.prism.s_matrix.SMatrix.multislice

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrix.multislice
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

````{py:method} reduce(scan: numpy.ndarray | abtem.scan.BaseScan = None, detectors: abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector] = None, ctf: abtem.transfer.CTF | dict = None, reduction_scheme: str = 'auto', max_batch_multislice: str | int = 'auto', max_batch_reduction: str | int = 'auto', disable_s_matrix_chunks: bool = 'auto', lazy: bool = None) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
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

````{py:method} scan(scan: numpy.ndarray | abtem.scan.BaseScan = None, detectors: abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector] = None, ctf: abtem.transfer.CTF | dict = None, max_batch_multislice: str | int = 'auto', max_batch_reduction: str | int = 'auto', reduction_scheme: str = 'auto', disable_s_matrix_chunks: bool = 'auto', lazy: bool = None) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
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

````{py:property} wave_vectors
:canonical: abtem.prism.s_matrix.SMatrix.wave_vectors
:type: numpy.ndarray

````

````{py:property} window_extent
:canonical: abtem.prism.s_matrix.SMatrix.window_extent

````

````{py:property} window_gpts
:canonical: abtem.prism.s_matrix.SMatrix.window_gpts

````

`````

`````{py:class} SMatrixArray(array: numpy.ndarray, wave_vectors: numpy.ndarray, semiangle_cutoff: float, energy: float = None, interpolation: int | tuple[int, int] = (1, 1), sampling: float | tuple[float, float] = None, extent: float | tuple[float, float] = None, window_gpts: tuple[int, int] = (0, 0), window_offset: tuple[int, int] = (0, 0), periodic: tuple[bool, bool] = (True, True), device: str = None, ensemble_axes_metadata: list[abtem.core.axes.AxisMetadata] = None, metadata: dict = None)
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

````{py:method} copy_to_device(device: str) -> abtem.prism.s_matrix.SMatrixArray
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

````{py:method} from_array_and_metadata(axes_metadata, metadata)
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

````{py:method} multislice(potential: abtem.potentials.iam.BasePotential = None) -> abtem.prism.s_matrix.SMatrixArray
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

````{py:method} rechunk(chunks: abtem.core.chunks.Chunks, in_place: bool = True)
:canonical: abtem.prism.s_matrix.SMatrixArray.rechunk

````

````{py:method} reduce(scan: abtem.scan.BaseScan = None, ctf: abtem.transfer.CTF = None, detectors: abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector] = None, max_batch_reduction: int | str = 'auto', reduction_scheme: str = 'auto') -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.prism.s_matrix.SMatrixArray.reduce

```{autodoc2-docstring} abtem.prism.s_matrix.SMatrixArray.reduce
:parser: rst
```

````

````{py:method} scan(scan: abtem.scan.BaseScan = None, detectors: abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector] = None, ctf: abtem.transfer.CTF = None, max_batch_reduction: int | str = 'auto', rechunk: tuple[int, int] | str = 'auto')
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
