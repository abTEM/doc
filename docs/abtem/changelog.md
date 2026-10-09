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
- `Potential(sampling="auto", slice_thickness="auto")` automatically finds a grid commensurate with the atomic
  lattice — so translation-equivalent atoms discretize identically — near the usual default targets
  ($0.05 \ \mathrm{Å}$, $1 \ \mathrm{Å}$), preferring FFT-fast grid sizes wherever that is compatible with
  commensurability. New `grid.round-to-fast-fft` config key (`'auto'`/`True`/`False`), `Grid.round_to_fast_fft()`,
  and `is_fast_fft_size`/`next_fast_fft_size` helpers in `abtem.core.fft`
  ([PR #274](https://github.com/abTEM/abTEM/pull/274), [PR #347](https://github.com/abTEM/abTEM/pull/347))
- Significant improvements on simulating large potentials on GPU, alongside minor performance improvements
  ([PR #269](https://github.com/abTEM/abTEM/pull/269))
    - The potential is now built in chunks of contiguous slices instead of all at once, keeping peak VRAM
      bounded; new config key `potential.slice-chunk-size` (default `"auto"`)
    - Opt-in multi-GPU via the new config key `dask.multi-gpu` (requires `dask-cuda`)
    - `cupy.fft-cache-size`'s previous `0 MB` default silently disabled the cuFFT plan cache; changed to
      `-1` (unlimited) here, then to the device-relative `auto` default below once unbounded retention
      turned out to cost tens of GB on FFT-unfriendly grids

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
- `Probe.transition_potential_scan` raised for a scan split into more than one chunk (for example through
  `max_batch`) unless the scattering sites were passed explicitly
  ([PR #353](https://github.com/abTEM/abTEM/pull/353))
- Colorbars did not span multi-row exploded plots, and neighbouring panels could abut closely enough for
  their tick labels to collide ([PR #354](https://github.com/abTEM/abTEM/pull/354))
- Multi-GPU hardening, and the configuration fix found while chasing it
  ([PR #346](https://github.com/abTEM/abTEM/pull/346))
    - **The client's configuration now reaches `distributed` workers.** *ab*TEM resolves configuration
      inside each task, and worker processes start fresh and previously saw only the YAML defaults, so
      any distributed computation with a non-default configuration silently used the defaults instead —
      most consequentially `precision`, which meant `float64` runs were computed in `float32`.
      Distributed results obtained with a non-default configuration are worth repeating. Applies to any
      distributed client, CPU clusters included
    - `to_zarr()` on a lazy result honours `dask.multi-gpu`; it previously ignored the flag and ran the
      whole computation on a single device
    - `cupy.fft-cache-size` defaults to `auto` — 25 % of each device's memory, resolved per device —
      rather than unlimited. `-1` restores unlimited, `0 MB` disables the cache, and a size such as
      `512 MB` sets a fixed bound. A single plan larger than the bound runs uncached with a warning
      instead of raising
    - New config keys `dask.multi-gpu-rmm-pool` and `dask.multi-gpu-devices`, for an RMM memory pool per
      worker and for restricting the cluster to a subset of GPUs
    - Automatically sized scan batches are halved on grid sizes that force cuFFT's Bluestein fallback,
      which needs a much larger FFT workspace
    - Warnings replace silent fallbacks: multi-GPU requested but declined (with the reason), a missing
      `if __name__ == "__main__"` guard, and a grid size that forces the Bluestein fallback (naming the
      next fast size)
- Changed results of `integrate_gradient` and `block_direct()`, and fixes to lazy `Waves.normalize()`, eager
  `SMatrix.build()`, `GPAWPotential` with a trajectory and arithmetic between CPU and GPU data
  ([PR #556](https://github.com/abTEM/abTEM/pull/556))
    - **Behaviour change:** `Images.integrate_gradient` shifts every image of an ensemble so that its own
      minimum is 0. An eager ensemble previously shared one constant, the minimum over the whole ensemble, and
      a lazy result was shifted by the minimum of each dask block, so it depended on the chunking. Only the
      offset of an ensemble member differs; a single image gives the same result. This applies to
      `DiffractionPatterns.integrated_center_of_mass` as well
    - **Behaviour change:** `DiffractionPatterns.block_direct()` without a `semiangle_cutoff` in the metadata
      blocks only the zero-angle pixel: the default radius is half the smaller angular sampling. It was the
      larger angular sampling, which also zeroed the neighbouring pixels (four, for similar samplings); for the
      pattern of a single unit cell those are the first-order reflections. Patterns with a `semiangle_cutoff`
      and calls with an explicit `radius` are unchanged. With `margin=True` and no `radius`, the margin (the
      larger angular sampling) is added to the new, smaller radius, so fewer pixels are blocked than before
    - Lazy `Waves.normalize()` raised `AttributeError`; it now gives the eager result for any chunking,
      whether the waves are stored in real or reciprocal space
    - Under `float64` the eager `SMatrix.build()` stored `complex64` plane waves; it now follows the configured
      precision, as the lazy build does. The eager S-matrix, on the device or on the host, is `complex128` and
      takes twice the memory it did; `float32` is unchanged
    - Eager `SMatrix.build()` with `store_on_host=True` raised `AttributeError` on the CPU device
    - A `GPAWPotential` of a single calculator with an `AtomsEnsemble` or `EnergyResolvedAtomsEnsemble` as
      `frozen_phonons` raises a `ValueError` at construction. It was accepted, and then raised `TypeError` in
      every build and multislice. One calculator takes `FrozenPhonons`; for a trajectory, pass one calculator
      per frame
    - Arithmetic between CPU and GPU data (an array object with CuPy data and a NumPy array, a dask array of
      NumPy chunks or an array object with CPU data, or the reverse) raises a `TypeError` that says to move
      one operand with `copy_to_device`, in either operand order and for lazy data when the expression is
      built. It raised CuPy's `TypeError` before, for lazy data only at compute time. NumPy scalars and Python
      numbers are accepted as before

Documentation:

- `sampling="auto"`/`slice_thickness="auto"` documented in detail in the potentials walkthrough, including a
  worked example of the commensurability artifact they remove; cross-referenced from the convergence appendix
  (manual commensurate sampling) and the performance-tips appendix (fast FFT sizes)
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
- The multiple-GPUs section of the parallelization walkthrough is expanded to cover the multi-GPU
  hardening fixes above, and the FFT plan-cache documentation is corrected to match the shipped `auto`
  default (it previously described a stale `0 MB` default that was never shipped)

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
