# {py:mod}`abtem.antialias`

```{py:module} abtem.antialias
```

```{autodoc2-docstring} abtem.antialias
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AntialiasAperture <abtem.antialias.AntialiasAperture>`
  - ```{autodoc2-docstring} abtem.antialias.AntialiasAperture
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`antialias_aperture <abtem.antialias.antialias_aperture>`
  - ```{autodoc2-docstring} abtem.antialias.antialias_aperture
    :summary:
    ```
````

### API

````{py:function} antialias_aperture(gpts: tuple[int, int], sampling: tuple[float, float], xp=None) -> numpy.ndarray
:canonical: abtem.antialias.antialias_aperture

```{autodoc2-docstring} abtem.antialias.antialias_aperture
```
````

`````{py:class} AntialiasAperture()
:canonical: abtem.antialias.AntialiasAperture

Bases: {py:obj}`abtem.core.grid.HasGrid2DMixin`, {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.antialias.AntialiasAperture
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.antialias.AntialiasAperture.__init__
```

````{py:method} get_array(x: abtem.antialias.U)
:canonical: abtem.antialias.AntialiasAperture.get_array

```{autodoc2-docstring} abtem.antialias.AntialiasAperture.get_array
```

````

````{py:method} bandlimit(x: abtem.antialias.U, in_place: bool = False) -> abtem.antialias.U
:canonical: abtem.antialias.AntialiasAperture.bandlimit

```{autodoc2-docstring} abtem.antialias.AntialiasAperture.bandlimit
```

````

`````
