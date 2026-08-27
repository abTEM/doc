# {py:mod}`abtem.transfer`

```{py:module} abtem.transfer
```

```{autodoc2-docstring} abtem.transfer
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`BaseTransferFunction <abtem.transfer.BaseTransferFunction>`
  - ```{autodoc2-docstring} abtem.transfer.BaseTransferFunction
    :summary:
    ```
* - {py:obj}`BaseAperture <abtem.transfer.BaseAperture>`
  - ```{autodoc2-docstring} abtem.transfer.BaseAperture
    :summary:
    ```
* - {py:obj}`Aperture <abtem.transfer.Aperture>`
  - ```{autodoc2-docstring} abtem.transfer.Aperture
    :summary:
    ```
* - {py:obj}`Bullseye <abtem.transfer.Bullseye>`
  - ```{autodoc2-docstring} abtem.transfer.Bullseye
    :summary:
    ```
* - {py:obj}`Vortex <abtem.transfer.Vortex>`
  - ```{autodoc2-docstring} abtem.transfer.Vortex
    :summary:
    ```
* - {py:obj}`AnnularAperture <abtem.transfer.AnnularAperture>`
  - ```{autodoc2-docstring} abtem.transfer.AnnularAperture
    :summary:
    ```
* - {py:obj}`Zernike <abtem.transfer.Zernike>`
  - ```{autodoc2-docstring} abtem.transfer.Zernike
    :summary:
    ```
* - {py:obj}`RadialPhasePlate <abtem.transfer.RadialPhasePlate>`
  -
* - {py:obj}`TemporalEnvelope <abtem.transfer.TemporalEnvelope>`
  - ```{autodoc2-docstring} abtem.transfer.TemporalEnvelope
    :summary:
    ```
* - {py:obj}`SpatialEnvelope <abtem.transfer.SpatialEnvelope>`
  - ```{autodoc2-docstring} abtem.transfer.SpatialEnvelope
    :summary:
    ```
* - {py:obj}`Aberrations <abtem.transfer.Aberrations>`
  - ```{autodoc2-docstring} abtem.transfer.Aberrations
    :summary:
    ```
* - {py:obj}`CTF <abtem.transfer.CTF>`
  - ```{autodoc2-docstring} abtem.transfer.CTF
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`soft_aperture <abtem.transfer.soft_aperture>`
  - ```{autodoc2-docstring} abtem.transfer.soft_aperture
    :summary:
    ```
* - {py:obj}`hard_aperture <abtem.transfer.hard_aperture>`
  - ```{autodoc2-docstring} abtem.transfer.hard_aperture
    :summary:
    ```
* - {py:obj}`symbol_to_tex_symbol <abtem.transfer.symbol_to_tex_symbol>`
  - ```{autodoc2-docstring} abtem.transfer.symbol_to_tex_symbol
    :summary:
    ```
* - {py:obj}`nyquist_sampling <abtem.transfer.nyquist_sampling>`
  - ```{autodoc2-docstring} abtem.transfer.nyquist_sampling
    :summary:
    ```
* - {py:obj}`scherzer_defocus <abtem.transfer.scherzer_defocus>`
  - ```{autodoc2-docstring} abtem.transfer.scherzer_defocus
    :summary:
    ```
* - {py:obj}`point_resolution <abtem.transfer.point_resolution>`
  - ```{autodoc2-docstring} abtem.transfer.point_resolution
    :summary:
    ```
* - {py:obj}`polar2cartesian <abtem.transfer.polar2cartesian>`
  - ```{autodoc2-docstring} abtem.transfer.polar2cartesian
    :summary:
    ```
* - {py:obj}`cartesian2polar <abtem.transfer.cartesian2polar>`
  - ```{autodoc2-docstring} abtem.transfer.cartesian2polar
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`polar_aliases <abtem.transfer.polar_aliases>`
  - ```{autodoc2-docstring} abtem.transfer.polar_aliases
    :summary:
    ```
* - {py:obj}`polar_symbols <abtem.transfer.polar_symbols>`
  - ```{autodoc2-docstring} abtem.transfer.polar_symbols
    :summary:
    ```
````

### API

`````{py:class} BaseTransferFunction(energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, distributions: tuple[str, ...] = ())
:canonical: abtem.transfer.BaseTransferFunction

Bases: {py:obj}`abtem.transform.ReciprocalSpaceMultiplication`, {py:obj}`abtem.core.energy.HasAcceleratorMixin`, {py:obj}`abtem.core.grid.HasGrid2DMixin`

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.__init__
```

````{py:property} angular_sampling
:canonical: abtem.transfer.BaseTransferFunction.angular_sampling
:type: tuple[float, float]

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.angular_sampling
```

````

````{py:method} to_diffraction_patterns(max_angle: typing.Optional[float] = None, gpts: typing.Optional[int | tuple[int, int]] = None) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.transfer.BaseTransferFunction.to_diffraction_patterns

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.to_diffraction_patterns
```

````

````{py:method} show(max_angle: typing.Optional[float] = None, **kwargs: typing.Any) -> abtem.visualize.Visualization
:canonical: abtem.transfer.BaseTransferFunction.show

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.show
```

````

`````

`````{py:class} BaseAperture(semiangle_cutoff: float | abtem.distributions.BaseDistribution = np.inf, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, distributions: tuple[str, ...] = ())
:canonical: abtem.transfer.BaseAperture

Bases: {py:obj}`abtem.transfer.BaseTransferFunction`

```{autodoc2-docstring} abtem.transfer.BaseAperture
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.BaseAperture.__init__
```

````{py:property} metadata
:canonical: abtem.transfer.BaseAperture.metadata
:type: dict

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.BaseAperture.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} nyquist_sampling
:canonical: abtem.transfer.BaseAperture.nyquist_sampling
:type: float

```{autodoc2-docstring} abtem.transfer.BaseAperture.nyquist_sampling
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.transfer.BaseAperture.semiangle_cutoff
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.BaseAperture.semiangle_cutoff
```

````

`````

````{py:function} soft_aperture(alpha: numpy.ndarray, phi: numpy.ndarray, semiangle_cutoff: float | numpy.ndarray, angular_sampling: tuple[float, float]) -> numpy.ndarray
:canonical: abtem.transfer.soft_aperture

```{autodoc2-docstring} abtem.transfer.soft_aperture
```
````

````{py:function} hard_aperture(alpha: numpy.ndarray, semiangle_cutoff: float | abtem.distributions.BaseDistribution) -> numpy.ndarray
:canonical: abtem.transfer.hard_aperture

```{autodoc2-docstring} abtem.transfer.hard_aperture
```
````

`````{py:class} Aperture(semiangle_cutoff: float | abtem.distributions.BaseDistribution, soft: bool = True, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None)
:canonical: abtem.transfer.Aperture

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.Aperture
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Aperture.__init__
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.Aperture.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} soft
:canonical: abtem.transfer.Aperture.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.Aperture.soft
```

````

`````

`````{py:class} Bullseye(num_spokes: int, spoke_width: float, num_rings: int, ring_width: float, semiangle_cutoff: float, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, edge_softness: float = 0.0, corner_radius: float = 0.0)
:canonical: abtem.transfer.Bullseye

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.Bullseye
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Bullseye.__init__
```

````{py:property} soft
:canonical: abtem.transfer.Bullseye.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.Bullseye.soft
```

````

````{py:property} num_spokes
:canonical: abtem.transfer.Bullseye.num_spokes
:type: int

```{autodoc2-docstring} abtem.transfer.Bullseye.num_spokes
```

````

````{py:property} spoke_width
:canonical: abtem.transfer.Bullseye.spoke_width
:type: float

```{autodoc2-docstring} abtem.transfer.Bullseye.spoke_width
```

````

````{py:property} num_rings
:canonical: abtem.transfer.Bullseye.num_rings
:type: int

```{autodoc2-docstring} abtem.transfer.Bullseye.num_rings
```

````

````{py:property} ring_width
:canonical: abtem.transfer.Bullseye.ring_width
:type: float

```{autodoc2-docstring} abtem.transfer.Bullseye.ring_width
```

````

````{py:property} edge_softness
:canonical: abtem.transfer.Bullseye.edge_softness
:type: float

```{autodoc2-docstring} abtem.transfer.Bullseye.edge_softness
```

````

````{py:property} corner_radius
:canonical: abtem.transfer.Bullseye.corner_radius
:type: float

```{autodoc2-docstring} abtem.transfer.Bullseye.corner_radius
```

````

````{py:property} soft_edges
:canonical: abtem.transfer.Bullseye.soft_edges
:type: bool

```{autodoc2-docstring} abtem.transfer.Bullseye.soft_edges
```

````

`````

`````{py:class} Vortex(quantum_number: int, semiangle_cutoff: float, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, soft: bool = False)
:canonical: abtem.transfer.Vortex

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.Vortex
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Vortex.__init__
```

````{py:property} soft
:canonical: abtem.transfer.Vortex.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.Vortex.soft
```

````

````{py:property} quantum_number
:canonical: abtem.transfer.Vortex.quantum_number
:type: int

```{autodoc2-docstring} abtem.transfer.Vortex.quantum_number
```

````

`````

`````{py:class} AnnularAperture(inner_cutoff: float, semiangle_cutoff: float, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None)
:canonical: abtem.transfer.AnnularAperture

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.AnnularAperture
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.AnnularAperture.__init__
```

````{py:property} inner_cutoff
:canonical: abtem.transfer.AnnularAperture.inner_cutoff
:type: float

```{autodoc2-docstring} abtem.transfer.AnnularAperture.inner_cutoff
```

````

````{py:property} soft
:canonical: abtem.transfer.AnnularAperture.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.AnnularAperture.soft
```

````

`````

`````{py:class} Zernike(center_hole_cutoff: float, phase_shift: float, semiangle_cutoff: float, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None)
:canonical: abtem.transfer.Zernike

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.Zernike
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Zernike.__init__
```

````{py:property} center_hole_cutoff
:canonical: abtem.transfer.Zernike.center_hole_cutoff
:type: float

```{autodoc2-docstring} abtem.transfer.Zernike.center_hole_cutoff
```

````

````{py:property} soft
:canonical: abtem.transfer.Zernike.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.Zernike.soft
```

````

````{py:property} phase_shift
:canonical: abtem.transfer.Zernike.phase_shift
:type: float

```{autodoc2-docstring} abtem.transfer.Zernike.phase_shift
```

````

`````

`````{py:class} RadialPhasePlate(num_flips: int, semiangle_cutoff: float, phase_shift: float = np.pi, power_law: float = 2.0, shift_central_semiangle: float = 0.0, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None)
:canonical: abtem.transfer.RadialPhasePlate

Bases: {py:obj}`abtem.transfer.BaseAperture`

````{py:property} soft
:canonical: abtem.transfer.RadialPhasePlate.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.soft
```

````

````{py:property} num_flips
:canonical: abtem.transfer.RadialPhasePlate.num_flips
:type: int

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.num_flips
```

````

````{py:property} phase_shift
:canonical: abtem.transfer.RadialPhasePlate.phase_shift
:type: float

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.phase_shift
```

````

````{py:property} power_law
:canonical: abtem.transfer.RadialPhasePlate.power_law
:type: float

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.power_law
```

````

````{py:property} shift_central_semiangle
:canonical: abtem.transfer.RadialPhasePlate.shift_central_semiangle
:type: float

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.shift_central_semiangle
```

````

`````

`````{py:class} TemporalEnvelope(focal_spread: float | abtem.distributions.BaseDistribution, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None)
:canonical: abtem.transfer.TemporalEnvelope

Bases: {py:obj}`abtem.transfer.BaseTransferFunction`

```{autodoc2-docstring} abtem.transfer.TemporalEnvelope
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.TemporalEnvelope.__init__
```

````{py:property} focal_spread
:canonical: abtem.transfer.TemporalEnvelope.focal_spread
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.TemporalEnvelope.focal_spread
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.TemporalEnvelope.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

`````

````{py:function} symbol_to_tex_symbol(symbol: str) -> str
:canonical: abtem.transfer.symbol_to_tex_symbol

```{autodoc2-docstring} abtem.transfer.symbol_to_tex_symbol
```
````

````{py:data} polar_aliases
:canonical: abtem.transfer.polar_aliases
:value: >
   None

```{autodoc2-docstring} abtem.transfer.polar_aliases
```

````

````{py:data} polar_symbols
:canonical: abtem.transfer.polar_symbols
:value: >
   None

```{autodoc2-docstring} abtem.transfer.polar_symbols
```

````

`````{py:class} SpatialEnvelope(angular_spread: float | abtem.distributions.BaseDistribution, aberration_coefficients: typing.Optional[typing.Mapping[str, str | float | abtem.distributions.BaseDistribution]] = None, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, **kwargs: str | float | abtem.distributions.BaseDistribution)
:canonical: abtem.transfer.SpatialEnvelope

Bases: {py:obj}`abtem.transfer.BaseTransferFunction`, {py:obj}`abtem.transfer._HasAberrations`

```{autodoc2-docstring} abtem.transfer.SpatialEnvelope
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.SpatialEnvelope.__init__
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.SpatialEnvelope.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} angular_spread
:canonical: abtem.transfer.SpatialEnvelope.angular_spread
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.SpatialEnvelope.angular_spread
```

````

`````

`````{py:class} Aberrations(aberration_coefficients: typing.Optional[typing.Mapping[str, str | float | abtem.distributions.BaseDistribution]] = None, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, **kwargs: typing.Any)
:canonical: abtem.transfer.Aberrations

Bases: {py:obj}`abtem.transfer.BaseTransferFunction`, {py:obj}`abtem.transfer._HasAberrations`

```{autodoc2-docstring} abtem.transfer.Aberrations
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Aberrations.__init__
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.Aberrations.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} defocus
:canonical: abtem.transfer.Aberrations.defocus
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.Aberrations.defocus
```

````

`````

`````{py:class} CTF(semiangle_cutoff: float | abtem.distributions.BaseDistribution = np.inf, soft: bool = True, focal_spread: float | abtem.distributions.BaseDistribution = 0.0, angular_spread: float | abtem.distributions.BaseDistribution = 0.0, aberration_coefficients: typing.Optional[typing.Mapping[str, float | abtem.distributions.BaseDistribution]] = None, energy: typing.Optional[float] = None, extent: typing.Optional[float | tuple[float, float]] = None, gpts: typing.Optional[int | tuple[int, int]] = None, sampling: typing.Optional[float | tuple[float, float]] = None, flip_phase: bool = False, wiener_snr: float = 0.0, **kwargs: typing.Any)
:canonical: abtem.transfer.CTF

Bases: {py:obj}`abtem.transfer._HasAberrations`, {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.CTF
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.CTF.__init__
```

````{py:property} scherzer_defocus
:canonical: abtem.transfer.CTF.scherzer_defocus
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.scherzer_defocus
```

````

````{py:property} crossover_angle
:canonical: abtem.transfer.CTF.crossover_angle
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.crossover_angle
```

````

````{py:property} point_resolution
:canonical: abtem.transfer.CTF.point_resolution
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.point_resolution
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.CTF.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} soft
:canonical: abtem.transfer.CTF.soft
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.soft
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.transfer.CTF.semiangle_cutoff
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.CTF.semiangle_cutoff
```

````

````{py:property} focal_spread
:canonical: abtem.transfer.CTF.focal_spread
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.CTF.focal_spread
```

````

````{py:property} angular_spread
:canonical: abtem.transfer.CTF.angular_spread
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.CTF.angular_spread
```

````

````{py:property} flip_phase
:canonical: abtem.transfer.CTF.flip_phase
:type: bool

```{autodoc2-docstring} abtem.transfer.CTF.flip_phase
```

````

````{py:property} wiener_snr
:canonical: abtem.transfer.CTF.wiener_snr
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.wiener_snr
```

````

````{py:method} to_point_spread_functions(gpts: int | tuple[int, int], extent: float | tuple[float, float]) -> abtem.measurements.Images
:canonical: abtem.transfer.CTF.to_point_spread_functions

```{autodoc2-docstring} abtem.transfer.CTF.to_point_spread_functions
```

````

````{py:method} profiles(gpts: int = 1000, max_angle: typing.Optional[float] = None, phi: float | numpy.ndarray = 0.0) -> abtem.measurements.ReciprocalSpaceLineProfiles
:canonical: abtem.transfer.CTF.profiles

```{autodoc2-docstring} abtem.transfer.CTF.profiles
```

````

`````

````{py:function} nyquist_sampling(semiangle_cutoff: float, energy: float) -> float
:canonical: abtem.transfer.nyquist_sampling

```{autodoc2-docstring} abtem.transfer.nyquist_sampling
```
````

````{py:function} scherzer_defocus(Cs: float, energy: float) -> float
:canonical: abtem.transfer.scherzer_defocus

```{autodoc2-docstring} abtem.transfer.scherzer_defocus
```
````

````{py:function} point_resolution(Cs: float, energy: float) -> float
:canonical: abtem.transfer.point_resolution

```{autodoc2-docstring} abtem.transfer.point_resolution
```
````

````{py:function} polar2cartesian(polar: dict) -> dict
:canonical: abtem.transfer.polar2cartesian

```{autodoc2-docstring} abtem.transfer.polar2cartesian
```
````

````{py:function} cartesian2polar(cartesian: dict) -> dict
:canonical: abtem.transfer.cartesian2polar

```{autodoc2-docstring} abtem.transfer.cartesian2polar
```
````
