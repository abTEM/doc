# {py:mod}`abtem.inelastic.core_loss`

```{py:module} abtem.inelastic.core_loss
```

```{autodoc2-docstring} abtem.inelastic.core_loss
:parser: rst
:allowtitles:
```

## Module Contents

### Classes

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`AtomicWaveFunction <abtem.inelastic.core_loss.AtomicWaveFunction>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction
    :parser: rst
    :summary:
    ```
* - {py:obj}`BaseTransitionCollection <abtem.inelastic.core_loss.BaseTransitionCollection>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.BaseTransitionCollection
    :parser: rst
    :summary:
    ```
* - {py:obj}`BaseTransitionPotential <abtem.inelastic.core_loss.BaseTransitionPotential>`
  -
* - {py:obj}`RadialWavefunction <abtem.inelastic.core_loss.RadialWavefunction>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction
    :parser: rst
    :summary:
    ```
* - {py:obj}`SubshellTransitions <abtem.inelastic.core_loss.SubshellTransitions>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions
    :parser: rst
    :summary:
    ```
* - {py:obj}`TransitionPotential <abtem.inelastic.core_loss.TransitionPotential>`
  -
* - {py:obj}`TransitionPotentialArray <abtem.inelastic.core_loss.TransitionPotentialArray>`
  -
````

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`calculate_bound_radial_wavefunction <abtem.inelastic.core_loss.calculate_bound_radial_wavefunction>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.calculate_bound_radial_wavefunction
    :parser: rst
    :summary:
    ```
* - {py:obj}`calculate_continuum_radial_wavefunction <abtem.inelastic.core_loss.calculate_continuum_radial_wavefunction>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.calculate_continuum_radial_wavefunction
    :parser: rst
    :summary:
    ```
* - {py:obj}`check_valid_quantum_number <abtem.inelastic.core_loss.check_valid_quantum_number>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.check_valid_quantum_number
    :parser: rst
    :summary:
    ```
* - {py:obj}`config_str_to_config_tuples <abtem.inelastic.core_loss.config_str_to_config_tuples>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.config_str_to_config_tuples
    :parser: rst
    :summary:
    ```
* - {py:obj}`config_tuples_to_config_str <abtem.inelastic.core_loss.config_tuples_to_config_str>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.config_tuples_to_config_str
    :parser: rst
    :summary:
    ```
* - {py:obj}`fast_roll <abtem.inelastic.core_loss.fast_roll>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.fast_roll
    :parser: rst
    :summary:
    ```
* - {py:obj}`numerov <abtem.inelastic.core_loss.numerov>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.numerov
    :parser: rst
    :summary:
    ```
* - {py:obj}`prism_transition_potential_scan <abtem.inelastic.core_loss.prism_transition_potential_scan>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.prism_transition_potential_scan
    :parser: rst
    :summary:
    ```
* - {py:obj}`prism_transition_potential_scan_beam_basis <abtem.inelastic.core_loss.prism_transition_potential_scan_beam_basis>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.prism_transition_potential_scan_beam_basis
    :parser: rst
    :summary:
    ```
* - {py:obj}`radial_schroedinger_equation <abtem.inelastic.core_loss.radial_schroedinger_equation>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.radial_schroedinger_equation
    :parser: rst
    :summary:
    ```
* - {py:obj}`remove_electron_from_config_str <abtem.inelastic.core_loss.remove_electron_from_config_str>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.remove_electron_from_config_str
    :parser: rst
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`azimuthal_letter <abtem.inelastic.core_loss.azimuthal_letter>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.azimuthal_letter
    :parser: rst
    :summary:
    ```
* - {py:obj}`azimuthal_number <abtem.inelastic.core_loss.azimuthal_number>`
  - ```{autodoc2-docstring} abtem.inelastic.core_loss.azimuthal_number
    :parser: rst
    :summary:
    ```
````

### API

`````{py:class} AtomicWaveFunction(...)
:canonical: abtem.inelastic.core_loss.AtomicWaveFunction

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction.__init__
:parser: rst
```

````{py:property} bound
:canonical: abtem.inelastic.core_loss.AtomicWaveFunction.bound

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction.bound
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.inelastic.core_loss.AtomicWaveFunction.energy

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction.energy
:parser: rst
```

````

````{py:property} l
:canonical: abtem.inelastic.core_loss.AtomicWaveFunction.l

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction.l
:parser: rst
```

````

````{py:property} ml
:canonical: abtem.inelastic.core_loss.AtomicWaveFunction.ml

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction.ml
:parser: rst
```

````

````{py:property} n
:canonical: abtem.inelastic.core_loss.AtomicWaveFunction.n

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction.n
:parser: rst
```

````

````{py:property} quantum_numbers
:canonical: abtem.inelastic.core_loss.AtomicWaveFunction.quantum_numbers

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction.quantum_numbers
:parser: rst
```

````

````{py:property} radial_grid
:canonical: abtem.inelastic.core_loss.AtomicWaveFunction.radial_grid

```{autodoc2-docstring} abtem.inelastic.core_loss.AtomicWaveFunction.radial_grid
:parser: rst
```

````

`````

`````{py:class} BaseTransitionCollection(...)
:canonical: abtem.inelastic.core_loss.BaseTransitionCollection

```{autodoc2-docstring} abtem.inelastic.core_loss.BaseTransitionCollection
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.core_loss.BaseTransitionCollection.__init__
:parser: rst
```

````{py:property} Z
:canonical: abtem.inelastic.core_loss.BaseTransitionCollection.Z

```{autodoc2-docstring} abtem.inelastic.core_loss.BaseTransitionCollection.Z
:parser: rst
```

````

````{py:method} get_transition_potential()
:canonical: abtem.inelastic.core_loss.BaseTransitionCollection.get_transition_potential
:abstractmethod:

```{autodoc2-docstring} abtem.inelastic.core_loss.BaseTransitionCollection.get_transition_potential
:parser: rst
```

````

`````

`````{py:class} BaseTransitionPotential(...)
:canonical: abtem.inelastic.core_loss.BaseTransitionPotential

Bases: {py:obj}`abtem.core.energy.HasAcceleratorMixin`, {py:obj}`abtem.core.grid.HasGrid2DMixin`, {py:obj}`abtem.core.utils.CopyMixin`

````{py:property} Z
:canonical: abtem.inelastic.core_loss.BaseTransitionPotential.Z
:type: int

```{autodoc2-docstring} abtem.inelastic.core_loss.BaseTransitionPotential.Z
:parser: rst
```

````

````{py:property} double_channel
:canonical: abtem.inelastic.core_loss.BaseTransitionPotential.double_channel
:type: bool

```{autodoc2-docstring} abtem.inelastic.core_loss.BaseTransitionPotential.double_channel
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.inelastic.core_loss.BaseTransitionPotential.metadata
:abstractmethod:
:type: dict

```{autodoc2-docstring} abtem.inelastic.core_loss.BaseTransitionPotential.metadata
:parser: rst
```

````

`````

`````{py:class} RadialWavefunction(...)
:canonical: abtem.inelastic.core_loss.RadialWavefunction

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction.__init__
:parser: rst
```

````{py:property} bound
:canonical: abtem.inelastic.core_loss.RadialWavefunction.bound

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction.bound
:parser: rst
```

````

````{py:property} energy
:canonical: abtem.inelastic.core_loss.RadialWavefunction.energy

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction.energy
:parser: rst
```

````

````{py:property} l
:canonical: abtem.inelastic.core_loss.RadialWavefunction.l

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction.l
:parser: rst
```

````

````{py:property} n
:canonical: abtem.inelastic.core_loss.RadialWavefunction.n

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction.n
:parser: rst
```

````

````{py:property} radial_grid
:canonical: abtem.inelastic.core_loss.RadialWavefunction.radial_grid

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction.radial_grid
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.inelastic.core_loss.RadialWavefunction.show

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction.show
:parser: rst
```

````

````{py:method} to_lineprofiles(...)
:canonical: abtem.inelastic.core_loss.RadialWavefunction.to_lineprofiles

```{autodoc2-docstring} abtem.inelastic.core_loss.RadialWavefunction.to_lineprofiles
:parser: rst
```

````

`````

`````{py:class} SubshellTransitions(...)
:canonical: abtem.inelastic.core_loss.SubshellTransitions

Bases: {py:obj}`abtem.inelastic.core_loss.BaseTransitionCollection`

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions
:parser: rst
```

```{rubric} Initialization
```

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.__init__
:parser: rst
```

````{py:property} bound_configuration
:canonical: abtem.inelastic.core_loss.SubshellTransitions.bound_configuration

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.bound_configuration
:parser: rst
```

````

````{py:property} epsilon
:canonical: abtem.inelastic.core_loss.SubshellTransitions.epsilon

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.epsilon
:parser: rst
```

````

````{py:property} excited_configuration
:canonical: abtem.inelastic.core_loss.SubshellTransitions.excited_configuration

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.excited_configuration
:parser: rst
```

````

````{py:method} get_bound_wave_function()
:canonical: abtem.inelastic.core_loss.SubshellTransitions.get_bound_wave_function

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.get_bound_wave_function
:parser: rst
```

````

````{py:method} get_excited_wave_functions()
:canonical: abtem.inelastic.core_loss.SubshellTransitions.get_excited_wave_functions

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.get_excited_wave_functions
:parser: rst
```

````

````{py:method} get_transition_potentials(...)
:canonical: abtem.inelastic.core_loss.SubshellTransitions.get_transition_potentials

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.get_transition_potentials
:parser: rst
```

````

````{py:method} get_transition_quantum_numbers()
:canonical: abtem.inelastic.core_loss.SubshellTransitions.get_transition_quantum_numbers

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.get_transition_quantum_numbers
:parser: rst
```

````

````{py:method} get_transitions()
:canonical: abtem.inelastic.core_loss.SubshellTransitions.get_transitions

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.get_transitions
:parser: rst
```

````

````{py:property} l
:canonical: abtem.inelastic.core_loss.SubshellTransitions.l

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.l
:parser: rst
```

````

````{py:property} lprimes
:canonical: abtem.inelastic.core_loss.SubshellTransitions.lprimes

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.lprimes
:parser: rst
```

````

````{py:property} min_contrast
:canonical: abtem.inelastic.core_loss.SubshellTransitions.min_contrast

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.min_contrast
:parser: rst
```

````

````{py:property} n
:canonical: abtem.inelastic.core_loss.SubshellTransitions.n

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.n
:parser: rst
```

````

````{py:property} order
:canonical: abtem.inelastic.core_loss.SubshellTransitions.order

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.order
:parser: rst
```

````

````{py:property} xc
:canonical: abtem.inelastic.core_loss.SubshellTransitions.xc

```{autodoc2-docstring} abtem.inelastic.core_loss.SubshellTransitions.xc
:parser: rst
```

````

`````

`````{py:class} TransitionPotential(...)
:canonical: abtem.inelastic.core_loss.TransitionPotential

Bases: {py:obj}`abtem.inelastic.core_loss.BaseTransitionPotential`

````{py:property} Z
:canonical: abtem.inelastic.core_loss.TransitionPotential.Z
:type: int

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.Z
:parser: rst
```

````

````{py:method} build() -> abtem.inelastic.core_loss.TransitionPotentialArray
:canonical: abtem.inelastic.core_loss.TransitionPotential.build

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.build
:parser: rst
```

````

````{py:property} double_channel
:canonical: abtem.inelastic.core_loss.TransitionPotential.double_channel
:type: bool

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.double_channel
:parser: rst
```

````

````{py:property} ensemble_axes_metadata
:canonical: abtem.inelastic.core_loss.TransitionPotential.ensemble_axes_metadata
:type: list[abtem.core.axes.AxisMetadata]

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.ensemble_axes_metadata
:parser: rst
```

````

````{py:property} ensemble_shape
:canonical: abtem.inelastic.core_loss.TransitionPotential.ensemble_shape
:type: tuple[int]

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.ensemble_shape
:parser: rst
```

````

````{py:method} filter_by_intensity(...) -> abtem.inelastic.core_loss.TransitionPotential
:canonical: abtem.inelastic.core_loss.TransitionPotential.filter_by_intensity

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.filter_by_intensity
:parser: rst
```

````

````{py:method} integrated_intensities()
:canonical: abtem.inelastic.core_loss.TransitionPotential.integrated_intensities

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.integrated_intensities
:parser: rst
```

````

````{py:property} metadata
:canonical: abtem.inelastic.core_loss.TransitionPotential.metadata
:type: dict

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.metadata
:parser: rst
```

````

````{py:property} orbital_filling_factor
:canonical: abtem.inelastic.core_loss.TransitionPotential.orbital_filling_factor
:type: bool

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.orbital_filling_factor
:parser: rst
```

````

````{py:method} scatter(...) -> abtem.waves.Waves
:canonical: abtem.inelastic.core_loss.TransitionPotential.scatter

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.scatter
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.inelastic.core_loss.TransitionPotential.show

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.show
:parser: rst
```

````

````{py:property} transition_quantum_numbers
:canonical: abtem.inelastic.core_loss.TransitionPotential.transition_quantum_numbers

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.transition_quantum_numbers
:parser: rst
```

````

````{py:property} transitions
:canonical: abtem.inelastic.core_loss.TransitionPotential.transitions

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotential.transitions
:parser: rst
```

````

`````

`````{py:class} TransitionPotentialArray(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray

Bases: {py:obj}`abtem.array.ArrayObject`, {py:obj}`abtem.inelastic.core_loss.BaseTransitionPotential`

````{py:method} absolute_threshold(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.absolute_threshold

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.absolute_threshold
:parser: rst
```

````

````{py:method} filter_by_intensity(...) -> abtem.inelastic.core_loss.TransitionPotential
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.filter_by_intensity

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.filter_by_intensity
:parser: rst
```

````

````{py:method} filter_sites(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.filter_sites

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.filter_sites
:parser: rst
```

````

````{py:method} from_array_and_metadata(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.from_array_and_metadata
:abstractmethod:

````

````{py:method} generate_scattered_waves(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.generate_scattered_waves

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.generate_scattered_waves
:parser: rst
```

````

````{py:method} integrated_intensities(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.integrated_intensities

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.integrated_intensities
:parser: rst
```

````

````{py:method} local_potential(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.local_potential

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.local_potential
:parser: rst
```

````

````{py:method} scatter(...) -> abtem.waves.Waves
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.scatter

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.scatter
:parser: rst
```

````

````{py:method} set_threshold(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.set_threshold

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.set_threshold
:parser: rst
```

````

````{py:method} show(...)
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.show

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.show
:parser: rst
```

````

````{py:method} to_images()
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.to_images

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.to_images
:parser: rst
```

````

````{py:method} validate_sites(...) -> numpy.ndarray
:canonical: abtem.inelastic.core_loss.TransitionPotentialArray.validate_sites

```{autodoc2-docstring} abtem.inelastic.core_loss.TransitionPotentialArray.validate_sites
:parser: rst
```

````

`````

````{py:data} azimuthal_letter
:canonical: abtem.inelastic.core_loss.azimuthal_letter
:value: >
   None

```{autodoc2-docstring} abtem.inelastic.core_loss.azimuthal_letter
:parser: rst
```

````

````{py:data} azimuthal_number
:canonical: abtem.inelastic.core_loss.azimuthal_number
:value: >
   None

```{autodoc2-docstring} abtem.inelastic.core_loss.azimuthal_number
:parser: rst
```

````

````{py:function} calculate_bound_radial_wavefunction(...)
:canonical: abtem.inelastic.core_loss.calculate_bound_radial_wavefunction

```{autodoc2-docstring} abtem.inelastic.core_loss.calculate_bound_radial_wavefunction
:parser: rst
```
````

````{py:function} calculate_continuum_radial_wavefunction(...)
:canonical: abtem.inelastic.core_loss.calculate_continuum_radial_wavefunction

```{autodoc2-docstring} abtem.inelastic.core_loss.calculate_continuum_radial_wavefunction
:parser: rst
```
````

````{py:function} check_valid_quantum_number(...)
:canonical: abtem.inelastic.core_loss.check_valid_quantum_number

```{autodoc2-docstring} abtem.inelastic.core_loss.check_valid_quantum_number
:parser: rst
```
````

````{py:function} config_str_to_config_tuples(...)
:canonical: abtem.inelastic.core_loss.config_str_to_config_tuples

```{autodoc2-docstring} abtem.inelastic.core_loss.config_str_to_config_tuples
:parser: rst
```
````

````{py:function} config_tuples_to_config_str(...)
:canonical: abtem.inelastic.core_loss.config_tuples_to_config_str

```{autodoc2-docstring} abtem.inelastic.core_loss.config_tuples_to_config_str
:parser: rst
```
````

````{py:function} fast_roll(...)
:canonical: abtem.inelastic.core_loss.fast_roll

```{autodoc2-docstring} abtem.inelastic.core_loss.fast_roll
:parser: rst
```
````

````{py:function} numerov(...)
:canonical: abtem.inelastic.core_loss.numerov

```{autodoc2-docstring} abtem.inelastic.core_loss.numerov
:parser: rst
```
````

````{py:function} prism_transition_potential_scan(...)
:canonical: abtem.inelastic.core_loss.prism_transition_potential_scan

```{autodoc2-docstring} abtem.inelastic.core_loss.prism_transition_potential_scan
:parser: rst
```
````

````{py:function} prism_transition_potential_scan_beam_basis(...)
:canonical: abtem.inelastic.core_loss.prism_transition_potential_scan_beam_basis

```{autodoc2-docstring} abtem.inelastic.core_loss.prism_transition_potential_scan_beam_basis
:parser: rst
```
````

````{py:function} radial_schroedinger_equation(...)
:canonical: abtem.inelastic.core_loss.radial_schroedinger_equation

```{autodoc2-docstring} abtem.inelastic.core_loss.radial_schroedinger_equation
:parser: rst
```
````

````{py:function} remove_electron_from_config_str(...)
:canonical: abtem.inelastic.core_loss.remove_electron_from_config_str

```{autodoc2-docstring} abtem.inelastic.core_loss.remove_electron_from_config_str
:parser: rst
```
````
