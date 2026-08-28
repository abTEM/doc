# {py:mod}`abtem.measurements`

```{py:module} abtem.measurements
```

```{autodoc2-docstring} abtem.measurements
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseMeasurements <abtem.measurements.BaseMeasurements>`
  - ```{autodoc2-docstring} abtem.measurements.BaseMeasurements
    :parser: rst
    :summary:
    ```
* - {py:obj}`DiffractionPatterns <abtem.measurements.DiffractionPatterns>`
  - ```{autodoc2-docstring} abtem.measurements.DiffractionPatterns
    :parser: rst
    :summary:
    ```
* - {py:obj}`Images <abtem.measurements.Images>`
  - ```{autodoc2-docstring} abtem.measurements.Images
    :parser: rst
    :summary:
    ```
* - {py:obj}`IndexedDiffractionPatterns <abtem.measurements.IndexedDiffractionPatterns>`
  - ```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns
    :parser: rst
    :summary:
    ```
* - {py:obj}`MeasurementsEnsemble <abtem.measurements.MeasurementsEnsemble>`
  -
* - {py:obj}`MomentumResolvedSpectrum <abtem.measurements.MomentumResolvedSpectrum>`
  - ```{autodoc2-docstring} abtem.measurements.MomentumResolvedSpectrum
    :parser: rst
    :summary:
    ```
* - {py:obj}`PolarMeasurements <abtem.measurements.PolarMeasurements>`
  - ```{autodoc2-docstring} abtem.measurements.PolarMeasurements
    :parser: rst
    :summary:
    ```
* - {py:obj}`RealSpaceLineProfiles <abtem.measurements.RealSpaceLineProfiles>`
  - ```{autodoc2-docstring} abtem.measurements.RealSpaceLineProfiles
    :parser: rst
    :summary:
    ```
* - {py:obj}`ReciprocalSpaceLineProfiles <abtem.measurements.ReciprocalSpaceLineProfiles>`
  - ```{autodoc2-docstring} abtem.measurements.ReciprocalSpaceLineProfiles
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`calculate_max_reciprocal_space_vector <abtem.measurements.calculate_max_reciprocal_space_vector>`
  - ```{autodoc2-docstring} abtem.measurements.calculate_max_reciprocal_space_vector
    :parser: rst
    :summary:
    ```
* - {py:obj}`integrate_disc <abtem.measurements.integrate_disc>`
  - ```{autodoc2-docstring} abtem.measurements.integrate_disc
    :parser: rst
    :summary:
    ```
* - {py:obj}`momentum_resolved_spectrum <abtem.measurements.momentum_resolved_spectrum>`
  - ```{autodoc2-docstring} abtem.measurements.momentum_resolved_spectrum
    :parser: rst
    :summary:
    ```
* - {py:obj}`periodic_crop <abtem.measurements.periodic_crop>`
  - ```{autodoc2-docstring} abtem.measurements.periodic_crop
    :parser: rst
    :summary:
    ```
* - {py:obj}`phonon_loss_diffraction_patterns <abtem.measurements.phonon_loss_diffraction_patterns>`
  - ```{autodoc2-docstring} abtem.measurements.phonon_loss_diffraction_patterns
    :parser: rst
    :summary:
    ```
* - {py:obj}`reciprocal_lattice_vector_lengths <abtem.measurements.reciprocal_lattice_vector_lengths>`
  - ```{autodoc2-docstring} abtem.measurements.reciprocal_lattice_vector_lengths
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseMeasurementsSubclass <abtem.measurements.BaseMeasurementsSubclass>`
  - ```{autodoc2-docstring} abtem.measurements.BaseMeasurementsSubclass
    :parser: rst
    :summary:
    ```
* - {py:obj}`interpolate_bilinear_cuda <abtem.measurements.interpolate_bilinear_cuda>`
  - ```{autodoc2-docstring} abtem.measurements.interpolate_bilinear_cuda
    :parser: rst
    :summary:
    ```
* - {py:obj}`pd <abtem.measurements.pd>`
  - ```{autodoc2-docstring} abtem.measurements.pd
    :parser: rst
    :summary:
    ```
* - {py:obj}`sum_run_length_encoded <abtem.measurements.sum_run_length_encoded>`
  - ```{autodoc2-docstring} abtem.measurements.sum_run_length_encoded
    :parser: rst
    :summary:
    ```
* - {py:obj}`sum_run_length_encoded_cuda <abtem.measurements.sum_run_length_encoded_cuda>`
  - ```{autodoc2-docstring} abtem.measurements.sum_run_length_encoded_cuda
    :parser: rst
    :summary:
    ```
* - {py:obj}`xr <abtem.measurements.xr>`
  - ```{autodoc2-docstring} abtem.measurements.xr
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BaseMeasurements(...)
:canonical: abtem.measurements.BaseMeasurements

Bases: {py:obj}`abtem.array.ArrayObject`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.measurements.BaseMeasurements
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.__init__
:parser: rst
```

````{py:method} abs() -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.abs

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.abs
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.measurements.BaseMeasurements.base_axes_metadata
:abstractmethod:
:type: list

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.base_axes_metadata
:parser: rst
```

````

````{py:method} from_array_and_metadata(...) -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.from_array_and_metadata
:abstractmethod:
:classmethod:

````

````{py:method} imag() -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.imag

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.imag
:parser: rst
```

````

````{py:method} intensity() -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.intensity

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.intensity
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.measurements.BaseMeasurements.metadata
:type: dict

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.metadata
:parser: rst
```

````

````{py:method} normalize_ensemble(...)
:canonical: abtem.measurements.BaseMeasurements.normalize_ensemble

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.normalize_ensemble
:parser: rst
```

````

````{py:method} phase() -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.phase

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.phase
:parser: rst
```

````

````{py:method} poisson_noise(...) -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.poisson_noise

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.poisson_noise
:parser: rst
```

````

````{py:method} real() -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.real

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.real
:parser: rst
```

````

````{py:method} reduce_ensemble() -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.reduce_ensemble

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.reduce_ensemble
:parser: rst
```

````

````{py:method} relative_difference(...) -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.relative_difference

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.relative_difference
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.measurements.BaseMeasurements.show
:abstractmethod:

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.show
:parser: rst
```

````

````{py:method} to_measurement_ensemble()
:canonical: abtem.measurements.BaseMeasurements.to_measurement_ensemble

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.to_measurement_ensemble
:parser: rst
```

````

`````

````{py:data} BaseMeasurementsSubclass
:canonical: abtem.measurements.BaseMeasurementsSubclass
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.measurements.BaseMeasurementsSubclass
:parser: rst
```

````

`````{py:class} DiffractionPatterns(...)
:canonical: abtem.measurements.DiffractionPatterns

Bases: {py:obj}`abtem.measurements._BaseMeasurement2D`

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.__init__
:parser: rst
```

````{py:property} angular_coordinates
:canonical: abtem.measurements.DiffractionPatterns.angular_coordinates
:type: tuple[numpy.ndarray, numpy.ndarray]

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.angular_coordinates
:parser: rst
```

````

````{py:property} angular_limits
:canonical: abtem.measurements.DiffractionPatterns.angular_limits
:type: list[tuple[float, float]]

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.angular_limits
:parser: rst
```

````

````{py:property} angular_sampling
:canonical: abtem.measurements.DiffractionPatterns.angular_sampling
:type: tuple[float, float]

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.angular_sampling
:parser: rst
```

````

````{py:method} azimuthal_average(...) -> abtem.measurements.ReciprocalSpaceLineProfiles
:canonical: abtem.measurements.DiffractionPatterns.azimuthal_average

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.azimuthal_average
:parser: rst
```

````

````{py:method} bandlimit(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.bandlimit

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.bandlimit
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.measurements.DiffractionPatterns.base_axes_metadata

````

````{py:method} block_direct(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.block_direct

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.block_direct
:parser: rst
```

````

````{py:method} center_of_mass(...) -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.measurements.DiffractionPatterns.center_of_mass

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.center_of_mass
:parser: rst
```

````

````{py:property} coordinates
:canonical: abtem.measurements.DiffractionPatterns.coordinates
:type: tuple[numpy.ndarray, numpy.ndarray]

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.coordinates
:parser: rst
```

````

````{py:method} crop(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.crop

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.crop
:parser: rst
```

````

````{py:property} extent
:canonical: abtem.measurements.DiffractionPatterns.extent
:type: tuple[float, float]

````

````{py:property} fftshift
:canonical: abtem.measurements.DiffractionPatterns.fftshift
:type: bool

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.fftshift
:parser: rst
```

````

````{py:method} from_array_and_metadata(...) -> typing.Self
:canonical: abtem.measurements.DiffractionPatterns.from_array_and_metadata
:classmethod:

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.from_array_and_metadata
:parser: rst
```

````

````{py:method} gaussian_source_size(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.gaussian_source_size

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.gaussian_source_size
:parser: rst
```

````

````{py:method} index_diffraction_spots(...) -> abtem.measurements.IndexedDiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.index_diffraction_spots

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.index_diffraction_spots
:parser: rst
```

````

````{py:method} integrate_radial(...) -> abtem.measurements.Images
:canonical: abtem.measurements.DiffractionPatterns.integrate_radial

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.integrate_radial
:parser: rst
```

````

````{py:method} integrated_center_of_mass() -> abtem.measurements.Images
:canonical: abtem.measurements.DiffractionPatterns.integrated_center_of_mass

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.integrated_center_of_mass
:parser: rst
```

````

````{py:method} interpolate(...)
:canonical: abtem.measurements.DiffractionPatterns.interpolate

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.interpolate
:parser: rst
```

````

````{py:property} limits
:canonical: abtem.measurements.DiffractionPatterns.limits
:type: list[tuple[float, float]]

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.limits
:parser: rst
```

````

````{py:method} lorentzian_source_size(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.lorentzian_source_size

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.lorentzian_source_size
:parser: rst
```

````

````{py:property} max_angles
:canonical: abtem.measurements.DiffractionPatterns.max_angles
:type: tuple[float, float]

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.max_angles
:parser: rst
```

````

````{py:property} max_frequency
:canonical: abtem.measurements.DiffractionPatterns.max_frequency

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.max_frequency
:parser: rst
```

````

````{py:property} offset
:canonical: abtem.measurements.DiffractionPatterns.offset
:type: tuple[float, float]

````

````{py:method} poisson_noise(...)
:canonical: abtem.measurements.DiffractionPatterns.poisson_noise

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.poisson_noise
:parser: rst
```

````

````{py:method} polar_binning(...)
:canonical: abtem.measurements.DiffractionPatterns.polar_binning

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.polar_binning
:parser: rst
```

````

````{py:method} pseudo_voigtian_source_size(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.pseudo_voigtian_source_size

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.pseudo_voigtian_source_size
:parser: rst
```

````

````{py:method} radial_binning(...) -> abtem.measurements.PolarMeasurements
:canonical: abtem.measurements.DiffractionPatterns.radial_binning

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.radial_binning
:parser: rst
```

````

````{py:property} sampling
:canonical: abtem.measurements.DiffractionPatterns.sampling
:type: tuple[float, float]

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.sampling
:parser: rst
```

````

````{py:method} tile_scan(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.tile_scan

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.tile_scan
:parser: rst
```

````

````{py:method} voigtian_source_size(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.voigtian_source_size

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.voigtian_source_size
:parser: rst
```

````

`````

`````{py:class} Images(...)
:canonical: abtem.measurements.Images

Bases: {py:obj}`abtem.measurements._BaseMeasurement2D`

```{autodoc2-docstring} abtem.measurements.Images
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.measurements.Images.__init__
:parser: rst
```

````{py:property} base_axes_metadata
:canonical: abtem.measurements.Images.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} coordinates
:canonical: abtem.measurements.Images.coordinates
:type: tuple[numpy.ndarray, numpy.ndarray]

```{autodoc2-docstring} abtem.measurements.Images.coordinates
:parser: rst
```

````

````{py:method} crop(...)
:canonical: abtem.measurements.Images.crop

```{autodoc2-docstring} abtem.measurements.Images.crop
:parser: rst
```

````

````{py:method} diffractograms() -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.Images.diffractograms

```{autodoc2-docstring} abtem.measurements.Images.diffractograms
:parser: rst
```

````

````{py:property} extent
:canonical: abtem.measurements.Images.extent
:type: tuple[float, float]

````

````{py:method} from_array_and_metadata(...) -> abtem.measurements.Images
:canonical: abtem.measurements.Images.from_array_and_metadata
:classmethod:

```{autodoc2-docstring} abtem.measurements.Images.from_array_and_metadata
:parser: rst
```

````

````{py:method} integrate_disc(...) -> float
:canonical: abtem.measurements.Images.integrate_disc

```{autodoc2-docstring} abtem.measurements.Images.integrate_disc
:parser: rst
```

````

````{py:method} integrate_gradient()
:canonical: abtem.measurements.Images.integrate_gradient

```{autodoc2-docstring} abtem.measurements.Images.integrate_gradient
:parser: rst
```

````

````{py:method} interpolate(...) -> abtem.measurements.Images
:canonical: abtem.measurements.Images.interpolate

```{autodoc2-docstring} abtem.measurements.Images.interpolate
:parser: rst
```

````

````{py:property} offset
:canonical: abtem.measurements.Images.offset
:type: tuple[float, float]

````

````{py:property} sampling
:canonical: abtem.measurements.Images.sampling
:type: tuple[float, float]

````

````{py:method} scan_noise(...)
:canonical: abtem.measurements.Images.scan_noise

```{autodoc2-docstring} abtem.measurements.Images.scan_noise
:parser: rst
```

````

````{py:method} tile(...) -> abtem.measurements.Images
:canonical: abtem.measurements.Images.tile

```{autodoc2-docstring} abtem.measurements.Images.tile
:parser: rst
```

````

`````

`````{py:class} IndexedDiffractionPatterns(...)
:canonical: abtem.measurements.IndexedDiffractionPatterns

Bases: {py:obj}`abtem.measurements.BaseMeasurements`

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.__init__
:parser: rst
```

````{py:property} all_positions
:canonical: abtem.measurements.IndexedDiffractionPatterns.all_positions
:type: numpy.ndarray

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.all_positions
:parser: rst
```

````

````{py:property} angular_positions
:canonical: abtem.measurements.IndexedDiffractionPatterns.angular_positions

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.angular_positions
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.measurements.IndexedDiffractionPatterns.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:method} block_direct()
:canonical: abtem.measurements.IndexedDiffractionPatterns.block_direct

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.block_direct
:parser: rst
```

````

````{py:method} crop(...)
:canonical: abtem.measurements.IndexedDiffractionPatterns.crop

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.crop
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.measurements.IndexedDiffractionPatterns.ensemble_shape
:type: tuple

````

````{py:method} from_array_and_metadata(...) -> abtem.measurements.BaseMeasurements
:canonical: abtem.measurements.IndexedDiffractionPatterns.from_array_and_metadata
:abstractmethod:

````

````{py:property} intensities
:canonical: abtem.measurements.IndexedDiffractionPatterns.intensities
:type: numpy.ndarray

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.intensities
:parser: rst
```

````

````{py:property} intensities_dict
:canonical: abtem.measurements.IndexedDiffractionPatterns.intensities_dict
:type: dict[tuple, numpy.ndarray]

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.intensities_dict
:parser: rst
```

````

````{py:method} max_reciprocal_space_vector_length()
:canonical: abtem.measurements.IndexedDiffractionPatterns.max_reciprocal_space_vector_length

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.max_reciprocal_space_vector_length
:parser: rst
```

````

````{py:property} miller_indices
:canonical: abtem.measurements.IndexedDiffractionPatterns.miller_indices
:type: numpy.ndarray

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.miller_indices
:parser: rst
```

````

````{py:method} normalize_to_spot(...)
:canonical: abtem.measurements.IndexedDiffractionPatterns.normalize_to_spot

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.normalize_to_spot
:parser: rst
```

````

````{py:property} positions
:canonical: abtem.measurements.IndexedDiffractionPatterns.positions
:type: numpy.ndarray

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.positions
:parser: rst
```

````

````{py:property} positions_dict
:canonical: abtem.measurements.IndexedDiffractionPatterns.positions_dict
:type: dict[tuple, numpy.ndarray]

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.positions_dict
:parser: rst
```

````

````{py:property} reciprocal_lattice_vectors
:canonical: abtem.measurements.IndexedDiffractionPatterns.reciprocal_lattice_vectors
:type: numpy.ndarray

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.reciprocal_lattice_vectors
:parser: rst
```

````

````{py:method} remove_low_intensity(...)
:canonical: abtem.measurements.IndexedDiffractionPatterns.remove_low_intensity

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.remove_low_intensity
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.measurements.IndexedDiffractionPatterns.show

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.show
:parser: rst
```

````

````{py:method} sort(...)
:canonical: abtem.measurements.IndexedDiffractionPatterns.sort

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.sort
:parser: rst
```

````

````{py:method} to_data_array()
:canonical: abtem.measurements.IndexedDiffractionPatterns.to_data_array

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.to_data_array
:parser: rst
```

````

````{py:method} to_dataframe()
:canonical: abtem.measurements.IndexedDiffractionPatterns.to_dataframe

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.to_dataframe
:parser: rst
```

````

`````

`````{py:class} MeasurementsEnsemble(...)
:canonical: abtem.measurements.MeasurementsEnsemble

Bases: {py:obj}`abtem.measurements.BaseMeasurements`

````{py:property} base_axes_metadata
:canonical: abtem.measurements.MeasurementsEnsemble.base_axes_metadata

````

````{py:method} from_array_and_metadata(...) -> abtem.measurements.BaseMeasurementsSubclass
:canonical: abtem.measurements.MeasurementsEnsemble.from_array_and_metadata
:classmethod:

````

````{py:method} show(...) -> abtem.visualize.visualizations.Visualization
:canonical: abtem.measurements.MeasurementsEnsemble.show

```{autodoc2-docstring} abtem.measurements.MeasurementsEnsemble.show
:parser: rst
```

````

`````

`````{py:class} MomentumResolvedSpectrum(...)
:canonical: abtem.measurements.MomentumResolvedSpectrum

Bases: {py:obj}`abtem.measurements.BaseMeasurements`

```{autodoc2-docstring} abtem.measurements.MomentumResolvedSpectrum
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.measurements.MomentumResolvedSpectrum.__init__
:parser: rst
```

````{py:property} base_axes_metadata
:canonical: abtem.measurements.MomentumResolvedSpectrum.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:method} crop(...) -> abtem.measurements.MomentumResolvedSpectrum
:canonical: abtem.measurements.MomentumResolvedSpectrum.crop

```{autodoc2-docstring} abtem.measurements.MomentumResolvedSpectrum.crop
:parser: rst
```

````

````{py:property} e_values
:canonical: abtem.measurements.MomentumResolvedSpectrum.e_values
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.measurements.MomentumResolvedSpectrum.e_values
:parser: rst
```

````

````{py:method} from_array_and_metadata(...) -> abtem.measurements.MomentumResolvedSpectrum
:canonical: abtem.measurements.MomentumResolvedSpectrum.from_array_and_metadata
:classmethod:

````

````{py:property} q_values
:canonical: abtem.measurements.MomentumResolvedSpectrum.q_values
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.measurements.MomentumResolvedSpectrum.q_values
:parser: rst
```

````

````{py:method} show(...) -> tuple
:canonical: abtem.measurements.MomentumResolvedSpectrum.show

```{autodoc2-docstring} abtem.measurements.MomentumResolvedSpectrum.show
:parser: rst
```

````

`````

`````{py:class} PolarMeasurements(...)
:canonical: abtem.measurements.PolarMeasurements

Bases: {py:obj}`abtem.measurements.BaseMeasurements`

```{autodoc2-docstring} abtem.measurements.PolarMeasurements
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.__init__
:parser: rst
```

````{py:property} azimuthal_offset
:canonical: abtem.measurements.PolarMeasurements.azimuthal_offset
:type: float

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.azimuthal_offset
:parser: rst
```

````

````{py:property} azimuthal_sampling
:canonical: abtem.measurements.PolarMeasurements.azimuthal_sampling
:type: float

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.azimuthal_sampling
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.measurements.PolarMeasurements.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:method} differentials(...) -> abtem.measurements.Images
:canonical: abtem.measurements.PolarMeasurements.differentials

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.differentials
:parser: rst
```

````

````{py:property} extent
:canonical: abtem.measurements.PolarMeasurements.extent

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.extent
:parser: rst
```

````

````{py:method} from_array_and_metadata(...) -> abtem.measurements.PolarMeasurements
:canonical: abtem.measurements.PolarMeasurements.from_array_and_metadata
:classmethod:

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.from_array_and_metadata
:parser: rst
```

````

````{py:method} gaussian_source_size(...) -> abtem.measurements.PolarMeasurements
:canonical: abtem.measurements.PolarMeasurements.gaussian_source_size

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.gaussian_source_size
:parser: rst
```

````

````{py:method} integrate(...) -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.measurements.PolarMeasurements.integrate

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.integrate
:parser: rst
```

````

````{py:method} integrate_radial(...) -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.measurements.PolarMeasurements.integrate_radial

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.integrate_radial
:parser: rst
```

````

````{py:method} lorentzian_source_size(...) -> abtem.measurements.PolarMeasurements
:canonical: abtem.measurements.PolarMeasurements.lorentzian_source_size

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.lorentzian_source_size
:parser: rst
```

````

````{py:property} offset
:canonical: abtem.measurements.PolarMeasurements.offset

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.offset
:parser: rst
```

````

````{py:property} outer_angle
:canonical: abtem.measurements.PolarMeasurements.outer_angle
:type: float

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.outer_angle
:parser: rst
```

````

````{py:method} poisson_noise(...)
:canonical: abtem.measurements.PolarMeasurements.poisson_noise

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.poisson_noise
:parser: rst
```

````

````{py:method} pseudo_voigtian_source_size(...) -> abtem.measurements.PolarMeasurements
:canonical: abtem.measurements.PolarMeasurements.pseudo_voigtian_source_size

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.pseudo_voigtian_source_size
:parser: rst
```

````

````{py:property} radial_offset
:canonical: abtem.measurements.PolarMeasurements.radial_offset
:type: float

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.radial_offset
:parser: rst
```

````

````{py:property} radial_sampling
:canonical: abtem.measurements.PolarMeasurements.radial_sampling
:type: float

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.radial_sampling
:parser: rst
```

````

````{py:property} sampling
:canonical: abtem.measurements.PolarMeasurements.sampling

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.sampling
:parser: rst
```

````

````{py:method} show(...) -> abtem.visualize.visualizations.Visualization
:canonical: abtem.measurements.PolarMeasurements.show

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.show
:parser: rst
```

````

````{py:method} to_diffraction_patterns(...)
:canonical: abtem.measurements.PolarMeasurements.to_diffraction_patterns

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.to_diffraction_patterns
:parser: rst
```

````

````{py:method} to_image_ensemble()
:canonical: abtem.measurements.PolarMeasurements.to_image_ensemble

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.to_image_ensemble
:parser: rst
```

````

````{py:method} voigtian_source_size(...) -> abtem.measurements.PolarMeasurements
:canonical: abtem.measurements.PolarMeasurements.voigtian_source_size

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.voigtian_source_size
:parser: rst
```

````

`````

`````{py:class} RealSpaceLineProfiles(...)
:canonical: abtem.measurements.RealSpaceLineProfiles

Bases: {py:obj}`abtem.measurements._BaseMeasurement1D`

```{autodoc2-docstring} abtem.measurements.RealSpaceLineProfiles
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.measurements.RealSpaceLineProfiles.__init__
:parser: rst
```

````{py:property} base_axes_metadata
:canonical: abtem.measurements.RealSpaceLineProfiles.base_axes_metadata
:type: list[abtem.core.axes.RealSpaceAxis]

````

````{py:method} tile(...) -> abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.measurements.RealSpaceLineProfiles.tile

```{autodoc2-docstring} abtem.measurements.RealSpaceLineProfiles.tile
:parser: rst
```

````

`````

`````{py:class} ReciprocalSpaceLineProfiles(...)
:canonical: abtem.measurements.ReciprocalSpaceLineProfiles

Bases: {py:obj}`abtem.measurements._BaseMeasurement1D`

```{autodoc2-docstring} abtem.measurements.ReciprocalSpaceLineProfiles
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.measurements.ReciprocalSpaceLineProfiles.__init__
:parser: rst
```

````{py:property} angular_extent
:canonical: abtem.measurements.ReciprocalSpaceLineProfiles.angular_extent

```{autodoc2-docstring} abtem.measurements.ReciprocalSpaceLineProfiles.angular_extent
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.measurements.ReciprocalSpaceLineProfiles.base_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

`````

````{py:function} calculate_max_reciprocal_space_vector(...)
:canonical: abtem.measurements.calculate_max_reciprocal_space_vector

```{autodoc2-docstring} abtem.measurements.calculate_max_reciprocal_space_vector
:parser: rst
```
````

````{py:function} integrate_disc(...) -> float
:canonical: abtem.measurements.integrate_disc

```{autodoc2-docstring} abtem.measurements.integrate_disc
:parser: rst
```
````

````{py:data} interpolate_bilinear_cuda
:canonical: abtem.measurements.interpolate_bilinear_cuda
:type: typing.Optional[typing.Callable]
:value: >
   None

```{autodoc2-docstring} abtem.measurements.interpolate_bilinear_cuda
:parser: rst
```

````

````{py:function} momentum_resolved_spectrum(...) -> abtem.measurements.MomentumResolvedSpectrum
:canonical: abtem.measurements.momentum_resolved_spectrum

```{autodoc2-docstring} abtem.measurements.momentum_resolved_spectrum
:parser: rst
```
````

````{py:data} pd
:canonical: abtem.measurements.pd
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.measurements.pd
:parser: rst
```

````

````{py:function} periodic_crop(...) -> numpy.ndarray
:canonical: abtem.measurements.periodic_crop

```{autodoc2-docstring} abtem.measurements.periodic_crop
:parser: rst
```
````

````{py:function} phonon_loss_diffraction_patterns(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.phonon_loss_diffraction_patterns

```{autodoc2-docstring} abtem.measurements.phonon_loss_diffraction_patterns
:parser: rst
```
````

````{py:function} reciprocal_lattice_vector_lengths(...)
:canonical: abtem.measurements.reciprocal_lattice_vector_lengths

```{autodoc2-docstring} abtem.measurements.reciprocal_lattice_vector_lengths
:parser: rst
```
````

````{py:data} sum_run_length_encoded
:canonical: abtem.measurements.sum_run_length_encoded
:type: typing.Optional[typing.Callable]
:value: >
   None

```{autodoc2-docstring} abtem.measurements.sum_run_length_encoded
:parser: rst
```

````

````{py:data} sum_run_length_encoded_cuda
:canonical: abtem.measurements.sum_run_length_encoded_cuda
:type: typing.Optional[typing.Callable]
:value: >
   None

```{autodoc2-docstring} abtem.measurements.sum_run_length_encoded_cuda
:parser: rst
```

````

````{py:data} xr
:canonical: abtem.measurements.xr
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.measurements.xr
:parser: rst
```

````
