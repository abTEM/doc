# {py:mod}`abtem.magnetism.gpaw`

```{py:module} abtem.magnetism.gpaw
```

```{autodoc2-docstring} abtem.magnetism.gpaw
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`GPAW <abtem.magnetism.gpaw.GPAW>`
  -
* - {py:obj}`GPAWMagneticField <abtem.magnetism.gpaw.GPAWMagneticField>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticField
    :parser: rst
    :summary:
    ```
* - {py:obj}`GPAWVectorPotential <abtem.magnetism.gpaw.GPAWVectorPotential>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWVectorPotential
    :parser: rst
    :summary:
    ```
* - {py:obj}`SpinDensityMagneticField <abtem.magnetism.gpaw.SpinDensityMagneticField>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.SpinDensityMagneticField
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`calculate_constant_magnetic_field <abtem.magnetism.gpaw.calculate_constant_magnetic_field>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.calculate_constant_magnetic_field
    :parser: rst
    :summary:
    ```
* - {py:obj}`calculate_magnetic_vector_potential <abtem.magnetism.gpaw.calculate_magnetic_vector_potential>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.calculate_magnetic_vector_potential
    :parser: rst
    :summary:
    ```
* - {py:obj}`get_magnetic_field_from_gpaw <abtem.magnetism.gpaw.get_magnetic_field_from_gpaw>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.get_magnetic_field_from_gpaw
    :parser: rst
    :summary:
    ```
* - {py:obj}`get_vector_potential_from_gpaw <abtem.magnetism.gpaw.get_vector_potential_from_gpaw>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.get_vector_potential_from_gpaw
    :parser: rst
    :summary:
    ```
* - {py:obj}`rotate_vector_field <abtem.magnetism.gpaw.rotate_vector_field>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.rotate_vector_field
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} GPAW
:canonical: abtem.magnetism.gpaw.GPAW

Bases: {py:obj}`typing.Protocol`

````{py:property} atoms
:canonical: abtem.magnetism.gpaw.GPAW.atoms
:type: ase.Atoms

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAW.atoms
:parser: rst
```

````

````{py:method} get_number_of_grid_points() -> numpy.ndarray
:canonical: abtem.magnetism.gpaw.GPAW.get_number_of_grid_points

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAW.get_number_of_grid_points
:parser: rst
```

````

`````

````{py:class} GPAWMagneticField(calculators: abtem.magnetism.gpaw.GPAW | list[abtem.magnetism.gpaw.GPAW] | list[str] | str, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, slice_thickness: float | tuple[float, ...] = 1.0, exit_planes: typing.Optional[int | tuple[int, ...]] = None, plane: str = 'xy', rotate_field: typing.Optional[tuple[float, float, float]] = None, origin: tuple[float, float, float] = (0.0, 0.0, 0.0), box: typing.Optional[tuple[float, float, float]] = None, periodic: bool = True, frozen_phonons: typing.Optional[abtem.inelastic.phonons.BaseFrozenPhonons] = None, repetitions: tuple[int, int, int] = (1, 1, 1), gridrefinement: int = 1, projection: str = 'fft', device: typing.Optional[str] = None)
:canonical: abtem.magnetism.gpaw.GPAWMagneticField

Bases: {py:obj}`abtem.magnetism.gpaw._GPAWMagnetics`, {py:obj}`abtem.magnetism.iam.BaseMagneticField`

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticField
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticField.__init__
:parser: rst
```

````

````{py:class} GPAWVectorPotential(calculators: abtem.magnetism.gpaw.GPAW | list[abtem.magnetism.gpaw.GPAW] | list[str] | str, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, slice_thickness: float | tuple[float, ...] = 1.0, exit_planes: typing.Optional[int | tuple[int, ...]] = None, plane: str = 'xy', rotate_field: typing.Optional[tuple[float, float, float]] = None, origin: tuple[float, float, float] = (0.0, 0.0, 0.0), box: typing.Optional[tuple[float, float, float]] = None, periodic: bool = True, frozen_phonons: typing.Optional[abtem.inelastic.phonons.BaseFrozenPhonons] = None, repetitions: tuple[int, int, int] = (1, 1, 1), gridrefinement: int = 1, projection: str = 'fft', device: typing.Optional[str] = None)
:canonical: abtem.magnetism.gpaw.GPAWVectorPotential

Bases: {py:obj}`abtem.magnetism.gpaw._GPAWMagnetics`, {py:obj}`abtem.magnetism.iam.BaseVectorPotential`

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWVectorPotential
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWVectorPotential.__init__
:parser: rst
```

````

````{py:class} SpinDensityMagneticField(spin_density, cell)
:canonical: abtem.magnetism.gpaw.SpinDensityMagneticField

```{autodoc2-docstring} abtem.magnetism.gpaw.SpinDensityMagneticField
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.magnetism.gpaw.SpinDensityMagneticField.__init__
:parser: rst
```

````

````{py:function} calculate_constant_magnetic_field()
:canonical: abtem.magnetism.gpaw.calculate_constant_magnetic_field

```{autodoc2-docstring} abtem.magnetism.gpaw.calculate_constant_magnetic_field
:parser: rst
```
````

````{py:function} calculate_magnetic_vector_potential(spin_density, cell)
:canonical: abtem.magnetism.gpaw.calculate_magnetic_vector_potential

```{autodoc2-docstring} abtem.magnetism.gpaw.calculate_magnetic_vector_potential
:parser: rst
```
````

````{py:function} get_magnetic_field_from_gpaw(calc, gridrefinement=2, assume_colinear=True)
:canonical: abtem.magnetism.gpaw.get_magnetic_field_from_gpaw

```{autodoc2-docstring} abtem.magnetism.gpaw.get_magnetic_field_from_gpaw
:parser: rst
```
````

````{py:function} get_vector_potential_from_gpaw(calc, gridrefinement=2, assume_colinear=True)
:canonical: abtem.magnetism.gpaw.get_vector_potential_from_gpaw

```{autodoc2-docstring} abtem.magnetism.gpaw.get_vector_potential_from_gpaw
:parser: rst
```
````

````{py:function} rotate_vector_field(vector_field: numpy.ndarray, euler_angles: tuple[float, float, float]) -> numpy.ndarray
:canonical: abtem.magnetism.gpaw.rotate_vector_field

```{autodoc2-docstring} abtem.magnetism.gpaw.rotate_vector_field
:parser: rst
```
````
