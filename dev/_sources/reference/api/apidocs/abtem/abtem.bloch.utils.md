# {py:mod}`abtem.bloch.utils`

```{py:module} abtem.bloch.utils
```

```{autodoc2-docstring} abtem.bloch.utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`all_positions_have_relative_periodic_pair <abtem.bloch.utils.all_positions_have_relative_periodic_pair>`
  - ```{autodoc2-docstring} abtem.bloch.utils.all_positions_have_relative_periodic_pair
    :summary:
    ```
* - {py:obj}`are_vectors_orthogonal <abtem.bloch.utils.are_vectors_orthogonal>`
  - ```{autodoc2-docstring} abtem.bloch.utils.are_vectors_orthogonal
    :summary:
    ```
* - {py:obj}`auto_detect_centering <abtem.bloch.utils.auto_detect_centering>`
  - ```{autodoc2-docstring} abtem.bloch.utils.auto_detect_centering
    :summary:
    ```
* - {py:obj}`calculate_g_vec <abtem.bloch.utils.calculate_g_vec>`
  - ```{autodoc2-docstring} abtem.bloch.utils.calculate_g_vec
    :summary:
    ```
* - {py:obj}`calculate_g_vec_length <abtem.bloch.utils.calculate_g_vec_length>`
  - ```{autodoc2-docstring} abtem.bloch.utils.calculate_g_vec_length
    :summary:
    ```
* - {py:obj}`cell_bounds <abtem.bloch.utils.cell_bounds>`
  - ```{autodoc2-docstring} abtem.bloch.utils.cell_bounds
    :summary:
    ```
* - {py:obj}`check_orthogonality <abtem.bloch.utils.check_orthogonality>`
  - ```{autodoc2-docstring} abtem.bloch.utils.check_orthogonality
    :summary:
    ```
* - {py:obj}`excitation_errors <abtem.bloch.utils.excitation_errors>`
  - ```{autodoc2-docstring} abtem.bloch.utils.excitation_errors
    :summary:
    ```
* - {py:obj}`fast_filter_excitation_errors <abtem.bloch.utils.fast_filter_excitation_errors>`
  - ```{autodoc2-docstring} abtem.bloch.utils.fast_filter_excitation_errors
    :summary:
    ```
* - {py:obj}`filter_reciprocal_space_vectors <abtem.bloch.utils.filter_reciprocal_space_vectors>`
  - ```{autodoc2-docstring} abtem.bloch.utils.filter_reciprocal_space_vectors
    :summary:
    ```
* - {py:obj}`generate_linear_combinations <abtem.bloch.utils.generate_linear_combinations>`
  - ```{autodoc2-docstring} abtem.bloch.utils.generate_linear_combinations
    :summary:
    ```
* - {py:obj}`get_reflection_condition <abtem.bloch.utils.get_reflection_condition>`
  - ```{autodoc2-docstring} abtem.bloch.utils.get_reflection_condition
    :summary:
    ```
* - {py:obj}`get_shortest_g_vec_length <abtem.bloch.utils.get_shortest_g_vec_length>`
  - ```{autodoc2-docstring} abtem.bloch.utils.get_shortest_g_vec_length
    :summary:
    ```
* - {py:obj}`hkl_strings_to_array <abtem.bloch.utils.hkl_strings_to_array>`
  - ```{autodoc2-docstring} abtem.bloch.utils.hkl_strings_to_array
    :summary:
    ```
* - {py:obj}`make_hkl_grid <abtem.bloch.utils.make_hkl_grid>`
  - ```{autodoc2-docstring} abtem.bloch.utils.make_hkl_grid
    :summary:
    ```
* - {py:obj}`ravel_hkl <abtem.bloch.utils.ravel_hkl>`
  - ```{autodoc2-docstring} abtem.bloch.utils.ravel_hkl
    :summary:
    ```
* - {py:obj}`reciprocal_cell <abtem.bloch.utils.reciprocal_cell>`
  - ```{autodoc2-docstring} abtem.bloch.utils.reciprocal_cell
    :summary:
    ```
* - {py:obj}`reciprocal_space_gpts <abtem.bloch.utils.reciprocal_space_gpts>`
  - ```{autodoc2-docstring} abtem.bloch.utils.reciprocal_space_gpts
    :summary:
    ```
* - {py:obj}`relative_positions_for_centering <abtem.bloch.utils.relative_positions_for_centering>`
  - ```{autodoc2-docstring} abtem.bloch.utils.relative_positions_for_centering
    :summary:
    ```
* - {py:obj}`retrieve_structure_factor_values <abtem.bloch.utils.retrieve_structure_factor_values>`
  - ```{autodoc2-docstring} abtem.bloch.utils.retrieve_structure_factor_values
    :summary:
    ```
* - {py:obj}`wrapped_is_close <abtem.bloch.utils.wrapped_is_close>`
  - ```{autodoc2-docstring} abtem.bloch.utils.wrapped_is_close
    :summary:
    ```
````

### API

````{py:function} all_positions_have_relative_periodic_pair(positions: numpy.ndarray, relative_positions: numpy.ndarray) -> bool
:canonical: abtem.bloch.utils.all_positions_have_relative_periodic_pair

```{autodoc2-docstring} abtem.bloch.utils.all_positions_have_relative_periodic_pair
```
````

````{py:function} are_vectors_orthogonal(v1: numpy.ndarray, v2: numpy.ndarray, tol: float = 1e-09) -> bool
:canonical: abtem.bloch.utils.are_vectors_orthogonal

```{autodoc2-docstring} abtem.bloch.utils.are_vectors_orthogonal
```
````

````{py:function} auto_detect_centering(atoms: ase.Atoms, centerings_to_check: typing.Optional[set] = None) -> str
:canonical: abtem.bloch.utils.auto_detect_centering

```{autodoc2-docstring} abtem.bloch.utils.auto_detect_centering
```
````

````{py:function} calculate_g_vec(hkl: numpy.ndarray, cell: numpy.ndarray | ase.cell.Cell) -> numpy.ndarray
:canonical: abtem.bloch.utils.calculate_g_vec

```{autodoc2-docstring} abtem.bloch.utils.calculate_g_vec
```
````

````{py:function} calculate_g_vec_length(hkl: numpy.ndarray, cell: numpy.ndarray | ase.cell.Cell) -> numpy.ndarray
:canonical: abtem.bloch.utils.calculate_g_vec_length

```{autodoc2-docstring} abtem.bloch.utils.calculate_g_vec_length
```
````

````{py:function} cell_bounds(cell: numpy.ndarray | ase.cell.Cell) -> numpy.ndarray
:canonical: abtem.bloch.utils.cell_bounds

```{autodoc2-docstring} abtem.bloch.utils.cell_bounds
```
````

````{py:function} check_orthogonality(vectors: numpy.ndarray, tol: float = 1e-09) -> bool
:canonical: abtem.bloch.utils.check_orthogonality

```{autodoc2-docstring} abtem.bloch.utils.check_orthogonality
```
````

````{py:function} excitation_errors(g: numpy.ndarray, energy: float, use_wave_eq: bool = False) -> numpy.ndarray
:canonical: abtem.bloch.utils.excitation_errors

```{autodoc2-docstring} abtem.bloch.utils.excitation_errors
```
````

````{py:function} fast_filter_excitation_errors(mask: numpy.ndarray, g: numpy.ndarray, orientation_matrices: numpy.ndarray, wavelength: float, sg_max: float) -> None
:canonical: abtem.bloch.utils.fast_filter_excitation_errors

```{autodoc2-docstring} abtem.bloch.utils.fast_filter_excitation_errors
```
````

````{py:function} filter_reciprocal_space_vectors(hkl: numpy.ndarray, cell: ase.cell.Cell, energy: float, sg_max: float, g_max: float, centering: str = 'P', orientation_matrices: typing.Optional[numpy.ndarray] = None) -> numpy.ndarray
:canonical: abtem.bloch.utils.filter_reciprocal_space_vectors

```{autodoc2-docstring} abtem.bloch.utils.filter_reciprocal_space_vectors
```
````

````{py:function} generate_linear_combinations(vectors: numpy.ndarray, coefficients: typing.Sequence[int], exclude_zero: bool = False) -> numpy.ndarray
:canonical: abtem.bloch.utils.generate_linear_combinations

```{autodoc2-docstring} abtem.bloch.utils.generate_linear_combinations
```
````

````{py:function} get_reflection_condition(hkl: numpy.ndarray, centering: str) -> numpy.ndarray
:canonical: abtem.bloch.utils.get_reflection_condition

```{autodoc2-docstring} abtem.bloch.utils.get_reflection_condition
```
````

````{py:function} get_shortest_g_vec_length(cell: ase.cell.Cell) -> float
:canonical: abtem.bloch.utils.get_shortest_g_vec_length

```{autodoc2-docstring} abtem.bloch.utils.get_shortest_g_vec_length
```
````

````{py:function} hkl_strings_to_array(hkl: list[str]) -> numpy.ndarray
:canonical: abtem.bloch.utils.hkl_strings_to_array

```{autodoc2-docstring} abtem.bloch.utils.hkl_strings_to_array
```
````

````{py:function} make_hkl_grid(cell: numpy.ndarray | ase.cell.Cell, g_max: float, axes: tuple[int, ...] = (0, 1, 2)) -> numpy.ndarray
:canonical: abtem.bloch.utils.make_hkl_grid

```{autodoc2-docstring} abtem.bloch.utils.make_hkl_grid
```
````

````{py:function} ravel_hkl(hkl: numpy.ndarray, gpts: tuple[int, int, int]) -> numpy.ndarray
:canonical: abtem.bloch.utils.ravel_hkl

```{autodoc2-docstring} abtem.bloch.utils.ravel_hkl
```
````

````{py:function} reciprocal_cell(cell: numpy.ndarray | ase.cell.Cell) -> numpy.ndarray
:canonical: abtem.bloch.utils.reciprocal_cell

```{autodoc2-docstring} abtem.bloch.utils.reciprocal_cell
```
````

````{py:function} reciprocal_space_gpts(cell: numpy.ndarray | ase.cell.Cell, g_max: float) -> tuple[int, int, int]
:canonical: abtem.bloch.utils.reciprocal_space_gpts

```{autodoc2-docstring} abtem.bloch.utils.reciprocal_space_gpts
```
````

````{py:function} relative_positions_for_centering() -> dict[str, numpy.ndarray]
:canonical: abtem.bloch.utils.relative_positions_for_centering

```{autodoc2-docstring} abtem.bloch.utils.relative_positions_for_centering
```
````

````{py:function} retrieve_structure_factor_values(array: numpy.ndarray, hkl_source: numpy.ndarray, hkl_destination: numpy.ndarray, gpts: tuple[int, int, int]) -> numpy.ndarray
:canonical: abtem.bloch.utils.retrieve_structure_factor_values

```{autodoc2-docstring} abtem.bloch.utils.retrieve_structure_factor_values
```
````

````{py:function} wrapped_is_close(a, b)
:canonical: abtem.bloch.utils.wrapped_is_close

```{autodoc2-docstring} abtem.bloch.utils.wrapped_is_close
```
````
