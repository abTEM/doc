# {py:mod}`abtem.inelastic.phonons`

```{py:module} abtem.inelastic.phonons
```

```{autodoc2-docstring} abtem.inelastic.phonons
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AtomsEnsemble <abtem.inelastic.phonons.AtomsEnsemble>`
  - ```{autodoc2-docstring} abtem.inelastic.phonons.AtomsEnsemble
    :parser: rst
    :summary:
    ```
* - {py:obj}`BaseFrozenPhonons <abtem.inelastic.phonons.BaseFrozenPhonons>`
  - ```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons
    :parser: rst
    :summary:
    ```
* - {py:obj}`DummyFrozenPhonons <abtem.inelastic.phonons.DummyFrozenPhonons>`
  - ```{autodoc2-docstring} abtem.inelastic.phonons.DummyFrozenPhonons
    :parser: rst
    :summary:
    ```
* - {py:obj}`EnergyResolvedAtomsEnsemble <abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble>`
  - ```{autodoc2-docstring} abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble
    :parser: rst
    :summary:
    ```
* - {py:obj}`FrozenPhonons <abtem.inelastic.phonons.FrozenPhonons>`
  - ```{autodoc2-docstring} abtem.inelastic.phonons.FrozenPhonons
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`validate_seeds <abtem.inelastic.phonons.validate_seeds>`
  - ```{autodoc2-docstring} abtem.inelastic.phonons.validate_seeds
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Reader <abtem.inelastic.phonons.Reader>`
  - ```{autodoc2-docstring} abtem.inelastic.phonons.Reader
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} AtomsEnsemble(...)
:canonical: abtem.inelastic.phonons.AtomsEnsemble

Bases: {py:obj}`abtem.inelastic.phonons.BaseFrozenPhonons`

```{autodoc2-docstring} abtem.inelastic.phonons.AtomsEnsemble
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.phonons.AtomsEnsemble.__init__
:parser: rst
```

````{py:property} atoms
:canonical: abtem.inelastic.phonons.AtomsEnsemble.atoms
:type: ase.Atoms

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.inelastic.phonons.AtomsEnsemble.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_shape
:canonical: abtem.inelastic.phonons.AtomsEnsemble.ensemble_shape
:type: tuple[int, ...]

````

````{py:method} mean_squared_deviations() -> numpy.ndarray
:canonical: abtem.inelastic.phonons.AtomsEnsemble.mean_squared_deviations

```{autodoc2-docstring} abtem.inelastic.phonons.AtomsEnsemble.mean_squared_deviations
:parser: rst
```

````

````{py:property} num_configs
:canonical: abtem.inelastic.phonons.AtomsEnsemble.num_configs
:type: int

````

````{py:property} numbers
:canonical: abtem.inelastic.phonons.AtomsEnsemble.numbers

```{autodoc2-docstring} abtem.inelastic.phonons.AtomsEnsemble.numbers
:parser: rst
```

````

````{py:method} randomize(...) -> ase.Atoms
:canonical: abtem.inelastic.phonons.AtomsEnsemble.randomize

````

````{py:method} standard_deviations() -> numpy.ndarray
:canonical: abtem.inelastic.phonons.AtomsEnsemble.standard_deviations

```{autodoc2-docstring} abtem.inelastic.phonons.AtomsEnsemble.standard_deviations
:parser: rst
```

````

````{py:property} trajectory
:canonical: abtem.inelastic.phonons.AtomsEnsemble.trajectory
:type: numpy.ndarray | dask.array.core.Array

```{autodoc2-docstring} abtem.inelastic.phonons.AtomsEnsemble.trajectory
:parser: rst
```

````

`````

`````{py:class} BaseFrozenPhonons(...)
:canonical: abtem.inelastic.phonons.BaseFrozenPhonons

Bases: {py:obj}`abtem.core.ensemble.Ensemble`, {py:obj}`abtem.core.utils.EqualityMixin`, {py:obj}`abtem.core.utils.CopyMixin`

```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons.__init__
:parser: rst
```

````{py:property} atomic_numbers
:canonical: abtem.inelastic.phonons.BaseFrozenPhonons.atomic_numbers
:type: numpy.ndarray

```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons.atomic_numbers
:parser: rst
```

````

````{py:property} atoms
:canonical: abtem.inelastic.phonons.BaseFrozenPhonons.atoms
:abstractmethod:
:type: ase.Atoms

```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons.atoms
:parser: rst
```

````

````{py:property} cell
:canonical: abtem.inelastic.phonons.BaseFrozenPhonons.cell
:type: ase.cell.Cell

```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons.cell
:parser: rst
```

````

````{py:property} ensemble_mean
:canonical: abtem.inelastic.phonons.BaseFrozenPhonons.ensemble_mean

```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons.ensemble_mean
:parser: rst
```

````

````{py:property} num_configs
:canonical: abtem.inelastic.phonons.BaseFrozenPhonons.num_configs
:abstractmethod:

```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons.num_configs
:parser: rst
```

````

````{py:method} randomize(...) -> ase.Atoms
:canonical: abtem.inelastic.phonons.BaseFrozenPhonons.randomize
:abstractmethod:

```{autodoc2-docstring} abtem.inelastic.phonons.BaseFrozenPhonons.randomize
:parser: rst
```

````

`````

`````{py:class} DummyFrozenPhonons(...)
:canonical: abtem.inelastic.phonons.DummyFrozenPhonons

Bases: {py:obj}`abtem.inelastic.phonons.BaseFrozenPhonons`

```{autodoc2-docstring} abtem.inelastic.phonons.DummyFrozenPhonons
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.phonons.DummyFrozenPhonons.__init__
:parser: rst
```

````{py:property} atoms
:canonical: abtem.inelastic.phonons.DummyFrozenPhonons.atoms

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.inelastic.phonons.DummyFrozenPhonons.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_shape
:canonical: abtem.inelastic.phonons.DummyFrozenPhonons.ensemble_shape

````

````{py:property} num_configs
:canonical: abtem.inelastic.phonons.DummyFrozenPhonons.num_configs

````

````{py:property} numbers
:canonical: abtem.inelastic.phonons.DummyFrozenPhonons.numbers

```{autodoc2-docstring} abtem.inelastic.phonons.DummyFrozenPhonons.numbers
:parser: rst
```

````

````{py:method} randomize(...) -> ase.Atoms
:canonical: abtem.inelastic.phonons.DummyFrozenPhonons.randomize

````

`````

`````{py:class} EnergyResolvedAtomsEnsemble(...)
:canonical: abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble

Bases: {py:obj}`abtem.inelastic.phonons.BaseFrozenPhonons`

```{autodoc2-docstring} abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.__init__
:parser: rst
```

````{py:property} atoms
:canonical: abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.atoms
:type: ase.Atoms

````

````{py:property} energies
:canonical: abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.energies
:type: numpy.ndarray

```{autodoc2-docstring} abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.energies
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_shape
:canonical: abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.ensemble_shape
:type: tuple[int, ...]

````

````{py:property} num_configs
:canonical: abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.num_configs
:type: int

````

````{py:method} randomize(...) -> ase.Atoms
:canonical: abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.randomize

````

````{py:property} snapshots
:canonical: abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.snapshots
:type: numpy.ndarray

```{autodoc2-docstring} abtem.inelastic.phonons.EnergyResolvedAtomsEnsemble.snapshots
:parser: rst
```

````

`````

`````{py:class} FrozenPhonons(...)
:canonical: abtem.inelastic.phonons.FrozenPhonons

Bases: {py:obj}`abtem.inelastic.phonons.BaseFrozenPhonons`

```{autodoc2-docstring} abtem.inelastic.phonons.FrozenPhonons
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.phonons.FrozenPhonons.__init__
:parser: rst
```

````{py:property} atoms
:canonical: abtem.inelastic.phonons.FrozenPhonons.atoms
:type: ase.Atoms

````

````{py:property} directions
:canonical: abtem.inelastic.phonons.FrozenPhonons.directions
:type: str

```{autodoc2-docstring} abtem.inelastic.phonons.FrozenPhonons.directions
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.inelastic.phonons.FrozenPhonons.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_shape
:canonical: abtem.inelastic.phonons.FrozenPhonons.ensemble_shape

````

````{py:property} num_configs
:canonical: abtem.inelastic.phonons.FrozenPhonons.num_configs
:type: int

````

````{py:method} randomize(...) -> ase.Atoms
:canonical: abtem.inelastic.phonons.FrozenPhonons.randomize

````

````{py:property} seed
:canonical: abtem.inelastic.phonons.FrozenPhonons.seed
:type: tuple[int, ...]

```{autodoc2-docstring} abtem.inelastic.phonons.FrozenPhonons.seed
:parser: rst
```

````

````{py:property} sigmas
:canonical: abtem.inelastic.phonons.FrozenPhonons.sigmas
:type: numpy.ndarray | dict[str, numpy.ndarray]

```{autodoc2-docstring} abtem.inelastic.phonons.FrozenPhonons.sigmas
:parser: rst
```

````

````{py:method} to_atoms_ensemble()
:canonical: abtem.inelastic.phonons.FrozenPhonons.to_atoms_ensemble

```{autodoc2-docstring} abtem.inelastic.phonons.FrozenPhonons.to_atoms_ensemble
:parser: rst
```

````

`````

````{py:data} Reader
:canonical: abtem.inelastic.phonons.Reader
:type: typing.Optional[typing.Callable]
:value: >
   None

```{autodoc2-docstring} abtem.inelastic.phonons.Reader
:parser: rst
```

````

````{py:function} validate_seeds(...) -> tuple[int, ...]
:canonical: abtem.inelastic.phonons.validate_seeds

```{autodoc2-docstring} abtem.inelastic.phonons.validate_seeds
:parser: rst
```
````
