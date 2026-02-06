# Changelog

Starting the changelog with version 1.0.8.

## 1.0.10 (upcoming)
Features:
- Greatly expanded real-space multislice with propagator- and fully-corrected algorithms, as well as backscattered waves
- Updated `BullseyeAperture` to use smoothed aperture edges

Dependencies:
- Support for Zarr 3 `ZipStore` (requiring `rich` as an additional dependency)
- Deprecated `[gpu]` optional dependency (just asking for `cupy` won't install the correct CUDA version)
- Moved testing, docs, and dev from optional dependencies to groups

## 1.0.9
Dependencies:
- Support for `scipy>=1.7` and `cupy>=12`.
- Restricted Dask versions (>=2022.12.1,!=2025.12.*,!=2026.1.*") to avoid an issue with Numba in the latest ones 

## 1.0.8
Features:
- Fully featured Bloch-wave simulations
- Simple real-space multislice algorithm
- Fully tested core-loss filtered imaging
- Structured illumination (custom apertures and phase plates)

Documentation:
- Updated and fixed example gallery
- Appendix on convergence
- Expanded tutorial on orthogonal periodic supercells

Bugfixes:
- Numerous small bugfixes and improvements
