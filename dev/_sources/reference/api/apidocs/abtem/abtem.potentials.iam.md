# {py:mod}`abtem.potentials.iam`

```{py:module} abtem.potentials.iam
```

```{autodoc2-docstring} abtem.potentials.iam
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseField <abtem.potentials.iam.BaseField>`
  - ```{autodoc2-docstring} abtem.potentials.iam.BaseField
    :parser: rst
    :summary:
    ```
* - {py:obj}`BasePotential <abtem.potentials.iam.BasePotential>`
  - ```{autodoc2-docstring} abtem.potentials.iam.BasePotential
    :parser: rst
    :summary:
    ```
* - {py:obj}`CrystalPotential <abtem.potentials.iam.CrystalPotential>`
  - ```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential
    :parser: rst
    :summary:
    ```
* - {py:obj}`FieldArray <abtem.potentials.iam.FieldArray>`
  -
* - {py:obj}`Potential <abtem.potentials.iam.Potential>`
  - ```{autodoc2-docstring} abtem.potentials.iam.Potential
    :parser: rst
    :summary:
    ```
* - {py:obj}`PotentialArray <abtem.potentials.iam.PotentialArray>`
  - ```{autodoc2-docstring} abtem.potentials.iam.PotentialArray
    :parser: rst
    :summary:
    ```
* - {py:obj}`TransmissionFunction <abtem.potentials.iam.TransmissionFunction>`
  - ```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_potential <abtem.potentials.iam.validate_potential>`
  - ```{autodoc2-docstring} abtem.potentials.iam.validate_potential
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BaseField
:canonical: abtem.potentials.iam.BaseField

Bases: {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.grid.HasGrid2DMixin`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.potentials.iam.BaseField
:parser: rst
```

````{py:property} base_axes_metadata
:canonical: abtem.potentials.iam.BaseField.base_axes_metadata
:abstractmethod:

````

````{py:property} base_shape
:canonical: abtem.potentials.iam.BaseField.base_shape

```{autodoc2-docstring} abtem.potentials.iam.BaseField.base_shape
:parser: rst
```

````

````{py:method} build(...)
:canonical: abtem.potentials.iam.BaseField.build
:abstractmethod:

```{autodoc2-docstring} abtem.potentials.iam.BaseField.build
:parser: rst
```

````

````{py:method} depth_profile(...) -> abtem.measurements.Images
:canonical: abtem.potentials.iam.BaseField.depth_profile

```{autodoc2-docstring} abtem.potentials.iam.BaseField.depth_profile
:parser: rst
```

````

````{py:property} exit_planes
:canonical: abtem.potentials.iam.BaseField.exit_planes
:abstractmethod:
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.potentials.iam.BaseField.exit_planes
:parser: rst
```

````

````{py:property} exit_thicknesses
:canonical: abtem.potentials.iam.BaseField.exit_thicknesses
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.potentials.iam.BaseField.exit_thicknesses
:parser: rst
```

````

````{py:method} generate_chunked_slices(...)
:canonical: abtem.potentials.iam.BaseField.generate_chunked_slices

```{autodoc2-docstring} abtem.potentials.iam.BaseField.generate_chunked_slices
:parser: rst
```

````

````{py:method} generate_slices(...)
:canonical: abtem.potentials.iam.BaseField.generate_slices
:abstractmethod:

```{autodoc2-docstring} abtem.potentials.iam.BaseField.generate_slices
:parser: rst
```

````

````{py:property} num_configurations
:canonical: abtem.potentials.iam.BaseField.num_configurations
:abstractmethod:

```{autodoc2-docstring} abtem.potentials.iam.BaseField.num_configurations
:parser: rst
```

````

````{py:property} num_exit_planes
:canonical: abtem.potentials.iam.BaseField.num_exit_planes
:type: int

```{autodoc2-docstring} abtem.potentials.iam.BaseField.num_exit_planes
:parser: rst
```

````

````{py:property} num_slices
:canonical: abtem.potentials.iam.BaseField.num_slices
:type: int

```{autodoc2-docstring} abtem.potentials.iam.BaseField.num_slices
:parser: rst
```

````

````{py:method} project() -> abtem.measurements.Images
:canonical: abtem.potentials.iam.BaseField.project

```{autodoc2-docstring} abtem.potentials.iam.BaseField.project
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.potentials.iam.BaseField.show

```{autodoc2-docstring} abtem.potentials.iam.BaseField.show
:parser: rst
```

````

````{py:method} show_depth_profile(...)
:canonical: abtem.potentials.iam.BaseField.show_depth_profile

```{autodoc2-docstring} abtem.potentials.iam.BaseField.show_depth_profile
:parser: rst
```

````

````{py:property} slice_limits
:canonical: abtem.potentials.iam.BaseField.slice_limits
:type: list[tuple[float, float]]

```{autodoc2-docstring} abtem.potentials.iam.BaseField.slice_limits
:parser: rst
```

````

````{py:property} slice_thickness
:canonical: abtem.potentials.iam.BaseField.slice_thickness
:abstractmethod:
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.potentials.iam.BaseField.slice_thickness
:parser: rst
```

````

````{py:property} thickness
:canonical: abtem.potentials.iam.BaseField.thickness
:type: float

```{autodoc2-docstring} abtem.potentials.iam.BaseField.thickness
:parser: rst
```

````

````{py:method} to_images()
:canonical: abtem.potentials.iam.BaseField.to_images

```{autodoc2-docstring} abtem.potentials.iam.BaseField.to_images
:parser: rst
```

````

`````

`````{py:class} BasePotential
:canonical: abtem.potentials.iam.BasePotential

Bases: {py:obj}`abtem.potentials.iam.BaseField`

```{autodoc2-docstring} abtem.potentials.iam.BasePotential
:parser: rst
```

````{py:property} base_axes_metadata
:canonical: abtem.potentials.iam.BasePotential.base_axes_metadata

```{autodoc2-docstring} abtem.potentials.iam.BasePotential.base_axes_metadata
:parser: rst
```

````

`````

`````{py:class} CrystalPotential(...)
:canonical: abtem.potentials.iam.CrystalPotential

Bases: {py:obj}`abtem.potentials.iam._PotentialBuilder`

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.__init__
:parser: rst
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.potentials.iam.CrystalPotential.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_mean
:canonical: abtem.potentials.iam.CrystalPotential.ensemble_mean
:type: bool

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.ensemble_mean
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.potentials.iam.CrystalPotential.ensemble_shape
:type: tuple[int, ...]

````

````{py:method} generate_chunked_slices(...)
:canonical: abtem.potentials.iam.CrystalPotential.generate_chunked_slices

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.generate_chunked_slices
:parser: rst
```

````

````{py:method} generate_slices(...)
:canonical: abtem.potentials.iam.CrystalPotential.generate_slices

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.generate_slices
:parser: rst
```

````

````{py:method} get_sliced_atoms() -> abtem.slicing.BaseSlicedAtoms
:canonical: abtem.potentials.iam.CrystalPotential.get_sliced_atoms

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.get_sliced_atoms
:parser: rst
```

````

````{py:property} gpts
:canonical: abtem.potentials.iam.CrystalPotential.gpts
:type: tuple[int, int] | None

````

````{py:property} num_configurations
:canonical: abtem.potentials.iam.CrystalPotential.num_configurations

````

````{py:property} num_slices
:canonical: abtem.potentials.iam.CrystalPotential.num_slices
:type: int

````

````{py:property} potential_unit
:canonical: abtem.potentials.iam.CrystalPotential.potential_unit
:type: abtem.potentials.iam.BasePotential

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.potential_unit
:parser: rst
```

````

````{py:property} repetitions
:canonical: abtem.potentials.iam.CrystalPotential.repetitions
:type: tuple[int, int, int]

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.repetitions
:parser: rst
```

````

````{py:property} sampling
:canonical: abtem.potentials.iam.CrystalPotential.sampling
:type: tuple[float, float] | None

````

````{py:property} seeds
:canonical: abtem.potentials.iam.CrystalPotential.seeds

```{autodoc2-docstring} abtem.potentials.iam.CrystalPotential.seeds
:parser: rst
```

````

`````

`````{py:class} FieldArray(...)
:canonical: abtem.potentials.iam.FieldArray

Bases: {py:obj}`abtem.potentials.iam.BaseField`, {py:obj}`abtem.array.ArrayObject`

````{py:method} build(...)
:canonical: abtem.potentials.iam.FieldArray.build

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.build
:parser: rst
```

````

````{py:method} depth_profile(...) -> abtem.measurements.Images
:canonical: abtem.potentials.iam.FieldArray.depth_profile

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.depth_profile
:parser: rst
```

````

````{py:property} exit_planes
:canonical: abtem.potentials.iam.FieldArray.exit_planes
:type: tuple[int, ...]

````

````{py:method} generate_chunked_slices(...)
:canonical: abtem.potentials.iam.FieldArray.generate_chunked_slices

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.generate_chunked_slices
:parser: rst
```

````

````{py:method} generate_slices(...)
:canonical: abtem.potentials.iam.FieldArray.generate_slices

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.generate_slices
:parser: rst
```

````

````{py:property} num_configurations
:canonical: abtem.potentials.iam.FieldArray.num_configurations

````

````{py:method} project() -> abtem.measurements.Images
:canonical: abtem.potentials.iam.FieldArray.project

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.project
:parser: rst
```

````

````{py:property} slice_thickness
:canonical: abtem.potentials.iam.FieldArray.slice_thickness
:type: tuple[float, ...]

````

````{py:method} tile(...)
:canonical: abtem.potentials.iam.FieldArray.tile

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.tile
:parser: rst
```

````

````{py:method} to_hyperspy(...)
:canonical: abtem.potentials.iam.FieldArray.to_hyperspy

````

````{py:method} to_images()
:canonical: abtem.potentials.iam.FieldArray.to_images

```{autodoc2-docstring} abtem.potentials.iam.FieldArray.to_images
:parser: rst
```

````

`````

````{py:class} Potential(...)
:canonical: abtem.potentials.iam.Potential

Bases: {py:obj}`abtem.potentials.iam._FieldBuilderFromAtoms`, {py:obj}`abtem.potentials.iam.BasePotential`

```{autodoc2-docstring} abtem.potentials.iam.Potential
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.iam.Potential.__init__
:parser: rst
```

````

`````{py:class} PotentialArray(...)
:canonical: abtem.potentials.iam.PotentialArray

Bases: {py:obj}`abtem.potentials.iam.BasePotential`, {py:obj}`abtem.potentials.iam.FieldArray`

```{autodoc2-docstring} abtem.potentials.iam.PotentialArray
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.iam.PotentialArray.__init__
:parser: rst
```

````{py:method} from_array_and_metadata(...) -> abtem.potentials.iam.PotentialArray
:canonical: abtem.potentials.iam.PotentialArray.from_array_and_metadata
:abstractmethod:
:classmethod:

````

````{py:method} transmission_function(...) -> abtem.potentials.iam.TransmissionFunction
:canonical: abtem.potentials.iam.PotentialArray.transmission_function

```{autodoc2-docstring} abtem.potentials.iam.PotentialArray.transmission_function
:parser: rst
```

````

````{py:method} transmit(...) -> abtem.waves.Waves
:canonical: abtem.potentials.iam.PotentialArray.transmit

```{autodoc2-docstring} abtem.potentials.iam.PotentialArray.transmit
:parser: rst
```

````

`````

`````{py:class} TransmissionFunction(...)
:canonical: abtem.potentials.iam.TransmissionFunction

Bases: {py:obj}`abtem.potentials.iam.PotentialArray`, {py:obj}`abtem.core.energy.HasAcceleratorMixin`

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction.__init__
:parser: rst
```

````{py:method} get_chunk(...) -> abtem.potentials.iam.TransmissionFunction
:canonical: abtem.potentials.iam.TransmissionFunction.get_chunk

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction.get_chunk
:parser: rst
```

````

````{py:method} transmission_function(...) -> abtem.potentials.iam.TransmissionFunction
:canonical: abtem.potentials.iam.TransmissionFunction.transmission_function

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction.transmission_function
:parser: rst
```

````

````{py:method} transmit(...) -> abtem.waves.Waves
:canonical: abtem.potentials.iam.TransmissionFunction.transmit

```{autodoc2-docstring} abtem.potentials.iam.TransmissionFunction.transmit
:parser: rst
```

````

`````

````{py:function} validate_potential(...) -> abtem.potentials.iam.BasePotential
:canonical: abtem.potentials.iam.validate_potential

```{autodoc2-docstring} abtem.potentials.iam.validate_potential
:parser: rst
```
````
