# ACC_Exercises
Exercises for the Computational Astrophysics and Cosmology course

## Exercises

### 01_NGC6397_CMD

#### [esercizio](01_NGC6397_CMD/esercizio.ipynb)
- # Exercise 1 — Color-Magnitude Diagram of NGC 6397 with Gaia DR3 and identification of the Main-Sequence Turn-Off
- **Course topics covered:**
- - Querying astronomical archives via `astroquery`.
- - Manipulating FITS tables with `astropy.io.fits` and `astropy.table`.
- - Selecting members of a stellar cluster via proper motions.
- - Building a clean color-magnitude diagram (CMD).
- **Reference papers:**
- - Gaia Collaboration, [Babusiaux, C., van Leeuwen, F., Barstow, M. A., et al. 2018, *A&A* **616**, A10](https://arxiv.org/abs/1804.09378) — Figure 11 shows the CMDs of several Milky Way globular clusters obtained with Gaia DR2. In this exercise we qualitatively reproduce the panel relative to NGC 6397 using Gaia DR3.
- - [Vasiliev, E. & Baumgardt, H. 2021, *MNRAS* **505**, 5978](https://arxiv.org/abs/2102.09568) — catalog of members and mean proper motions of MW globular clusters, from which we take the mean proper-motion values for the member selection.
- **Dataset:** Gaia DR3 via `astroquery.gaia`, cone search around NGC 6397 (RA = 265.175 deg, Dec = -53.6743 deg) with radius 0.25 deg.
- **Scientific scenario.** A globular cluster is a nearly coeval and chemically homogeneous stellar population: its CMD is the "snapshot" of a single isochrone at the cluster's distance. Proper motions allow us to remove almost all foreground/background field stars and obtain a clean CMD even for clusters projected onto crowded fields like NGC 6397.

### 02_PSZ_MassFunction

#### [esercizio](02_PSZ_MassFunction/esercizio.ipynb)
- # Exercise 1 — The Planck PSZ2 Catalogue and the Y–M Scaling Relation
- **Course topics covered:**
- - Reading and inspecting FITS binary tables with `astropy.io.fits`.
- - Visualising survey sky coverage in Galactic coordinates.
- - Identifying and handling missing or flagged data in astronomical catalogues.
- - Computing the observed cluster mass function and its Poisson uncertainties.
- - Fitting power-law models with `scipy.optimize.least_squares` and χ² minimisation.
- - Bayesian parameter estimation with a custom Metropolis–Hastings sampler.
- **Reference papers:**
- - Planck Collaboration, [Ade, P. A. R., et al. 2016, *A&A* **594**, A27](https://arxiv.org/abs/1502.01598) — the second Planck catalogue of SZ sources (PSZ2); the dataset used in this exercise.
- - [Kravtsov, A. V., Vikhlinin, A., & Nagai, D. 2006, *ApJ* **650**, 128](https://arxiv.org/abs/astro-ph/0602117) — derivation of the Y–M scaling relation from simulations; discusses the self-similar expectation Y ∝ M^(5/3).
- **Dataset:** `planck_sz_catalogue.fit` — 1653 galaxy cluster candidates detected by the Planck satellite via the Sunyaev–Zel'dovich (SZ) effect. Key columns: `GLON`/`GLAT` (Galactic coordinates, deg); `SNR` (detection signal-to-noise); `q_neural` (neural-network quality score, 0–1); `COSMO` (flag for the cosmological sub-sample); `Z` (spectroscopic redshift; −1 if unavailable); `Y5R500`/`e_Y5R500` (integrated Compton-y within 5R₅₀₀, in units of 10⁻³ arcmin², with uncertainty); `MSZ`/`E_MSZ` (mass M₅₀₀ inferred from the Y–M scaling relation, in units of 10¹⁴ M☉, with upper uncertainty).
- **Scientific scenario.** The Sunyaev–Zel'dovich (SZ) effect is a spectral distortion of the cosmic microwave background (CMB) caused by inverse Compton scattering of CMB photons off the hot electrons of the intracluster medium. The integrated Compton-y parameter Y₅R₅₀₀ is proportional to the total thermal energy of the gas and is tightly correlated with the cluster mass M through a power-law scaling relation, Y ∝ M^α. Calibrating this Y–M relation and measuring the cluster mass function are fundamental steps for using SZ-selected cluster catalogues as cosmological probes of the growth of large-scale structure.

### 03_NBody_Clustering

#### [esercizio](03_NBody_Clustering/esercizio.ipynb)
- # Exercise — Galaxy Clustering and Power Spectrum from the Magneticum Hydrodynamical Simulation
- **Course topics covered:**
- - Loading and cleaning a large-scale simulation galaxy catalogue.
- - Visualising the three-dimensional large-scale structure and the cosmic web.
- - Computing the stellar mass function and star-formation scaling relations.
- - Implementing a galaxy power-spectrum estimator from scratch (NGP → FFT → spherical binning).
- - Measuring galaxy bias as a function of stellar mass and star-formation activity.
- - *(Optional)* Comparing mass-assignment schemes: NGP, CIC, TSC.
- **Reference papers:**
- - Dolag, K., et al. 2016, *MNRAS* **463**, L69 — overview of the Magneticum Pathfinder simulations.
-   Web portal and data access: <http://www.magneticum.org>
- - Springel, V., et al. 2005, *Nature* **435**, 629 — the Millennium simulation (N-body counterpart).
- - Eisenstein, D. J. & Hu, W. 1998, *ApJ* **496**, 605 — analytical CDM transfer function.
- - Tinker, J. L., et al. 2010, *ApJ* **724**, 878 — halo bias fitting function.
- - Croton, D. J., et al. 2007, *MNRAS* **374**, 1303 — galaxy clustering and bias.
- **Dataset:** Magneticum Pathfinder **Box2b/hr** galaxy catalogue, snapshot 031
- (`galaxies.txt.gz`, ~547 MB compressed).
- Download from <http://wwwmpa.mpa-garching.mpg.de/HydroSims/Magneticum/Downloads/Magneticum/Box2b_hr/snap_031/>.
- Box size $L = 640\;h^{-1}\,\mathrm{Mpc}$, cosmology WMAP7
- ($\Omega_m=0.272$, $\Omega_\Lambda=0.728$, $h=0.704$, $\sigma_8=0.809$, $n_s=0.963$).
- **Catalogue columns** (after loading):
- | Name | Description | Unit |
- |------|-------------|------|
- | `uid` | Unique galaxy identifier | — |
- | `x_kpc`, `y_kpc`, `z_kpc` | Comoving position | $h^{-1}$ kpc |
- | `m_star` | Stellar mass | $h^{-1}\,M_\odot$ |
- | `sfr` | Star formation rate | $M_\odot\,\mathrm{yr}^{-1}$ |
- | `host` | UID of the group's central galaxy | — |
- | `dist_kpc` | Distance to group centre | $h^{-1}$ kpc |
- | `log_m_cD` | $\log_{10}(m_{\rm cD}/m_*)$ | — |
- | `m_gas` | Stellar mass of the gas component | $h^{-1}\,M_\odot$ |
- | `vx`, `vy`, `vz` | Peculiar velocity components | km s$^{-1}$ |
- **Scientific scenario.** Hydrodynamical cosmological simulations model dark matter, gas, stars,
- and black holes self-consistently. Unlike pure N-body runs, they produce realistic galaxies
- with stellar masses, star-formation rates, and ICM properties. The spatial distribution of
- these galaxies is a biased tracer of the underlying matter field: the **galaxy power spectrum**
- $P_{\rm gal}(k) = b^2\,P_{\rm matter}(k)$ on large scales, where the bias $b$ depends on the
- galaxy sample selected. Comparing $P(k)$ for star-forming versus quiescent galaxies, or for
- different stellar-mass thresholds, directly probes the environmental dependence of galaxy
- formation.

### 04_DESI_BAO_Cosmology

#### [esercizio](04_DESI_BAO_Cosmology/esercizio.ipynb)
- # Exercise 4 — Joint posterior $(\Omega_m,\, H_0 r_d)$ from DESI BAO via MCMC
- **Course:** Computational Astrophysics and Cosmology — University of Roma Tre (Master's degree)
- **Course topics covered:**
- - 2D Metropolis-Hastings MCMC with flat priors.
- - Cosmological distances in flat $\Lambda$CDM: $D_C$, $D_M$, $D_A$, $D_H$, $D_V$.
- - Natural parameterization of BAO: fitting $(\Omega_m, H_0 r_d)$ without fixing the sound horizon.
- - Multi-measurement BAO likelihood with isotropic ($D_V/r_d$), transverse ($D_M/r_d$), and line-of-sight ($D_H/r_d$) observables.
- - *(Optional)* Extension to alternative dark-energy cosmologies.
- **Reference papers (DESI 2024 Year 1):**
- - DESI Collaboration, 2024, *AJ* **168**, 58 — *DESI 2024 I: A Panchromatic View of the Universe with a Wide-Area Spectroscopic Survey* — [arXiv:2306.06308](https://arxiv.org/abs/2306.06308).
- - DESI Collaboration, 2024 — *DESI 2024 III: Baryon Acoustic Oscillations from Galaxies and Quasars* — [arXiv:2404.03002](https://arxiv.org/abs/2404.03002).  Table 1 contains the final BAO measurements for each tracer.
- - DESI Collaboration, 2024 — *DESI 2024 IV: Baryon Acoustic Oscillations from the Lyman Alpha Forest* — [arXiv:2404.03001](https://arxiv.org/abs/2404.03001).  Table 1 contains the Ly$\alpha$ BAO measurement.
- - DESI Collaboration, 2024 — *DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations* — [arXiv:2404.03000](https://arxiv.org/abs/2404.03000).  This is the primary reference for cosmological interpretation.
- **Dataset:** BAO measurements from the DESI Year 1 (2024) spectroscopic survey.  
- The student is expected to retrieve the numerical values from the tables of the papers listed above before running this notebook.  The cells below indicate precisely which table and which columns to extract.
- **Parameterization.** Flat $\Lambda$CDM.  Free MCMC parameters: $(\Omega_m,\; H_0 r_d)$.  No external prior on $r_d$ is needed: all BAO observables $D/r_d$ depend only on $(\Omega_m, H_0 r_d)$.  If an external measurement of $r_d$ is available (e.g. from CMB or BBN), $H_0$ can be derived *a posteriori*.
- **Scientific scenario — what BAO alone constrains.**
- BAO use the sound horizon $r_d$ at the drag epoch as a *standard ruler*. Measuring $D_M(z)/r_d$, $D_H(z)/r_d$, or $D_V(z)/r_d$ at multiple redshifts constrains the expansion history $H(z)$.  In flat $\Lambda$CDM the two free parameters are $\Omega_m$ (shape of $H(z)/H_0$) and the combination $H_0 r_d$ (overall amplitude, since $D \propto c/(H_0 r_d)$).  Neither $H_0$ nor $r_d$ alone is accessible from BAO without an external anchor.  Fixing $r_d$ from Planck 2018 ($r_d = 147.78$ Mpc, Aghanim+2020) converts the BAO constraint on $H_0 r_d$ into a constraint on $H_0 \approx 68$ km/s/Mpc — on the CMB side of the **Hubble tension**.
