# {py:mod}`abtem.waves`

```{py:module} abtem.waves
```

```{autodoc2-docstring} abtem.waves
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseWaves <abtem.waves.BaseWaves>`
  - ```{autodoc2-docstring} abtem.waves.BaseWaves
    :summary:
    ```
* - {py:obj}`PlaneWave <abtem.waves.PlaneWave>`
  - ```{autodoc2-docstring} abtem.waves.PlaneWave
    :summary:
    ```
* - {py:obj}`Probe <abtem.waves.Probe>`
  - ```{autodoc2-docstring} abtem.waves.Probe
    :summary:
    ```
* - {py:obj}`Waves <abtem.waves.Waves>`
  - ```{autodoc2-docstring} abtem.waves.Waves
    :summary:
    ```
* - {py:obj}`WavesBuilder <abtem.waves.WavesBuilder>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`reduce_ensemble <abtem.waves.reduce_ensemble>`
  - ```{autodoc2-docstring} abtem.waves.reduce_ensemble
    :summary:
    ```
````

### API

`````{py:class} BaseWaves
:canonical: abtem.waves.BaseWaves

Bases: {py:obj}`abtem.core.grid.HasGrid2DMixin`, {py:obj}`abtem.core.energy.HasAcceleratorMixin`

```{autodoc2-docstring} abtem.waves.BaseWaves
```

````{py:property} angular_sampling
:canonical: abtem.waves.BaseWaves.angular_sampling
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.angular_sampling
```

````

````{py:property} antialias_cutoff_gpts
:canonical: abtem.waves.BaseWaves.antialias_cutoff_gpts
:type: tuple[int, int]

```{autodoc2-docstring} abtem.waves.BaseWaves.antialias_cutoff_gpts
```

````

````{py:property} antialias_valid_gpts
:canonical: abtem.waves.BaseWaves.antialias_valid_gpts
:type: tuple[int, int]

```{autodoc2-docstring} abtem.waves.BaseWaves.antialias_valid_gpts
```

````

````{py:property} base_axes_metadata
:canonical: abtem.waves.BaseWaves.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.waves.BaseWaves.base_axes_metadata
```

````

````{py:property} cutoff_angles
:canonical: abtem.waves.BaseWaves.cutoff_angles
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.cutoff_angles
```

````

````{py:property} cutoff_frequencies
:canonical: abtem.waves.BaseWaves.cutoff_frequencies
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.cutoff_frequencies
```

````

````{py:property} device
:canonical: abtem.waves.BaseWaves.device
:abstractmethod:
:type: str

```{autodoc2-docstring} abtem.waves.BaseWaves.device
```

````

````{py:property} dtype
:canonical: abtem.waves.BaseWaves.dtype
:type: numpy.dtype

```{autodoc2-docstring} abtem.waves.BaseWaves.dtype
```

````

````{py:property} full_cutoff_angles
:canonical: abtem.waves.BaseWaves.full_cutoff_angles
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.full_cutoff_angles
```

````

````{py:property} metadata
:canonical: abtem.waves.BaseWaves.metadata
:abstractmethod:
:type: dict

```{autodoc2-docstring} abtem.waves.BaseWaves.metadata
```

````

````{py:property} reciprocal_space_axes_metadata
:canonical: abtem.waves.BaseWaves.reciprocal_space_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.waves.BaseWaves.reciprocal_space_axes_metadata
```

````

````{py:property} rectangle_cutoff_angles
:canonical: abtem.waves.BaseWaves.rectangle_cutoff_angles
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.rectangle_cutoff_angles
```

````

`````

`````{py:class} PlaneWave(extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, energy: typing.Optional[float] = None, normalize: bool = False, tilt: tuple[float, float] = (0.0, 0.0), device: typing.Optional[str] = None)
:canonical: abtem.waves.PlaneWave

Bases: {py:obj}`abtem.waves.WavesBuilder`

```{autodoc2-docstring} abtem.waves.PlaneWave
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.waves.PlaneWave.__init__
```

````{py:method} build(lazy: typing.Optional[bool] = None, max_batch: int | str = 'auto') -> abtem.waves.Waves
:canonical: abtem.waves.PlaneWave.build

```{autodoc2-docstring} abtem.waves.PlaneWave.build
```

````

````{py:property} metadata
:canonical: abtem.waves.PlaneWave.metadata

````

````{py:method} multislice(potential: abtem.potentials.iam.BasePotential | ase.Atoms, detectors: typing.Optional[abtem.detectors.BaseDetector] = None, max_batch: int | str = 'auto', lazy: typing.Optional[bool] = None, **multislice_func_kwargs) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.waves.PlaneWave.multislice

```{autodoc2-docstring} abtem.waves.PlaneWave.multislice
```

````

````{py:property} normalize
:canonical: abtem.waves.PlaneWave.normalize

```{autodoc2-docstring} abtem.waves.PlaneWave.normalize
```

````

````{py:property} tilt
:canonical: abtem.waves.PlaneWave.tilt

```{autodoc2-docstring} abtem.waves.PlaneWave.tilt
```

````

`````

`````{py:class} Probe(semiangle_cutoff: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, energy: typing.Optional[float] = None, soft: bool = True, tilt: abtem.tilt.TiltType2D = (0.0, 0.0), device: typing.Optional[str] = None, aperture: typing.Optional[abtem.transfer.BaseAperture] = None, aberrations: typing.Optional[abtem.transfer.Aberrations | dict] = None, scan_positions: typing.Optional[abtem.scan.BaseScan] = None, metadata: typing.Optional[dict] = None, **kwargs)
:canonical: abtem.waves.Probe

Bases: {py:obj}`abtem.waves.WavesBuilder`

```{autodoc2-docstring} abtem.waves.Probe
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.waves.Probe.__init__
```

````{py:property} aberrations
:canonical: abtem.waves.Probe.aberrations
:type: abtem.transfer.Aberrations

```{autodoc2-docstring} abtem.waves.Probe.aberrations
```

````

````{py:property} aperture
:canonical: abtem.waves.Probe.aperture
:type: abtem.transfer.BaseAperture

```{autodoc2-docstring} abtem.waves.Probe.aperture
```

````

````{py:method} build(scan: typing.Optional[typing.Sequence | abtem.scan.BaseScan] = None, max_batch: int | str = 'auto', lazy: typing.Optional[bool] = None) -> abtem.waves.Waves
:canonical: abtem.waves.Probe.build

```{autodoc2-docstring} abtem.waves.Probe.build
```

````

````{py:property} ctf
:canonical: abtem.waves.Probe.ctf

```{autodoc2-docstring} abtem.waves.Probe.ctf
```

````

````{py:property} metadata
:canonical: abtem.waves.Probe.metadata
:type: dict

```{autodoc2-docstring} abtem.waves.Probe.metadata
```

````

````{py:method} multislice(potential: abtem.potentials.iam.BasePotential | ase.Atoms, scan: typing.Optional[typing.Sequence | abtem.scan.BaseScan] = None, detectors: typing.Optional[abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector]] = None, max_batch: int | str = 'auto', lazy: typing.Optional[bool] = None, **multislice_func_kwargs) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.Probe.multislice

```{autodoc2-docstring} abtem.waves.Probe.multislice
```

````

````{py:method} profiles(angle: float = 0.0) -> abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.waves.Probe.profiles

```{autodoc2-docstring} abtem.waves.Probe.profiles
```

````

````{py:method} scan(potential: ase.Atoms | abtem.potentials.iam.BasePotential, scan: typing.Optional[typing.Sequence | abtem.scan.BaseScan] = None, detectors: typing.Optional[abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector]] = None, max_batch: int | str = 'auto', lazy: typing.Optional[bool] = None, **multislice_func_kwargs) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.waves.Probe.scan

```{autodoc2-docstring} abtem.waves.Probe.scan
```

````

````{py:property} scan_positions
:canonical: abtem.waves.Probe.scan_positions
:type: abtem.scan.BaseScan

```{autodoc2-docstring} abtem.waves.Probe.scan_positions
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.waves.Probe.semiangle_cutoff

```{autodoc2-docstring} abtem.waves.Probe.semiangle_cutoff
```

````

````{py:method} show(convert_complex: str = 'intensity', **kwargs) -> abtem.visualize.Visualization
:canonical: abtem.waves.Probe.show

```{autodoc2-docstring} abtem.waves.Probe.show
```

````

````{py:property} soft
:canonical: abtem.waves.Probe.soft

```{autodoc2-docstring} abtem.waves.Probe.soft
```

````

````{py:method} transition_potential_scan(potential: abtem.potentials.iam.BasePotential | ase.Atoms, transition_potentials: abtem.inelastic.core_loss.BaseTransitionPotential | list[abtem.inelastic.core_loss.BaseTransitionPotential], scan: typing.Optional[abtem.scan.BaseScan | typing.Sequence] = None, detectors: typing.Optional[abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector]] = None, sites: typing.Optional[abtem.slicing.SliceIndexedAtoms | ase.Atoms] = None, max_batch: int | str = 'auto', lazy: typing.Optional[bool] = None, **multislice_func_kwargs) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.Probe.transition_potential_scan

```{autodoc2-docstring} abtem.waves.Probe.transition_potential_scan
```

````

`````

`````{py:class} Waves(array: numpy.ndarray | dask.array.core.Array, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, reciprocal_space: bool = False, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
:canonical: abtem.waves.Waves

Bases: {py:obj}`abtem.waves.BaseWaves`, {py:obj}`abtem.array.ArrayObject`

```{autodoc2-docstring} abtem.waves.Waves
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.waves.Waves.__init__
```

````{py:method} apply_ctf(ctf: typing.Optional[abtem.transfer.CTF] = None, max_batch: int | str = 'auto', **kwargs: typing.Any) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.apply_ctf

```{autodoc2-docstring} abtem.waves.Waves.apply_ctf
```

````

````{py:property} base_tilt
:canonical: abtem.waves.Waves.base_tilt
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.Waves.base_tilt
```

````

````{py:method} convolve(kernel: numpy.ndarray, axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, out_space: str = 'in_space', in_place: bool = False) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.convolve

```{autodoc2-docstring} abtem.waves.Waves.convolve
```

````

````{py:method} depth_profile(projection_axis: str = 'y', depth: typing.Optional[float] = None, convert_complex: str = 'intensity') -> abtem.measurements.Images
:canonical: abtem.waves.Waves.depth_profile

```{autodoc2-docstring} abtem.waves.Waves.depth_profile
```

````

````{py:property} device
:canonical: abtem.waves.Waves.device
:type: str

```{autodoc2-docstring} abtem.waves.Waves.device
```

````

````{py:method} diffraction_patterns(max_angle: typing.Optional[str | float] = 'cutoff', block_direct: bool | float = False, fftshift: bool = True, parity: str = 'odd', return_complex: bool = False, renormalize: bool = True) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.waves.Waves.diffraction_patterns

```{autodoc2-docstring} abtem.waves.Waves.diffraction_patterns
```

````

````{py:method} downsample(max_angle: str | float = 'cutoff', gpts: typing.Optional[tuple[int, int]] = None, normalization: str = 'values') -> abtem.waves.Waves
:canonical: abtem.waves.Waves.downsample

```{autodoc2-docstring} abtem.waves.Waves.downsample
```

````

````{py:method} ensure_real_space(overwrite_x: bool = False) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.ensure_real_space

```{autodoc2-docstring} abtem.waves.Waves.ensure_real_space
```

````

````{py:method} ensure_reciprocal_space(overwrite_x: bool = False) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.ensure_reciprocal_space

```{autodoc2-docstring} abtem.waves.Waves.ensure_reciprocal_space
```

````

````{py:method} from_array_and_metadata(array: numpy.ndarray | dask.array.core.Array, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: typing.Optional[dict] = None) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.from_array_and_metadata
:classmethod:

```{autodoc2-docstring} abtem.waves.Waves.from_array_and_metadata
```

````

````{py:method} imag() -> abtem.measurements.Images
:canonical: abtem.waves.Waves.imag

```{autodoc2-docstring} abtem.waves.Waves.imag
```

````

````{py:method} intensity() -> abtem.measurements.Images
:canonical: abtem.waves.Waves.intensity

```{autodoc2-docstring} abtem.waves.Waves.intensity
```

````

````{py:property} metadata
:canonical: abtem.waves.Waves.metadata
:type: dict

````

````{py:method} multislice(potential: ase.Atoms | abtem.potentials.iam.BasePotential, detectors: typing.Optional[abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector]] = None, **multislice_func_kwargs) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.Waves.multislice

```{autodoc2-docstring} abtem.waves.Waves.multislice
```

````

````{py:method} normalize(space: str = 'reciprocal', in_place: bool = False) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.normalize

```{autodoc2-docstring} abtem.waves.Waves.normalize
```

````

````{py:method} phase() -> abtem.measurements.Images
:canonical: abtem.waves.Waves.phase

```{autodoc2-docstring} abtem.waves.Waves.phase
```

````

````{py:method} phase_shift(amount: float) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.phase_shift

```{autodoc2-docstring} abtem.waves.Waves.phase_shift
```

````

````{py:method} real() -> abtem.measurements.Images
:canonical: abtem.waves.Waves.real

```{autodoc2-docstring} abtem.waves.Waves.real
```

````

````{py:property} reciprocal_space
:canonical: abtem.waves.Waves.reciprocal_space
:type: bool

```{autodoc2-docstring} abtem.waves.Waves.reciprocal_space
```

````

````{py:method} scan(scan: abtem.scan.BaseScan | numpy.ndarray, potential: typing.Optional[ase.Atoms | abtem.potentials.iam.BasePotential] = None, detectors: typing.Optional[abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector]] = None, max_batch: int | str = 'auto', **multislice_func_kwargs) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.Waves.scan

```{autodoc2-docstring} abtem.waves.Waves.scan
```

````

````{py:method} show(convert_complex: str = 'intensity', **kwargs) -> abtem.visualize.Visualization
:canonical: abtem.waves.Waves.show

```{autodoc2-docstring} abtem.waves.Waves.show
```

````

````{py:method} show_depth_profile(projection_axis: str = 'y', depth: typing.Optional[float] = None, convert_complex: str = 'intensity', z_scale: float = 1.0, slice_lines: bool = False, ax=None, cbar: bool = False, cmap: typing.Optional[str] = None, vmin: typing.Optional[float] = None, vmax: typing.Optional[float] = None, power: float = 1.0, common_color_scale: bool = False, explode: bool | typing.Sequence[int] = (), figsize: typing.Optional[tuple[int, int]] = None, title: bool | str = True, **kwargs) -> abtem.visualize.Visualization
:canonical: abtem.waves.Waves.show_depth_profile

```{autodoc2-docstring} abtem.waves.Waves.show_depth_profile
```

````

````{py:method} tile(repetitions: tuple[int, int], renormalize: bool = False) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.tile

```{autodoc2-docstring} abtem.waves.Waves.tile
```

````

````{py:method} to_images(convert_complex: typing.Optional[str] = None) -> abtem.measurements.Images
:canonical: abtem.waves.Waves.to_images

```{autodoc2-docstring} abtem.waves.Waves.to_images
```

````

````{py:method} transition_potential_multislice(potential: abtem.potentials.iam.BasePotential, transition_potentials: abtem.inelastic.core_loss.BaseTransitionPotential | list[abtem.inelastic.core_loss.BaseTransitionPotential], detectors: typing.Optional[abtem.detectors.BaseDetector | list[abtem.detectors.BaseDetector]] = None, sites: typing.Optional[abtem.slicing.SliceIndexedAtoms | ase.Atoms] = None, **multislice_func_kwargs) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements
:canonical: abtem.waves.Waves.transition_potential_multislice

```{autodoc2-docstring} abtem.waves.Waves.transition_potential_multislice
```

````

`````

`````{py:class} WavesBuilder(ensemble_names: tuple[str, ...], device: str | None, tilt: abtem.tilt.TiltType2D = (0.0, 0.0))
:canonical: abtem.waves.WavesBuilder

Bases: {py:obj}`abtem.waves.BaseWaves`, {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

````{py:method} apply_transform(transform, max_batch: int | str = 'auto', lazy: bool = True)
:canonical: abtem.waves.WavesBuilder.apply_transform

```{autodoc2-docstring} abtem.waves.WavesBuilder.apply_transform
```

````

````{py:property} axes_metadata
:canonical: abtem.waves.WavesBuilder.axes_metadata
:type: abtem.core.axes.AxesMetadataList

```{autodoc2-docstring} abtem.waves.WavesBuilder.axes_metadata
```

````

````{py:property} base_shape
:canonical: abtem.waves.WavesBuilder.base_shape
:type: tuple[int, int]

```{autodoc2-docstring} abtem.waves.WavesBuilder.base_shape
```

````

````{py:method} build(*args, **kwargs) -> abtem.waves.Waves
:canonical: abtem.waves.WavesBuilder.build
:abstractmethod:

```{autodoc2-docstring} abtem.waves.WavesBuilder.build
```

````

````{py:method} check_can_build()
:canonical: abtem.waves.WavesBuilder.check_can_build

```{autodoc2-docstring} abtem.waves.WavesBuilder.check_can_build
```

````

````{py:property} device
:canonical: abtem.waves.WavesBuilder.device
:type: str

```{autodoc2-docstring} abtem.waves.WavesBuilder.device
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.waves.WavesBuilder.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.waves.WavesBuilder.ensemble_axes_metadata
```

````

````{py:property} ensemble_shape
:canonical: abtem.waves.WavesBuilder.ensemble_shape

```{autodoc2-docstring} abtem.waves.WavesBuilder.ensemble_shape
```

````

````{py:property} shape
:canonical: abtem.waves.WavesBuilder.shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.waves.WavesBuilder.shape
```

````

````{py:property} tilt
:canonical: abtem.waves.WavesBuilder.tilt

```{autodoc2-docstring} abtem.waves.WavesBuilder.tilt
```

````

`````

````{py:function} reduce_ensemble(ensemble: Waves | abtem.measurements.BaseMeasurements | list[Waves | abtem.measurements.BaseMeasurements]) -> Waves | abtem.measurements.BaseMeasurements | list[Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.reduce_ensemble

```{autodoc2-docstring} abtem.waves.reduce_ensemble
```
````
