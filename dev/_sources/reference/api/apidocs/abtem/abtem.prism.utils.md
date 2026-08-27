# {py:mod}`abtem.prism.utils`

```{py:module} abtem.prism.utils
```

```{autodoc2-docstring} abtem.prism.utils
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`batch_crop_2d <abtem.prism.utils.batch_crop_2d>`
  - ```{autodoc2-docstring} abtem.prism.utils.batch_crop_2d
    :summary:
    ```
* - {py:obj}`minimum_crop <abtem.prism.utils.minimum_crop>`
  - ```{autodoc2-docstring} abtem.prism.utils.minimum_crop
    :summary:
    ```
* - {py:obj}`plane_waves <abtem.prism.utils.plane_waves>`
  - ```{autodoc2-docstring} abtem.prism.utils.plane_waves
    :summary:
    ```
* - {py:obj}`prism_coefficients <abtem.prism.utils.prism_coefficients>`
  - ```{autodoc2-docstring} abtem.prism.utils.prism_coefficients
    :summary:
    ```
* - {py:obj}`prism_wave_vectors <abtem.prism.utils.prism_wave_vectors>`
  - ```{autodoc2-docstring} abtem.prism.utils.prism_wave_vectors
    :summary:
    ```
* - {py:obj}`wrapped_crop_2d <abtem.prism.utils.wrapped_crop_2d>`
  - ```{autodoc2-docstring} abtem.prism.utils.wrapped_crop_2d
    :summary:
    ```
* - {py:obj}`wrapped_slices <abtem.prism.utils.wrapped_slices>`
  - ```{autodoc2-docstring} abtem.prism.utils.wrapped_slices
    :summary:
    ```
````

### API

````{py:function} batch_crop_2d(array: numpy.ndarray, corners: numpy.ndarray, new_shape: typing.Tuple[int, int])
:canonical: abtem.prism.utils.batch_crop_2d

```{autodoc2-docstring} abtem.prism.utils.batch_crop_2d
```
````

````{py:function} minimum_crop(positions: numpy.ndarray, shape)
:canonical: abtem.prism.utils.minimum_crop

```{autodoc2-docstring} abtem.prism.utils.minimum_crop
```
````

````{py:function} plane_waves(wave_vectors: numpy.ndarray, extent: typing.Tuple[float, float], gpts: typing.Tuple[int, int], reverse: bool = False) -> numpy.ndarray
:canonical: abtem.prism.utils.plane_waves

```{autodoc2-docstring} abtem.prism.utils.plane_waves
```
````

````{py:function} prism_coefficients(positions, wave_vectors, xp, ctf=None)
:canonical: abtem.prism.utils.prism_coefficients

```{autodoc2-docstring} abtem.prism.utils.prism_coefficients
```
````

````{py:function} prism_wave_vectors(cutoff: float, extent: typing.Tuple[float, float], energy: float, interpolation: typing.Tuple[int, int], xp=np) -> numpy.ndarray
:canonical: abtem.prism.utils.prism_wave_vectors

```{autodoc2-docstring} abtem.prism.utils.prism_wave_vectors
```
````

````{py:function} wrapped_crop_2d(array: numpy.ndarray, corner: typing.Tuple[int, int], size: typing.Tuple[int, int]) -> numpy.ndarray
:canonical: abtem.prism.utils.wrapped_crop_2d

```{autodoc2-docstring} abtem.prism.utils.wrapped_crop_2d
```
````

````{py:function} wrapped_slices(start: int, stop: int, n: int) -> typing.Tuple[slice, slice]
:canonical: abtem.prism.utils.wrapped_slices

```{autodoc2-docstring} abtem.prism.utils.wrapped_slices
```
````
