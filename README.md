# ssDNA Formation and DNA Replication Origin Usage Analysis
The purpose of this project is to query activation status of each individual DNA replication origin at a genome-wide level and build a database of active replication origins in different yeast strains. This project uses whether ssDNA formed or not at each DNA replication origin location to predict the activation of the origin. [Peng et al., 2014](https://link.springer.com/protocol/10.1007%2F978-1-4939-0888-2_27) is the protocol to visualize single-stranded DNA (ssDNA) in budding yeast by Agilent Yeast Whole Genome ChIP-to-chip 4 × 44K (G4493A) microarrays. The code here is developed for comparing ssDNA quantity and locations in different budding yeast strains and the manuscript (Peng et al., 2017) is submitted.

## Rescaling: image processing normalization
The process rescales ssDNA profile of one yeast strain to a comparable level of the other strain based on the DNA replication origin efficiency measure using a two-dimensional agarose gel and the transformation are following:

![equation](https://github.com/DNApower/ssDNAproject/blob/master/image/math.gif)

![result](https://github.com/DNApower/ssDNAproject/blob/master/image/rescaling.png)

## Peak finding
The ssDNA locations are defined as the ssDNA peak positions. The ssDNA peaks are found by first-order derivative through INDEXES function from [PeakUtils 1.1.0](https://pypi.python.org/pypi/PeakUtils)
