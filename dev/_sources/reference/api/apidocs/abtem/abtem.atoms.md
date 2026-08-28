# {py:mod}`abtem.atoms`

```{py:module} abtem.atoms
```

```{autodoc2-docstring} abtem.atoms
:parser: rst
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`B_to_sigma <abtem.atoms.B_to_sigma>`
  - ```{autodoc2-docstring} abtem.atoms.B_to_sigma
    :parser: rst
    :summary:
    ```
* - {py:obj}`atom_property_dict_to_atom_property_array <abtem.atoms.atom_property_dict_to_atom_property_array>`
  - ```{autodoc2-docstring} abtem.atoms.atom_property_dict_to_atom_property_array
    :parser: rst
    :summary:
    ```
* - {py:obj}`atoms_in_cell <abtem.atoms.atoms_in_cell>`
  - ```{autodoc2-docstring} abtem.atoms.atoms_in_cell
    :parser: rst
    :summary:
    ```
* - {py:obj}`best_orthogonal_cell <abtem.atoms.best_orthogonal_cell>`
  - ```{autodoc2-docstring} abtem.atoms.best_orthogonal_cell
    :parser: rst
    :summary:
    ```
* - {py:obj}`cut_cell <abtem.atoms.cut_cell>`
  - ```{autodoc2-docstring} abtem.atoms.cut_cell
    :parser: rst
    :summary:
    ```
* - {py:obj}`decompose_affine_transform <abtem.atoms.decompose_affine_transform>`
  - ```{autodoc2-docstring} abtem.atoms.decompose_affine_transform
    :parser: rst
    :summary:
    ```
* - {py:obj}`euler_sequence <abtem.atoms.euler_sequence>`
  - ```{autodoc2-docstring} abtem.atoms.euler_sequence
    :parser: rst
    :summary:
    ```
* - {py:obj}`euler_to_rotation <abtem.atoms.euler_to_rotation>`
  - ```{autodoc2-docstring} abtem.atoms.euler_to_rotation
    :parser: rst
    :summary:
    ```
* - {py:obj}`flip_atoms <abtem.atoms.flip_atoms>`
  - ```{autodoc2-docstring} abtem.atoms.flip_atoms
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_cell_hexagonal <abtem.atoms.is_cell_hexagonal>`
  - ```{autodoc2-docstring} abtem.atoms.is_cell_hexagonal
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_cell_orthogonal <abtem.atoms.is_cell_orthogonal>`
  - ```{autodoc2-docstring} abtem.atoms.is_cell_orthogonal
    :parser: rst
    :summary:
    ```
* - {py:obj}`is_cell_valid <abtem.atoms.is_cell_valid>`
  - ```{autodoc2-docstring} abtem.atoms.is_cell_valid
    :parser: rst
    :summary:
    ```
* - {py:obj}`merge_close_atoms <abtem.atoms.merge_close_atoms>`
  - ```{autodoc2-docstring} abtem.atoms.merge_close_atoms
    :parser: rst
    :summary:
    ```
* - {py:obj}`orthogonalize_cell <abtem.atoms.orthogonalize_cell>`
  - ```{autodoc2-docstring} abtem.atoms.orthogonalize_cell
    :parser: rst
    :summary:
    ```
* - {py:obj}`pad_atoms <abtem.atoms.pad_atoms>`
  - ```{autodoc2-docstring} abtem.atoms.pad_atoms
    :parser: rst
    :summary:
    ```
* - {py:obj}`plane_to_axes <abtem.atoms.plane_to_axes>`
  - ```{autodoc2-docstring} abtem.atoms.plane_to_axes
    :parser: rst
    :summary:
    ```
* - {py:obj}`pretty_print_transform <abtem.atoms.pretty_print_transform>`
  - ```{autodoc2-docstring} abtem.atoms.pretty_print_transform
    :parser: rst
    :summary:
    ```
* - {py:obj}`rotate_atoms <abtem.atoms.rotate_atoms>`
  - ```{autodoc2-docstring} abtem.atoms.rotate_atoms
    :parser: rst
    :summary:
    ```
* - {py:obj}`rotate_atoms_to_plane <abtem.atoms.rotate_atoms_to_plane>`
  - ```{autodoc2-docstring} abtem.atoms.rotate_atoms_to_plane
    :parser: rst
    :summary:
    ```
* - {py:obj}`rotation_matrix_from_plane <abtem.atoms.rotation_matrix_from_plane>`
  - ```{autodoc2-docstring} abtem.atoms.rotation_matrix_from_plane
    :parser: rst
    :summary:
    ```
* - {py:obj}`rotation_matrix_to_euler <abtem.atoms.rotation_matrix_to_euler>`
  - ```{autodoc2-docstring} abtem.atoms.rotation_matrix_to_euler
    :parser: rst
    :summary:
    ```
* - {py:obj}`shrink_cell <abtem.atoms.shrink_cell>`
  - ```{autodoc2-docstring} abtem.atoms.shrink_cell
    :parser: rst
    :summary:
    ```
* - {py:obj}`sigma_to_B <abtem.atoms.sigma_to_B>`
  - ```{autodoc2-docstring} abtem.atoms.sigma_to_B
    :parser: rst
    :summary:
    ```
* - {py:obj}`standardize_cell <abtem.atoms.standardize_cell>`
  - ```{autodoc2-docstring} abtem.atoms.standardize_cell
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_per_atom_property <abtem.atoms.validate_per_atom_property>`
  - ```{autodoc2-docstring} abtem.atoms.validate_per_atom_property
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_sigmas <abtem.atoms.validate_sigmas>`
  - ```{autodoc2-docstring} abtem.atoms.validate_sigmas
    :parser: rst
    :summary:
    ```
* - {py:obj}`wrap_with_tolerance <abtem.atoms.wrap_with_tolerance>`
  - ```{autodoc2-docstring} abtem.atoms.wrap_with_tolerance
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AtomProperties <abtem.atoms.AtomProperties>`
  - ```{autodoc2-docstring} abtem.atoms.AtomProperties
    :parser: rst
    :summary:
    ```
* - {py:obj}`axis_mapping <abtem.atoms.axis_mapping>`
  - ```{autodoc2-docstring} abtem.atoms.axis_mapping
    :parser: rst
    :summary:
    ```
````

### API

````{py:data} AtomProperties
:canonical: abtem.atoms.AtomProperties
:value: >
   None

```{autodoc2-docstring} abtem.atoms.AtomProperties
:parser: rst
```

````

````{py:function} B_to_sigma(B: float | numpy.ndarray) -> float | numpy.ndarray
:canonical: abtem.atoms.B_to_sigma

```{autodoc2-docstring} abtem.atoms.B_to_sigma
:parser: rst
```
````

````{py:function} atom_property_dict_to_atom_property_array(atoms: ase.Atoms, props: dict[str, numpy.ndarray]) -> numpy.ndarray
:canonical: abtem.atoms.atom_property_dict_to_atom_property_array

```{autodoc2-docstring} abtem.atoms.atom_property_dict_to_atom_property_array
:parser: rst
```
````

````{py:function} atoms_in_cell(atoms: ase.Atoms, margin: typing.SupportsFloat | tuple[float, float, float] = 0.0) -> ase.Atoms
:canonical: abtem.atoms.atoms_in_cell

```{autodoc2-docstring} abtem.atoms.atoms_in_cell
:parser: rst
```
````

````{py:data} axis_mapping
:canonical: abtem.atoms.axis_mapping
:value: >
   None

```{autodoc2-docstring} abtem.atoms.axis_mapping
:parser: rst
```

````

````{py:function} best_orthogonal_cell(cell: numpy.ndarray, max_repetitions: int | tuple[int, int, int] = 5, eps: float = 1e-12) -> numpy.ndarray
:canonical: abtem.atoms.best_orthogonal_cell

```{autodoc2-docstring} abtem.atoms.best_orthogonal_cell
:parser: rst
```
````

````{py:function} cut_cell(atoms: ase.Atoms, cell: tuple[float, float, float] | None = None, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy', origin: tuple[float, float, float] = (0.0, 0.0, 0.0), margin: float | tuple[float, float, float] = 0.0) -> ase.Atoms
:canonical: abtem.atoms.cut_cell

```{autodoc2-docstring} abtem.atoms.cut_cell
:parser: rst
```
````

````{py:function} decompose_affine_transform(affine_transform: numpy.ndarray) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]
:canonical: abtem.atoms.decompose_affine_transform

```{autodoc2-docstring} abtem.atoms.decompose_affine_transform
:parser: rst
```
````

````{py:function} euler_sequence(axes: str, convention: str) -> tuple[int, int, int, int]
:canonical: abtem.atoms.euler_sequence

```{autodoc2-docstring} abtem.atoms.euler_sequence
:parser: rst
```
````

````{py:function} euler_to_rotation(ai: float, aj: float, ak: float, axes: str = 'xyz', convention: str = 'intrinsic') -> numpy.ndarray
:canonical: abtem.atoms.euler_to_rotation

```{autodoc2-docstring} abtem.atoms.euler_to_rotation
:parser: rst
```
````

````{py:function} flip_atoms(atoms: ase.Atoms, axis: int = 2) -> ase.Atoms
:canonical: abtem.atoms.flip_atoms

```{autodoc2-docstring} abtem.atoms.flip_atoms
:parser: rst
```
````

````{py:function} is_cell_hexagonal(atoms: ase.Atoms | ase.cell.Cell) -> bool
:canonical: abtem.atoms.is_cell_hexagonal

```{autodoc2-docstring} abtem.atoms.is_cell_hexagonal
:parser: rst
```
````

````{py:function} is_cell_orthogonal(cell: ase.Atoms | ase.cell.Cell | numpy.ndarray, tol: float = 1e-12)
:canonical: abtem.atoms.is_cell_orthogonal

```{autodoc2-docstring} abtem.atoms.is_cell_orthogonal
:parser: rst
```
````

````{py:function} is_cell_valid(atoms: ase.Atoms, tol: float = 1e-12) -> bool
:canonical: abtem.atoms.is_cell_valid

```{autodoc2-docstring} abtem.atoms.is_cell_valid
:parser: rst
```
````

````{py:function} merge_close_atoms(atoms: ase.Atoms, tol: float = 1e-07) -> ase.Atoms
:canonical: abtem.atoms.merge_close_atoms

```{autodoc2-docstring} abtem.atoms.merge_close_atoms
:parser: rst
```
````

````{py:function} orthogonalize_cell(atoms: ase.Atoms, max_repetitions: int = 5, return_transform: bool = False, return_transform_matrix: bool = False, allow_transform: bool = True, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy', origin: tuple[float, float, float] = (0.0, 0.0, 0.0), box: tuple[float, float, float] | None = None, tolerance: float = 0.01)
:canonical: abtem.atoms.orthogonalize_cell

```{autodoc2-docstring} abtem.atoms.orthogonalize_cell
:parser: rst
```
````

````{py:function} pad_atoms(atoms: ase.Atoms, margins: typing.SupportsFloat | tuple[float, float, float], directions: str = 'xyz') -> ase.Atoms
:canonical: abtem.atoms.pad_atoms

```{autodoc2-docstring} abtem.atoms.pad_atoms
:parser: rst
```
````

````{py:function} plane_to_axes(plane: str) -> tuple[int, ...]
:canonical: abtem.atoms.plane_to_axes

```{autodoc2-docstring} abtem.atoms.plane_to_axes
:parser: rst
```
````

````{py:function} pretty_print_transform(decomposed: tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray])
:canonical: abtem.atoms.pretty_print_transform

```{autodoc2-docstring} abtem.atoms.pretty_print_transform
:parser: rst
```
````

````{py:function} rotate_atoms(atoms: ase.Atoms, axes: str = 'zxz', angles: float | tuple[float, float, float] = (0.0, 0.0, 0.0), convention: str = 'intrinsic') -> ase.Atoms
:canonical: abtem.atoms.rotate_atoms

```{autodoc2-docstring} abtem.atoms.rotate_atoms
:parser: rst
```
````

````{py:function} rotate_atoms_to_plane(atoms: ase.Atoms, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy') -> ase.Atoms
:canonical: abtem.atoms.rotate_atoms_to_plane

```{autodoc2-docstring} abtem.atoms.rotate_atoms_to_plane
:parser: rst
```
````

````{py:function} rotation_matrix_from_plane(plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy') -> numpy.ndarray
:canonical: abtem.atoms.rotation_matrix_from_plane

```{autodoc2-docstring} abtem.atoms.rotation_matrix_from_plane
:parser: rst
```
````

````{py:function} rotation_matrix_to_euler(R: numpy.ndarray, axes: str = 'xyz', convention: str = 'intrinsic', eps: float = 1e-06) -> tuple[float, float, float]
:canonical: abtem.atoms.rotation_matrix_to_euler

```{autodoc2-docstring} abtem.atoms.rotation_matrix_to_euler
:parser: rst
```
````

````{py:function} shrink_cell(atoms: ase.Atoms, repetitions: tuple[int, int] = (2, 3), tol: float = 1e-06) -> ase.Atoms
:canonical: abtem.atoms.shrink_cell

```{autodoc2-docstring} abtem.atoms.shrink_cell
:parser: rst
```
````

````{py:function} sigma_to_B(sigma: float | numpy.ndarray) -> float | numpy.ndarray
:canonical: abtem.atoms.sigma_to_B

```{autodoc2-docstring} abtem.atoms.sigma_to_B
:parser: rst
```
````

````{py:function} standardize_cell(atoms: ase.Atoms, tol: float = 1e-12) -> ase.Atoms
:canonical: abtem.atoms.standardize_cell

```{autodoc2-docstring} abtem.atoms.standardize_cell
:parser: rst
```
````

````{py:function} validate_per_atom_property(atoms: ase.Atoms, props: abtem.atoms.AtomProperties, return_array: bool = False) -> numpy.ndarray | dict[str, numpy.ndarray]
:canonical: abtem.atoms.validate_per_atom_property

```{autodoc2-docstring} abtem.atoms.validate_per_atom_property
:parser: rst
```
````

````{py:function} validate_sigmas(atoms: ase.Atoms, sigmas: abtem.atoms.AtomProperties, return_array: bool = False) -> tuple[numpy.ndarray | dict[str, numpy.ndarray], bool]
:canonical: abtem.atoms.validate_sigmas

```{autodoc2-docstring} abtem.atoms.validate_sigmas
:parser: rst
```
````

````{py:function} wrap_with_tolerance(atoms: ase.Atoms, tol: float = 1e-06) -> ase.Atoms
:canonical: abtem.atoms.wrap_with_tolerance

```{autodoc2-docstring} abtem.atoms.wrap_with_tolerance
:parser: rst
```
````
