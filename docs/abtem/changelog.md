# Changelog

## Upcoming: 1.1.0

The `dev` branch is at version `1.1.0`. The entries below are merged into `dev` but not yet released.

Features:

- Energy ensemble support across the codebase: `PlaneWave`, `Probe`, `SMatrix`, `BlochWaves` and `CTF`
  accept a list of energies, and the resulting `EnergyAxis` propagates through indexing, angular sampling,
  unit conversion and diffraction-spot indexing ([PR #257](https://github.com/abTEM/abTEM/pull/257))
- C-PRISM: `SMatrix(upsample=True)` reduces every probe from the complete plane-wave expansion of the
  aperture, so the interpolation factor only sets the number of multislice runs. Adds
  `CompressedSMatrixArray` and `GridScan.commensurate` ([PR #318](https://github.com/abTEM/abTEM/pull/318))
- Phonon-loss (thermal diffuse scattering) energy-loss workflow: `EnergyResolvedAtomsEnsemble`,
  `phonon_loss_diffraction_patterns`, `momentum_resolved_spectrum` and `MomentumResolvedSpectrum`,
  the `SpectralAnnularDetector` and `SpectralSlitDetector`, and detailed-balance thermal weighting that
  splits the classical TDS signal into loss and gain sides
  ([PR #324](https://github.com/abTEM/abTEM/pull/324), [PR #351](https://github.com/abTEM/abTEM/pull/351))
- Linear-scaling PRISM-EELS for core-loss simulations: `SMatrix.transition_potential_scan`, with
  single- and double-channel scattering and an optional windowed inelastic crop
  ([PR #289](https://github.com/abTEM/abTEM/pull/289))
- In addition to the Gaussian (G) distribution, now also implemented Lorentzian (L), Voigtian (convolution L * G) and
  pseudo-Voigtian (L + G) source-size distributions and filters ([PR #270](https://github.com/abTEM/abTEM/pull/270))
- The exact free-space propagator is now the default for Fourier multislice,
  `FourierMultislice(order="exact")`, replacing the paraxial approximation. Spatial frequencies beyond
  `k > 1 / lambda` are treated as evanescent rather than propagating; the paraxial propagator remains
  available as `order=1` ([PR #298](https://github.com/abTEM/abTEM/pull/298))
- Magnetic potentials and fields from collinear GPAW calculations: `gpaw_magnetic_fields` builds the
  electrostatic potential, vector potential and magnetic field from the same calculator(s) in one call,
  returning a `GPAWMagneticFields` bundle with `.tile()`, `.combined_potential()` and `.show()`;
  `rotate_field` now defaults to `"auto"` ([PR #326](https://github.com/abTEM/abTEM/pull/326))
- `GPAWParametrization` is now usable: it fits a Lobato-form IAM potential to the X-ray scattering factor
  of an all-electron GPAW calculation, with working ionization support and a regularized fit
  ([PR #329](https://github.com/abTEM/abTEM/pull/329))
- Significant improvements on simulating large potentials on GPU, alongside minor performance improvements
  ([PR #269](https://github.com/abTEM/abTEM/pull/269))
    - The potential is now built in chunks of contiguous slices instead of all at once, keeping peak VRAM
      bounded; new config key `potential.slice-chunk-size` (default `"auto"`)
    - Opt-in multi-GPU via the new config key `dask.multi-gpu` (requires `dask-cuda`)
    - `cupy.fft-cache-size` now defaults to `-1` (unlimited, the CuPy default); the previous `0 MB` default
      silently disabled the cuFFT plan cache

Performance:

- The projection integrator is shared by reference across ensemble members instead of being deep-copied
  (and re-uploaded to the GPU) for each ([PR #350](https://github.com/abTEM/abTEM/pull/350))
- Removed a redundant potential rebuild on every scan chunk ([PR #340](https://github.com/abTEM/abTEM/pull/340))

Dependencies:

- The `core-loss` extra is merged into a single `gpaw = ["hankel", "sympy"]` extra, and a new `all` extra
  installs every optional runtime dependency ([PR #329](https://github.com/abTEM/abTEM/pull/329))

Bugfixes:

- `GPAWPotential` for the new-style GPAW calculator API (GPAW 26+), and `GPAWPotential.from_file` on
  old-style restarted calculators ([PR #325](https://github.com/abTEM/abTEM/pull/325))
- `GPAWPotential` single-calculator `frozen_phonons` ensemble building
  ([PR #327](https://github.com/abTEM/abTEM/pull/327)), plus removal of dead and broken code from
  `GPAWPotential` and `GPAWParametrization` ([PR #328](https://github.com/abTEM/abTEM/pull/328))
- `FieldArray.tile()` for vector-valued fields, and unsupported `frozen_phonons`/`repetitions` on magnetic
  fields now raise instead of being silently ignored ([PR #326](https://github.com/abTEM/abTEM/pull/326))
- Silent corruption in eager multislice for potentials with two or more ensemble axes
  ([PR #333](https://github.com/abTEM/abTEM/pull/333))
- `numba` `TypingError` in quasi-dipole interpolation on some numba/numpy pairings
  ([PR #332](https://github.com/abTEM/abTEM/pull/332))
- Single-point `GridScan` failing when built lazily ([PR #342](https://github.com/abTEM/abTEM/pull/342))
- `LinearAxis` losing its offset under dask ensemble chunk partitioning
  ([PR #344](https://github.com/abTEM/abTEM/pull/344))
- Nondeterministic atom loss in `orthogonalize_cell`, and a hardened Gram-Schmidt fallback
  ([PR #345](https://github.com/abTEM/abTEM/pull/345))
- Repeated axis labels and colorbar overlap in exploded spectrum panels, and silently returned zeros for
  single-configuration TDS ([PR #351](https://github.com/abTEM/abTEM/pull/351))
- Azimuthal convention in `prism_coefficients`, which reflected azimuthally dependent aberrations in a PRISM
  reduction with a `CTF`, and exit planes not being remapped when slicing a `PotentialArray`
  ([PR #318](https://github.com/abTEM/abTEM/pull/318))
- `numpy` 2.5 test failures caused by an ASE deprecation warning
  ([PR #343](https://github.com/abTEM/abTEM/pull/343))

Documentation:

- New tutorial on phonon-loss spectroscopy: energy-resolved frozen phonons, the TDS decomposition, the
  momentum-resolved spectrum $S(q, E)$, the spectral detectors and detailed-balance thermal weighting
- Energy ensembles documented in the wave-function walkthrough, with an energy series added to the
  multislice walkthrough
- PRISM-EELS added to the core-loss tutorial, compared against the equivalent multislice scan
- The exact free-space propagator is documented in the multislice walkthrough and the real-space multislice
  tutorial, which now selects the paraxial propagator explicitly where it compares algorithms at equal order
- The installation page documents the optional pip extras (`gpaw`, `extra`, `all`) and why the GPU packages
  are not among them
- The configuration reference is synchronized with the new and changed config keys

Planned for this release (not yet merged):

- Support for skewed pixels (non-orthogonal x,y,z cell axes) ([PR #282](https://github.com/abTEM/abTEM/pull/282))
- Radially variable detector sensitivity ([PR #283](https://github.com/abTEM/abTEM/pull/283))
- Plasmons: fast `PhaseScramblePlasmons` for multislice and PRISM, and `MonteCarloPlasmons` for Bloch wave
- CBED patterns for Bloch waves ([PR #254](https://github.com/abTEM/abTEM/pull/254))

## 1.0.10

Features:

- Expanded real-space multislice with propagator- and fully-corrected algorithms, and backscattered waves ([PR #236](https://github.com/abTEM/abTEM/pull/236))
    - Related internal function name change: standard multislice is now properly called `FourierMultislice`
- Updated `BullseyeAperture` to use smoothed aperture edges/corners ([PR #266](https://github.com/abTEM/abTEM/pull/266))
- Logarithmic scale display for `DiffractionPatterns` and images ([PR #303](https://github.com/abTEM/abTEM/pull/303))
- Finite-projection integrals 7x faster on CPU ([PR #309](https://github.com/abTEM/abTEM/pull/309))

Documentation:

- Expanded tutorial on real-space multislice
- Depth-profile visualization of potentials in the walkthrough
- Single-file Zarr zip storage, logarithmic display scaling, soft Bullseye apertures, anisotropic
  Debye-Waller factors and B-factor conversion helpers
- All published notebooks verified to run with this release

Dependencies:

- NumPy 2.0 or newer is now required ([PR #245](https://github.com/abTEM/abTEM/pull/245))
- GitHub actions based on `uv` and now cover more versions (including Python 3.14) ([PR #308](https://github.com/abTEM/abTEM/pull/308))
- New branching structure: `dev` for development, `main` for releases (only via PRs from `dev`)
- Support for Zarr 3 `ZipStore` (requiring `zarr>=3.1`)
    - Added Zstandard compression of the arrays in the ZipStore at default level 4 (hat tip: quantEM) ([PR #252](https://github.com/abTEM/abTEM/pull/252))
- Deprecated `[gpu]` optional dependency (as just specifying `cupy` will not install the correct CUDA version)
- Moved `testing`, `docs`, and `dev` from optional dependencies to groups
- Narrow Dask version exclusion to !=2025.12.*,!=2026.1.0,!=2026.1.1 ([PR #285](https://github.com/abTEM/abTEM/pull/285))
- Declared `sympy` as an optional dependency (`core-loss` extra), required for core-loss EELS form
  factors ([PR #320](https://github.com/abTEM/abTEM/pull/320))


Bugfixes:

- Frozen-phonon ensemble handling ([PR #267](https://github.com/abTEM/abTEM/pull/267) & [PR #292](https://github.com/abTEM/abTEM/pull/292))
  - May also have resulted in incorrect behavior with `ensemble_mean = False` for e.g. defocus distributions
- `CrystalPotential` with frozen phonons bugs (especially bad on – luckily rare – eager compute) ([PR #306](https://github.com/abTEM/abTEM/pull/306))
- Minor bugs, unsafe patterns, and dead code ([PR #265](https://github.com/abTEM/abTEM/pull/265))
- Anistropic Debye-Waller factors for Bloch wave ([PR #271](https://github.com/abTEM/abTEM/pull/271))
  - Added helper functions to convert between crystallographic B-factors and thermal sigmas
- Added missing `.calculate_exit_waves` for `BlochwaveEnsamble` ([PR #294](https://github.com/abTEM/abTEM/pull/294))
- Silent atom drop when `z`-position lands in SliceIndexedAtoms blind spot  ([PR #273](https://github.com/abTEM/abTEM/pull/273))
- Early-exit bug in orthogonalize_cell ([PR #291](https://github.com/abTEM/abTEM/pull/291))
- Fixed broken tutorial workflow for core-loss filtered imaging ([PR #284](https://github.com/abTEM/abTEM/pull/284))
  - Minor performance improvements for `transition_potential_scan` ([PR #286](https://github.com/abTEM/abTEM/pull/286))
- `Bullseye` aperture: `ring_width` and `spoke_width` are now validated, rejecting values that previously
  produced a silently wrong (solid disk) aperture; docstring corrected to describe the actual fractional
  units introduced by the soft-edge redesign ([PR #319](https://github.com/abTEM/abTEM/pull/319))
- Unified the task-level progress bar config key on `diagnostics.task_progress` (Bloch-wave code paths
  previously read a different, non-functional key) ([PR #321](https://github.com/abTEM/abTEM/pull/321))

## 1.0.9

Dependencies:

- Support for `scipy>=1.7` and `cupy>=12`.
- Restricted Dask versions (`>=2022.12.1,!=2025.12.*,!=2026.1.*"`) to avoid an issue with Numba in the latest ones

## 1.0.8

Starting the changelog with version 1.0.8.

Features:

- Fully featured Bloch-wave simulations
- Simple real-space multislice algorithm
- Core-loss filtered imaging
- Structured illumination (custom apertures and phase plates)

Documentation:

- Updated and fixed example gallery
- Appendix on convergence
- Expanded tutorial on orthogonal periodic supercells

Bugfixes:

- Numerous small bugfixes and improvements
