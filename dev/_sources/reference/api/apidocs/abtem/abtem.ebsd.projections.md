# {py:mod}`abtem.ebsd.projections`

```{py:module} abtem.ebsd.projections
```

```{autodoc2-docstring} abtem.ebsd.projections
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`HemisphereProjection <abtem.ebsd.projections.HemisphereProjection>`
  - ```{autodoc2-docstring} abtem.ebsd.projections.HemisphereProjection
    :parser: rst
    :summary:
    ```
* - {py:obj}`SquareLambertProjection <abtem.ebsd.projections.SquareLambertProjection>`
  - ```{autodoc2-docstring} abtem.ebsd.projections.SquareLambertProjection
    :parser: rst
    :summary:
    ```
* - {py:obj}`StereographicProjection <abtem.ebsd.projections.StereographicProjection>`
  - ```{autodoc2-docstring} abtem.ebsd.projections.StereographicProjection
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`bin_directions <abtem.ebsd.projections.bin_directions>`
  - ```{autodoc2-docstring} abtem.ebsd.projections.bin_directions
    :parser: rst
    :summary:
    ```
* - {py:obj}`pixel_centers <abtem.ebsd.projections.pixel_centers>`
  - ```{autodoc2-docstring} abtem.ebsd.projections.pixel_centers
    :parser: rst
    :summary:
    ```
* - {py:obj}`validate_projection <abtem.ebsd.projections.validate_projection>`
  - ```{autodoc2-docstring} abtem.ebsd.projections.validate_projection
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} HemisphereProjection
:canonical: abtem.ebsd.projections.HemisphereProjection

Bases: {py:obj}`abc.ABC`

```{autodoc2-docstring} abtem.ebsd.projections.HemisphereProjection
:parser: rst
```

````{py:method} domain_mask(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.HemisphereProjection.domain_mask
:abstractmethod:

```{autodoc2-docstring} abtem.ebsd.projections.HemisphereProjection.domain_mask
:parser: rst
```

````

````{py:method} grid(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.HemisphereProjection.grid

```{autodoc2-docstring} abtem.ebsd.projections.HemisphereProjection.grid
:parser: rst
```

````

````{py:attribute} name
:canonical: abtem.ebsd.projections.HemisphereProjection.name
:type: str
:value: >
   None

```{autodoc2-docstring} abtem.ebsd.projections.HemisphereProjection.name
:parser: rst
```

````

````{py:method} project(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.HemisphereProjection.project
:abstractmethod:

```{autodoc2-docstring} abtem.ebsd.projections.HemisphereProjection.project
:parser: rst
```

````

````{py:method} unproject(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.HemisphereProjection.unproject
:abstractmethod:

```{autodoc2-docstring} abtem.ebsd.projections.HemisphereProjection.unproject
:parser: rst
```

````

`````

`````{py:class} SquareLambertProjection
:canonical: abtem.ebsd.projections.SquareLambertProjection

Bases: {py:obj}`abtem.ebsd.projections.HemisphereProjection`

```{autodoc2-docstring} abtem.ebsd.projections.SquareLambertProjection
:parser: rst
```

````{py:method} domain_mask(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.SquareLambertProjection.domain_mask

````

````{py:method} grid(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.SquareLambertProjection.grid

````

````{py:attribute} name
:canonical: abtem.ebsd.projections.SquareLambertProjection.name
:value: >
   'lambert'

```{autodoc2-docstring} abtem.ebsd.projections.SquareLambertProjection.name
:parser: rst
```

````

````{py:method} project(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.SquareLambertProjection.project

````

````{py:method} unproject(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.SquareLambertProjection.unproject

````

`````

`````{py:class} StereographicProjection
:canonical: abtem.ebsd.projections.StereographicProjection

Bases: {py:obj}`abtem.ebsd.projections.HemisphereProjection`

```{autodoc2-docstring} abtem.ebsd.projections.StereographicProjection
:parser: rst
```

````{py:method} domain_mask(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.StereographicProjection.domain_mask

````

````{py:attribute} name
:canonical: abtem.ebsd.projections.StereographicProjection.name
:value: >
   'stereographic'

```{autodoc2-docstring} abtem.ebsd.projections.StereographicProjection.name
:parser: rst
```

````

````{py:method} project(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.StereographicProjection.project

````

````{py:method} unproject(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.StereographicProjection.unproject

````

`````

````{py:function} bin_directions(...) -> numpy.ndarray | tuple[numpy.ndarray, numpy.ndarray]
:canonical: abtem.ebsd.projections.bin_directions

```{autodoc2-docstring} abtem.ebsd.projections.bin_directions
:parser: rst
```
````

````{py:function} pixel_centers(...) -> numpy.ndarray
:canonical: abtem.ebsd.projections.pixel_centers

```{autodoc2-docstring} abtem.ebsd.projections.pixel_centers
:parser: rst
```
````

````{py:function} validate_projection(...) -> abtem.ebsd.projections.HemisphereProjection
:canonical: abtem.ebsd.projections.validate_projection

```{autodoc2-docstring} abtem.ebsd.projections.validate_projection
:parser: rst
```
````
