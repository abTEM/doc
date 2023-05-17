(reference:api)=

# API 

The *ab*TEM API generally follows an object-oriented design with objects representing elements of the underlying 
physical models. Numpy-style docstrings embedded in the code allow the reference to be automatically generated.

```{eval-rst}
.. autosummary::
   :toctree: _autosummary
   :template: custom-module-template.rst
   :recursive:

   abtem.waves
   abtem.scan
   abtem.detectors
   abtem.measurements
   abtem.transfer
   abtem.distributions
   abtem.potentials.iam
   abtem.potentials.charge_density
   abtem.potentials.gpaw
   abtem.visualize
   abtem.atoms
   abtem.multislice
   abtem.prism.s_matrix
   abtem.indexing
```