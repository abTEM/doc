# {py:mod}`abtem.atoms`

```{py:module} abtem.atoms
```

```{autodoc2-docstring} abtem.atoms
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`euler_sequence <abtem.atoms.euler_sequence>`
  - ```{autodoc2-docstring} abtem.atoms.euler_sequence
    :summary:
    ```
* - {py:obj}`plane_to_axes <abtem.atoms.plane_to_axes>`
  - ```{autodoc2-docstring} abtem.atoms.plane_to_axes
    :summary:
    ```
* - {py:obj}`is_cell_hexagonal <abtem.atoms.is_cell_hexagonal>`
  - ```{autodoc2-docstring} abtem.atoms.is_cell_hexagonal
    :summary:
    ```
* - {py:obj}`is_cell_orthogonal <abtem.atoms.is_cell_orthogonal>`
  - ```{autodoc2-docstring} abtem.atoms.is_cell_orthogonal
    :summary:
    ```
* - {py:obj}`is_cell_valid <abtem.atoms.is_cell_valid>`
  - ```{autodoc2-docstring} abtem.atoms.is_cell_valid
    :summary:
    ```
* - {py:obj}`standardize_cell <abtem.atoms.standardize_cell>`
  - ```{autodoc2-docstring} abtem.atoms.standardize_cell
    :summary:
    ```
* - {py:obj}`rotation_matrix_to_euler <abtem.atoms.rotation_matrix_to_euler>`
  - ```{autodoc2-docstring} abtem.atoms.rotation_matrix_to_euler
    :summary:
    ```
* - {py:obj}`euler_to_rotation <abtem.atoms.euler_to_rotation>`
  - ```{autodoc2-docstring} abtem.atoms.euler_to_rotation
    :summary:
    ```
* - {py:obj}`decompose_affine_transform <abtem.atoms.decompose_affine_transform>`
  - ```{autodoc2-docstring} abtem.atoms.decompose_affine_transform
    :summary:
    ```
* - {py:obj}`pretty_print_transform <abtem.atoms.pretty_print_transform>`
  - ```{autodoc2-docstring} abtem.atoms.pretty_print_transform
    :summary:
    ```
* - {py:obj}`merge_close_atoms <abtem.atoms.merge_close_atoms>`
  - ```{autodoc2-docstring} abtem.atoms.merge_close_atoms
    :summary:
    ```
* - {py:obj}`wrap_with_tolerance <abtem.atoms.wrap_with_tolerance>`
  - ```{autodoc2-docstring} abtem.atoms.wrap_with_tolerance
    :summary:
    ```
* - {py:obj}`shrink_cell <abtem.atoms.shrink_cell>`
  - ```{autodoc2-docstring} abtem.atoms.shrink_cell
    :summary:
    ```
* - {py:obj}`rotation_matrix_from_plane <abtem.atoms.rotation_matrix_from_plane>`
  - ```{autodoc2-docstring} abtem.atoms.rotation_matrix_from_plane
    :summary:
    ```
* - {py:obj}`rotate_atoms <abtem.atoms.rotate_atoms>`
  - ```{autodoc2-docstring} abtem.atoms.rotate_atoms
    :summary:
    ```
* - {py:obj}`rotate_atoms_to_plane <abtem.atoms.rotate_atoms_to_plane>`
  - ```{autodoc2-docstring} abtem.atoms.rotate_atoms_to_plane
    :summary:
    ```
* - {py:obj}`flip_atoms <abtem.atoms.flip_atoms>`
  - ```{autodoc2-docstring} abtem.atoms.flip_atoms
    :summary:
    ```
* - {py:obj}`best_orthogonal_cell <abtem.atoms.best_orthogonal_cell>`
  - ```{autodoc2-docstring} abtem.atoms.best_orthogonal_cell
    :summary:
    ```
* - {py:obj}`orthogonalize_cell <abtem.atoms.orthogonalize_cell>`
  - ```{autodoc2-docstring} abtem.atoms.orthogonalize_cell
    :summary:
    ```
* - {py:obj}`atoms_in_cell <abtem.atoms.atoms_in_cell>`
  - ```{autodoc2-docstring} abtem.atoms.atoms_in_cell
    :summary:
    ```
* - {py:obj}`cut_cell <abtem.atoms.cut_cell>`
  - ```{autodoc2-docstring} abtem.atoms.cut_cell
    :summary:
    ```
* - {py:obj}`pad_atoms <abtem.atoms.pad_atoms>`
  - ```{autodoc2-docstring} abtem.atoms.pad_atoms
    :summary:
    ```
* - {py:obj}`atom_property_dict_to_atom_property_array <abtem.atoms.atom_property_dict_to_atom_property_array>`
  - ```{autodoc2-docstring} abtem.atoms.atom_property_dict_to_atom_property_array
    :summary:
    ```
* - {py:obj}`validate_per_atom_property <abtem.atoms.validate_per_atom_property>`
  - ```{autodoc2-docstring} abtem.atoms.validate_per_atom_property
    :summary:
    ```
* - {py:obj}`validate_sigmas <abtem.atoms.validate_sigmas>`
  - ```{autodoc2-docstring} abtem.atoms.validate_sigmas
    :summary:
    ```
* - {py:obj}`sigma_to_B <abtem.atoms.sigma_to_B>`
  - ```{autodoc2-docstring} abtem.atoms.sigma_to_B
    :summary:
    ```
* - {py:obj}`B_to_sigma <abtem.atoms.B_to_sigma>`
  - ```{autodoc2-docstring} abtem.atoms.B_to_sigma
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`axis_mapping <abtem.atoms.axis_mapping>`
  - ```{autodoc2-docstring} abtem.atoms.axis_mapping
    :summary:
    ```
* - {py:obj}`AtomProperties <abtem.atoms.AtomProperties>`
  - ```{autodoc2-docstring} abtem.atoms.AtomProperties
    :summary:
    ```
````

### API

````{py:data} axis_mapping
:canonical: abtem.atoms.axis_mapping
:value: >
   None

```{autodoc2-docstring} abtem.atoms.axis_mapping
```

````

````{py:function} euler_sequence(axes: str, convention: str) -> tuple[int, int, int, int]
:canonical: abtem.atoms.euler_sequence

```{autodoc2-docstring} abtem.atoms.euler_sequence
```
````

````{py:function} plane_to_axes(plane: str) -> tuple[int, ...]
:canonical: abtem.atoms.plane_to_axes

```{autodoc2-docstring} abtem.atoms.plane_to_axes
```
````

````{py:function} is_cell_hexagonal(atoms: ase.Atoms | ase.cell.Cell) -> bool
:canonical: abtem.atoms.is_cell_hexagonal

```{autodoc2-docstring} abtem.atoms.is_cell_hexagonal
```
````

````{py:function} is_cell_orthogonal(cell: ase.Atoms | ase.cell.Cell | numpy.ndarray, tol: float = 1e-12)
:canonical: abtem.atoms.is_cell_orthogonal

```{autodoc2-docstring} abtem.atoms.is_cell_orthogonal
```
````

````{py:function} is_cell_valid(atoms: ase.Atoms, tol: float = 1e-12) -> bool
:canonical: abtem.atoms.is_cell_valid

```{autodoc2-docstring} abtem.atoms.is_cell_valid
```
````

````{py:function} standardize_cell(atoms: ase.Atoms, tol: float = 1e-12) -> ase.Atoms
:canonical: abtem.atoms.standardize_cell

```{autodoc2-docstring} abtem.atoms.standardize_cell
```
````

````{py:function} rotation_matrix_to_euler(R: numpy.ndarray, axes: str = 'xyz', convention: str = 'intrinsic', eps: float = 1e-06) -> tuple[float, float, float]
:canonical: abtem.atoms.rotation_matrix_to_euler

```{autodoc2-docstring} abtem.atoms.rotation_matrix_to_euler
```
````

````{py:function} euler_to_rotation(ai: float, aj: float, ak: float, axes: str = 'xyz', convention: str = 'intrinsic') -> numpy.ndarray
:canonical: abtem.atoms.euler_to_rotation

```{autodoc2-docstring} abtem.atoms.euler_to_rotation
```
````

````{py:function} decompose_affine_transform(affine_transform: numpy.ndarray) -> tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray]
:canonical: abtem.atoms.decompose_affine_transform

```{autodoc2-docstring} abtem.atoms.decompose_affine_transform
```
````

````{py:function} pretty_print_transform(decomposed: tuple[numpy.ndarray, numpy.ndarray, numpy.ndarray])
:canonical: abtem.atoms.pretty_print_transform

```{autodoc2-docstring} abtem.atoms.pretty_print_transform
```
````

````{py:function} merge_close_atoms(atoms: ase.Atoms, tol: float = 1e-07) -> ase.Atoms
:canonical: abtem.atoms.merge_close_atoms

```{autodoc2-docstring} abtem.atoms.merge_close_atoms
```
````

````{py:function} wrap_with_tolerance(atoms: ase.Atoms, tol: float = 1e-06) -> ase.Atoms
:canonical: abtem.atoms.wrap_with_tolerance

```{autodoc2-docstring} abtem.atoms.wrap_with_tolerance
```
````

````{py:function} shrink_cell(atoms: ase.Atoms, repetitions: tuple[int, int] = (2, 3), tol: float = 1e-06) -> ase.Atoms
:canonical: abtem.atoms.shrink_cell

```{autodoc2-docstring} abtem.atoms.shrink_cell
```
````

````{py:function} rotation_matrix_from_plane(plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy') -> numpy.ndarray
:canonical: abtem.atoms.rotation_matrix_from_plane

```{autodoc2-docstring} abtem.atoms.rotation_matrix_from_plane
```
````

````{py:function} rotate_atoms(atoms: ase.Atoms, axes: str = 'zxz', angles: float | tuple[float, float, float] = (0.0, 0.0, 0.0), convention: str = 'intrinsic') -> ase.Atoms
:canonical: abtem.atoms.rotate_atoms

```{autodoc2-docstring} abtem.atoms.rotate_atoms
```
````

````{py:function} rotate_atoms_to_plane(atoms: ase.Atoms, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy') -> ase.Atoms
:canonical: abtem.atoms.rotate_atoms_to_plane

```{autodoc2-docstring} abtem.atoms.rotate_atoms_to_plane
```
````

````{py:function} flip_atoms(atoms: ase.Atoms, axis: int = 2) -> ase.Atoms
:canonical: abtem.atoms.flip_atoms

```{autodoc2-docstring} abtem.atoms.flip_atoms
```
````

````{py:function} best_orthogonal_cell(cell: numpy.ndarray, max_repetitions: int | tuple[int, int, int] = 5, eps: float = 1e-12) -> numpy.ndarray
:canonical: abtem.atoms.best_orthogonal_cell

```{autodoc2-docstring} abtem.atoms.best_orthogonal_cell
```
````

````{py:function} orthogonalize_cell(atoms: ase.Atoms, max_repetitions: int = 5, return_transform: bool = False, return_transform_matrix: bool = False, allow_transform: bool = True, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy', origin: tuple[float, float, float] = (0.0, 0.0, 0.0), box: tuple[float, float, float] | None = None, tolerance: float = 0.01)
:canonical: abtem.atoms.orthogonalize_cell

```{autodoc2-docstring} abtem.atoms.orthogonalize_cell
```
````

````{py:function} atoms_in_cell(atoms: ase.Atoms, margin: typing.SupportsFloat | tuple[float, float, float] = 0.0) -> ase.Atoms
:canonical: abtem.atoms.atoms_in_cell

```{autodoc2-docstring} abtem.atoms.atoms_in_cell
```
````

````{py:function} cut_cell(atoms: ase.Atoms, cell: tuple[float, float, float] | None = None, plane: str | tuple[tuple[float, float, float], tuple[float, float, float]] = 'xy', origin: tuple[float, float, float] = (0.0, 0.0, 0.0), margin: float | tuple[float, float, float] = 0.0) -> ase.Atoms
:canonical: abtem.atoms.cut_cell

```{autodoc2-docstring} abtem.atoms.cut_cell
```
````

````{py:function} pad_atoms(atoms: ase.Atoms, margins: typing.SupportsFloat | tuple[float, float, float], directions: str = 'xyz') -> ase.Atoms
:canonical: abtem.atoms.pad_atoms

```{autodoc2-docstring} abtem.atoms.pad_atoms
```
````

````{py:data} AtomProperties
:canonical: abtem.atoms.AtomProperties
:value: >
   None

```{autodoc2-docstring} abtem.atoms.AtomProperties
```

````

````{py:function} atom_property_dict_to_atom_property_array(atoms: ase.Atoms, props: dict[str, numpy.ndarray]) -> numpy.ndarray
:canonical: abtem.atoms.atom_property_dict_to_atom_property_array

```{autodoc2-docstring} abtem.atoms.atom_property_dict_to_atom_property_array
```
````

````{py:function} validate_per_atom_property(atoms: ase.Atoms, props: abtem.atoms.AtomProperties, return_array: bool = False) -> numpy.ndarray | dict[str, numpy.ndarray]
:canonical: abtem.atoms.validate_per_atom_property

```{autodoc2-docstring} abtem.atoms.validate_per_atom_property
```
````

````{py:function} validate_sigmas(atoms: ase.Atoms, sigmas: abtem.atoms.AtomProperties, return_array: bool = False) -> tuple[numpy.ndarray | dict[str, numpy.ndarray], bool]
:canonical: abtem.atoms.validate_sigmas

```{autodoc2-docstring} abtem.atoms.validate_sigmas
```
````

````{py:function} sigma_to_B(sigma: float | numpy.ndarray) -> float | numpy.ndarray
:canonical: abtem.atoms.sigma_to_B

```{autodoc2-docstring} abtem.atoms.sigma_to_B
```
````

````{py:function} B_to_sigma(B: float | numpy.ndarray) -> float | numpy.ndarray
:canonical: abtem.atoms.B_to_sigma

```{autodoc2-docstring} abtem.atoms.B_to_sigma
```
````
