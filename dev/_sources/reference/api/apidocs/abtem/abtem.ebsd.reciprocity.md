# {py:mod}`abtem.ebsd.reciprocity`

```{py:module} abtem.ebsd.reciprocity
```

```{autodoc2-docstring} abtem.ebsd.reciprocity
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`EBSD <abtem.ebsd.reciprocity.EBSD>`
  - ```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DepthWeight <abtem.ebsd.reciprocity.DepthWeight>`
  - ```{autodoc2-docstring} abtem.ebsd.reciprocity.DepthWeight
    :parser: rst
    :summary:
    ```
````

### API

````{py:data} DepthWeight
:canonical: abtem.ebsd.reciprocity.DepthWeight
:value: >
   None

```{autodoc2-docstring} abtem.ebsd.reciprocity.DepthWeight
:parser: rst
```

````

`````{py:class} EBSD(...)
:canonical: abtem.ebsd.reciprocity.EBSD

Bases: {py:obj}`abtem.core.utils.CopyMixin`, {py:obj}`abtem.core.utils.EqualityMixin`

```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD.__init__
:parser: rst
```

````{py:method} build(...) -> abtem.measurements.DiffractionPatterns | abtem.ebsd.measurements.SphericalPattern
:canonical: abtem.ebsd.reciprocity.EBSD.build

```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD.build
:parser: rst
```

````

````{py:property} detector
:canonical: abtem.ebsd.reciprocity.EBSD.detector
:type: abtem.ebsd.detectors.BackscatterDetector

```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD.detector
:parser: rst
```

````

````{py:property} device
:canonical: abtem.ebsd.reciprocity.EBSD.device
:type: str

```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD.device
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.ebsd.reciprocity.EBSD.energy
:type: float

```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD.energy
:parser: rst
```

````

````{py:property} illumination
:canonical: abtem.ebsd.reciprocity.EBSD.illumination
:type: typing.Optional[numpy.ndarray]

```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD.illumination
:parser: rst
```

````

````{py:property} potential
:canonical: abtem.ebsd.reciprocity.EBSD.potential
:type: abtem.potentials.iam.BasePotential

```{autodoc2-docstring} abtem.ebsd.reciprocity.EBSD.potential
:parser: rst
```

````

`````
