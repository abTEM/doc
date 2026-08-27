# {py:mod}`abtem.core.fft`

```{py:module} abtem.core.fft
```

```{autodoc2-docstring} abtem.core.fft
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`CachedFFTWConvolution <abtem.core.fft.CachedFFTWConvolution>`
  - ```{autodoc2-docstring} abtem.core.fft.CachedFFTWConvolution
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fft2 <abtem.core.fft.fft2>`
  - ```{autodoc2-docstring} abtem.core.fft.fft2
    :summary:
    ```
* - {py:obj}`fft2_convolve <abtem.core.fft.fft2_convolve>`
  - ```{autodoc2-docstring} abtem.core.fft.fft2_convolve
    :summary:
    ```
* - {py:obj}`fft_crop <abtem.core.fft.fft_crop>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_crop
    :summary:
    ```
* - {py:obj}`fft_interpolate <abtem.core.fft.fft_interpolate>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_interpolate
    :summary:
    ```
* - {py:obj}`fft_interpolation_masks <abtem.core.fft.fft_interpolation_masks>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_interpolation_masks
    :summary:
    ```
* - {py:obj}`fft_shift <abtem.core.fft.fft_shift>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_shift
    :summary:
    ```
* - {py:obj}`fft_shift_kernel <abtem.core.fft.fft_shift_kernel>`
  - ```{autodoc2-docstring} abtem.core.fft.fft_shift_kernel
    :summary:
    ```
* - {py:obj}`fftn <abtem.core.fft.fftn>`
  - ```{autodoc2-docstring} abtem.core.fft.fftn
    :summary:
    ```
* - {py:obj}`get_fftw_object <abtem.core.fft.get_fftw_object>`
  - ```{autodoc2-docstring} abtem.core.fft.get_fftw_object
    :summary:
    ```
* - {py:obj}`ifft2 <abtem.core.fft.ifft2>`
  - ```{autodoc2-docstring} abtem.core.fft.ifft2
    :summary:
    ```
* - {py:obj}`ifftn <abtem.core.fft.ifftn>`
  - ```{autodoc2-docstring} abtem.core.fft.ifftn
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`U <abtem.core.fft.U>`
  - ```{autodoc2-docstring} abtem.core.fft.U
    :summary:
    ```
````

### API

````{py:class} CachedFFTWConvolution()
:canonical: abtem.core.fft.CachedFFTWConvolution

```{autodoc2-docstring} abtem.core.fft.CachedFFTWConvolution
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.core.fft.CachedFFTWConvolution.__init__
```

````

````{py:data} U
:canonical: abtem.core.fft.U
:value: >
   'TypeVar(...)'

```{autodoc2-docstring} abtem.core.fft.U
```

````

````{py:function} fft2(x: abtem.core.fft.U, overwrite_x: bool = False, **kwargs) -> abtem.core.fft.U
:canonical: abtem.core.fft.fft2

```{autodoc2-docstring} abtem.core.fft.fft2
```
````

````{py:function} fft2_convolve(x: abtem.core.fft.U, kernel: numpy.ndarray, overwrite_x: bool = False) -> abtem.core.fft.U
:canonical: abtem.core.fft.fft2_convolve

```{autodoc2-docstring} abtem.core.fft.fft2_convolve
```
````

````{py:function} fft_crop(array: numpy.ndarray, new_shape: tuple[int, ...], normalize: bool = False)
:canonical: abtem.core.fft.fft_crop

```{autodoc2-docstring} abtem.core.fft.fft_crop
```
````

````{py:function} fft_interpolate(array: numpy.ndarray, new_shape: typing.Tuple[int, ...], normalization: str = 'values', overwrite_x: bool = False)
:canonical: abtem.core.fft.fft_interpolate

```{autodoc2-docstring} abtem.core.fft.fft_interpolate
```
````

````{py:function} fft_interpolation_masks(shape_in: tuple[int, ...], shape_out: tuple[int, ...]) -> tuple[numpy.ndarray, numpy.ndarray]
:canonical: abtem.core.fft.fft_interpolation_masks

```{autodoc2-docstring} abtem.core.fft.fft_interpolation_masks
```
````

````{py:function} fft_shift(array: numpy.ndarray, positions: numpy.ndarray) -> numpy.ndarray
:canonical: abtem.core.fft.fft_shift

```{autodoc2-docstring} abtem.core.fft.fft_shift
```
````

````{py:function} fft_shift_kernel(positions: numpy.ndarray, shape: tuple[int, ...]) -> numpy.ndarray
:canonical: abtem.core.fft.fft_shift_kernel

```{autodoc2-docstring} abtem.core.fft.fft_shift_kernel
```
````

````{py:function} fftn(x: abtem.core.fft.U, overwrite_x: bool = False, **kwargs) -> abtem.core.fft.U
:canonical: abtem.core.fft.fftn

```{autodoc2-docstring} abtem.core.fft.fftn
```
````

````{py:function} get_fftw_object(array: numpy.ndarray, name: str, allow_new_wisdom: bool = True, overwrite_x: bool = False, axes: tuple[int, ...] = (-2, -1))
:canonical: abtem.core.fft.get_fftw_object

```{autodoc2-docstring} abtem.core.fft.get_fftw_object
```
````

````{py:function} ifft2(x: abtem.core.fft.U, overwrite_x: bool = False, **kwargs) -> abtem.core.fft.U
:canonical: abtem.core.fft.ifft2

```{autodoc2-docstring} abtem.core.fft.ifft2
```
````

````{py:function} ifftn(x: abtem.core.fft.U, overwrite_x: bool = False, **kwargs) -> abtem.core.fft.U
:canonical: abtem.core.fft.ifftn

```{autodoc2-docstring} abtem.core.fft.ifftn
```
````
