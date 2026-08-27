# {py:mod}`abtem.slicing`

```{py:module} abtem.slicing
```

```{autodoc2-docstring} abtem.slicing
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseSlicedAtoms <abtem.slicing.BaseSlicedAtoms>`
  - ```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms
    :summary:
    ```
* - {py:obj}`SliceIndexedAtoms <abtem.slicing.SliceIndexedAtoms>`
  - ```{autodoc2-docstring} abtem.slicing.SliceIndexedAtoms
    :summary:
    ```
* - {py:obj}`SlicedAtoms <abtem.slicing.SlicedAtoms>`
  - ```{autodoc2-docstring} abtem.slicing.SlicedAtoms
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`crystal_slice_thicknesses <abtem.slicing.crystal_slice_thicknesses>`
  - ```{autodoc2-docstring} abtem.slicing.crystal_slice_thicknesses
    :summary:
    ```
* - {py:obj}`is_number <abtem.slicing.is_number>`
  - ```{autodoc2-docstring} abtem.slicing.is_number
    :summary:
    ```
* - {py:obj}`slice_limits <abtem.slicing.slice_limits>`
  - ```{autodoc2-docstring} abtem.slicing.slice_limits
    :summary:
    ```
````

### API

`````{py:class} BaseSlicedAtoms(atoms: ase.Atoms, slice_thickness: float | typing.Sequence[float] | str)
:canonical: abtem.slicing.BaseSlicedAtoms

Bases: {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.__init__
```

````{py:property} atoms
:canonical: abtem.slicing.BaseSlicedAtoms.atoms
:type: ase.Atoms

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.atoms
```

````

````{py:property} box
:canonical: abtem.slicing.BaseSlicedAtoms.box
:type: tuple[float, float, float]

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.box
```

````

````{py:method} check_slice_idx(index: int)
:canonical: abtem.slicing.BaseSlicedAtoms.check_slice_idx

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.check_slice_idx
```

````

````{py:method} generate_atoms_in_slices(first_slice: int = 0, last_slice: typing.Optional[int] = None, atomic_number: typing.Optional[int] = None)
:canonical: abtem.slicing.BaseSlicedAtoms.generate_atoms_in_slices

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.generate_atoms_in_slices
```

````

````{py:method} get_atoms_in_slices(first_slice: int, last_slice: typing.Optional[int] = None, atomic_number: typing.Optional[int] = None) -> ase.Atoms
:canonical: abtem.slicing.BaseSlicedAtoms.get_atoms_in_slices
:abstractmethod:

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.get_atoms_in_slices
```

````

````{py:property} num_slices
:canonical: abtem.slicing.BaseSlicedAtoms.num_slices
:type: int

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.num_slices
```

````

````{py:property} slice_limits
:canonical: abtem.slicing.BaseSlicedAtoms.slice_limits
:type: list[tuple[float, float]]

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.slice_limits
```

````

````{py:property} slice_thickness
:canonical: abtem.slicing.BaseSlicedAtoms.slice_thickness
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.slice_thickness
```

````

`````

`````{py:class} SliceIndexedAtoms(atoms: ase.Atoms, slice_thickness: float | typing.Sequence[float])
:canonical: abtem.slicing.SliceIndexedAtoms

Bases: {py:obj}`abtem.slicing.BaseSlicedAtoms`

```{autodoc2-docstring} abtem.slicing.SliceIndexedAtoms
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.slicing.SliceIndexedAtoms.__init__
```

````{py:method} get_atoms_in_slices(first_slice: int, last_slice: typing.Optional[int] = None, atomic_number: typing.Optional[int] = None) -> ase.Atoms
:canonical: abtem.slicing.SliceIndexedAtoms.get_atoms_in_slices

````

`````

`````{py:class} SlicedAtoms(atoms: ase.Atoms, slice_thickness: float | typing.Sequence[float], xy_padding: float = 0.0, z_padding: float = 0.0)
:canonical: abtem.slicing.SlicedAtoms

Bases: {py:obj}`abtem.slicing.BaseSlicedAtoms`

```{autodoc2-docstring} abtem.slicing.SlicedAtoms
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.slicing.SlicedAtoms.__init__
```

````{py:method} get_atoms_in_slices(first_slice: int, last_slice: typing.Optional[int] = None, atomic_number: typing.Optional[int] = None) -> ase.Atoms
:canonical: abtem.slicing.SlicedAtoms.get_atoms_in_slices

````

`````

````{py:function} crystal_slice_thicknesses(atoms: ase.Atoms, tolerance: float = 0.2) -> numpy.ndarray
:canonical: abtem.slicing.crystal_slice_thicknesses

```{autodoc2-docstring} abtem.slicing.crystal_slice_thicknesses
```
````

````{py:function} is_number(value: typing.Any) -> typing.TypeGuard[int | float | numpy.ndarray]
:canonical: abtem.slicing.is_number

```{autodoc2-docstring} abtem.slicing.is_number
```
````

````{py:function} slice_limits(slice_thickness) -> list[tuple[float, float]]
:canonical: abtem.slicing.slice_limits

```{autodoc2-docstring} abtem.slicing.slice_limits
```
````
