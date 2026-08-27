# {py:mod}`abtem.mcf`

```{py:module} abtem.mcf
```

```{autodoc2-docstring} abtem.mcf
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`DiagonalMCF <abtem.mcf.DiagonalMCF>`
  -
````

### API

`````{py:class} DiagonalMCF(eigenvectors: typing.Union[int, typing.Tuple[int]], focal_spread: float = 0.0, source_size: float = 0.0, rectangular_offset: typing.Tuple[float, float] = (0.0, 0.0), energy: float = None, semiangle_cutoff: float = None)
:canonical: abtem.mcf.DiagonalMCF

Bases: {py:obj}`abtem.transfer.ArrayWaveTransform`, {py:obj}`abtem.core.energy.HasAcceleratorMixin`

````{py:method} copy()
:canonical: abtem.mcf.DiagonalMCF.copy

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.copy
```

````

````{py:property} default_ensemble_chunks
:canonical: abtem.mcf.DiagonalMCF.default_ensemble_chunks

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.default_ensemble_chunks
```

````

````{py:property} eigenvectors
:canonical: abtem.mcf.DiagonalMCF.eigenvectors

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.eigenvectors
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.mcf.DiagonalMCF.ensemble_axes_metadata

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.ensemble_axes_metadata
```

````

````{py:method} ensemble_blocks(chunks)
:canonical: abtem.mcf.DiagonalMCF.ensemble_blocks

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.ensemble_blocks
```

````

````{py:method} ensemble_partial()
:canonical: abtem.mcf.DiagonalMCF.ensemble_partial

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.ensemble_partial
```

````

````{py:property} ensemble_shape
:canonical: abtem.mcf.DiagonalMCF.ensemble_shape

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.ensemble_shape
```

````

````{py:method} evaluate(waves, return_correlation: bool = False)
:canonical: abtem.mcf.DiagonalMCF.evaluate

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.evaluate
```

````

````{py:property} focal_spread
:canonical: abtem.mcf.DiagonalMCF.focal_spread

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.focal_spread
```

````

````{py:property} rectangular_offset
:canonical: abtem.mcf.DiagonalMCF.rectangular_offset

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.rectangular_offset
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.mcf.DiagonalMCF.semiangle_cutoff

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.semiangle_cutoff
```

````

````{py:property} source_size
:canonical: abtem.mcf.DiagonalMCF.source_size

```{autodoc2-docstring} abtem.mcf.DiagonalMCF.source_size
```

````

`````
