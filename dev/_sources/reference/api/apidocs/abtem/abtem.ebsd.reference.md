# {py:mod}`abtem.ebsd.reference`

```{py:module} abtem.ebsd.reference
```

```{autodoc2-docstring} abtem.ebsd.reference
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EBSDReferencePattern <abtem.ebsd.reference.EBSDReferencePattern>`
  - ```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`fft_friendly_gpts <abtem.ebsd.reference.fft_friendly_gpts>`
  - ```{autodoc2-docstring} abtem.ebsd.reference.fft_friendly_gpts
    :parser: rst
    :summary:
    ```
* - {py:obj}`patch_half_angle <abtem.ebsd.reference.patch_half_angle>`
  - ```{autodoc2-docstring} abtem.ebsd.reference.patch_half_angle
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} EBSDReferencePattern(...)
:canonical: abtem.ebsd.reference.EBSDReferencePattern

Bases: {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.__init__
:parser: rst
```

````{py:property} atoms
:canonical: abtem.ebsd.reference.EBSDReferencePattern.atoms
:type: ase.Atoms

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.atoms
:parser: rst
```

````

````{py:method} build(...) -> abtem.ebsd.measurements.SphericalPattern
:canonical: abtem.ebsd.reference.EBSDReferencePattern.build

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.build
:parser: rst
```

````

````{py:property} centrosymmetric
:canonical: abtem.ebsd.reference.EBSDReferencePattern.centrosymmetric
:type: bool

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.centrosymmetric
:parser: rst
```

````

````{py:property} directions
:canonical: abtem.ebsd.reference.EBSDReferencePattern.directions
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.directions
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.ebsd.reference.EBSDReferencePattern.energy
:type: float

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.energy
:parser: rst
```

````

````{py:property} frozen_phonons
:canonical: abtem.ebsd.reference.EBSDReferencePattern.frozen_phonons
:type: typing.Optional[abtem.inelastic.phonons.FrozenPhonons]

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.frozen_phonons
:parser: rst
```

````

````{py:property} gpts
:canonical: abtem.ebsd.reference.EBSDReferencePattern.gpts
:type: int

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.gpts
:parser: rst
```

````

````{py:property} hemisphere
:canonical: abtem.ebsd.reference.EBSDReferencePattern.hemisphere
:type: str

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.hemisphere
:parser: rst
```

````

````{py:property} max_angle
:canonical: abtem.ebsd.reference.EBSDReferencePattern.max_angle
:type: float

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.max_angle
:parser: rst
```

````

````{py:property} n_patches
:canonical: abtem.ebsd.reference.EBSDReferencePattern.n_patches
:type: int

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.n_patches
:parser: rst
```

````

````{py:property} potential_gpts
:canonical: abtem.ebsd.reference.EBSDReferencePattern.potential_gpts
:type: tuple[int, int]

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.potential_gpts
:parser: rst
```

````

````{py:property} projection
:canonical: abtem.ebsd.reference.EBSDReferencePattern.projection
:type: abtem.ebsd.projections.HemisphereProjection

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.projection
:parser: rst
```

````

````{py:property} sampling
:canonical: abtem.ebsd.reference.EBSDReferencePattern.sampling
:type: float

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.sampling
:parser: rst
```

````

````{py:property} slab_cell
:canonical: abtem.ebsd.reference.EBSDReferencePattern.slab_cell
:type: tuple[float, float, float]

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.slab_cell
:parser: rst
```

````

````{py:property} zone_axes
:canonical: abtem.ebsd.reference.EBSDReferencePattern.zone_axes
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.reference.EBSDReferencePattern.zone_axes
:parser: rst
```

````

`````

````{py:function} fft_friendly_gpts(...) -> tuple[int, int]
:canonical: abtem.ebsd.reference.fft_friendly_gpts

```{autodoc2-docstring} abtem.ebsd.reference.fft_friendly_gpts
:parser: rst
```
````

````{py:function} patch_half_angle(...) -> float
:canonical: abtem.ebsd.reference.patch_half_angle

```{autodoc2-docstring} abtem.ebsd.reference.patch_half_angle
:parser: rst
```
````
