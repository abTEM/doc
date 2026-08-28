# {py:mod}`abtem.bloch.indexing`

```{py:module} abtem.bloch.indexing
```

```{autodoc2-docstring} abtem.bloch.indexing
:parser: rst
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`antialiased_disk <abtem.bloch.indexing.antialiased_disk>`
  - ```{autodoc2-docstring} abtem.bloch.indexing.antialiased_disk
    :parser: rst
    :summary:
    ```
* - {py:obj}`create_ellipse <abtem.bloch.indexing.create_ellipse>`
  - ```{autodoc2-docstring} abtem.bloch.indexing.create_ellipse
    :parser: rst
    :summary:
    ```
* - {py:obj}`estimate_necessary_excitation_error <abtem.bloch.indexing.estimate_necessary_excitation_error>`
  - ```{autodoc2-docstring} abtem.bloch.indexing.estimate_necessary_excitation_error
    :parser: rst
    :summary:
    ```
* - {py:obj}`index_diffraction_spots <abtem.bloch.indexing.index_diffraction_spots>`
  - ```{autodoc2-docstring} abtem.bloch.indexing.index_diffraction_spots
    :parser: rst
    :summary:
    ```
* - {py:obj}`integrate_ellipse_around_pixels <abtem.bloch.indexing.integrate_ellipse_around_pixels>`
  - ```{autodoc2-docstring} abtem.bloch.indexing.integrate_ellipse_around_pixels
    :parser: rst
    :summary:
    ```
* - {py:obj}`miller_to_miller_bravais <abtem.bloch.indexing.miller_to_miller_bravais>`
  - ```{autodoc2-docstring} abtem.bloch.indexing.miller_to_miller_bravais
    :parser: rst
    :summary:
    ```
* - {py:obj}`overlapping_spots_mask <abtem.bloch.indexing.overlapping_spots_mask>`
  - ```{autodoc2-docstring} abtem.bloch.indexing.overlapping_spots_mask
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_cell <abtem.bloch.indexing.validate_cell>`
  - ```{autodoc2-docstring} abtem.bloch.indexing.validate_cell
    :parser: rst
    :summary:
    ```
````

### API

````{py:function} antialiased_disk(r: float, sampling: tuple[float, float]) -> numpy.ndarray
:canonical: abtem.bloch.indexing.antialiased_disk

```{autodoc2-docstring} abtem.bloch.indexing.antialiased_disk
:parser: rst
```
````

````{py:function} create_ellipse(a: int, b: int) -> numpy.ndarray
:canonical: abtem.bloch.indexing.create_ellipse

```{autodoc2-docstring} abtem.bloch.indexing.create_ellipse
:parser: rst
```
````

````{py:function} estimate_necessary_excitation_error(energy: float, k_max: float) -> float
:canonical: abtem.bloch.indexing.estimate_necessary_excitation_error

```{autodoc2-docstring} abtem.bloch.indexing.estimate_necessary_excitation_error
:parser: rst
```
````

````{py:function} index_diffraction_spots(array: numpy.ndarray, hkl: numpy.ndarray, sampling: tuple[float, float], cell: ase.cell.Cell | numpy.ndarray, energy: float, orientation_matrices: typing.Optional[numpy.ndarray] = None, radius: typing.Optional[float] = None) -> numpy.ndarray
:canonical: abtem.bloch.indexing.index_diffraction_spots

```{autodoc2-docstring} abtem.bloch.indexing.index_diffraction_spots
:parser: rst
```
````

````{py:function} integrate_ellipse_around_pixels(array: numpy.ndarray, nm: numpy.ndarray, r: float, sampling: tuple[float, float], priority: typing.Optional[numpy.ndarray] = None) -> numpy.ndarray
:canonical: abtem.bloch.indexing.integrate_ellipse_around_pixels

```{autodoc2-docstring} abtem.bloch.indexing.integrate_ellipse_around_pixels
:parser: rst
```
````

````{py:function} miller_to_miller_bravais(hkl: tuple[int, int, int]) -> tuple[int, int, int, int]
:canonical: abtem.bloch.indexing.miller_to_miller_bravais

```{autodoc2-docstring} abtem.bloch.indexing.miller_to_miller_bravais
:parser: rst
```
````

````{py:function} overlapping_spots_mask(nm: numpy.ndarray, sg: numpy.ndarray) -> numpy.ndarray
:canonical: abtem.bloch.indexing.overlapping_spots_mask

```{autodoc2-docstring} abtem.bloch.indexing.overlapping_spots_mask
:parser: rst
```
````

````{py:function} validate_cell(cell: ase.Atoms | ase.cell.Cell | numpy.ndarray | float | tuple[float, float, float]) -> ase.cell.Cell
:canonical: abtem.bloch.indexing.validate_cell

```{autodoc2-docstring} abtem.bloch.indexing.validate_cell
:parser: rst
```
````
