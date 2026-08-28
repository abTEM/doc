# {py:mod}`abtem.waves`

```{py:module} abtem.waves
```

```{autodoc2-docstring} abtem.waves
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseWaves <abtem.waves.BaseWaves>`
  - ```{autodoc2-docstring} abtem.waves.BaseWaves
    :parser: rst
    :summary:
    ```
* - {py:obj}`EnergyEnsemble <abtem.waves.EnergyEnsemble>`
  - ```{autodoc2-docstring} abtem.waves.EnergyEnsemble
    :parser: rst
    :summary:
    ```
* - {py:obj}`PlaneWave <abtem.waves.PlaneWave>`
  - ```{autodoc2-docstring} abtem.waves.PlaneWave
    :parser: rst
    :summary:
    ```
* - {py:obj}`Probe <abtem.waves.Probe>`
  - ```{autodoc2-docstring} abtem.waves.Probe
    :parser: rst
    :summary:
    ```
* - {py:obj}`Waves <abtem.waves.Waves>`
  - ```{autodoc2-docstring} abtem.waves.Waves
    :parser: rst
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
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_energy <abtem.waves.validate_energy>`
  - ```{autodoc2-docstring} abtem.waves.validate_energy
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BaseWaves
:canonical: abtem.waves.BaseWaves

Bases: {py:obj}`abtem.core.grid.HasGrid2DMixin`, {py:obj}`abtem.core.energy.HasAcceleratorMixin`

```{autodoc2-docstring} abtem.waves.BaseWaves
:parser: rst
```

````{py:property} angular_sampling
:canonical: abtem.waves.BaseWaves.angular_sampling
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.angular_sampling
:parser: rst
```

````

````{py:property} antialias_cutoff_gpts
:canonical: abtem.waves.BaseWaves.antialias_cutoff_gpts
:type: tuple[int, int]

```{autodoc2-docstring} abtem.waves.BaseWaves.antialias_cutoff_gpts
:parser: rst
```

````

````{py:property} antialias_valid_gpts
:canonical: abtem.waves.BaseWaves.antialias_valid_gpts
:type: tuple[int, int]

```{autodoc2-docstring} abtem.waves.BaseWaves.antialias_valid_gpts
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.waves.BaseWaves.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.waves.BaseWaves.base_axes_metadata
:parser: rst
```

````

````{py:property} cutoff_angles
:canonical: abtem.waves.BaseWaves.cutoff_angles
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.cutoff_angles
:parser: rst
```

````

````{py:property} cutoff_frequencies
:canonical: abtem.waves.BaseWaves.cutoff_frequencies
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.cutoff_frequencies
:parser: rst
```

````

````{py:property} device
:canonical: abtem.waves.BaseWaves.device
:abstractmethod:
:type: str

```{autodoc2-docstring} abtem.waves.BaseWaves.device
:parser: rst
```

````

````{py:property} dtype
:canonical: abtem.waves.BaseWaves.dtype
:type: numpy.dtype

```{autodoc2-docstring} abtem.waves.BaseWaves.dtype
:parser: rst
```

````

````{py:property} full_cutoff_angles
:canonical: abtem.waves.BaseWaves.full_cutoff_angles
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.full_cutoff_angles
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.waves.BaseWaves.metadata
:abstractmethod:
:type: dict

```{autodoc2-docstring} abtem.waves.BaseWaves.metadata
:parser: rst
```

````

````{py:property} reciprocal_space_axes_metadata
:canonical: abtem.waves.BaseWaves.reciprocal_space_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.waves.BaseWaves.reciprocal_space_axes_metadata
:parser: rst
```

````

````{py:property} rectangle_cutoff_angles
:canonical: abtem.waves.BaseWaves.rectangle_cutoff_angles
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.BaseWaves.rectangle_cutoff_angles
:parser: rst
```

````

`````

`````{py:class} EnergyEnsemble(...)
:canonical: abtem.waves.EnergyEnsemble

Bases: {py:obj}`abtem.distributions.EnsembleFromDistributions`

```{autodoc2-docstring} abtem.waves.EnergyEnsemble
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.waves.EnergyEnsemble.__init__
:parser: rst
```

````{py:property} energy
:canonical: abtem.waves.EnergyEnsemble.energy

```{autodoc2-docstring} abtem.waves.EnergyEnsemble.energy
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.waves.EnergyEnsemble.ensemble_axes_metadata
:type: list

````

`````

`````{py:class} PlaneWave(...)
:canonical: abtem.waves.PlaneWave

Bases: {py:obj}`abtem.waves.WavesBuilder`

```{autodoc2-docstring} abtem.waves.PlaneWave
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.waves.PlaneWave.__init__
:parser: rst
```

````{py:method} build(...) -> abtem.waves.Waves
:canonical: abtem.waves.PlaneWave.build

```{autodoc2-docstring} abtem.waves.PlaneWave.build
:parser: rst
```

````

````{py:method} check_can_build()
:canonical: abtem.waves.PlaneWave.check_can_build

````

````{py:property} energy
:canonical: abtem.waves.PlaneWave.energy

````

````{py:property} metadata
:canonical: abtem.waves.PlaneWave.metadata

````

````{py:method} multislice(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.waves.PlaneWave.multislice

```{autodoc2-docstring} abtem.waves.PlaneWave.multislice
:parser: rst
```

````

````{py:property} normalize
:canonical: abtem.waves.PlaneWave.normalize

```{autodoc2-docstring} abtem.waves.PlaneWave.normalize
:parser: rst
```

````

````{py:property} tilt
:canonical: abtem.waves.PlaneWave.tilt

```{autodoc2-docstring} abtem.waves.PlaneWave.tilt
:parser: rst
```

````

`````

`````{py:class} Probe(...)
:canonical: abtem.waves.Probe

Bases: {py:obj}`abtem.waves.WavesBuilder`

```{autodoc2-docstring} abtem.waves.Probe
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.waves.Probe.__init__
:parser: rst
```

````{py:property} aberrations
:canonical: abtem.waves.Probe.aberrations
:type: abtem.transfer.Aberrations

```{autodoc2-docstring} abtem.waves.Probe.aberrations
:parser: rst
```

````

````{py:property} aperture
:canonical: abtem.waves.Probe.aperture
:type: abtem.transfer.BaseAperture

```{autodoc2-docstring} abtem.waves.Probe.aperture
:parser: rst
```

````

````{py:method} build(...) -> abtem.waves.Waves
:canonical: abtem.waves.Probe.build

```{autodoc2-docstring} abtem.waves.Probe.build
:parser: rst
```

````

````{py:method} check_can_build()
:canonical: abtem.waves.Probe.check_can_build

````

````{py:property} ctf
:canonical: abtem.waves.Probe.ctf

```{autodoc2-docstring} abtem.waves.Probe.ctf
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.waves.Probe.energy

````

````{py:property} metadata
:canonical: abtem.waves.Probe.metadata
:type: dict

```{autodoc2-docstring} abtem.waves.Probe.metadata
:parser: rst
```

````

````{py:method} multislice(...) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.Probe.multislice

```{autodoc2-docstring} abtem.waves.Probe.multislice
:parser: rst
```

````

````{py:method} profiles(...) -> abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.waves.Probe.profiles

```{autodoc2-docstring} abtem.waves.Probe.profiles
:parser: rst
```

````

````{py:method} scan(...) -> abtem.measurements.BaseMeasurements | abtem.waves.Waves | list[abtem.measurements.BaseMeasurements | abtem.waves.Waves]
:canonical: abtem.waves.Probe.scan

```{autodoc2-docstring} abtem.waves.Probe.scan
:parser: rst
```

````

````{py:property} scan_positions
:canonical: abtem.waves.Probe.scan_positions
:type: abtem.scan.BaseScan

```{autodoc2-docstring} abtem.waves.Probe.scan_positions
:parser: rst
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.waves.Probe.semiangle_cutoff

```{autodoc2-docstring} abtem.waves.Probe.semiangle_cutoff
:parser: rst
```

````

````{py:method} show(...) -> abtem.visualize.Visualization
:canonical: abtem.waves.Probe.show

```{autodoc2-docstring} abtem.waves.Probe.show
:parser: rst
```

````

````{py:property} soft
:canonical: abtem.waves.Probe.soft

```{autodoc2-docstring} abtem.waves.Probe.soft
:parser: rst
```

````

````{py:method} transition_potential_scan(...) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.Probe.transition_potential_scan

```{autodoc2-docstring} abtem.waves.Probe.transition_potential_scan
:parser: rst
```

````

`````

`````{py:class} Waves(...)
:canonical: abtem.waves.Waves

Bases: {py:obj}`abtem.waves.BaseWaves`, {py:obj}`abtem.array.ArrayObject`

```{autodoc2-docstring} abtem.waves.Waves
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.waves.Waves.__init__
:parser: rst
```

````{py:property} angular_sampling
:canonical: abtem.waves.Waves.angular_sampling
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.Waves.angular_sampling
:parser: rst
```

````

````{py:method} apply_ctf(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.apply_ctf

```{autodoc2-docstring} abtem.waves.Waves.apply_ctf
:parser: rst
```

````

````{py:property} base_tilt
:canonical: abtem.waves.Waves.base_tilt
:type: tuple[float, float]

```{autodoc2-docstring} abtem.waves.Waves.base_tilt
:parser: rst
```

````

````{py:method} convolve(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.convolve

```{autodoc2-docstring} abtem.waves.Waves.convolve
:parser: rst
```

````

````{py:method} depth_profile(...) -> abtem.measurements.Images
:canonical: abtem.waves.Waves.depth_profile

```{autodoc2-docstring} abtem.waves.Waves.depth_profile
:parser: rst
```

````

````{py:property} device
:canonical: abtem.waves.Waves.device
:type: str

```{autodoc2-docstring} abtem.waves.Waves.device
:parser: rst
```

````

````{py:method} diffraction_patterns(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.waves.Waves.diffraction_patterns

```{autodoc2-docstring} abtem.waves.Waves.diffraction_patterns
:parser: rst
```

````

````{py:method} downsample(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.downsample

```{autodoc2-docstring} abtem.waves.Waves.downsample
:parser: rst
```

````

````{py:method} ensure_real_space(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.ensure_real_space

```{autodoc2-docstring} abtem.waves.Waves.ensure_real_space
:parser: rst
```

````

````{py:method} ensure_reciprocal_space(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.ensure_reciprocal_space

```{autodoc2-docstring} abtem.waves.Waves.ensure_reciprocal_space
:parser: rst
```

````

````{py:method} from_array_and_metadata(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.from_array_and_metadata
:classmethod:

```{autodoc2-docstring} abtem.waves.Waves.from_array_and_metadata
:parser: rst
```

````

````{py:method} imag() -> abtem.measurements.Images
:canonical: abtem.waves.Waves.imag

```{autodoc2-docstring} abtem.waves.Waves.imag
:parser: rst
```

````

````{py:method} intensity() -> abtem.measurements.Images
:canonical: abtem.waves.Waves.intensity

```{autodoc2-docstring} abtem.waves.Waves.intensity
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.waves.Waves.metadata
:type: dict

````

````{py:method} multislice(...) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.Waves.multislice

```{autodoc2-docstring} abtem.waves.Waves.multislice
:parser: rst
```

````

````{py:method} normalize(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.normalize

```{autodoc2-docstring} abtem.waves.Waves.normalize
:parser: rst
```

````

````{py:method} phase() -> abtem.measurements.Images
:canonical: abtem.waves.Waves.phase

```{autodoc2-docstring} abtem.waves.Waves.phase
:parser: rst
```

````

````{py:method} phase_shift(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.phase_shift

```{autodoc2-docstring} abtem.waves.Waves.phase_shift
:parser: rst
```

````

````{py:method} phonon_loss_diffraction_patterns(...)
:canonical: abtem.waves.Waves.phonon_loss_diffraction_patterns

```{autodoc2-docstring} abtem.waves.Waves.phonon_loss_diffraction_patterns
:parser: rst
```

````

````{py:method} real() -> abtem.measurements.Images
:canonical: abtem.waves.Waves.real

```{autodoc2-docstring} abtem.waves.Waves.real
:parser: rst
```

````

````{py:property} reciprocal_space
:canonical: abtem.waves.Waves.reciprocal_space
:type: bool

```{autodoc2-docstring} abtem.waves.Waves.reciprocal_space
:parser: rst
```

````

````{py:method} scan(...) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements | list[abtem.waves.Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.Waves.scan

```{autodoc2-docstring} abtem.waves.Waves.scan
:parser: rst
```

````

````{py:method} show(...) -> abtem.visualize.Visualization
:canonical: abtem.waves.Waves.show

```{autodoc2-docstring} abtem.waves.Waves.show
:parser: rst
```

````

````{py:method} show_depth_profile(...) -> abtem.visualize.Visualization
:canonical: abtem.waves.Waves.show_depth_profile

```{autodoc2-docstring} abtem.waves.Waves.show_depth_profile
:parser: rst
```

````

````{py:method} tile(...) -> abtem.waves.Waves
:canonical: abtem.waves.Waves.tile

```{autodoc2-docstring} abtem.waves.Waves.tile
:parser: rst
```

````

````{py:method} to_images(...) -> abtem.measurements.Images
:canonical: abtem.waves.Waves.to_images

```{autodoc2-docstring} abtem.waves.Waves.to_images
:parser: rst
```

````

````{py:method} transition_potential_multislice(...) -> abtem.waves.Waves | abtem.measurements.BaseMeasurements
:canonical: abtem.waves.Waves.transition_potential_multislice

```{autodoc2-docstring} abtem.waves.Waves.transition_potential_multislice
:parser: rst
```

````

````{py:property} wavelength
:canonical: abtem.waves.Waves.wavelength
:type: float

```{autodoc2-docstring} abtem.waves.Waves.wavelength
:parser: rst
```

````

`````

`````{py:class} WavesBuilder(...)
:canonical: abtem.waves.WavesBuilder

Bases: {py:obj}`abtem.waves.BaseWaves`, {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

````{py:method} apply_transform(...)
:canonical: abtem.waves.WavesBuilder.apply_transform

```{autodoc2-docstring} abtem.waves.WavesBuilder.apply_transform
:parser: rst
```

````

````{py:property} axes_metadata
:canonical: abtem.waves.WavesBuilder.axes_metadata
:type: abtem.core.axes.AxesMetadataList

```{autodoc2-docstring} abtem.waves.WavesBuilder.axes_metadata
:parser: rst
```

````

````{py:property} base_shape
:canonical: abtem.waves.WavesBuilder.base_shape
:type: tuple[int, int]

```{autodoc2-docstring} abtem.waves.WavesBuilder.base_shape
:parser: rst
```

````

````{py:method} build(...) -> abtem.waves.Waves
:canonical: abtem.waves.WavesBuilder.build
:abstractmethod:

```{autodoc2-docstring} abtem.waves.WavesBuilder.build
:parser: rst
```

````

````{py:method} check_can_build()
:canonical: abtem.waves.WavesBuilder.check_can_build

```{autodoc2-docstring} abtem.waves.WavesBuilder.check_can_build
:parser: rst
```

````

````{py:property} device
:canonical: abtem.waves.WavesBuilder.device
:type: str

```{autodoc2-docstring} abtem.waves.WavesBuilder.device
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.waves.WavesBuilder.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.waves.WavesBuilder.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.waves.WavesBuilder.ensemble_shape

```{autodoc2-docstring} abtem.waves.WavesBuilder.ensemble_shape
:parser: rst
```

````

````{py:property} shape
:canonical: abtem.waves.WavesBuilder.shape
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.waves.WavesBuilder.shape
:parser: rst
```

````

````{py:property} tilt
:canonical: abtem.waves.WavesBuilder.tilt

```{autodoc2-docstring} abtem.waves.WavesBuilder.tilt
:parser: rst
```

````

`````

````{py:function} reduce_ensemble(...) -> Waves | abtem.measurements.BaseMeasurements | list[Waves | abtem.measurements.BaseMeasurements]
:canonical: abtem.waves.reduce_ensemble

```{autodoc2-docstring} abtem.waves.reduce_ensemble
:parser: rst
```
````

````{py:function} validate_energy(...) -> abtem.waves.EnergyEnsemble
:canonical: abtem.waves.validate_energy

```{autodoc2-docstring} abtem.waves.validate_energy
:parser: rst
```
````
