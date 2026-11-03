# {py:mod}`abtem.ebsd.detector_pattern`

```{py:module} abtem.ebsd.detector_pattern
```

```{autodoc2-docstring} abtem.ebsd.detector_pattern
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EBSDDetectorPattern <abtem.ebsd.detector_pattern.EBSDDetectorPattern>`
  - ```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} EBSDDetectorPattern(...)
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern

Bases: {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.__init__
:parser: rst
```

````{py:property} atoms
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.atoms
:type: ase.Atoms

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.atoms
:parser: rst
```

````

````{py:property} beam_direction
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.beam_direction
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.beam_direction
:parser: rst
```

````

````{py:method} build(...) -> abtem.ebsd.measurements.EBSDPatternImages
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.build

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.build
:parser: rst
```

````

````{py:property} directions
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.directions
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.directions
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.energy
:type: float

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.energy
:parser: rst
```

````

````{py:property} euler
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.euler
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.euler
:parser: rst
```

````

````{py:property} frozen_phonons
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.frozen_phonons
:type: typing.Optional[abtem.inelastic.phonons.FrozenPhonons]

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.frozen_phonons
:parser: rst
```

````

````{py:property} geometry
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.geometry
:type: abtem.ebsd.geometry.EBSDGeometry

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.geometry
:parser: rst
```

````

````{py:property} incident_cell
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.incident_cell
:type: tuple[float, float, float]

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.incident_cell
:parser: rst
```

````

````{py:property} max_angle
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.max_angle
:type: float

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.max_angle
:parser: rst
```

````

````{py:property} n_patches
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.n_patches
:type: typing.Optional[int]

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.n_patches
:parser: rst
```

````

````{py:property} potential_gpts
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.potential_gpts
:type: tuple[int, int]

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.potential_gpts
:parser: rst
```

````

````{py:property} sampling
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.sampling
:type: float

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.sampling
:parser: rst
```

````

````{py:method} scan(...) -> abtem.ebsd.measurements.EBSDPatternImages
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.scan

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.scan
:parser: rst
```

````

````{py:property} slab_cell
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.slab_cell
:type: tuple[float, float, float]

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.slab_cell
:parser: rst
```

````

````{py:property} zone_axes
:canonical: abtem.ebsd.detector_pattern.EBSDDetectorPattern.zone_axes
:type: numpy.ndarray

```{autodoc2-docstring} abtem.ebsd.detector_pattern.EBSDDetectorPattern.zone_axes
:parser: rst
```

````

`````
