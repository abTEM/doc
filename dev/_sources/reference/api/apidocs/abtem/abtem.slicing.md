# {py:mod}`abtem.slicing`

```{py:module} abtem.slicing
```

```{autodoc2-docstring} abtem.slicing
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseSlicedAtoms <abtem.slicing.BaseSlicedAtoms>`
  - ```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms
    :parser: rst
    :summary:
    ```
* - {py:obj}`SliceIndexedAtoms <abtem.slicing.SliceIndexedAtoms>`
  - ```{autodoc2-docstring} abtem.slicing.SliceIndexedAtoms
    :parser: rst
    :summary:
    ```
* - {py:obj}`SlicedAtoms <abtem.slicing.SlicedAtoms>`
  - ```{autodoc2-docstring} abtem.slicing.SlicedAtoms
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`crystal_slice_thicknesses <abtem.slicing.crystal_slice_thicknesses>`
  - ```{autodoc2-docstring} abtem.slicing.crystal_slice_thicknesses
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_number <abtem.slicing.is_number>`
  - ```{autodoc2-docstring} abtem.slicing.is_number
    :parser: rst
    :summary:
    ```
* - {py:obj}`slice_limits <abtem.slicing.slice_limits>`
  - ```{autodoc2-docstring} abtem.slicing.slice_limits
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} BaseSlicedAtoms(...)
:canonical: abtem.slicing.BaseSlicedAtoms

Bases: {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.__init__
:parser: rst
```

````{py:property} atoms
:canonical: abtem.slicing.BaseSlicedAtoms.atoms
:type: ase.Atoms

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.atoms
:parser: rst
```

````

````{py:property} box
:canonical: abtem.slicing.BaseSlicedAtoms.box
:type: tuple[float, float, float]

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.box
:parser: rst
```

````

````{py:method} check_slice_idx(...)
:canonical: abtem.slicing.BaseSlicedAtoms.check_slice_idx

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.check_slice_idx
:parser: rst
```

````

````{py:method} generate_atoms_in_slices(...)
:canonical: abtem.slicing.BaseSlicedAtoms.generate_atoms_in_slices

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.generate_atoms_in_slices
:parser: rst
```

````

````{py:method} get_atoms_in_slices(...) -> ase.Atoms
:canonical: abtem.slicing.BaseSlicedAtoms.get_atoms_in_slices
:abstractmethod:

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.get_atoms_in_slices
:parser: rst
```

````

````{py:property} num_slices
:canonical: abtem.slicing.BaseSlicedAtoms.num_slices
:type: int

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.num_slices
:parser: rst
```

````

````{py:property} slice_limits
:canonical: abtem.slicing.BaseSlicedAtoms.slice_limits
:type: list[tuple[float, float]]

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.slice_limits
:parser: rst
```

````

````{py:property} slice_thickness
:canonical: abtem.slicing.BaseSlicedAtoms.slice_thickness
:type: tuple[float, ...]

```{autodoc2-docstring} abtem.slicing.BaseSlicedAtoms.slice_thickness
:parser: rst
```

````

`````

`````{py:class} SliceIndexedAtoms(...)
:canonical: abtem.slicing.SliceIndexedAtoms

Bases: {py:obj}`abtem.slicing.BaseSlicedAtoms`

```{autodoc2-docstring} abtem.slicing.SliceIndexedAtoms
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.slicing.SliceIndexedAtoms.__init__
:parser: rst
```

````{py:method} get_atoms_in_slices(...) -> ase.Atoms
:canonical: abtem.slicing.SliceIndexedAtoms.get_atoms_in_slices

````

`````

`````{py:class} SlicedAtoms(...)
:canonical: abtem.slicing.SlicedAtoms

Bases: {py:obj}`abtem.slicing.BaseSlicedAtoms`

```{autodoc2-docstring} abtem.slicing.SlicedAtoms
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.slicing.SlicedAtoms.__init__
:parser: rst
```

````{py:method} get_atoms_in_slices(...) -> ase.Atoms
:canonical: abtem.slicing.SlicedAtoms.get_atoms_in_slices

````

`````

````{py:function} crystal_slice_thicknesses(...) -> numpy.ndarray
:canonical: abtem.slicing.crystal_slice_thicknesses

```{autodoc2-docstring} abtem.slicing.crystal_slice_thicknesses
:parser: rst
```
````

````{py:function} is_number(...) -> typing.TypeGuard[int | float | numpy.ndarray]
:canonical: abtem.slicing.is_number

```{autodoc2-docstring} abtem.slicing.is_number
:parser: rst
```
````

````{py:function} slice_limits(...) -> list[tuple[float, float]]
:canonical: abtem.slicing.slice_limits

```{autodoc2-docstring} abtem.slicing.slice_limits
:parser: rst
```
````
