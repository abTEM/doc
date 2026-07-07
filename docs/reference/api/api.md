(reference:api)=

# API 

The *ab*TEM API generally follows an object-oriented design with objects representing elements of the underlying 
physical models. Numpy-style docstrings embedded in the code allow the reference to be automatically generated.

## Core class families

The diagrams below show how the main user-facing classes in each part of the API relate to one another; see the
full reference below for every class and function.

### Wave functions

```{inheritance-diagram} abtem.waves.PlaneWave abtem.waves.Probe abtem.waves.Waves
:parts: 1
```

### Potentials

```{inheritance-diagram} abtem.potentials.iam.Potential abtem.potentials.iam.PotentialArray abtem.potentials.iam.CrystalPotential
:parts: 1
```

### Detectors

```{inheritance-diagram} abtem.detectors.AnnularDetector abtem.detectors.PixelatedDetector abtem.detectors.SegmentedDetector abtem.detectors.FlexibleAnnularDetector
:parts: 1
```

### Scan patterns

```{inheritance-diagram} abtem.scan.GridScan abtem.scan.LineScan abtem.scan.CustomScan
:parts: 1
```

### Contrast transfer function

```{inheritance-diagram} abtem.transfer.CTF abtem.transfer.Aperture abtem.transfer.TemporalEnvelope
:parts: 1
```

## Full reference

```{toctree}
:titlesonly:
:maxdepth: 3

apidocs/abtem/abtem
```
