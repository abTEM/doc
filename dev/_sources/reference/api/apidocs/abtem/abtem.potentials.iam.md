# {py:mod}`abtem.potentials.iam`

```{py:module} abtem.potentials.iam
```

```{autodoc2-docstring} abtem.potentials.iam
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseField <abtem.potentials.iam.BaseField>`
  - ```{autodoc2-docstring} abtem.potentials.iam.BaseField
    :summary:
    ```
* - {py:obj}`BasePotential <abtem.potentials.iam.BasePotential>`
  - ```{autodoc2-docstring} abtem.potentials.iam.BasePotential
    :summary:
    ```
* - {py:obj}`Potential <abtem.potentials.iam.Potential>`
  - ```{autodoc2-docstring} abtem.potentials.iam.Potential
    :summary:
    ```
* - {py:obj}`FieldArray <abtem.potentials.iam.FieldArray>`
  -
* - {py:obj}`PotentialArray <abtem.potentials.iam.PotentialArray>`
  - ```{autodoc2-docstring} abtem.potentials.iam.PotentialArray
    :summary:
    ```
* - {py:obj}`TransmissionFunction <abtem.potentials.iam.TransmissionFunction>`
  - ```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction
    :summary:
    ```
* - {py:obj}`CrystalPotential <abtem.potentials.iam.CrystalPotential>`
  - ```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_potential <abtem.potentials.iam.validate_potential>`
  - ```{autodoc2-docstring} abtem.potentials.iam.validate_potential
    :summary:
    ```
````

### API

`````{py:class} BaseField
:canonical: abtem.potentials.iam.BaseField

Bases: {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.grid.HasGrid2DMixin`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.potentials.iam.BaseField
```

````{py:property} base_shape
:canonical: abtem.potentials.iam.BaseField.base_shape

```{autodoc2-docstring} abtem.potentials.iam.BaseField.base_shape
```

````

````{py:property} num_configurations
:canonical: abtem.potentials.iam.BaseField.num_configurations
:abstractmethod:

```{autodoc2-docstring} abtem.potentials.iam.BaseField.num_configurations
```

````

````{py:property} base_axes_metadata
:canonical: abtem.potentials.iam.BaseField.base_axes_metadata
:abstractmethod:

````

````{py:property} exit_planes
:canonical: abtem.potentials.iam.BaseField.exit_planes
:abstractmethod:
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.potentials.iam.BaseField.exit_planes
```

````

````{py:property} exit_thicknesses
:canonical: abtem.potentials.iam.BaseField.exit_thicknesses
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.potentials.iam.BaseField.exit_thicknesses
```

````

````{py:property} num_exit_planes
:canonical: abtem.potentials.iam.BaseField.num_exit_planes
:type: int

```{autodoc2-docstring} abtem.potentials.iam.BaseField.num_exit_planes
```

````

````{py:method} generate_slices(first_slice: int = 0, last_slice: typing.Optional[int] = None)
:canonical: abtem.potentials.iam.BaseField.generate_slices
:abstractmethod:

```{autodoc2-docstring} abtem.potentials.iam.BaseField.generate_slices
```

````

````{py:method} build(first_slice: int = 0, last_slice: typing.Optional[int] = None, chunks: int = 1, lazy: typing.Optional[bool] = None)
:canonical: abtem.potentials.iam.BaseField.build
:abstractmethod:

```{autodoc2-docstring} abtem.potentials.iam.BaseField.build
```

````

````{py:property} num_slices
:canonical: abtem.potentials.iam.BaseField.num_slices
:type: int

```{autodoc2-docstring} abtem.potentials.iam.BaseField.num_slices
```

````

````{py:property} slice_thickness
:canonical: abtem.potentials.iam.BaseField.slice_thickness
:abstractmethod:
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.potentials.iam.BaseField.slice_thickness
```

````

````{py:property} slice_limits
:canonical: abtem.potentials.iam.BaseField.slice_limits
:type: list[tuple[float, float]]

```{autodoc2-docstring} abtem.potentials.iam.BaseField.slice_limits
```

````

````{py:property} thickness
:canonical: abtem.potentials.iam.BaseField.thickness
:type: float

```{autodoc2-docstring} abtem.potentials.iam.BaseField.thickness
```

````

````{py:method} project() -> abtem.measurements.Images
:canonical: abtem.potentials.iam.BaseField.project

```{autodoc2-docstring} abtem.potentials.iam.BaseField.project
```

````

````{py:method} to_images()
:canonical: abtem.potentials.iam.BaseField.to_images

```{autodoc2-docstring} abtem.potentials.iam.BaseField.to_images
```

````

````{py:method} show(project: bool = True, **kwargs)
:canonical: abtem.potentials.iam.BaseField.show

```{autodoc2-docstring} abtem.potentials.iam.BaseField.show
```

````

````{py:method} depth_profile(projection_axis: str = 'y', depth: typing.Optional[float] = None) -> abtem.measurements.Images
:canonical: abtem.potentials.iam.BaseField.depth_profile

```{autodoc2-docstring} abtem.potentials.iam.BaseField.depth_profile
```

````

````{py:method} show_depth_profile(projection_axis: str = 'y', depth: typing.Optional[float] = None, z_scale: float = 1.0, slice_lines: bool = True, ax=None, cbar: bool = False, cmap: typing.Optional[str] = None, vmin: typing.Optional[float] = None, vmax: typing.Optional[float] = None, power: float = 1.0, common_color_scale: bool = False, explode: bool | typing.Sequence[int] = (), figsize: typing.Optional[tuple[int, int]] = None, title: bool | str = True, **kwargs)
:canonical: abtem.potentials.iam.BaseField.show_depth_profile

```{autodoc2-docstring} abtem.potentials.iam.BaseField.show_depth_profile
```

````

`````

`````{py:class} BasePotential
:canonical: abtem.potentials.iam.BasePotential

Bases: {py:obj}`abtem.potentials.iam.BaseField`

```{autodoc2-docstring} abtem.potentials.iam.BasePotential
```

````{py:property} base_axes_metadata
:canonical: abtem.potentials.iam.BasePotential.base_axes_metadata

```{autodoc2-docstring} abtem.potentials.iam.BasePotential.base_axes_metadata
```

````

`````

````{py:function} validate_potential(potential: ase.Atoms | abtem.potentials.iam.BasePotential, waves: typing.Optional[abtem.waves.BaseWaves] = None) -> abtem.potentials.iam.BasePotential
:canonical: abtem.potentials.iam.validate_potential

```{autodoc2-docstring} abtem.potentials.iam.validate_potential
```
````

````{py:class} Potential(atoms: ase.Atoms | abtem.inelastic.phonons.BaseFrozenPhonons, gpts: int | tuple[int, int] | None = None, sampling: float | tuple[float, float] | None = None, slice_thickness: float | tuple[float, ...] = 1, parametrization: str | abtem.parametrizations.Parametrization = 'lobato', projection: str = 'infinite', exit_planes: int | tuple[int, ...] | None = None, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy', origin: tuple[float, float, float] = (0.0, 0.0, 0.0), box: tuple[float, float, float] | None = None, periodic: bool = True, integrator: abtem.integrals.FieldIntegrator | None = None, device: str | None = None)
:canonical: abtem.potentials.iam.Potential

Bases: {py:obj}`abtem.potentials.iam._FieldBuilderFromAtoms`, {py:obj}`abtem.potentials.iam.BasePotential`

```{autodoc2-docstring} abtem.potentials.iam.Potential
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.iam.Potential.__init__
```

````

`````{py:class} FieldArray(array: numpy.ndarray | dask.array.core.Array, slice_thickness: float | typing.Sequence[float], extent: typing.Optional[float | tuple[float, float]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, exit_planes: typing.Optional[int | tuple[int, ...]] = None, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
:canonical: abtem.potentials.iam.FieldArray

Bases: {py:obj}`abtem.potentials.iam.BaseField`, {py:obj}`abtem.array.ArrayObject`

````{py:property} num_configurations
:canonical: abtem.potentials.iam.FieldArray.num_configurations

````

````{py:property} slice_thickness
:canonical: abtem.potentials.iam.FieldArray.slice_thickness
:type: tuple[float, ...]

````

````{py:property} exit_planes
:canonical: abtem.potentials.iam.FieldArray.exit_planes
:type: tuple[int, ...]

````

````{py:method} build(first_slice: int = 0, last_slice: typing.Optional[int] = None, chunks: int = 1, lazy: typing.Optional[bool] = None)
:canonical: abtem.potentials.iam.FieldArray.build

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.build
```

````

````{py:method} generate_slices(first_slice: int = 0, last_slice: typing.Optional[int] = None)
:canonical: abtem.potentials.iam.FieldArray.generate_slices

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.generate_slices
```

````

````{py:method} tile(repetitions: tuple[int, int] | tuple[int, int, int])
:canonical: abtem.potentials.iam.FieldArray.tile

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.tile
```

````

````{py:method} to_hyperspy(transpose: bool = True)
:canonical: abtem.potentials.iam.FieldArray.to_hyperspy

````

````{py:method} to_images()
:canonical: abtem.potentials.iam.FieldArray.to_images

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.to_images
```

````

````{py:method} depth_profile(projection_axis: str = 'y', depth: typing.Optional[float] = None) -> abtem.measurements.Images
:canonical: abtem.potentials.iam.FieldArray.depth_profile

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.depth_profile
```

````

````{py:method} project() -> abtem.measurements.Images
:canonical: abtem.potentials.iam.FieldArray.project

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.project
```

````

`````

`````{py:class} PotentialArray(array: numpy.ndarray | dask.array.core.Array, slice_thickness: float | typing.Sequence[float], extent: typing.Optional[float | tuple[float, float]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, exit_planes: typing.Optional[int | tuple[int, ...]] = None, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
:canonical: abtem.potentials.iam.PotentialArray

Bases: {py:obj}`abtem.potentials.iam.BasePotential`, {py:obj}`abtem.potentials.iam.FieldArray`

```{autodoc2-docstring} abtem.potentials.iam.PotentialArray
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.iam.PotentialArray.__init__
```

````{py:method} from_array_and_metadata(array: numpy.ndarray | dask.array.core.Array, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: dict) -> abtem.potentials.iam.PotentialArray
:canonical: abtem.potentials.iam.PotentialArray.from_array_and_metadata
:abstractmethod:
:classmethod:

````

````{py:method} transmission_function(energy: float) -> abtem.potentials.iam.TransmissionFunction
:canonical: abtem.potentials.iam.PotentialArray.transmission_function

```{autodoc2-docstring} abtem.potentials.iam.PotentialArray.transmission_function
```

````

````{py:method} transmit(waves: abtem.waves.Waves, conjugate: bool = False) -> abtem.waves.Waves
:canonical: abtem.potentials.iam.PotentialArray.transmit

```{autodoc2-docstring} abtem.potentials.iam.PotentialArray.transmit
```

````

`````

`````{py:class} TransmissionFunction(array: numpy.ndarray, slice_thickness: float | typing.Sequence[float], extent: typing.Optional[float | tuple[float, float]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, energy: typing.Optional[float] = None)
:canonical: abtem.potentials.iam.TransmissionFunction

Bases: {py:obj}`abtem.potentials.iam.PotentialArray`, {py:obj}`abtem.core.energy.HasAcceleratorMixin`

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction.__init__
```

````{py:method} get_chunk(first_slice, last_slice) -> abtem.potentials.iam.TransmissionFunction
:canonical: abtem.potentials.iam.TransmissionFunction.get_chunk

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction.get_chunk
```

````

````{py:method} transmission_function(energy) -> abtem.potentials.iam.TransmissionFunction
:canonical: abtem.potentials.iam.TransmissionFunction.transmission_function

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction.transmission_function
```

````

````{py:method} transmit(waves: abtem.waves.Waves, conjugate: bool = False) -> abtem.waves.Waves
:canonical: abtem.potentials.iam.TransmissionFunction.transmit

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction.transmit
```

````

`````

`````{py:class} CrystalPotential(potential_unit: abtem.potentials.iam.BasePotential, repetitions: tuple[int, int, int], num_frozen_phonons: int | None = None, exit_planes: int | None = None, seeds: int | tuple[int, ...] | None = None, ensemble_mean: bool = True)
:canonical: abtem.potentials.iam.CrystalPotential

Bases: {py:obj}`abtem.potentials.iam._PotentialBuilder`

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.__init__
```

````{py:property} ensemble_mean
:canonical: abtem.potentials.iam.CrystalPotential.ensemble_mean
:type: bool

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.ensemble_mean
```

````

````{py:property} ensemble_shape
:canonical: abtem.potentials.iam.CrystalPotential.ensemble_shape
:type: tuple[int, ...]

````

````{py:property} num_configurations
:canonical: abtem.potentials.iam.CrystalPotential.num_configurations

````

````{py:property} seeds
:canonical: abtem.potentials.iam.CrystalPotential.seeds

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.seeds
```

````

````{py:property} potential_unit
:canonical: abtem.potentials.iam.CrystalPotential.potential_unit
:type: abtem.potentials.iam.BasePotential

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.potential_unit
```

````

````{py:property} gpts
:canonical: abtem.potentials.iam.CrystalPotential.gpts
:type: tuple[int, int] | None

````

````{py:property} sampling
:canonical: abtem.potentials.iam.CrystalPotential.sampling
:type: tuple[float, float] | None

````

````{py:property} repetitions
:canonical: abtem.potentials.iam.CrystalPotential.repetitions
:type: tuple[int, int, int]

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.repetitions
```

````

````{py:property} num_slices
:canonical: abtem.potentials.iam.CrystalPotential.num_slices
:type: int

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.potentials.iam.CrystalPotential.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:method} get_sliced_atoms() -> abtem.slicing.BaseSlicedAtoms
:canonical: abtem.potentials.iam.CrystalPotential.get_sliced_atoms

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.get_sliced_atoms
```

````

````{py:method} generate_slices(first_slice: int = 0, last_slice: typing.Optional[int] = None, return_depth: bool = False)
:canonical: abtem.potentials.iam.CrystalPotential.generate_slices

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.generate_slices
```

````

`````
