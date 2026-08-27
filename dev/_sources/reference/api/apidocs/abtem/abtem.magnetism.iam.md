# {py:mod}`abtem.magnetism.iam`

```{py:module} abtem.magnetism.iam
```

```{autodoc2-docstring} abtem.magnetism.iam
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`QuasiDipoleProjections <abtem.magnetism.iam.QuasiDipoleProjections>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections
    :summary:
    ```
* - {py:obj}`QuasiDipoleMagneticFieldProjections <abtem.magnetism.iam.QuasiDipoleMagneticFieldProjections>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleMagneticFieldProjections
    :summary:
    ```
* - {py:obj}`QuasiDipoleVectorPotentialProjections <abtem.magnetism.iam.QuasiDipoleVectorPotentialProjections>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleVectorPotentialProjections
    :summary:
    ```
* - {py:obj}`BaseMagneticField <abtem.magnetism.iam.BaseMagneticField>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.BaseMagneticField
    :summary:
    ```
* - {py:obj}`BaseVectorPotential <abtem.magnetism.iam.BaseVectorPotential>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.BaseVectorPotential
    :summary:
    ```
* - {py:obj}`MagneticFieldArray <abtem.magnetism.iam.MagneticFieldArray>`
  -
* - {py:obj}`VectorPotentialArray <abtem.magnetism.iam.VectorPotentialArray>`
  -
* - {py:obj}`MagneticField <abtem.magnetism.iam.MagneticField>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.MagneticField
    :summary:
    ```
* - {py:obj}`VectorPotential <abtem.magnetism.iam.VectorPotential>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.VectorPotential
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`radial_prefactor_a <abtem.magnetism.iam.radial_prefactor_a>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.radial_prefactor_a
    :summary:
    ```
* - {py:obj}`radial_prefactor_b1 <abtem.magnetism.iam.radial_prefactor_b1>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.radial_prefactor_b1
    :summary:
    ```
* - {py:obj}`radial_prefactor_b2 <abtem.magnetism.iam.radial_prefactor_b2>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.radial_prefactor_b2
    :summary:
    ```
* - {py:obj}`unit_vector_from_angles <abtem.magnetism.iam.unit_vector_from_angles>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.unit_vector_from_angles
    :summary:
    ```
* - {py:obj}`atomic_vector_potential_3d <abtem.magnetism.iam.atomic_vector_potential_3d>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.atomic_vector_potential_3d
    :summary:
    ```
* - {py:obj}`atomic_magnetic_field_3d <abtem.magnetism.iam.atomic_magnetic_field_3d>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.atomic_magnetic_field_3d
    :summary:
    ```
* - {py:obj}`magnetic_field_3d <abtem.magnetism.iam.magnetic_field_3d>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.magnetic_field_3d
    :summary:
    ```
* - {py:obj}`vector_potential_3d <abtem.magnetism.iam.vector_potential_3d>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.vector_potential_3d
    :summary:
    ```
* - {py:obj}`radial_cutoff <abtem.magnetism.iam.radial_cutoff>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.radial_cutoff
    :summary:
    ```
* - {py:obj}`index_mask <abtem.magnetism.iam.index_mask>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.index_mask
    :summary:
    ```
* - {py:obj}`rotate_points_2d <abtem.magnetism.iam.rotate_points_2d>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.rotate_points_2d
    :summary:
    ```
* - {py:obj}`cartesian2polar_3d <abtem.magnetism.iam.cartesian2polar_3d>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.cartesian2polar_3d
    :summary:
    ```
* - {py:obj}`symmetric_arange <abtem.magnetism.iam.symmetric_arange>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.symmetric_arange
    :summary:
    ```
* - {py:obj}`bilinear_weighted_sum <abtem.magnetism.iam.bilinear_weighted_sum>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.bilinear_weighted_sum
    :summary:
    ```
* - {py:obj}`interpolate <abtem.magnetism.iam.interpolate>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.interpolate
    :summary:
    ```
* - {py:obj}`interpolate_quasi_dipole_field_projections <abtem.magnetism.iam.interpolate_quasi_dipole_field_projections>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.interpolate_quasi_dipole_field_projections
    :summary:
    ```
* - {py:obj}`interpolate_quasi_dipole_vector_field_projections <abtem.magnetism.iam.interpolate_quasi_dipole_vector_field_projections>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.interpolate_quasi_dipole_vector_field_projections
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CUTOFF <abtem.magnetism.iam.CUTOFF>`
  - ```{autodoc2-docstring} abtem.magnetism.iam.CUTOFF
    :summary:
    ```
````

### API

````{py:data} CUTOFF
:canonical: abtem.magnetism.iam.CUTOFF
:value: >
   4.25

```{autodoc2-docstring} abtem.magnetism.iam.CUTOFF
```

````

````{py:function} radial_prefactor_a(r: numpy.ndarray, parameters: numpy.ndarray) -> typing.Callable
:canonical: abtem.magnetism.iam.radial_prefactor_a

```{autodoc2-docstring} abtem.magnetism.iam.radial_prefactor_a
```
````

````{py:function} radial_prefactor_b1(r: numpy.ndarray, parameters: numpy.ndarray) -> typing.Callable
:canonical: abtem.magnetism.iam.radial_prefactor_b1

```{autodoc2-docstring} abtem.magnetism.iam.radial_prefactor_b1
```
````

````{py:function} radial_prefactor_b2(r: numpy.ndarray, parameters: numpy.ndarray) -> typing.Callable
:canonical: abtem.magnetism.iam.radial_prefactor_b2

```{autodoc2-docstring} abtem.magnetism.iam.radial_prefactor_b2
```
````

````{py:function} unit_vector_from_angles(theta: numpy.ndarray, phi: numpy.ndarray) -> numpy.ndarray
:canonical: abtem.magnetism.iam.unit_vector_from_angles

```{autodoc2-docstring} abtem.magnetism.iam.unit_vector_from_angles
```
````

````{py:function} atomic_vector_potential_3d(extent: tuple[float, float, float], gpts: tuple[int, int, int], origin: tuple[float, float, float], magnetic_moment: numpy.ndarray, parameters: numpy.ndarray, cutoff: float) -> numpy.ndarray
:canonical: abtem.magnetism.iam.atomic_vector_potential_3d

```{autodoc2-docstring} abtem.magnetism.iam.atomic_vector_potential_3d
```
````

````{py:function} atomic_magnetic_field_3d(extent: tuple[float, float, float], gpts: tuple[int, int, int], origin: tuple[float, float, float], magnetic_moment: numpy.ndarray, parameters: numpy.ndarray, cutoff: float) -> numpy.ndarray
:canonical: abtem.magnetism.iam.atomic_magnetic_field_3d

```{autodoc2-docstring} abtem.magnetism.iam.atomic_magnetic_field_3d
```
````

````{py:function} magnetic_field_3d(atoms: ase.Atoms, gpts: tuple[int, int, int], cutoff: float = 6.0)
:canonical: abtem.magnetism.iam.magnetic_field_3d

```{autodoc2-docstring} abtem.magnetism.iam.magnetic_field_3d
```
````

````{py:function} vector_potential_3d(atoms: ase.Atoms, gpts: tuple[int, int, int], cutoff: float = 6.0)
:canonical: abtem.magnetism.iam.vector_potential_3d

```{autodoc2-docstring} abtem.magnetism.iam.vector_potential_3d
```
````

````{py:function} radial_cutoff(func: typing.Callable, tolerance: float = 0.001)
:canonical: abtem.magnetism.iam.radial_cutoff

```{autodoc2-docstring} abtem.magnetism.iam.radial_cutoff
```
````

````{py:function} index_mask(indices, shape)
:canonical: abtem.magnetism.iam.index_mask

```{autodoc2-docstring} abtem.magnetism.iam.index_mask
```
````

````{py:function} rotate_points_2d(points, phi)
:canonical: abtem.magnetism.iam.rotate_points_2d

```{autodoc2-docstring} abtem.magnetism.iam.rotate_points_2d
```
````

````{py:function} cartesian2polar_3d(v: numpy.ndarray) -> tuple[float, float, float]
:canonical: abtem.magnetism.iam.cartesian2polar_3d

```{autodoc2-docstring} abtem.magnetism.iam.cartesian2polar_3d
```
````

````{py:function} symmetric_arange(cutoff: float, sampling: float) -> numpy.ndarray
:canonical: abtem.magnetism.iam.symmetric_arange

```{autodoc2-docstring} abtem.magnetism.iam.symmetric_arange
```
````

````{py:function} bilinear_weighted_sum(array: numpy.ndarray, x: int, y: int, wx0: float, wx1: float, wy0: float, wy1: float) -> float
:canonical: abtem.magnetism.iam.bilinear_weighted_sum

```{autodoc2-docstring} abtem.magnetism.iam.bilinear_weighted_sum
```
````

````{py:function} interpolate(array_out, array_in, position, sampling_out, sampling_in)
:canonical: abtem.magnetism.iam.interpolate

```{autodoc2-docstring} abtem.magnetism.iam.interpolate
```
````

````{py:function} interpolate_quasi_dipole_field_projections(magnetic_field, sampling, positions, magnetic_moments, slice_limits, integral_limits, integral_sampling, tables)
:canonical: abtem.magnetism.iam.interpolate_quasi_dipole_field_projections

```{autodoc2-docstring} abtem.magnetism.iam.interpolate_quasi_dipole_field_projections
```
````

````{py:function} interpolate_quasi_dipole_vector_field_projections(magnetic_field, sampling, positions, magnetic_moments, slice_limits, integral_limits, integral_sampling, tables)
:canonical: abtem.magnetism.iam.interpolate_quasi_dipole_vector_field_projections

```{autodoc2-docstring} abtem.magnetism.iam.interpolate_quasi_dipole_vector_field_projections
```
````

`````{py:class} QuasiDipoleProjections(interpolation_func, parametrization: str = 'lyon', cutoff: float = CUTOFF, integration_steps: float = 0.01, sampling: float = 0.1, slice_thickness: float = 0.1)
:canonical: abtem.magnetism.iam.QuasiDipoleProjections

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.__init__
```

````{py:property} slice_thickness
:canonical: abtem.magnetism.iam.QuasiDipoleProjections.slice_thickness

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.slice_thickness
```

````

````{py:method} cutoff(symbol)
:canonical: abtem.magnetism.iam.QuasiDipoleProjections.cutoff

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.cutoff
```

````

````{py:property} parametrization
:canonical: abtem.magnetism.iam.QuasiDipoleProjections.parametrization

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.parametrization
```

````

````{py:property} finite
:canonical: abtem.magnetism.iam.QuasiDipoleProjections.finite

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.finite
```

````

````{py:property} periodic
:canonical: abtem.magnetism.iam.QuasiDipoleProjections.periodic

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.periodic
```

````

````{py:property} sampling
:canonical: abtem.magnetism.iam.QuasiDipoleProjections.sampling

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.sampling
```

````

````{py:method} get_integral_table(symbol: str)
:canonical: abtem.magnetism.iam.QuasiDipoleProjections.get_integral_table

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.get_integral_table
```

````

````{py:method} integrate_on_grid(atoms: ase.Atoms, a: float, b: float, gpts: tuple[int, int], sampling: tuple[float, float], device: str = 'cpu')
:canonical: abtem.magnetism.iam.QuasiDipoleProjections.integrate_on_grid

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleProjections.integrate_on_grid
```

````

`````

````{py:class} QuasiDipoleMagneticFieldProjections(parametrization: str = 'lyon', cutoff: float = CUTOFF, integration_steps: float = 0.01, sampling: float = 0.1, slice_thickness: float = 0.1)
:canonical: abtem.magnetism.iam.QuasiDipoleMagneticFieldProjections

Bases: {py:obj}`abtem.magnetism.iam.QuasiDipoleProjections`

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleMagneticFieldProjections
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleMagneticFieldProjections.__init__
```

````

````{py:class} QuasiDipoleVectorPotentialProjections(parametrization: str = 'lyon', cutoff: float = CUTOFF, integration_steps: float = 0.01, sampling: float = 0.1, slice_thickness: float = 0.1)
:canonical: abtem.magnetism.iam.QuasiDipoleVectorPotentialProjections

Bases: {py:obj}`abtem.magnetism.iam.QuasiDipoleProjections`

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleVectorPotentialProjections
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.magnetism.iam.QuasiDipoleVectorPotentialProjections.__init__
```

````

`````{py:class} BaseMagneticField
:canonical: abtem.magnetism.iam.BaseMagneticField

Bases: {py:obj}`abtem.potentials.iam.BaseField`

```{autodoc2-docstring} abtem.magnetism.iam.BaseMagneticField
```

````{py:property} base_shape
:canonical: abtem.magnetism.iam.BaseMagneticField.base_shape

```{autodoc2-docstring} abtem.magnetism.iam.BaseMagneticField.base_shape
```

````

````{py:property} base_axes_metadata
:canonical: abtem.magnetism.iam.BaseMagneticField.base_axes_metadata

```{autodoc2-docstring} abtem.magnetism.iam.BaseMagneticField.base_axes_metadata
```

````

`````

`````{py:class} BaseVectorPotential
:canonical: abtem.magnetism.iam.BaseVectorPotential

Bases: {py:obj}`abtem.potentials.iam.BaseField`

```{autodoc2-docstring} abtem.magnetism.iam.BaseVectorPotential
```

````{py:property} base_shape
:canonical: abtem.magnetism.iam.BaseVectorPotential.base_shape

```{autodoc2-docstring} abtem.magnetism.iam.BaseVectorPotential.base_shape
```

````

````{py:property} base_axes_metadata
:canonical: abtem.magnetism.iam.BaseVectorPotential.base_axes_metadata

```{autodoc2-docstring} abtem.magnetism.iam.BaseVectorPotential.base_axes_metadata
```

````

`````

`````{py:class} MagneticFieldArray(array: numpy.ndarray | dask.array.core.Array, slice_thickness: float | typing.Sequence[float], extent: typing.Optional[float | tuple[float, float]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, exit_planes: typing.Optional[int | tuple[int, ...]] = None, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
:canonical: abtem.magnetism.iam.MagneticFieldArray

Bases: {py:obj}`abtem.magnetism.iam.BaseMagneticField`, {py:obj}`abtem.potentials.iam.FieldArray`

````{py:method} from_array_and_metadata(array: numpy.ndarray | dask.array.core.Array, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: dict) -> abtem.magnetism.iam.MagneticFieldArray
:canonical: abtem.magnetism.iam.MagneticFieldArray.from_array_and_metadata
:abstractmethod:
:classmethod:

````

`````

`````{py:class} VectorPotentialArray(array: numpy.ndarray | dask.array.core.Array, slice_thickness: float | typing.Sequence[float], extent: typing.Optional[float | tuple[float, float]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, exit_planes: typing.Optional[int | tuple[int, ...]] = None, ensemble_axes_metadata: typing.Optional[list[abtem.core.axes.AxisMetadata]] = None, metadata: typing.Optional[dict] = None)
:canonical: abtem.magnetism.iam.VectorPotentialArray

Bases: {py:obj}`abtem.magnetism.iam.BaseVectorPotential`, {py:obj}`abtem.potentials.iam.FieldArray`

````{py:method} from_array_and_metadata(array: numpy.ndarray | dask.array.core.Array, axes_metadata: list[abtem.core.axes.AxisMetadata], metadata: dict) -> abtem.magnetism.iam.VectorPotentialArray
:canonical: abtem.magnetism.iam.VectorPotentialArray.from_array_and_metadata
:abstractmethod:
:classmethod:

````

````{py:method} adjust_coulomb_potential(potential_array: abtem.potentials.iam.PotentialArray, energy: float)
:canonical: abtem.magnetism.iam.VectorPotentialArray.adjust_coulomb_potential

```{autodoc2-docstring} abtem.magnetism.iam.VectorPotentialArray.adjust_coulomb_potential
```

````

`````

````{py:class} MagneticField(atoms: ase.Atoms | abtem.inelastic.phonons.BaseFrozenPhonons, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, slice_thickness: float | tuple[float, ...] = 1, parametrization: str = 'lyon', exit_planes: typing.Optional[int | tuple[int, ...]] = None, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy', origin: tuple[float, float, float] = (0.0, 0.0, 0.0), box: typing.Optional[tuple[float, float, float]] = None, periodic: bool = True, integrator=None, device: typing.Optional[str] = None)
:canonical: abtem.magnetism.iam.MagneticField

Bases: {py:obj}`abtem.potentials.iam._FieldBuilderFromAtoms`, {py:obj}`abtem.magnetism.iam.BaseMagneticField`

```{autodoc2-docstring} abtem.magnetism.iam.MagneticField
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.magnetism.iam.MagneticField.__init__
```

````

````{py:class} VectorPotential(atoms: ase.Atoms | abtem.inelastic.phonons.BaseFrozenPhonons, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, slice_thickness: float | tuple[float, ...] = 1, parametrization: str = 'lyon', exit_planes: typing.Optional[int | tuple[int, ...]] = None, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy', origin: tuple[float, float, float] = (0.0, 0.0, 0.0), box: typing.Optional[tuple[float, float, float]] = None, periodic: bool = True, integrator=None, device: typing.Optional[str] = None)
:canonical: abtem.magnetism.iam.VectorPotential

Bases: {py:obj}`abtem.potentials.iam._FieldBuilderFromAtoms`, {py:obj}`abtem.magnetism.iam.BaseMagneticField`

```{autodoc2-docstring} abtem.magnetism.iam.VectorPotential
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.magnetism.iam.VectorPotential.__init__
```

````
