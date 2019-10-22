---
title: Contribution
color: green
---

For the measurement, we chose the Part BBa_E0020, which is an engineered cyan fluorescent protein (CFP) derived from *A. victoria* GFP designed by Caitlin Conboy and Jennifer Braff. We performed the cloning with the restriction enzymes XbaI and EcoRI into the vector pUC19. CFP was under control of the lac promotor and the lac operator. For the amplification, the cloned plasmid was transformed by heat shock into the E.coli cloning strain DH5α. After plasmid preparation, the construct was transformed into the E.coli expression strains BL21 Star (DE3) and BL21 (DE3). The clones for overnight cultures were picked under a fluorescence microscope to ensure that they contain the CFP insert.
To assure the same amount of cells, the OD of the distinct strains of the overnight cultures was measured.

|  Culture  |  OD |
|---|---|
| Star CFP transformed | 2.59 |
| BL21 CFP transformed | 1.76. |
| Tuner CFP untransformed | 1.97 |
| Star CFP untransformed | 1.77 |
| BL21 CFP untransformed | 1.67 |

*Table 1: Measurement of the OD of the overnight cultures (Star, BL21, Tuner) of transformed and untransformed bacteria with the protein CFP by photometer*

Afterwards, they were set to an OD of 0.5 in a total volume of 5 ml. For induction of the expression, IPTG was used. The bacteria were induced for 2 h 20 min with 0 mM, 0.3 mM and 0.5 mM IPTG.

The fluorescence of the transformed bacteria was measured by fluorescence activated cell sorting (FACS). Therefore, the bacterial cells were separated from each other by treating them with 1:1 ELISA buffer (including 0,05% Tween). Afterwards, they were measured unstained within the FACS machine. Gain settings of the FACS were set to FSC 165 and SSC 400. The measuring part CFP was excited by the 405 nm laser line and detected by 485 nm.

# Results

The gating strategy for the identification of the *E.coli* cells by FACS machine can be seen in Figure 1. For the identification of the *E.coli* cells, the backgating method was used. The cell’s physical properties were investigated by using the forward and the sideward scatter, analysing the size and the granularity of the cells.

{{% figure id="1" title="Gating strategy for the identification of E.coli cells for further analysis of expressed CFP" src="/project/images/Identification of E.coli.png" %}}

{{% figure id="2" title="Comparison of IPTG inductions with different concentrations (0mM, 0.3mM, 0.5mM) in BL21 (Fig. A) and Star (Fig. B)" src="/project/images/IPTG induction of BL21 and Star.png" %}}

The CFP expression was analysed afterwards by measuring the fluorescence signal. For the analysis, the cell counts were normalized to mode. Different concentrations of IPTG were tested. In Figure 2 it can be seen that IPTG induction had no effect on the CFP expression. Nevertheless, CFP was expressed indicating a leaky expression independent of IPTG. According to the literature, leaky expression is a characteristic of lac promotors, which is a component of our chosen vector (Rosano und Ceccarelli 2014).

{{% figure id="3" title="Comparison of IPTG inductions with different concentrations (0mM, 0.3mM, 0.5mM) in BL21 (Fig. A) and Star (Fig. B)" src="/project/images/Comparison of transformed and untransformed cells.png" %}}

In Figure 3, a clear difference between transformed and non-transformed bacteria can be detected. Transformed bacteria were able to express CFP, which results in a higher fluorescence signal, whereas non-transformed bacteria showed no CFP signal. Therefore, it can be suggested that CFP is a non-toxic protein for the cells upon they survived the protein expression.

The fluorescence signal of BL21, Star and the negative control (Tuner) is compared in Figure 4.

{{% figure id="4" title="Comparison of BL21, Tuner and Star" src="/project/images/Comparison of BL21, Tuner and Star.png" %}}

BL21 shows the highest fluorescence signal meaning that CFP expression is stronger in this strain compared to Star. This result is contrary to our expectations, because Star has mutations in the RNAseE (rne131), which results in reduced mRNA degradation and therefore a higher protein expression was suggested (Lopez et al. 1999).

The FACS method can also be used to analyse a whole cell culture.

{{% figure id="5" title="Cell culture analysis by FACS" src="/project/images/Cell culture analysis by FACS.png" %}}

In Figure 5 BL21(DE3) is depicted, which was analysed by FACS as a preliminary experiment to investigate the properties of the strain. It was expected that the culture is monoclonal, derived from one single clone. The result of the FACS experiment demonstrates that the bacteria of this culture did not all origin from one clone, because two peaks at different fluorescent levels can be noticed. This suggests a special application of the FACS method to define the assets of a bacterial culture.

In summary, it can be said that BL21 Star (DE3) and BL21 (DE3) are able to express functional CFP. Furthermore, analysis of the bacterial cells can be conducted via the FACS method and cell cultures can be investigated upon their properties, like their uniformity.

## References

Lopez, P. J.; Marchand, I.; Joyce, S. A.; Dreyfus, M. (1999): The C-terminal half of RNase E, which organizes the Escherichia coli degradosome, participates in mRNA degradation but not rRNA processing in vivo. In: *Molecular microbiology* 33 (1), S. 188–199. DOI: 10.1046/j.1365-2958.1999.01465.x.

Rosano, Germán L.; Ceccarelli, Eduardo A. (2014): Recombinant protein expression in Escherichia coli: advances and challenges. In: *Frontiers in microbiology* 5, S. 172. DOI: 10.3389/fmicb.2014.00172.