# Microarray data rescaling and peak finding
[Peng et al., 2014](https://link.springer.com/protocol/10.1007%2F978-1-4939-0888-2_27) is the protocol to visualize single-stranded DNA (ssDNA) in budding yeast by Agilent Yeast Whole Genome ChIP-to-chip 4 × 44K (G4493A) microarrays. The code here is developed for comparing ssDNA quantity and locations in different budding yeast strains.

## Rescaling: image processing normalization
The process rescales ssDNA profile of one yeast strain to a comparable level of the other strain based on the DNA replication origin efficiency measure using a two-dimensional agarose gel and the transformation below:

ssDNA_{mutant_{norm}}=\frac{ssDNA_{mutant}-Min_{mutant_{origin}}}{Max_{mutant_{origin}}-Min_{mutant_{origin}}}*\left(Max_{WT_{origin}}*\frac{E_{mutant}}{E_{WT}}-Min_{mutant_{origin}}\right )+Min_{mutant_{origin}}
