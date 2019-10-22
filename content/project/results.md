---
title: Results
color: green
---

# Molecular Dynamics Simulations
The MD-simulations of the two linker types showed the average end-to-end distance of each considered linker. 
The results provide two interest insights. First, for every motif repeat *n*, the *(EA3K)n* linker always possessed a longer average end-to-end distance than the according *(G4S)n* (Fig 1).

{{% figure id="1a" title="Length distribution of the (G4S)n linker." src="/awards/images/g4s_hist.png" %}}

{{% figure id="1b" title="Length distribution of the (EA3K)n linker." src="/awards/images/eak_hist.png" %}}

Second, the end-to-end distance of both linkers showed a linear dependence from the number of amino acids. Here, the *(EA3K)n* revealed a steeper slope than the *(G4S)n* linker, which agrees with the aforementioned relation between the average lengths of those two linker types.

{{% figure id="2" title="Average length against number of amino acids." src="/awards/images/l_vs_n.png" %}}

In combination with existing literature our simulations allowed us to choose a linker sequence, leading to the successful expression of our bispecific antibody.

# Wet-lab

## Sequencing Data

To confirm the accuracy of the HEK293T transfection, sequencing of the constructs was performed. 
To cover the complete construct, the sequencing was done in both directions. 
The result are depicted in figures 3-5 and matched to the designed sequences.

{{% figure id="3" title="Sequencing data of K1 (complete bispecific antibody)" src="/project/images/Sequencing_K1_Results.png" %}}

{{% figure id="4" title="Sequencing data of K2a (GPA33+SpyCatcher)" src="/project/images/Sequencing_K2a_Results.png" %}}

{{% figure id="5" title="Sequencing data of K2b (CD3+SpyTag)" src="/project/images/Sequencing_K2b_Results.png" %}}


## Transport of the protein into the medium with the Ig{{% rawhtml %}}&kappa;{{% /rawhtml %}} leader

For the detection of the protein a western blot was conducted. 
The primary antibody was chosen against His-Tag, since all constructs include one or two HisTags. 
All three constructs - K1 (the complete bispecific antibody), K2a (GPA33+SpyCatcher), K2b (CD3+SpyTag) - were successfully expressed in HEK 293T cells. 
The western blot of the harvest is shown in figure 6, which confirmed the proteins at expected height (K1: 54 kDa, K2a: 42 kDa, K2b: 41 kDa). 
The presence of the protein was able to show the ability of the Igk leader to transport the protein into the medium. 
In lane K2a two bands can be seen. In the literature a second line below the expected line could be explained by the use of an additional Start codon downstream of the sequence (Kochetov, 2008). 
This phenomenon is unlikely for K2a, since the Ig{{% rawhtml %}}&kappa;{{% /rawhtml %}} leader sequence wouldn’t be transcripted and thereby the protein not transported out of the cell. 
This second band and the blurry band on the top in the line of K2a might be an effect of protease digestion. 

{{% figure id="6" title="Western blot of the harvest after transfection of HEK 293T cells with an anti His-Tag antibody of the constructs K1, K2a and K2b." src="/project/images/Composite_Part_Ernte.png" %}}


## Purification via HisTag

For the further use of the protein purification is necessary. 
The presence of the His-Tag in the constructs provides the possibility to detect the protein in a western blot and in addition to purify the protein. 
In figure 7 the western blot after the purification of the proteins over a HisTrap column can be seen. 
All constructs were still present after the purification. This shows that all constructs can be purified via their His-Tag. 
Blurry bands in the western blot might have been the result of protease degradation.

{{% figure id="7" title="Western blot of the purified constructs K1, K2a and K2b  with an anti His-Tag antibody" src="/project/images/Composite_Part_Aufreinigung.png" %}}


## SpyTag/SpyCatcher reaction

By combining K2a and K2b in a 1:1 ratio, the basis for the SpyTag/SpyCatcher reaction was provided. 
In the later on performed western blot, which is depicted in Fig. 8. A new specific band could be detected at ~120 kDa.
 A band of 83 kDa was expected. Self-reactivity of the constructs K2a and K2b, which is described in the literature \[Keeble et al., 2017\] can be excluded, 
due to the lack of this specific band in the lines of the constructs themselves. 
Regarding the size of the protein, which can be detected after combining K2a and K2b our suggestion is that a trimeric protein was produced. Polymeric proteins in the usage of the SpyTag/SpyCatcher system is described in the literature as a result of low level intramolecular interaction of the construct (Schoene, Fierer, Bennett, & Howarth, 2014). It is also described that scFvs may form multimers depending on the linker length connecting VH and VL \[Atwell et al., 1999\]

{{% figure id="8" title="Western blot of the constructs K2a, K2b and K2a+b (1:1 ratio K2a with K2b) with an anti His-Tag antibody" src="/project/images/tag_catcher_composite_part.png" %}}


## CD3 binding

For analysing the binding of the anti CD3 scFv to CD3 flow cytometry on T cells was performed. 
The used gating strategy is exemplary depicted in figure 9 for the negative control. 

{{% figure id="9" title="Gating strategy of the FACS analysis to determining CD3 binding. After gating for IgG negative cells T cells were selected by CD4/CD8 expression." src="/project/images/FACS_Gating.png" %}}

K1, K2b and the fused K2ab should possess the ability to bind CD3. 
In fact this is supported by the FACS analysis depicted in figure 10, visible as a nearly complete shift of the T cell population, 
showing a positive signal for anti His-Tag antibody binding. 
Just K2a, designed to bind GPA33 instead of CD3, was not able to bind the T cells.

{{% figure id="10" title="FACS analysis of the constructs K1, K2a, K2b and K2ab for binding to CD3 on T cells." src="/project/images/FACS_Konstrukte.png" %}}


## GPA33 binding

Binding of the anti GPA33 scFv to GPA33, should result in an increased anti His-Tag detection. 
Mirroring the previously described CD3 binding, GPA33 should be bound by K1, K2a and K2ab. 
Contrary to this presumption no shift of the signal in the corresponding channel is visible in figure 11.

This might be explained, if the CaCo-2 cells did not express GPA33 or if the GPA33 binding domain was defect. 
CaCo-2 cells are known to vary their GPA33 expression in a cell cycle dependent manner (Frey, 2011). 
The sequence of  the GPA33 binding region was derived from the patent EP1801208A1, in which a successful binding was reported. 
To confirm the transfected DNA, previously described sequencing was performed. 
In addition to the consideration of the protein sequence for the lack of binding, 
the protein might not folded properly or was damaged prior to the measurement as a result of unfavorable transport or buffer conditions. 

{{% figure id="11" title="Histogram of all constructs (K1, K2a, K2b, K2ab) added to CaCo cells to determine binding" src="/project/images/Histogram CaCo.png" %}}


## Bispecific antibody functionality

To test our bispecific antibodies’ functionality a chromium-51 release assay was performed. 
As the tested constructs do not possess a crystallizable fragment (Fc fragment) only a composite of the GPA33 binding and the CD3 binding scFv may facilitate killing. 
Tested were K1, K2a, K2b and the fused K2ab. Additional Rituximab, an anti CD20 binding antibody (Plosker & Figgitt, 2003) was used as negative control and Cetuximab, 
an epidermal growth factor receptor (EGFR) binding antibody was used as a positive control.
As described in Jonker et al., 2007 CaCo2 cells should express EGFR. However no sample showed an increasing amount of Cr-51, 
depicted in figure 12, indicating no killing in any sample. 
This is corroborated by the result that no GPA33 binding could be detected, as described previously. 

{{% figure id="12" title="Testing of the four constructs and two monoclonal antibodies in a Cr-51 release assay on CaCo cells" src="/project/images/Cr-51.png" %}}




# Artificial Neural Network "allerGEM"

Our allgerGEM achieved an accuracy of 99%. However, due to a bias in the relation of sequences with ten times more non-allergenic sequences than allergenic sequences, there are more reliant metrics for the performance of a binary classifier, like precision and recall. 

{{% figure id="13" title="Precision and recall." src="/awards/images/statistics-overview.svg" %}}

Our metric of choice was the area under curve (AUC) of the correctly allergenic labeled sequences plotted against the incorrectly allergenic labeled sequences. While an AUC value of 0.5 presents a random labeling and 1 perfectly labeled test data, our model scored a 0.985, and can thus be regarded as a quite successful classifier.

{{% figure id="14" title="Receiver operator curve" src="/awards/images/roc-final.png" %}}

## References

Atwell, J. L., et al., "scFv multimers of the anti-neuraminidase antibody NC10: length of the linker between VH and VL domains dictates precisely the transition between diabodies and triabodies.", *Protein engineering*, 1999:12(7), 597-604.

Frey, D. "Charakterisierung von gpA33 und Eignung als Antikörper-Target", 2011

Jonker, D. J., et al., "Cetuximab for the treatment of colorectal cancer.", *New England Journal of Medicine*, 2007:357(20), 2040-2048.

Keeble, A. H., et al., "Evolving accelerated amidation by SpyTag/SpyCatcher to analyze membrane dynamics.", *Angewandte Chemie International Edition*, 2017:56(52), 16521-16525.

Kochetov, A. V. "Alternative translation start sites and hidden coding potential of eukaryotic mRNAs.",  *Bioessays*, 2008:30(7), 683-691.

Plosker, G. L., & Figgitt, D. P. "Rituximab. Drugs", 2003:63(8), 803-843.

Schoene, C., et al., "SpyTag/SpyCatcher cyclization confers resilience to boiling on a mesophilic enzyme.", *Angewandte Chemie International Edition*, 2014:53(24), 6101-6104.