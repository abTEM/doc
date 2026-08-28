# {py:mod}`abtem.transfer`

```{py:module} abtem.transfer
```

```{autodoc2-docstring} abtem.transfer
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`Aberrations <abtem.transfer.Aberrations>`
  - ```{autodoc2-docstring} abtem.transfer.Aberrations
    :parser: rst
    :summary:
    ```
* - {py:obj}`AnnularAperture <abtem.transfer.AnnularAperture>`
  - ```{autodoc2-docstring} abtem.transfer.AnnularAperture
    :parser: rst
    :summary:
    ```
* - {py:obj}`Aperture <abtem.transfer.Aperture>`
  - ```{autodoc2-docstring} abtem.transfer.Aperture
    :parser: rst
    :summary:
    ```
* - {py:obj}`BaseAperture <abtem.transfer.BaseAperture>`
  - ```{autodoc2-docstring} abtem.transfer.BaseAperture
    :parser: rst
    :summary:
    ```
* - {py:obj}`BaseTransferFunction <abtem.transfer.BaseTransferFunction>`
  - ```{autodoc2-docstring} abtem.transfer.BaseTransferFunction
    :parser: rst
    :summary:
    ```
* - {py:obj}`Bullseye <abtem.transfer.Bullseye>`
  - ```{autodoc2-docstring} abtem.transfer.Bullseye
    :parser: rst
    :summary:
    ```
* - {py:obj}`CTF <abtem.transfer.CTF>`
  - ```{autodoc2-docstring} abtem.transfer.CTF
    :parser: rst
    :summary:
    ```
* - {py:obj}`RadialPhasePlate <abtem.transfer.RadialPhasePlate>`
  -
* - {py:obj}`SpatialEnvelope <abtem.transfer.SpatialEnvelope>`
  - ```{autodoc2-docstring} abtem.transfer.SpatialEnvelope
    :parser: rst
    :summary:
    ```
* - {py:obj}`TemporalEnvelope <abtem.transfer.TemporalEnvelope>`
  - ```{autodoc2-docstring} abtem.transfer.TemporalEnvelope
    :parser: rst
    :summary:
    ```
* - {py:obj}`Vortex <abtem.transfer.Vortex>`
  - ```{autodoc2-docstring} abtem.transfer.Vortex
    :parser: rst
    :summary:
    ```
* - {py:obj}`Zernike <abtem.transfer.Zernike>`
  - ```{autodoc2-docstring} abtem.transfer.Zernike
    :parser: rst
    :summary:
    ```
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`cartesian2polar <abtem.transfer.cartesian2polar>`
  - ```{autodoc2-docstring} abtem.transfer.cartesian2polar
    :parser: rst
    :summary:
    ```
* - {py:obj}`hard_aperture <abtem.transfer.hard_aperture>`
  - ```{autodoc2-docstring} abtem.transfer.hard_aperture
    :parser: rst
    :summary:
    ```
* - {py:obj}`nyquist_sampling <abtem.transfer.nyquist_sampling>`
  - ```{autodoc2-docstring} abtem.transfer.nyquist_sampling
    :parser: rst
    :summary:
    ```
* - {py:obj}`point_resolution <abtem.transfer.point_resolution>`
  - ```{autodoc2-docstring} abtem.transfer.point_resolution
    :parser: rst
    :summary:
    ```
* - {py:obj}`polar2cartesian <abtem.transfer.polar2cartesian>`
  - ```{autodoc2-docstring} abtem.transfer.polar2cartesian
    :parser: rst
    :summary:
    ```
* - {py:obj}`scherzer_defocus <abtem.transfer.scherzer_defocus>`
  - ```{autodoc2-docstring} abtem.transfer.scherzer_defocus
    :parser: rst
    :summary:
    ```
* - {py:obj}`soft_aperture <abtem.transfer.soft_aperture>`
  - ```{autodoc2-docstring} abtem.transfer.soft_aperture
    :parser: rst
    :summary:
    ```
* - {py:obj}`symbol_to_tex_symbol <abtem.transfer.symbol_to_tex_symbol>`
  - ```{autodoc2-docstring} abtem.transfer.symbol_to_tex_symbol
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`polar_aliases <abtem.transfer.polar_aliases>`
  - ```{autodoc2-docstring} abtem.transfer.polar_aliases
    :parser: rst
    :summary:
    ```
* - {py:obj}`polar_symbols <abtem.transfer.polar_symbols>`
  - ```{autodoc2-docstring} abtem.transfer.polar_symbols
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} Aberrations(...)
:canonical: abtem.transfer.Aberrations

Bases: {py:obj}`abtem.transfer.BaseTransferFunction`, {py:obj}`abtem.transfer._HasAberrations`

```{autodoc2-docstring} abtem.transfer.Aberrations
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Aberrations.__init__
:parser: rst
```

````{py:property} defocus
:canonical: abtem.transfer.Aberrations.defocus
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.Aberrations.defocus
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.Aberrations.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

`````

`````{py:class} AnnularAperture(...)
:canonical: abtem.transfer.AnnularAperture

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.AnnularAperture
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.AnnularAperture.__init__
:parser: rst
```

````{py:property} inner_cutoff
:canonical: abtem.transfer.AnnularAperture.inner_cutoff
:type: float

```{autodoc2-docstring} abtem.transfer.AnnularAperture.inner_cutoff
:parser: rst
```

````

````{py:property} soft
:canonical: abtem.transfer.AnnularAperture.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.AnnularAperture.soft
:parser: rst
```

````

`````

`````{py:class} Aperture(...)
:canonical: abtem.transfer.Aperture

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.Aperture
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Aperture.__init__
:parser: rst
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.Aperture.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} soft
:canonical: abtem.transfer.Aperture.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.Aperture.soft
:parser: rst
```

````

`````

`````{py:class} BaseAperture(...)
:canonical: abtem.transfer.BaseAperture

Bases: {py:obj}`abtem.transfer.BaseTransferFunction`

```{autodoc2-docstring} abtem.transfer.BaseAperture
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.BaseAperture.__init__
:parser: rst
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.BaseAperture.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} metadata
:canonical: abtem.transfer.BaseAperture.metadata
:type: dict

````

````{py:property} nyquist_sampling
:canonical: abtem.transfer.BaseAperture.nyquist_sampling
:type: float

```{autodoc2-docstring} abtem.transfer.BaseAperture.nyquist_sampling
:parser: rst
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.transfer.BaseAperture.semiangle_cutoff
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.BaseAperture.semiangle_cutoff
:parser: rst
```

````

`````

`````{py:class} BaseTransferFunction(...)
:canonical: abtem.transfer.BaseTransferFunction

Bases: {py:obj}`abtem.transform.ReciprocalSpaceMultiplication`, {py:obj}`abtem.core.energy.HasAcceleratorMixin`, {py:obj}`abtem.core.grid.HasGrid2DMixin`

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.__init__
:parser: rst
```

````{py:property} angular_sampling
:canonical: abtem.transfer.BaseTransferFunction.angular_sampling
:type: tuple[float, float]

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.angular_sampling
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.transfer.BaseTransferFunction.energy
:type: float | abtem.distributions.BaseDistribution | None

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.energy
:parser: rst
```

````

````{py:method} show(...) -> abtem.visualize.Visualization
:canonical: abtem.transfer.BaseTransferFunction.show

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.show
:parser: rst
```

````

````{py:method} to_diffraction_patterns(...) -> abtem.measurements.DiffractionPatterns
:canonical: abtem.transfer.BaseTransferFunction.to_diffraction_patterns

```{autodoc2-docstring} abtem.transfer.BaseTransferFunction.to_diffraction_patterns
:parser: rst
```

````

`````

`````{py:class} Bullseye(...)
:canonical: abtem.transfer.Bullseye

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.Bullseye
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Bullseye.__init__
:parser: rst
```

````{py:property} corner_radius
:canonical: abtem.transfer.Bullseye.corner_radius
:type: float

```{autodoc2-docstring} abtem.transfer.Bullseye.corner_radius
:parser: rst
```

````

````{py:property} edge_softness
:canonical: abtem.transfer.Bullseye.edge_softness
:type: float

```{autodoc2-docstring} abtem.transfer.Bullseye.edge_softness
:parser: rst
```

````

````{py:property} num_rings
:canonical: abtem.transfer.Bullseye.num_rings
:type: int

```{autodoc2-docstring} abtem.transfer.Bullseye.num_rings
:parser: rst
```

````

````{py:property} num_spokes
:canonical: abtem.transfer.Bullseye.num_spokes
:type: int

```{autodoc2-docstring} abtem.transfer.Bullseye.num_spokes
:parser: rst
```

````

````{py:property} ring_width
:canonical: abtem.transfer.Bullseye.ring_width
:type: float

```{autodoc2-docstring} abtem.transfer.Bullseye.ring_width
:parser: rst
```

````

````{py:property} soft
:canonical: abtem.transfer.Bullseye.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.Bullseye.soft
:parser: rst
```

````

````{py:property} soft_edges
:canonical: abtem.transfer.Bullseye.soft_edges
:type: bool

```{autodoc2-docstring} abtem.transfer.Bullseye.soft_edges
:parser: rst
```

````

````{py:property} spoke_width
:canonical: abtem.transfer.Bullseye.spoke_width
:type: float

```{autodoc2-docstring} abtem.transfer.Bullseye.spoke_width
:parser: rst
```

````

`````

`````{py:class} CTF(...)
:canonical: abtem.transfer.CTF

Bases: {py:obj}`abtem.transfer._HasAberrations`, {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.CTF
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.CTF.__init__
:parser: rst
```

````{py:property} angular_spread
:canonical: abtem.transfer.CTF.angular_spread
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.CTF.angular_spread
:parser: rst
```

````

````{py:property} crossover_angle
:canonical: abtem.transfer.CTF.crossover_angle
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.crossover_angle
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.CTF.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} flip_phase
:canonical: abtem.transfer.CTF.flip_phase
:type: bool

```{autodoc2-docstring} abtem.transfer.CTF.flip_phase
:parser: rst
```

````

````{py:property} focal_spread
:canonical: abtem.transfer.CTF.focal_spread
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.CTF.focal_spread
:parser: rst
```

````

````{py:property} point_resolution
:canonical: abtem.transfer.CTF.point_resolution
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.point_resolution
:parser: rst
```

````

````{py:method} profiles(...) -> abtem.measurements.ReciprocalSpaceLineProfiles
:canonical: abtem.transfer.CTF.profiles

```{autodoc2-docstring} abtem.transfer.CTF.profiles
:parser: rst
```

````

````{py:property} scherzer_defocus
:canonical: abtem.transfer.CTF.scherzer_defocus
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.scherzer_defocus
:parser: rst
```

````

````{py:property} semiangle_cutoff
:canonical: abtem.transfer.CTF.semiangle_cutoff
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.CTF.semiangle_cutoff
:parser: rst
```

````

````{py:property} soft
:canonical: abtem.transfer.CTF.soft
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.soft
:parser: rst
```

````

````{py:method} to_point_spread_functions(...) -> abtem.measurements.Images
:canonical: abtem.transfer.CTF.to_point_spread_functions

```{autodoc2-docstring} abtem.transfer.CTF.to_point_spread_functions
:parser: rst
```

````

````{py:property} wiener_snr
:canonical: abtem.transfer.CTF.wiener_snr
:type: float

```{autodoc2-docstring} abtem.transfer.CTF.wiener_snr
:parser: rst
```

````

`````

`````{py:class} RadialPhasePlate(...)
:canonical: abtem.transfer.RadialPhasePlate

Bases: {py:obj}`abtem.transfer.BaseAperture`

````{py:property} num_flips
:canonical: abtem.transfer.RadialPhasePlate.num_flips
:type: int

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.num_flips
:parser: rst
```

````

````{py:property} phase_shift
:canonical: abtem.transfer.RadialPhasePlate.phase_shift
:type: float

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.phase_shift
:parser: rst
```

````

````{py:property} power_law
:canonical: abtem.transfer.RadialPhasePlate.power_law
:type: float

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.power_law
:parser: rst
```

````

````{py:property} shift_central_semiangle
:canonical: abtem.transfer.RadialPhasePlate.shift_central_semiangle
:type: float

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.shift_central_semiangle
:parser: rst
```

````

````{py:property} soft
:canonical: abtem.transfer.RadialPhasePlate.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.RadialPhasePlate.soft
:parser: rst
```

````

`````

`````{py:class} SpatialEnvelope(...)
:canonical: abtem.transfer.SpatialEnvelope

Bases: {py:obj}`abtem.transfer.BaseTransferFunction`, {py:obj}`abtem.transfer._HasAberrations`

```{autodoc2-docstring} abtem.transfer.SpatialEnvelope
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.SpatialEnvelope.__init__
:parser: rst
```

````{py:property} angular_spread
:canonical: abtem.transfer.SpatialEnvelope.angular_spread
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.SpatialEnvelope.angular_spread
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.SpatialEnvelope.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

`````

`````{py:class} TemporalEnvelope(...)
:canonical: abtem.transfer.TemporalEnvelope

Bases: {py:obj}`abtem.transfer.BaseTransferFunction`

```{autodoc2-docstring} abtem.transfer.TemporalEnvelope
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.TemporalEnvelope.__init__
:parser: rst
```

````{py:property} ensemble_axes_metadata
:canonical: abtem.transfer.TemporalEnvelope.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

````

````{py:property} focal_spread
:canonical: abtem.transfer.TemporalEnvelope.focal_spread
:type: float | abtem.distributions.BaseDistribution

```{autodoc2-docstring} abtem.transfer.TemporalEnvelope.focal_spread
:parser: rst
```

````

`````

`````{py:class} Vortex(...)
:canonical: abtem.transfer.Vortex

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.Vortex
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Vortex.__init__
:parser: rst
```

````{py:property} quantum_number
:canonical: abtem.transfer.Vortex.quantum_number
:type: int

```{autodoc2-docstring} abtem.transfer.Vortex.quantum_number
:parser: rst
```

````

````{py:property} soft
:canonical: abtem.transfer.Vortex.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.Vortex.soft
:parser: rst
```

````

`````

`````{py:class} Zernike(...)
:canonical: abtem.transfer.Zernike

Bases: {py:obj}`abtem.transfer.BaseAperture`

```{autodoc2-docstring} abtem.transfer.Zernike
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.transfer.Zernike.__init__
:parser: rst
```

````{py:property} center_hole_cutoff
:canonical: abtem.transfer.Zernike.center_hole_cutoff
:type: float

```{autodoc2-docstring} abtem.transfer.Zernike.center_hole_cutoff
:parser: rst
```

````

````{py:property} phase_shift
:canonical: abtem.transfer.Zernike.phase_shift
:type: float

```{autodoc2-docstring} abtem.transfer.Zernike.phase_shift
:parser: rst
```

````

````{py:property} soft
:canonical: abtem.transfer.Zernike.soft
:type: bool

```{autodoc2-docstring} abtem.transfer.Zernike.soft
:parser: rst
```

````

`````

````{py:function} cartesian2polar(...) -> dict
:canonical: abtem.transfer.cartesian2polar

```{autodoc2-docstring} abtem.transfer.cartesian2polar
:parser: rst
```
````

````{py:function} hard_aperture(...) -> numpy.ndarray
:canonical: abtem.transfer.hard_aperture

```{autodoc2-docstring} abtem.transfer.hard_aperture
:parser: rst
```
````

````{py:function} nyquist_sampling(...) -> float
:canonical: abtem.transfer.nyquist_sampling

```{autodoc2-docstring} abtem.transfer.nyquist_sampling
:parser: rst
```
````

````{py:function} point_resolution(...) -> float
:canonical: abtem.transfer.point_resolution

```{autodoc2-docstring} abtem.transfer.point_resolution
:parser: rst
```
````

````{py:function} polar2cartesian(...) -> dict
:canonical: abtem.transfer.polar2cartesian

```{autodoc2-docstring} abtem.transfer.polar2cartesian
:parser: rst
```
````

````{py:data} polar_aliases
:canonical: abtem.transfer.polar_aliases
:value: >
   None

```{autodoc2-docstring} abtem.transfer.polar_aliases
:parser: rst
```

````

````{py:data} polar_symbols
:canonical: abtem.transfer.polar_symbols
:value: >
   None

```{autodoc2-docstring} abtem.transfer.polar_symbols
:parser: rst
```

````

````{py:function} scherzer_defocus(...) -> float
:canonical: abtem.transfer.scherzer_defocus

```{autodoc2-docstring} abtem.transfer.scherzer_defocus
:parser: rst
```
````

````{py:function} soft_aperture(...) -> numpy.ndarray
:canonical: abtem.transfer.soft_aperture

```{autodoc2-docstring} abtem.transfer.soft_aperture
:parser: rst
```
````

````{py:function} symbol_to_tex_symbol(...) -> str
:canonical: abtem.transfer.symbol_to_tex_symbol

```{autodoc2-docstring} abtem.transfer.symbol_to_tex_symbol
:parser: rst
```
````
