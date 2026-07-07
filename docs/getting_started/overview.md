(getting_started:overview)=

# Overview

Computer simulations have become an indispensable part of modern research. To reliably interpret the data from
experiments, a careful comparison between theoretical models and experiments is often required. The use of
dynamical scattering simulations based on the multislice algorithm has, for several decades, been an invaluable aid for
transmission electron microscopy (TEM). As a result, there are many excellent simulation codes, and *ab*TEM is another
one; however, our approach differs in many key aspects.

## How *ab*TEM differs

### No GUI; Jupyter notebooks

*ab*TEM does not implement a graphical user interface, instead focusing on scripts and especially  
[Jupyter notebooks](https://jupyter.org/). A Jupyter Notebook is a mix of code, explanatory text, and visualizations, which
immediately provides documentation of the simulation, allowing others to understand, share and reproduce it. *ab*TEM
aids a visual workflow by implementing methods for creating quick visualizations of each subtask, for example, a heatmap
of the projected potential or the profile of the electron probe. The use of open formats improves reproducibility
and transparency, and we always encourage users to share their code with publications.

### Flexible, no fixed simulation modes

*ab*TEM does not directly implement *any* of the common TEM experiments, instead inviting the user to mix and match
objects to construct the desired simulation. This provides the user with enormous flexibility to design the
simulation while *ab*TEM takes care of the computational details. See below for examples.

### "Pure Python", but fast

Python has become the most popular programming language in physics, thanks in particular to its extensive base
of open-source libraries. In the electron microscopy community, this includes packages such as
[HyperSpy](https://hyperspy.org/), [Libertem](https://libertem.github.io/LiberTEM/) and
[Py4DSTEM](https://py4dstem.readthedocs.io/en/latest/). Effective use of fast open-source numerical libraries such
as [NumPy](https://numpy.org/), [CuPy](https://cupy.dev/), [Numba](https://numba.pydata.org/) and
[PyFFTW](https://pyfftw.readthedocs.io/en/latest/), allows *ab*TEM to be extremely competitive in raw performance. The
combination of easy-to-understand Python code, excellent interoperability combined with uncompromising
simulation speed make for an attractive combination.

### Deploys anywhere, powered by Dask

*ab*TEM is created from the ground up to work with [Dask](https://www.dask.org/). Dask allows scaling from a single
laptop to hundreds of nodes at high-performance computing (HPC) facilities with minimal changes to the code. This makes
the code very well suited for diverse settings, from teaching to cutting-edge research.

### Open-source and open to contributions

The *ab*TEM developers are not alone in seeing the necessity of open-source software in electron microscopy. We are
striving to make this an inviting project for new contributors and collaborators. Everybody is invited to contribute
to use and develop the code; see our [guide for contributors](library:contributing).

## The *ab*TEM object model

abTEM
follows [domain-driven](https://en.wikipedia.org/wiki/Domain-driven_design) and [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming)
design principles. In short, that means that our implementation of the multislice algorithm is based on objects
representing physical concepts; for example, a plane wave function is represented by the `PlaneWave` object, and a
focused STEM probe wave function is represented by a `Probe` object. This makes the code easy to understand, not only for
specialists but anyone familiar with transmission electron microscopy.

The diagram below sketches how the core objects connect to form the six simulation modes shown below; see the
[API reference](reference:api) for the full class hierarchy behind each of them.

<figure style="margin: 1.5rem 0;">
<svg viewBox="0 0 980 430" role="img" aria-labelledby="object-model-title" style="max-width: 820px; width: 100%; height: auto; display: block; margin: 0 auto;">
<title id="object-model-title">The abTEM object-composition pipeline</title>
<defs>
  <marker id="om-arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0,0 L10,5 L0,10 z" fill="var(--pst-color-text-base)" />
  </marker>
</defs>
<g fill="none" stroke="var(--pst-color-text-base)" stroke-width="1.5">
  <line x1="130" y1="42" x2="205" y2="42" marker-end="url(#om-arrow)" />
  <line x1="190" y1="182" x2="325" y2="182" marker-end="url(#om-arrow)" />
  <line x1="480" y1="168" x2="695" y2="100" marker-end="url(#om-arrow)" />
  <line x1="480" y1="196" x2="695" y2="200" marker-end="url(#om-arrow)" />
  <line x1="130" y1="375" x2="695" y2="375" marker-end="url(#om-arrow)" />
</g>
<g font-size="12.5" fill="var(--pst-color-text-base)" text-anchor="middle">
  <text x="260" y="172">multislice(potential)</text>
  <text x="600" y="118">apply_ctf(CTF).intensity()</text>
  <text x="600" y="227">diffraction_patterns()</text>
  <text x="400" y="362">scan(potential, scan, detectors)</text>
</g>
<g stroke="var(--pst-color-border)" stroke-width="1.5" fill="var(--pst-color-surface)">
  <rect x="20" y="20" width="110" height="44" rx="8" />
  <rect x="210" y="20" width="160" height="44" rx="8" />
  <rect x="20" y="150" width="170" height="64" rx="8" />
  <rect x="330" y="150" width="150" height="64" rx="8" />
  <rect x="20" y="350" width="110" height="50" rx="8" />
</g>
<g stroke="var(--pst-color-primary)" stroke-width="1.5" fill="var(--pst-color-primary-bg)">
  <rect x="700" y="70" width="260" height="60" rx="8" />
  <rect x="700" y="170" width="260" height="60" rx="8" />
  <rect x="700" y="345" width="260" height="60" rx="8" />
</g>
<g fill="var(--pst-color-on-surface)" text-anchor="middle">
  <text x="75" y="47" font-size="14">Atoms</text>
  <text x="290" y="47" font-size="14">Potential</text>
  <text x="105" y="178" font-size="14" font-weight="600">Wave function</text>
  <text x="105" y="197" font-size="12">PlaneWave, Probe</text>
  <text x="405" y="186" font-size="14">Exit wave</text>
  <text x="75" y="380" font-size="14">Probe</text>
  <text x="830" y="97" font-size="14" font-weight="600">Measurement</text>
  <text x="830" y="116" font-size="12">HRTEM</text>
  <text x="830" y="197" font-size="14" font-weight="600">Measurement</text>
  <text x="830" y="216" font-size="12">SAED, CBED, PED</text>
  <text x="830" y="372" font-size="14" font-weight="600">Measurement</text>
  <text x="830" y="391" font-size="12">STEM, 4D-STEM</text>
</g>
</svg>
<figcaption style="text-align: center; font-size: 0.9em; color: var(--pst-color-text-muted);">
A <code>PlaneWave</code> or <code>Probe</code> propagated through a <code>Potential</code> yields an exit wave (single-shot
modes) or, via <code>Probe.scan</code>, a scanned measurement directly (STEM modes).
</figcaption>
</figure>

To simulate a (basic) high-resolution TEM (HRTEM) image, we need a `PlaneWave` at a given energy (by default in units of
$\mathrm{eV}$), a `Potential` with a given real-space sampling (in units of $\mathrm{Å}$), and a `CTF` (contrast
transfer function) representing the objective lens with a given aperture (in $\mathrm{mrad}$) and spherical aberration
coefficient (also in $\mathrm{Å}$). We show how this could be implemented in the code below; please change the tabs for
other simulation modes.

`````{tab-set}

````{tab-item} HRTEM
 
An image is measured by getting the `intensity` of the exit wave, calculated by propagating the plane wave through
the potential using the multislice algorithm and applying the `CTF`.

```python
wave = PlaneWave(energy=80e3)

potential = Potential(atoms, sampling=.05)

ctf = CTF(semiangle_cutoff=30, Cs=1e-3 * 1e10, defocus="scherzer")

exit_wave = wave.multislice(potential)

measurement = exit_wave.apply_ctf(ctf).intensity()
```
````

````{tab-item} SAED
We can turn the HRTEM simulation into a selected area electron diffraction (SAED) simulation by getting rid of the `CTF` 
and calculating `diffraction_patterns` from the exit wave instead of the `intensity`.

```python
wave = PlaneWave(energy=80e3)

potential = Potential(atoms, sampling=.05)

exit_wave = wave.multislice(potential)

measurement = exit_wave.diffraction_patterns()
```
````

````{tab-item} CBED
The SAED simulation becomes a converged-beam electron diffraction (CBED) simulation by only changing the 
`PlaneWave` for a `Probe`; the semiangle cutoff keyword now describes the condenser aperture of the probe.

```python
wave = Probe(energy=80e3, semiangle_cutoff=10)

potential = Potential(atoms, sampling=.05)

exit_wave = wave.multislice(potential)

measurement = exit_wave.diffraction_patterns()
```
````

````{tab-item} PED
The CBED simulation can become a precession ED simulation by setting the `tilt` property of the `Probe`, with 
a specified array of angles.

```python
wave = Probe(energy=80e3, semiangle_cutoff=30, Cs=1e-3 * 1e10, defocus="scherzer")

potential = Potential(atoms, sampling=.05)

wave.tilt = precession_tilts(precession_angle=20, num_samples=60)

exit_wave = probe.multislice(potential)

measurement = exit_wave.diffraction_patterns()
```
````

````{tab-item} STEM-MAADF
A STEM-ADF simulation requires defining the scan area using the `GridScan` (defaulting to the entire area of the 
cell) and an `AnnularDetector` defining the inner and outer detector angles (again in $\mathrm{mrad}$).

```python
wave = Probe(energy=80e3, semiangle_cutoff=30, Cs=1e-3 * 1e10, defocus="scherzer")

potential = Potential(atoms, sampling=.05)

detector = AnnularDetector(inner=60, outer=120)

scan = GridScan()

measurement = probe.scan(potential, detectors=detector, scan=scan)
```
````

````{tab-item} 4D-STEM
The STEM-ADF simulation is easily modified into a 4D-STEM simulation by swapping the
`AnnularDetector` for a `PixelatedDetector`.

```python
wave = Probe(energy=80e3, semiangle_cutoff=30, Cs=1e-3 * 1e10, defocus="scherzer")

potential = Potential(atoms, sampling=.05)

detector = PixelatedDetector()

scan = GridScan()

measurement = probe.scan(potential, detectors=detector, scan=scan)
```
````
`````

These examples demonstrate simplified *ab*TEM code for simulating several common electron microscopy experiments.
For clarity, we have omitted import statements, and the atomic models are assumed to be given as `atoms`.
Equivalent complete executable code examples can be found [further in the documentation](getting_started:basic_examples)
.

We *strongly* recommend that new users work through our [walkthrough](user_guide:walkthrough) to familiarize themselves with *ab*TEM and its features.