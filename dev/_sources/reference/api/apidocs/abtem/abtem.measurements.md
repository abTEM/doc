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
* - {py:obj}`periodic_crop <abtem.measurements.periodic_crop>`
  - ```{autodoc2-docstring} abtem.measurements.periodic_crop
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

`````{py:class} BaseMeasurements(array: numpy.ndarray | dask.array.core.Array, ensemble_axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: dict)
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

````{py:method} from_array_and_metadata(array: numpy.ndarray | dask.array.core.Array, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: typing.Optional[dict] = None) -> typing.Self
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

````{py:method} normalize_ensemble(scale: str = 'max', shift: str = 'mean')
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

````{py:method} poisson_noise(dose_per_area: typing.SupportsFloat | typing.Sequence[typing.SupportsFloat] | None = None, total_dose: typing.SupportsFloat | typing.Sequence[typing.SupportsFloat] | None = None, samples: int = 1, seed: typing.Optional[int] = None) -> typing.Self
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

````{py:method} relative_difference(other: abtem.measurements.BaseMeasurements, min_relative_tol: float = 0.0) -> typing.Self
:canonical: abtem.measurements.BaseMeasurements.relative_difference

```{autodoc2-docstring} abtem.measurements.BaseMeasurements.relative_difference
:parser: rst
```

````

````{py:method} show(*args, **kwargs)
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

`````{py:class} DiffractionPatterns(array: numpy.ndarray | dask.array.core.Array, sampling: float | tuple[float, float], fftshift: bool = False, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
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

````{py:method} azimuthal_average(max_angle: typing.Optional[float] = None, radial_sampling: float = 1.0, weighting_function: str = 'step', width: float = 1.0) -> abtem.measurements.ReciprocalSpaceLineProfiles
:canonical: abtem.measurements.DiffractionPatterns.azimuthal_average

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.azimuthal_average
:parser: rst
```

````

````{py:method} bandlimit(inner: float = 0.0, outer: float = np.inf) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.bandlimit

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.bandlimit
:parser: rst
```

````

````{py:property} base_axes_metadata
:canonical: abtem.measurements.DiffractionPatterns.base_axes_metadata

````

````{py:method} block_direct(radius: typing.Optional[float] = None, margin: typing.Optional[bool] = None) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.block_direct

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.block_direct
:parser: rst
```

````

````{py:method} center_of_mass(units: str = '1/Å') -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles
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

````{py:method} crop(max_angle: typing.Optional[float] = None, max_frequency: typing.Optional[float] = None, gpts: typing.Optional[tuple[int, int]] = None) -> abtem.measurements.DiffractionPatterns
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

````{py:method} from_array_and_metadata(array: numpy.ndarray, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: typing.Optional[dict] = None) -> typing.Self
:canonical: abtem.measurements.DiffractionPatterns.from_array_and_metadata
:classmethod:

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.from_array_and_metadata
:parser: rst
```

````

````{py:method} gaussian_source_size(sigma: float | tuple[float, float]) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.gaussian_source_size

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.gaussian_source_size
:parser: rst
```

````

````{py:method} index_diffraction_spots(cell: ase.cell.Cell | float | tuple[float, float, float], sg_max: typing.Optional[float] = None, g_max: typing.Optional[float] = None, orientation_matrices: typing.Optional[numpy.ndarray] = None, radius: typing.Optional[float] = None, centering: str = 'P', energy: typing.Optional[float] = None) -> abtem.measurements.IndexedDiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.index_diffraction_spots

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.index_diffraction_spots
:parser: rst
```

````

````{py:method} integrate_radial(inner: float, outer: float = None, offset: tuple[float, float] = (0.0, 0.0)) -> abtem.measurements.Images
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

````{py:method} interpolate(sampling: typing.Optional[str | float | tuple[float, float]] = None, gpts: typing.Optional[tuple[int, int]] = None)
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

````{py:method} poisson_noise(dose_per_area: typing.Optional[float] = None, total_dose: typing.Optional[float] = None, samples: int = 1, seed: typing.Optional[int] = None)
:canonical: abtem.measurements.DiffractionPatterns.poisson_noise

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.poisson_noise
:parser: rst
```

````

````{py:method} polar_binning(nbins_radial: int, nbins_azimuthal: int, inner: float = 0.0, outer: typing.Optional[float] = None, rotation: float = 0.0, offset: tuple[float, float] = (0.0, 0.0))
:canonical: abtem.measurements.DiffractionPatterns.polar_binning

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.polar_binning
:parser: rst
```

````

````{py:method} radial_binning(step_size: float = 1.0, inner: float = 0.0, outer: typing.Optional[float] = None) -> abtem.measurements.PolarMeasurements
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

````{py:method} tile_scan(repetitions: tuple[int, int]) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.measurements.DiffractionPatterns.tile_scan

```{autodoc2-docstring} abtem.measurements.DiffractionPatterns.tile_scan
:parser: rst
```

````

`````

`````{py:class} Images(array: dask.array.core.Array | numpy.array, sampling: float | tuple[float, float], ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[typing.Dict] = None)
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

````{py:method} crop(extent: tuple[float, float], offset: tuple[float, float] = (0.0, 0.0), centered: bool = False)
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

````{py:method} from_array_and_metadata(array: numpy.ndarray | dask.array.core.Array, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: typing.Optional[dict] = None) -> abtem.measurements.Images
:canonical: abtem.measurements.Images.from_array_and_metadata
:classmethod:

```{autodoc2-docstring} abtem.measurements.Images.from_array_and_metadata
:parser: rst
```

````

````{py:method} integrate_disc(position: numpy.ndarray, radius: float) -> float
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

````{py:method} interpolate(sampling: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, method: str = 'fft', boundary: str = 'periodic', order: int = 3, normalization: str = 'values', cval: float = 0.0) -> abtem.measurements.Images
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

````{py:method} scan_noise(dwell_time: float, flyback_time: float, rms_power: float, max_frequency: float = 500.0, num_components: int = 200, seed: typing.Optional[int] = None)
:canonical: abtem.measurements.Images.scan_noise

```{autodoc2-docstring} abtem.measurements.Images.scan_noise
:parser: rst
```

````

````{py:method} tile(repetitions: tuple[int, int]) -> abtem.measurements.Images
:canonical: abtem.measurements.Images.tile

```{autodoc2-docstring} abtem.measurements.Images.tile
:parser: rst
```

````

`````

`````{py:class} IndexedDiffractionPatterns(array: dask.array.core.Array | numpy.ndarray, miller_indices: numpy.ndarray, reciprocal_lattice_vectors: numpy.ndarray, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
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

````{py:method} crop(max_angle: typing.Optional[float] = None, k_max: typing.Optional[float] = None)
:canonical: abtem.measurements.IndexedDiffractionPatterns.crop

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.crop
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.measurements.IndexedDiffractionPatterns.ensemble_shape
:type: tuple

````

````{py:method} from_array_and_metadata(array: numpy.ndarray, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: dict) -> abtem.measurements.BaseMeasurements
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

````{py:method} normalize_to_spot(spot: typing.Optional[tuple[int, int, int]] = None)
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

````{py:method} remove_low_intensity(threshold: float = 0.001)
:canonical: abtem.measurements.IndexedDiffractionPatterns.remove_low_intensity

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.remove_low_intensity
:parser: rst
```

````

````{py:method} show(ax: typing.Optional[matplotlib.axes.Axes] = None, cbar: bool = False, cmap: typing.Optional[str] = None, vmin: typing.Optional[float] = None, vmax: typing.Optional[float] = None, power: float = 1.0, logscale: bool = False, common_color_scale: bool = False, scale: float = 0.5, explode: bool | typing.Sequence[bool] = (), overlay: bool | typing.Sequence[bool] = (), figsize: typing.Optional[tuple[int, int]] = None, title: bool | str = True, units: typing.Optional[str] = None, interact: bool = False, display: bool = True, **kwargs)
:canonical: abtem.measurements.IndexedDiffractionPatterns.show

```{autodoc2-docstring} abtem.measurements.IndexedDiffractionPatterns.show
:parser: rst
```

````

````{py:method} sort(criterion: str = 'distance')
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

`````{py:class} MeasurementsEnsemble(array: numpy.ndarray, ensemble_axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: dict | None = None)
:canonical: abtem.measurements.MeasurementsEnsemble

Bases: {py:obj}`abtem.measurements.BaseMeasurements`

````{py:property} base_axes_metadata
:canonical: abtem.measurements.MeasurementsEnsemble.base_axes_metadata

````

````{py:method} from_array_and_metadata(array: numpy.ndarray, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: dict) -> abtem.measurements.BaseMeasurementsSubclass
:canonical: abtem.measurements.MeasurementsEnsemble.from_array_and_metadata
:classmethod:

````

````{py:method} show(type: str = 'lines', ax: typing.Optional[matplotlib.axes.Axes] = None, power: float = 1.0, common_scale: bool = False, explode: bool | typing.Sequence[int] = (), overlay: bool | typing.Sequence[int] = (), figsize: typing.Optional[tuple[int, int]] = None, title: bool | str = True, units: typing.Optional[str] = None, interact: bool = False, display: bool = True, **kwargs) -> abtem.visualize.visualizations.Visualization
:canonical: abtem.measurements.MeasurementsEnsemble.show

```{autodoc2-docstring} abtem.measurements.MeasurementsEnsemble.show
:parser: rst
```

````

`````

`````{py:class} PolarMeasurements(array: numpy.ndarray | dask.array.core.Array, radial_sampling: float, azimuthal_sampling: float, radial_offset: float = 0.0, azimuthal_offset: float = 0.0, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
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

````{py:method} differentials(direction_1: tuple[int | tuple[int, ...], int | tuple[int, ...]], direction_2: tuple[int | tuple[int, ...], int | tuple[int, ...]], return_complex: bool = True) -> abtem.measurements.Images
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

````{py:method} from_array_and_metadata(array: numpy.ndarray, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: typing.Optional[dict] = None) -> abtem.measurements.PolarMeasurements
:canonical: abtem.measurements.PolarMeasurements.from_array_and_metadata
:classmethod:

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.from_array_and_metadata
:parser: rst
```

````

````{py:method} gaussian_source_size(sigma: float | tuple[float, float]) -> abtem.measurements.PolarMeasurements
:canonical: abtem.measurements.PolarMeasurements.gaussian_source_size

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.gaussian_source_size
:parser: rst
```

````

````{py:method} integrate(radial_limits: typing.Optional[tuple[float, float]] = None, azimuthal_limits: typing.Optional[tuple[float, float]] = None, detector_regions: typing.Optional[int | typing.Sequence[int]] = None) -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.measurements.PolarMeasurements.integrate

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.integrate
:parser: rst
```

````

````{py:method} integrate_radial(inner: float, outer: float) -> abtem.measurements.Images | abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.measurements.PolarMeasurements.integrate_radial

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.integrate_radial
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

````{py:method} poisson_noise(dose_per_area: typing.Optional[float] = None, total_dose: typing.Optional[float] = None, samples: int = 1, seed: typing.Optional[int] = None)
:canonical: abtem.measurements.PolarMeasurements.poisson_noise

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.poisson_noise
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

````{py:method} show(ax: typing.Optional[matplotlib.axes.Axes] = None, gpts: int | tuple[int, int] = (512, 512), cbar: bool = False, cmap: typing.Optional[str] = None, vmin: typing.Optional[float] = None, vmax: typing.Optional[float] = None, power: float = 1.0, logscale: bool = False, common_color_scale: bool = False, explode: bool | typing.Sequence[bool] = (), overlay: bool | typing.Sequence[int] = (), figsize: typing.Optional[tuple[int, int]] = None, title: bool | str = True, units: typing.Optional[str] = None, interact: bool = False, display: bool = True) -> abtem.visualize.visualizations.Visualization
:canonical: abtem.measurements.PolarMeasurements.show

```{autodoc2-docstring} abtem.measurements.PolarMeasurements.show
:parser: rst
```

````

````{py:method} to_diffraction_patterns(gpts: int | tuple[int, int], margin: float | tuple[float, float] = 0.1)
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

`````

`````{py:class} RealSpaceLineProfiles(array: numpy.ndarray, sampling: typing.Optional[float] = None, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
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

````{py:method} tile(repetitions: int) -> abtem.measurements.RealSpaceLineProfiles
:canonical: abtem.measurements.RealSpaceLineProfiles.tile

```{autodoc2-docstring} abtem.measurements.RealSpaceLineProfiles.tile
:parser: rst
```

````

`````

`````{py:class} ReciprocalSpaceLineProfiles(array: numpy.ndarray, sampling: typing.Optional[float] = None, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
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

````{py:function} calculate_max_reciprocal_space_vector(hkl, reciprocal_lattice_vectors)
:canonical: abtem.measurements.calculate_max_reciprocal_space_vector

```{autodoc2-docstring} abtem.measurements.calculate_max_reciprocal_space_vector
:parser: rst
```
````

````{py:function} integrate_disc(measurement: Images | DiffractionPatterns, position: numpy.ndarray, radius: float, return_mean: bool = False, border: str = 'wrap', interpolate: typing.Optional[tuple[float, bool]] = None) -> float
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

````{py:data} pd
:canonical: abtem.measurements.pd
:type: typing.Optional[types.ModuleType]
:value: >
   None

```{autodoc2-docstring} abtem.measurements.pd
:parser: rst
```

````

````{py:function} periodic_crop(array: numpy.ndarray, corner: tuple[float, float], new_shape: tuple[int, int]) -> numpy.ndarray
:canonical: abtem.measurements.periodic_crop

```{autodoc2-docstring} abtem.measurements.periodic_crop
:parser: rst
```
````

````{py:function} reciprocal_lattice_vector_lengths(hkl, reciprocal_lattice_vectors)
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
