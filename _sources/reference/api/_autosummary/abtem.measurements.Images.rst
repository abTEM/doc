Images
======

.. currentmodule:: abtem.measurements

.. autoclass:: abtem.measurements.Images
   :members:
   :show-inheritance:
   :inherited-members:

   
   .. automethod:: __init__

   
   .. rubric:: Methods

   .. autosummary::
   
      ~Images.__init__
      ~Images.abs
      ~Images.apply_func
      ~Images.apply_transform
      ~Images.compute
      ~Images.copy
      ~Images.copy_to_device
      ~Images.crop
      ~Images.diffractograms
      ~Images.ensemble_blocks
      ~Images.ensure_lazy
      ~Images.expand_dims
      ~Images.from_array_and_metadata
      ~Images.from_zarr
      ~Images.gaussian_filter
      ~Images.generate_blocks
      ~Images.get_from_metadata
      ~Images.get_items
      ~Images.imag
      ~Images.integrate_disc
      ~Images.integrate_gradient
      ~Images.intensity
      ~Images.interpolate
      ~Images.interpolate_line
      ~Images.interpolate_line_at_position
      ~Images.lazy
      ~Images.max
      ~Images.mean
      ~Images.min
      ~Images.no_base_chunks
      ~Images.normalize_ensemble
      ~Images.phase
      ~Images.poisson_noise
      ~Images.real
      ~Images.rechunk
      ~Images.reduce_ensemble
      ~Images.relative_difference
      ~Images.scan_noise
      ~Images.set_ensemble_axes_metadata
      ~Images.show
      ~Images.squeeze
      ~Images.std
      ~Images.sum
      ~Images.tile
      ~Images.to_cpu
      ~Images.to_data_array
      ~Images.to_gpu
      ~Images.to_hyperspy
      ~Images.to_measurement_ensemble
      ~Images.to_tiff
      ~Images.to_zarr
   
   

   
   
   .. rubric:: Attributes

   .. autosummary::
   
      ~Images.array
      ~Images.axes_metadata
      ~Images.base_axes_metadata
      ~Images.base_dims
      ~Images.base_shape
      ~Images.coordinates
      ~Images.device
      ~Images.dtype
      ~Images.ensemble_axes_metadata
      ~Images.ensemble_dims
      ~Images.ensemble_shape
      ~Images.extent
      ~Images.is_complex
      ~Images.is_lazy
      ~Images.metadata
      ~Images.offset
      ~Images.sampling
      ~Images.shape
   
   