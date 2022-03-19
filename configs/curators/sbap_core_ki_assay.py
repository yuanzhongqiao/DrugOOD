_base_ = ['../_base_/curators/sbap_defaults.py',
          '../_base_/curators/noises/core.py',
          '../_base_/curators/domains/assay.py']

path = dict(task=dict(subset="sbap_core_ki_assay"))

noise_filter = dict(assay=dict(measurement_type=['Ki'], assay_target_type=["SINGLE PROTEIN"]))