# {py:mod}`abtem.inelastic.plasmons`

```{py:module} abtem.inelastic.plasmons
```

```{autodoc2-docstring} abtem.inelastic.plasmons
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`PlasmonAxis <abtem.inelastic.plasmons.PlasmonAxis>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis
    :summary:
    ```
* - {py:obj}`PlasmonScatteringEvents <abtem.inelastic.plasmons.PlasmonScatteringEvents>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents
    :summary:
    ```
* - {py:obj}`MonteCarloPlasmons <abtem.inelastic.plasmons.MonteCarloPlasmons>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`draw_scattering_depths <abtem.inelastic.plasmons.draw_scattering_depths>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.draw_scattering_depths
    :summary:
    ```
* - {py:obj}`draw_radial_scattering_angle <abtem.inelastic.plasmons.draw_radial_scattering_angle>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.draw_radial_scattering_angle
    :summary:
    ```
* - {py:obj}`draw_azimuthal_angle <abtem.inelastic.plasmons.draw_azimuthal_angle>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.draw_azimuthal_angle
    :summary:
    ```
* - {py:obj}`excitations_weights <abtem.inelastic.plasmons.excitations_weights>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.excitations_weights
    :summary:
    ```
* - {py:obj}`reduce_plasmon_axes <abtem.inelastic.plasmons.reduce_plasmon_axes>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.reduce_plasmon_axes
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`nth <abtem.inelastic.plasmons.nth>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.nth
    :summary:
    ```
* - {py:obj}`ntuples <abtem.inelastic.plasmons.ntuples>`
  - ```{autodoc2-docstring} abtem.inelastic.plasmons.ntuples
    :summary:
    ```
````

### API

````{py:data} nth
:canonical: abtem.inelastic.plasmons.nth
:value: >
   None

```{autodoc2-docstring} abtem.inelastic.plasmons.nth
```

````

````{py:data} ntuples
:canonical: abtem.inelastic.plasmons.ntuples
:value: >
   None

```{autodoc2-docstring} abtem.inelastic.plasmons.ntuples
```

````

````{py:function} draw_scattering_depths(num_depths: int, num_samples: int, mean_free_path: float, max_depth: float, max_batch: int = 10000, max_attempts: int = 50000000, rng=None) -> typing.Tuple[typing.Tuple]
:canonical: abtem.inelastic.plasmons.draw_scattering_depths

```{autodoc2-docstring} abtem.inelastic.plasmons.draw_scattering_depths
```
````

````{py:function} draw_radial_scattering_angle(critical_angle: float, characteristic_angle: float, num_samples, num_depths, rng=None) -> typing.Tuple[typing.Tuple[float]]
:canonical: abtem.inelastic.plasmons.draw_radial_scattering_angle

```{autodoc2-docstring} abtem.inelastic.plasmons.draw_radial_scattering_angle
```
````

````{py:function} draw_azimuthal_angle(num_samples, num_depths, rng=None) -> typing.Tuple[float]
:canonical: abtem.inelastic.plasmons.draw_azimuthal_angle

```{autodoc2-docstring} abtem.inelastic.plasmons.draw_azimuthal_angle
```
````

````{py:function} excitations_weights(n: int, thickness: float, mean_free_path: float) -> float
:canonical: abtem.inelastic.plasmons.excitations_weights

```{autodoc2-docstring} abtem.inelastic.plasmons.excitations_weights
```
````

`````{py:class} PlasmonAxis
:canonical: abtem.inelastic.plasmons.PlasmonAxis

Bases: {py:obj}`abtem.core.axes.OrdinalAxis`

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis
```

````{py:attribute} units
:canonical: abtem.inelastic.plasmons.PlasmonAxis.units
:type: str
:value: <Multiline-String>

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.units
```

````

````{py:attribute} label
:canonical: abtem.inelastic.plasmons.PlasmonAxis.label
:type: str
:value: >
   'Plasmons excitations'

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.label
```

````

````{py:property} excitations
:canonical: abtem.inelastic.plasmons.PlasmonAxis.excitations

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.excitations
```

````

````{py:property} azimuthal_angles
:canonical: abtem.inelastic.plasmons.PlasmonAxis.azimuthal_angles

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.azimuthal_angles
```

````

````{py:property} radial_angles
:canonical: abtem.inelastic.plasmons.PlasmonAxis.radial_angles

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.radial_angles
```

````

````{py:property} depths
:canonical: abtem.inelastic.plasmons.PlasmonAxis.depths

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.depths
```

````

````{py:property} tilt
:canonical: abtem.inelastic.plasmons.PlasmonAxis.tilt

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.tilt
```

````

````{py:method} update(depth)
:canonical: abtem.inelastic.plasmons.PlasmonAxis.update

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonAxis.update
```

````

`````

````{py:function} reduce_plasmon_axes(measurement)
:canonical: abtem.inelastic.plasmons.reduce_plasmon_axes

```{autodoc2-docstring} abtem.inelastic.plasmons.reduce_plasmon_axes
```
````

`````{py:class} PlasmonScatteringEvents(depths: typing.Tuple[typing.Tuple[float, ...]], radial_angles: typing.Tuple[typing.Tuple[float, ...]], azimuthal_angles: typing.Tuple[typing.Tuple[float, ...]], weights: typing.Tuple[float], ensemble_mean: bool)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents

Bases: {py:obj}`abtem.transform.ArrayObjectTransform`

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.__init__
```

````{py:property} ensemble_shape
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.ensemble_shape

````

````{py:property} ensemble_mean
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.ensemble_mean

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.ensemble_mean
```

````

````{py:property} depths
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.depths
:type: typing.Tuple[typing.Tuple[float, ...]]

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.depths
```

````

````{py:property} radial_angles
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.radial_angles
:type: typing.Tuple[typing.Tuple[float, ...]]

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.radial_angles
```

````

````{py:property} azimuthal_angles
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.azimuthal_angles
:type: typing.Tuple[typing.Tuple[float, ...]]

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.azimuthal_angles
```

````

````{py:property} weights
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.weights
:type: typing.Tuple[float]

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.weights
```

````

````{py:property} num_events
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.num_events

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.num_events
```

````

````{py:property} num_excitations
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.num_excitations

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.num_excitations
```

````

````{py:property} max_excitations
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.max_excitations

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.max_excitations
```

````

````{py:method} show_excitations_histogram(ax: matplotlib.axes.Axes = None)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.show_excitations_histogram

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.show_excitations_histogram
```

````

````{py:method} get_scattering_event_depths(num_excitations: int = 1)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.get_scattering_event_depths

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.get_scattering_event_depths
```

````

````{py:method} show_cumulative_scattering_events(ax=None, num_excitations: typing.Union[int, typing.List[int]] = 1, **kwargs)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.show_cumulative_scattering_events

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.show_cumulative_scattering_events
```

````

````{py:method} show_scattering_angle_distribution(ax=None, **kwargs)
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.show_scattering_angle_distribution

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.show_scattering_angle_distribution
```

````

````{py:method} show_weights()
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.show_weights

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.show_weights
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.ensemble_axes_metadata
:type: typing.List[abtem.core.axes.AxisMetadata]

````

````{py:method} apply(waves: abtem.waves.Waves, in_place: bool = False) -> abtem.waves.Waves
:canonical: abtem.inelastic.plasmons.PlasmonScatteringEvents.apply

```{autodoc2-docstring} abtem.inelastic.plasmons.PlasmonScatteringEvents.apply
```

````

`````

`````{py:class} MonteCarloPlasmons(mean_free_path: float, excitation_energy: float, critical_angle: float, num_excitations: typing.Union[int, typing.Tuple[int, ...]] = None, num_samples: int = None, weights: typing.Union[bool] = True, ensemble_mean: bool = False, seed: typing.Union[int, typing.Tuple[int, ...]] = None)
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.__init__
```

````{py:property} ensemble_mean
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.ensemble_mean
:type: bool

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.ensemble_mean
```

````

````{py:property} num_samples
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.num_samples
:type: int

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.num_samples
```

````

````{py:property} mean_free_path
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.mean_free_path
:type: float

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.mean_free_path
```

````

````{py:property} seed
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.seed
:type: int

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.seed
```

````

````{py:method} characteristic_angle(energy: float) -> float
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.characteristic_angle

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.characteristic_angle
```

````

````{py:method} draw_events(waves: abtem.waves.Waves, potential: abtem.potentials.BasePotential) -> abtem.inelastic.plasmons.PlasmonScatteringEvents
:canonical: abtem.inelastic.plasmons.MonteCarloPlasmons.draw_events

```{autodoc2-docstring} abtem.inelastic.plasmons.MonteCarloPlasmons.draw_events
```

````

`````
