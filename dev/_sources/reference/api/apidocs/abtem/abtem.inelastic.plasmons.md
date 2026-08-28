# {py:mod}`abtem.inelastic.plasmons`

```{py:module} abtem.inelastic.plasmons
```

```{autodoc2-docstring} abtem.inelastic.plasmons
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`MonteCarloPlasmons <abtem.inelastic.plasmons.MonteCarloPlasmons>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons
    :parser: rst
    :summary:
    ```
* - {py:obj}`PlasmonAxis <abtem.inelastic.plasmons.PlasmonAxis>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis
    :parser: rst
    :summary:
    ```
* - {py:obj}`PlasmonScatteringEvents <abtem.inelastic.plasmons.PlasmonScatteringEvents>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`draw_azimuthal_angle <abtem.inelastic.plasmons.draw_azimuthal_angle>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.draw_azimuthal_angle
    :parser: rst
    :summary:
    ```
* - {py:obj}`draw_radial_scattering_angle <abtem.inelastic.plasmons.draw_radial_scattering_angle>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.draw_radial_scattering_angle
    :parser: rst
    :summary:
    ```
* - {py:obj}`draw_scattering_depths <abtem.inelastic.plasmons.draw_scattering_depths>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.draw_scattering_depths
    :parser: rst
    :summary:
    ```
* - {py:obj}`excitations_weights <abtem.inelastic.plasmons.excitations_weights>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.excitations_weights
    :parser: rst
    :summary:
    ```
* - {py:obj}`reduce_plasmon_axes <abtem.inelastic.plasmons.reduce_plasmon_axes>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.reduce_plasmon_axes
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`nth <abtem.inelastic.plasmons.nth>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.nth
    :parser: rst
    :summary:
    ```
* - {py:obj}`ntuples <abtem.inelastic.plasmons.ntuples>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.ntuples
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} MonteCarloPlasmons(mean_free_path: float, excitation_energy: float, critical_angle: float, num_excitations: typing.Union[int, typing.Tuple[int, ...]] = None, num_samples: int = None, weights: typing.Union[bool] = True, ensemble_mean: bool = False, seed: typing.Union[int, typing.Tuple[int, ...]] = None)
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.__init__
:parser: rst
```

````{py:method} characteristic_angle(energy: float) -> float
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.characteristic_angle

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.characteristic_angle
:parser: rst
```

````

````{py:method} draw_events(waves: abtem.waves.Waves, potential: abtem.potentials.BasePotential) -> abtem.inelastic.plasmons.PlasmonScatteringEvents
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.draw_events

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.draw_events
:parser: rst
```

````

````{py:property} ensemble_mean
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.ensemble_mean
:type: bool

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.ensemble_mean
:parser: rst
```

````

````{py:property} mean_free_path
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.mean_free_path
:type: float

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.mean_free_path
:parser: rst
```

````

````{py:property} num_samples
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.num_samples
:type: int

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.num_samples
:parser: rst
```

````

````{py:property} seed
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.seed
:type: int

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.seed
:parser: rst
```

````

`````

`````{py:class} PlasmonAxis
:canonical: abtem.inelastic.plasmons.PlasmonAxis

Bases: {py:obj}`abtem.core.axes.OrdinalAxis`

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis
:parser: rst
```

````{py:property} azimuthal_angles
:canonical: abtem.inelastic.plasmons.PlasmonAxis.azimuthal_angles

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.azimuthal_angles
:parser: rst
```

````

````{py:property} depths
:canonical: abtem.inelastic.plasmons.PlasmonAxis.depths

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.depths
:parser: rst
```

````

````{py:property} excitations
:canonical: abtem.inelastic.plasmons.PlasmonAxis.excitations

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.excitations
:parser: rst
```

````

````{py:attribute} label
:canonical: abtem.inelastic.plasmons.PlasmonAxis.label
:type: str
:value: >
   'Plasmons excitations'

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.label
:parser: rst
```

````

````{py:property} radial_angles
:canonical: abtem.inelastic.plasmons.PlasmonAxis.radial_angles

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.radial_angles
:parser: rst
```

````

````{py:property} tilt
:canonical: abtem.inelastic.plasmons.PlasmonAxis.tilt

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.tilt
:parser: rst
```

````

````{py:attribute} units
:canonical: abtem.inelastic.plasmons.PlasmonAxis.units
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.units
:parser: rst
```

````

````{py:method} update(depth)
:canonical: abtem.inelastic.plasmons.PlasmonAxis.update

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.update
:parser: rst
```

````

`````

`````{py:class} PlasmonScatteringEvents(depths: typing.Tuple[typing.Tuple[float, ...]], radial_angles: typing.Tuple[typing.Tuple[float, ...]], azimuthal_angles: typing.Tuple[typing.Tuple[float, ...]], weights: typing.Tuple[float], ensemble_mean: bool)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents

Bases: {py:obj}`abtem.transform.ArrayObjectTransform`

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.__init__
:parser: rst
```

````{py:method} apply(waves: abtem.waves.Waves, in_place: bool = False) -> abtem.waves.Waves
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.apply

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.apply
:parser: rst
```

````

````{py:property} azimuthal_angles
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.azimuthal_angles
:type: typing.Tuple[typing.Tuple[float, ...]]

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.azimuthal_angles
:parser: rst
```

````

````{py:property} depths
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.depths
:type: typing.Tuple[typing.Tuple[float, ...]]

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.depths
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.ensemble_axes_metadata
:type: typing.List[abtem.core.axes.AxisMetadata]

````

````{py:property} ensemble_mean
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.ensemble_mean

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.ensemble_mean
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.ensemble_shape

````

````{py:method} get_scattering_event_depths(num_excitations: int = 1)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.get_scattering_event_depths

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.get_scattering_event_depths
:parser: rst
```

````

````{py:property} max_excitations
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.max_excitations

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.max_excitations
:parser: rst
```

````

````{py:property} num_events
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.num_events

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.num_events
:parser: rst
```

````

````{py:property} num_excitations
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.num_excitations

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.num_excitations
:parser: rst
```

````

````{py:property} radial_angles
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.radial_angles
:type: typing.Tuple[typing.Tuple[float, ...]]

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.radial_angles
:parser: rst
```

````

````{py:method} show_cumulative_scattering_events(ax=None, num_excitations: typing.Union[int, typing.List[int]] = 1, **kwargs)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.show_cumulative_scattering_events

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.show_cumulative_scattering_events
:parser: rst
```

````

````{py:method} show_excitations_histogram(ax: matplotlib.axes.Axes = None)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.show_excitations_histogram

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.show_excitations_histogram
:parser: rst
```

````

````{py:method} show_scattering_angle_distribution(ax=None, **kwargs)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.show_scattering_angle_distribution

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.show_scattering_angle_distribution
:parser: rst
```

````

````{py:method} show_weights()
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.show_weights

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.show_weights
:parser: rst
```

````

````{py:property} weights
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.weights
:type: typing.Tuple[float]

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.weights
:parser: rst
```

````

`````

````{py:function} draw_azimuthal_angle(num_samples, num_depths, rng=None) -> typing.Tuple[float]
:canonical: abtem.inelastic.plasmons.draw_azimuthal_angle

```{autodoc2-docstring} abtem.inelastic.plasmons.draw_azimuthal_angle
:parser: rst
```
````

````{py:function} draw_radial_scattering_angle(critical_angle: float, characteristic_angle: float, num_samples, num_depths, rng=None) -> typing.Tuple[typing.Tuple[float]]
:canonical: abtem.inelastic.plasmons.draw_radial_scattering_angle

```{autodoc2-docstring} abtem.inelastic.plasmons.draw_radial_scattering_angle
:parser: rst
```
````

````{py:function} draw_scattering_depths(num_depths: int, num_samples: int, mean_free_path: float, max_depth: float, max_batch: int = 10000, max_attempts: int = 50000000, rng=None) -> typing.Tuple[typing.Tuple]
:canonical: abtem.inelastic.plasmons.draw_scattering_depths

```{autodoc2-docstring} abtem.inelastic.plasmons.draw_scattering_depths
:parser: rst
```
````

````{py:function} excitations_weights(n: int, thickness: float, mean_free_path: float) -> float
:canonical: abtem.inelastic.plasmons.excitations_weights

```{autodoc2-docstring} abtem.inelastic.plasmons.excitations_weights
:parser: rst
```
````

````{py:data} nth
:canonical: abtem.inelastic.plasmons.nth
:value: >
   None

```{autodoc2-docstring} abtem.inelastic.plasmons.nth
:parser: rst
```

````

````{py:data} ntuples
:canonical: abtem.inelastic.plasmons.ntuples
:value: >
   None

```{autodoc2-docstring} abtem.inelastic.plasmons.ntuples
:parser: rst
```

````

````{py:function} reduce_plasmon_axes(measurement)
:canonical: abtem.inelastic.plasmons.reduce_plasmon_axes

```{autodoc2-docstring} abtem.inelastic.plasmons.reduce_plasmon_axes
:parser: rst
```
````
