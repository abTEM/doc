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
* - {py:obj}`GPAWMagneticFields <abtem.magnetism.gpaw.GPAWMagneticFields>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticFields
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
* - {py:obj}`gpaw_magnetic_fields <abtem.magnetism.gpaw.gpaw_magnetic_fields>`
  - ```{autodoc2-docstring} abtem.magnetism.gpaw.gpaw_magnetic_fields
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

````{py:class} GPAWMagneticField(...)
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

`````{py:class} GPAWMagneticFields
:canonical: abtem.magnetism.gpaw.GPAWMagneticFields

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticFields
:parser: rst
```

````{py:method} combined_potential(...) -> abtem.potentials.iam.PotentialArray
:canonical: abtem.magnetism.gpaw.GPAWMagneticFields.combined_potential

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticFields.combined_potential
:parser: rst
```

````

````{py:attribute} magnetic_field
:canonical: abtem.magnetism.gpaw.GPAWMagneticFields.magnetic_field
:type: typing.Optional[abtem.magnetism.iam.MagneticFieldArray]
:value: >
   None

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticFields.magnetic_field
:parser: rst
```

````

````{py:attribute} potential
:canonical: abtem.magnetism.gpaw.GPAWMagneticFields.potential
:type: abtem.potentials.iam.PotentialArray
:value: >
   None

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticFields.potential
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.magnetism.gpaw.GPAWMagneticFields.show

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticFields.show
:parser: rst
```

````

````{py:method} tile(...) -> abtem.magnetism.gpaw.GPAWMagneticFields
:canonical: abtem.magnetism.gpaw.GPAWMagneticFields.tile

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticFields.tile
:parser: rst
```

````

````{py:attribute} vector_potential
:canonical: abtem.magnetism.gpaw.GPAWMagneticFields.vector_potential
:type: abtem.magnetism.iam.VectorPotentialArray
:value: >
   None

```{autodoc2-docstring} abtem.magnetism.gpaw.GPAWMagneticFields.vector_potential
:parser: rst
```

````

`````

````{py:class} GPAWVectorPotential(...)
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

````{py:class} SpinDensityMagneticField(...)
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

````{py:function} calculate_magnetic_vector_potential(...)
:canonical: abtem.magnetism.gpaw.calculate_magnetic_vector_potential

```{autodoc2-docstring} abtem.magnetism.gpaw.calculate_magnetic_vector_potential
:parser: rst
```
````

````{py:function} get_magnetic_field_from_gpaw(...)
:canonical: abtem.magnetism.gpaw.get_magnetic_field_from_gpaw

```{autodoc2-docstring} abtem.magnetism.gpaw.get_magnetic_field_from_gpaw
:parser: rst
```
````

````{py:function} get_vector_potential_from_gpaw(...)
:canonical: abtem.magnetism.gpaw.get_vector_potential_from_gpaw

```{autodoc2-docstring} abtem.magnetism.gpaw.get_vector_potential_from_gpaw
:parser: rst
```
````

````{py:function} gpaw_magnetic_fields(...) -> abtem.magnetism.gpaw.GPAWMagneticFields
:canonical: abtem.magnetism.gpaw.gpaw_magnetic_fields

```{autodoc2-docstring} abtem.magnetism.gpaw.gpaw_magnetic_fields
:parser: rst
```
````

````{py:function} rotate_vector_field(...) -> numpy.ndarray
:canonical: abtem.magnetism.gpaw.rotate_vector_field

```{autodoc2-docstring} abtem.magnetism.gpaw.rotate_vector_field
:parser: rst
```
````
