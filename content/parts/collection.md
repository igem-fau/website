---
title: Project Collection
color: purple 
---

The iGEM Team FAU_Erlangen 2019 created a part collection with all components to create different varieties of bispecific antibodies against the targets GPA33 on colon cancer and CD3 on T cells for eukaryotic and prokaryotic protein expression. The part collection consists of 21 parts ranging from BBa_K3117004 to BBa_K3117041.

The part collection of the team Erlangen is a toolbox to design a single chain fragment (scFv) bispecific antibody for eukaryotic and prokaryotic expression and a scFv bispecific antibody with the Tag and Catcher system as linker for eukaryotic and prokaryotic expression.


Antibodies are small molecules targeting distinct structures like surface markers. Our part collection provides the parts for the creation of bispecific antibodies which can bring T cells and colon cancer cells in a very close proximity (Mack et al. 1995). Therefore, the T cell can induce its cytotoxic properties and combat the cancer cells. Different kinds of targeting antibody fragments can be added to this part collection, resulting in new combinations for antibody design.

# Creation of a scFv bispecific antibody against CD3 and GPA33 linked by SpyTag/SpyCatcher

The SpyTag/SpyCatcher system is based on a modified domain from a streptococcus pyogenes surface protein (SpyCatcher), which recognizes a cognate 13-amino-acid peptide (SpyTag), which can bind spontaneously and form an isopeptide bond (Hatlem et al. 2019).

![Tag and Catcher](/project/images/TagCatchercells.svg)

  It is very suitable for the creation of a toolbox with a big variety of modular components, because SpyTag and SpyCatcher can be fused to arbitrary structures and create a binding.

Eukaryotic expression

For expression in HEK cells, the sequences of the constructs were firstly codon-optimized for mammalian expression.

  
## Construct 2b (including Tag) for mammalian expression:

![Construct_2b](/parts/images/Construct_2b_part.svg)

{{% accordion id="str1" title="BBa_K3117006: Igk leader" %}}

-   Igk is a leader sequence, which directs the secretion of proteins. It is cleaved off before the recombinant protein is secreted (Feng et al. 2011). It is used in construction 2b to secrete the protein to collect it from the harvest for further investigation.

{{% /accordion %}}

{{% accordion id="Str2" title="BBa_K3117015: SpyTag (eukaryotic expression)" %}}

-   The SpyTag is a short, unfolded peptide that can be genetically fused to exposed positions in target proteins. It is used in the construct to recognize the corresponding molecule, Catcher, and form a covalent isopeptide bond between the side chains of an reactive aspartate and lysine in SpyCatcher (Hatlem et al. 2019).

{{% /accordion %}}

{{% accordion id="str3" title="BBa_K3117024: ((Gly4)Ser) linker" %}}

-   The linker BBa_K3117024 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser) linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case one repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}

{{% accordion id="str4" title="BBa_K3117020: scFv heavy chain anti-CD3 (eukaryotic expression)" %}}

-   Part BBa_K3117020 is the single chain variable fragment of the heavy chain of an antibody targeting CD3. CD3 is co-expressed within the T cell receptor on T cells. Binding leads to downstream signalling cascades and activation of the T cell (Chetty und Gatter 1994). By binding CD3, the T cell can be activated. Regarding the whole bispecific antibody construct, the activated T cell can be brought in close proximity to the cancer cell by the surface marker GPA33 and combat the cancerous cell.

![Heavy chain CD3](/parts/images/Heavy_chain_CD3.svg)

{{% /accordion %}}

{{% accordion id="str5" title="BBa_K3117028: ((Gly4)Ser)x3 linker" %}}

-   The linker BBa_K3117028 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)3 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 4 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}


{{% accordion id="str6" title="BBa_K3117022: scFv light chain anti-CD3" %}}

-   Part BBa_K3117022 is the single chain variable fragment of the light chain of an antibody targeting CD3. CD3 is co-expressed within the T cell receptor on T cells. Binding leads to downstream signalling cascades and activation of the T cell (Chetty und Gatter 1994). By binding CD3, the T cell can be activated. Regarding the whole bispecific antibody construct, the activated T cell can be brought in close proximity to the cancer cell by the surface marker GPA33 and combat the cancerous cell.
 
![Light chain CD3](/parts/images/Light_chain_CD3.svg)

{{% /accordion %}}

{{% accordion id="str7" title="BBa_K3117005: 6xHis Tag" %}}

-   The 6xHis Tag was added to construct 2b for isolation of the recombinant protein by immobilized metal affinity chromatography experiments, in this case His SpinTrap (Booth et al. 2018).

{{% /accordion %}}

## Construct 2a (including Catcher) for mammalian expression:

![Construct_2a](/parts/images/Construct_2a_part.svg)

{{% accordion id="str8" title="BBa_K3117006: Igk leader" %}}

-   Igk is a leader sequence, which directs the secretion of proteins. It is cleaved off before the recombinant protein is secreted (Feng et al. 2011). It is used in construction 2a to secrete the protein to collect it from the harvest for further investigation.

{{% /accordion %}}

{{% accordion id="str9" title="BBa_K3117023: scFv light chain anti-GPA33" %}}

-   Glycoprotein A33 (GPA33) is a well-known surface marker of colon cancer. Under healthy conditions GPA33 is just expressed on gastric cells. On primary and metastatic colorectal cancers, GPA33 is overexpressed in 95% of primary and colorectal cancers (Carreras-Sangrà et al. 2012). The light chain of the single chain fragment targeting GPA33 was used to be fused to the other components of the bispecific antibody to target CD3 and GPA33.

![Light chain GPA33.svg](/parts/images/Light_chain_GPA33.svg)

{{% /accordion %}}

{{% accordion id="str10" title="BBa_K3117004: (Gly4)Ser)4 linker" %}}

-   The linker BBa_K3117004 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)4 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 4 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}

{{% accordion id="str11" title="BBa_K3117021: scFv heavy chain anti-GPA33" %}}

-   Glycoprotein A33 (GPA33) is a well-known surface marker of colon cancer. Under healthy conditions GPA33 is just expressed on gastric cells. On primary and metastatic colorectal cancers, GPA33 is overexpressed in 95% of primary and colorectal cancers (Carreras-Sangrà et al. 2012). The single chain fragment targeting GPA33 was used to be fused to the other components of the bispecific antibody to target CD3 and GPA33.

![Heavy chain GPA33](/parts/images/heavy_chain_GPA33.svg)

{{% /accordion %}}

{{% accordion id="str12" title="BBa_K3117024: ((Gly4)Ser) linker" %}}

-   The linker BBa_K3117024 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser) linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case one repeat of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}

{{% accordion id="str13" title="BBa_K3117016: SpyCatcher (eukaryotic expression)" %}}

-   The CnaB2 domain can be stably split into two components: a larger, incomplete immunoglobulin-like domain (termed SpyCatcher) of 138 residues (15 kDa) and a shorter peptide (SpyTag). SpyCatcher contains the reactive lysine and catalytic glutamate, which can bind to the reactive aspartate of SpyTag.

{{% /accordion %}}

{{% accordion id="str14" title="BBa_K3117005: 6xHis Tag" %}}

-   The 6xHis Tag was added to construct 2a for isolation of the recombinant protein by immobilized metal affinity chromatography experiments, in this case His SpinTrap (Booth et al. 2018).

{{% /accordion %}}

# Prokaryotic Expression

## Construct 2b (including Tag) for prokaryotic expression:

![Construct_2b](/parts/images/Construct_2b_part.svg)

For expression in *E.coli* bacteria, the sequences of the constructs were firstly codon-optimized for prokaryotic expression.

{{% accordion id="str15" title="BBa_K3117012: pelB leader sequence" %}}

-   pelB is a signal sequence, which can target recombinant proteins to the periplasmic space. It uses the post-translational translocation pathway (Singh et al. 2013). The secretion of the recombinant protein into the periplasma has distinct advantages like the oxidising environment for the formation of disulfide bonds, which does not occur in the reducing environment of the cytoplasm or foldases inside the periplasm which catalyse the formation and isomerisation of disulfide bonds (Schlegel et al. 2013).

{{% /accordion %}}

{{% accordion id="str16" title="BBa_K3117037: SpyTag (prokaryotic expression)" %}}

-   The SpyTag is a short, unfolded peptide that can be genetically fused to exposed positions in target proteins. It is used in the construct to recognize the corresponding molecule, Catcher, and form a covalent isopeptide bond between the side chains of an reactive aspartate and lysine in SpyCatcher (Hatlem et al. 2019).

{{% /accordion %}}

{{% accordion id="str17" title="BBa_K3117024: ((Gly4)Ser) linker" %}}

-   The linker BBa_K3117024 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser) linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case one repeat of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}

{{% accordion id="str18" title="BBa_K3117033: scFv heavy chain anti-CD3 (prokaryotic expression)" %}}

-   Part BBa_K3117022 is a single chain variable fragment of the heavy chain of an antibody targeting CD3. CD3 is co-expressed within the T cell receptor on T cells. Binding leads to downstream signalling cascades and activation of the T cell (Chetty und Gatter 1994). By binding CD3, the T cell can be activated. Regarding the whole bispecific antibody construct, the activated T cell can be brought in close proximity to the cancer cell by GPA33 and combat the cancerous cell.

![Heavy chain CD3](/parts/images/Heavy_chain_CD3.svg)

{{% /accordion %}}


{{% accordion id="str19" title="BBa_K3117028: (Gly4)Ser)3 linker" %}}

-   The linker BBa_K3117028 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)3 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case three repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}


{{% accordion id="str20" title="BBa_K3117035: scFv light chain anti-CD3 (prokaryotic expression)" %}}

-   Part BBa_K3117035 is the single chain variable fragment of the light chain of an antibody targeting CD3. CD3 is co-expressed within the T cell receptor on T cells. Binding leads to downstream signalling cascades and activation of the T cell (Chetty und Gatter 1994). By binding CD3, the T cell can be activated. Regarding the whole bispecific antibody construct, the activated T cell can be brought in close proximity to the cancer cell by GPA33 and combat the cancerous cell.

![Light chain CD3](/parts/images/Light_chain_CD3.svg)

{{% /accordion %}}


{{% accordion id="str21" title="BBa_K3117005: 6xHis Tag" %}}

-   The 6xHis Tag was added to construct 2b for isolation of the recombinant protein by immobilized metal affinity chromatography experiments, in this case His SpinTrap (Booth et al. 2018).

{{% /accordion %}}


## Construct 2a (including Catcher) for prokaryotic expression:

![Construct_2a](/parts/images/Construct_2a_part.svg)

{{% accordion id="str22" title="BBa_K3117012: pelB leader sequence" %}}

-   pelB is a signal sequence, which can target recombinant proteins to the periplasmic space. It uses the post-translational translocation pathway (Singh et al. 2013). The secretion of the recombinant protein into the periplasma has distinct advantages like the oxidising environment for the formation of disulfide bonds, which does not occur in the reducing environment of the cytoplasm or foldases inside the periplasm which catalyse the formation and isomerisation of disulfide bonds (Schlegel et al. 2013).

{{% /accordion %}}


{{% accordion id="str23" title="BBa_K3117036: scFv light chain anti-GPA33 (prokaryotic expression)" %}}

-   Glycoprotein A33 (GPA33) is a well-known surface marker of colon cancer. Under healthy conditions GPA33 is just expressed on gastric cells. On primary and metastatic colorectal cancers, GPA33 is overexpressed in 95% of primary and colorectal cancers (Carreras-Sangrà et al. 2012). The single chain fragment targeting GPA33 was used to be fused to the other components of the bispecific antibody to target CD3 and GPA33.

![Light chain GPA33.svg](/parts/images/Light_chain_GPA33.svg)

{{% /accordion %}}


{{% accordion id="str24" title="BBa_K3117004: (Gly4)Ser)4 linker" %}}

-   The linker BBa_K3117004 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)4 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 4 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}


{{% accordion id="str25" title="BBa_K3117034: scFv heavy chain anti-GPA33 (prokaryotic expression)" %}}

-   Glycoprotein A33 (GPA33) is a well-known surface marker of colon cancer. Under healthy conditions GPA33 is just expressed on gastric cells. On primary and metastatic colorectal cancers, GPA33 is overexpressed in 95% of primary and colorectal cancers (Carreras-Sangrà et al. 2012). The single chain fragment targeting GPA33 was used to be fused to the other components of the bispecific antibody to target CD3 and GPA33.

![Heavy chain GPA33](/parts/images/heavy_chain_GPA33.svg)

{{% /accordion %}}


{{% accordion id="str26" title="BBa_K3117024: ((Gly4)Ser) linker" %}}

-   The linker BBa_K3117024 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)1 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case one repeat of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}


{{% accordion id="str27" title="BBa_K3117038: SpyCatcher (prokaryotic expression)" %}}

-   The CnaB2 domain can be stably split into two components: a larger, incomplete immunoglobulin-like domain (termed SpyCatcher) of 138 residues (15 kDa) and a shorter peptide (SpyTag). SpyCatcher contains the reactive lysine and catalytic glutamate, which can bind to the reactive aspartate of SpyTag.

{{% /accordion %}}


{{% accordion id="str28" title="BBa_K3117005: 6xHis Tag" %}}

-   The 6xHis Tag was added to construct 2b for isolation of the recombinant protein by immobilized metal affinity chromatography experiments, in this case His SpinTrap (Booth et al. 2018).

{{% /accordion %}}


# Creation of a scFv bispecific antibody against CD3 and GPA33 linked by Glycine-Serine Linker

# Construct 1 (for eukaryotic expression)

For expression in HEK cells, the sequences of the constructs were at first codon-optimized for mammalian expression

![Construct_1_part](/parts/images/Construct_1_part.svg)

{{% accordion id="str29" title="BBa_K3117006: Igk leader" %}}

-   Igk is a leader sequence, which directs the secretion of proteins. It is cleaved off before the recombinant protein is secreted (Feng et al. 2011). It is used in construct 1 to secrete the protein to collect it from the harvest for further investigation.

{{% /accordion %}}


{{% accordion id="str30" title="BBa_K3117023: scFv light chain anti-GPA33" %}}

-   Glycoprotein A33 (GPA33) is a well-known surface marker of colon cancer. Under healthy conditions GPA33 is just expressed on gastric cells. On primary and metastatic colorectal cancers, GPA33 is overexpressed in 95% of primary and colorectal cancers (Carreras-Sangrà et al. 2012). The single chain fragment targeting GPA33 was used to be fused to the other components of the bispecific antibody to target CD3 and GPA33.

![Light chain GPA33.svg](/parts/images/Light_chain_GPA33.svg)

{{% /accordion %}}


{{% accordion id="str31" title="BBa_K3117004: (Gly4)Ser)4 linker" %}}

-   The linker BBa_K3117004 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)4 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 4 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}

{{% accordion id="str32" title="BBa_K3117021: scFv heavy chain anti-GPA33" %}}

-   Glycoprotein A33 (GPA33) is a well-known surface marker of colon cancer. Under healthy conditions GPA33 is just expressed on gastric cells. On primary and metastatic colorectal cancers, GPA33 is overexpressed in 95% of primary and colorectal cancers (Carreras-Sangrà et al. 2012). The single chain fragment targeting GPA33 was used to be fused to the other components of the bispecific antibody to target CD3 and GPA33.

![Heavy chain GPA33](/parts/images/heavy_chain_GPA33.svg)

{{% /accordion %}}


{{% accordion id="str33" title="BBa_K3117004: (Gly4)Ser)4 linker" %}}

-   The linker BBa_K3117004 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)4 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 4 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}


{{% accordion id="str34" title="BBa_K3117020: scFv heavy chain anti-CD3" %}}

-   Part BBa_K3117020 is the single chain variable fragment of the heavy chain of an antibody targeting CD3. CD3 is co-expressed within the T cell receptor on T cells. Binding leads to downstream signalling cascades and activation of the T cell (Chetty und Gatter 1994). By binding CD3, the T cell can be activated. Regarding the whole bispecific antibody construct, the activated T cell can be brought in close proximity to the cancer cell by the surface marker GPA33 and combat the cancerous cell.

![Heavy chain CD3](/parts/images/Heavy_chain_CD3.svg)

{{% /accordion %}}


{{% accordion id="str35" title="BBa_K3117028: ((Gly4)Ser)x3 linker" %}}

-   The linker BBa_K3117028 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)3 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 3 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}


{{% accordion id="str36" title="BBa_K3117022: scFv light chain anti-CD3" %}}

-   Part BBa_K3117022 is the single chain variable fragment of the light chain of an antibody targeting CD3. CD3 is co-expressed within the T cell receptor on T cells. Binding leads to downstream signalling cascades and activation of the T cell (Chetty und Gatter 1994). By binding CD3, the T cell can be activated. Regarding the whole bispecific antibody construct, the activated T cell can be brought in close proximity to the cancer cell by the surface marker GPA33 and combat the cancerous cell.

![Light chain CD3](/parts/images/Light_chain_CD3.svg)

{{% /accordion %}}


{{% accordion id="str37" title="BBa_K3117005: 6xHis Tag" %}}

-   The 6xHis Tag was added to construct 1 for isolation of the recombinant protein by immobilized metal affinity chromatography experiments, in this case His SpinTrap (Booth et al. 2018).

{{% /accordion %}}

# Construct 1 (for prokaryotic expression)

For expression in *E. coli* bacteria, the sequences of the constructs were at first codon-optimized for prokaryotic exrpression.

![Construct_1_part](/parts/images/Construct_1_part.svg)

{{% accordion id="str38" title="BBa_K3117012: pelB leader sequence" %}}

-   pelB is a signal sequence, which can target recombinant proteins to the periplasmic space. It uses the post-translational translocation pathway (Singh et al. 2013). The secretion of the recombinant protein into the periplasma has distinct advantages like the oxidising environment for the formation of disulfide bonds, which does not occur in the reducing environment of the cytoplasm or foldases inside the periplasm which catalyse the formation and isomerisation of disulfide bonds (Schlegel et al. 2013).

{{% /accordion %}}


{{% accordion id="str39" title="BBa_K3117036: scFv light chain anti-GPA33 (prokaryotic expression)" %}}

-   Glycoprotein A33 (GPA33) is a well-known surface marker of colon cancer. Under healthy conditions GPA33 is just expressed on gastric cells. On primary and metastatic colorectal cancers, GPA33 is overexpressed in 95% of primary and colorectal cancers (Carreras-Sangrà et al. 2012). The single chain fragment targeting GPA33 was used to be fused to the other components of the bispecific antibody to target CD3 and GPA33.

![Light chain GPA33.svg](/parts/images/Light_chain_GPA33.svg)

{{% /accordion %}}


{{% accordion id="str40" title="BBa_K3117004: (Gly4)Ser)4 linker" %}}

-   The linker BBa_K3117004 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)4 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 4 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}


{{% accordion id="str41" title="BBa_K3117034: scFv heavy chain anti-GPA33 (prokaryotic expression)" %}}

-   Glycoprotein A33 (GPA33) is a well-known surface marker of colon cancer. Under healthy conditions GPA33 is just expressed on gastric cells. On primary and metastatic colorectal cancers, GPA33 is overexpressed in 95% of primary and colorectal cancers (Carreras-Sangrà et al. 2012). The single chain fragment targeting GPA33 was used to be fused to the other components of the bispecific antibody to target CD3 and GPA33.

![Heavy chain GPA33](/parts/images/heavy_chain_GPA33.svg)

{{% /accordion %}}


{{% accordion id="str42" title="BBa_K3117004: (Gly4)Ser)4 linker" %}}

-   The linker BBa_K3117004 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)4 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 4 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}

{{% accordion id="str43" title="BBa_K3117033: scFv heavy chain anti-CD3 (prokaryotic expression)" %}}

-   Part BBa_K3117035 is the single chain variable fragment of the heavy chain of an antibody targeting CD3. CD3 is co-expressed within the T cell receptor on T cells. Binding leads to downstream signalling cascades and activation of the T cell (Chetty und Gatter 1994). By binding CD3, the T cell can be activated. Regarding the whole bispecific antibody construct, the activated T cell can be brought in close proximity to the cancer cell by the surface marker GPA33 and combat the cancerous cell.

![Heavy chain CD3](/parts/images/Heavy_chain_CD3.svg)

{{% /accordion %}}


{{% accordion id="str44" title="BBa_K3117028: (Gly4)Ser)3 linker" %}}

-   The linker BBa_K3117028 is composed of small, non-polar (Glycine) and polar (Serine) amino acids. (Gly4Ser)3 linker is one of the most widely used flexible linker that can sustain the bioactivity of fusion proteins. By adjusting the copy number, in this case 3 repeats of GGGGS, the length of this GS linker can be optimized to achieve appropriate separation of the proteins of interest (Chen et al. 2013).

{{% /accordion %}}


{{% accordion id="str45" title="BBa_K3117035: scFv light chain anti-CD3 (prokaryotic expression)" %}}

-   Part BBa_K3117035 is single chain variable fragment of the light chain of an antibody targeting CD3. CD3 is co-expressed within the T cell receptor on T cells. Binding leads to downstream signalling cascades and activation of the T cell (Chetty und Gatter 1994). By binding CD3, the T cell can be activated. Regarding the whole bispecific antibody construct, the activated T cell can be brought in close proximity to the cancer cell by the surface marker GPA33 and combat the cancerous cell.

![Light chain CD3](/parts/images/Light_chain_CD3.svg)

{{% /accordion %}}


{{% accordion id="str46" title="BBa_K3117005: 6xHis Tag" %}}

-   The 6xHis Tag was added to construct 2b for isolation of the recombinant protein by immobilized metal affinity chromatography experiments, in this case His SpinTrap (Booth et al. 2018).

{{% /accordion %}}


## References

Booth, William T.; Schlachter, Caleb R.; Pote, Swanandi; Ussin, Nikita; Mank, Nicholas J.; Klapper, Vincent et al. (2018): Impact of an N-terminal Polyhistidine Tag on Protein Thermal Stability. In: *ACS omega* 3 (1), S. 760–768. DOI: 10.1021/acsomega.7b01598.

Carreras-Sangrà, Nelson; Tomé-Amat, Jaime; García-Ortega, Lucía; Batt, Carl A.; Oñaderra, Mercedes; Martínez-del-Pozo, Alvaro et al. (2012): Production and characterization of a colon cancer-specific immunotoxin based on the fungal ribotoxin α-sarcin. In: *Protein engineering, design & selection* : PEDS 25 (8), S. 425–435. DOI: 10.1093/protein/gzs032.

Chen, Xiaoying; Zaro, Jennica L.; Shen, Wei-Chiang (2013): Fusion protein linkers: property, design and functionality. In: *Advanced drug delivery reviews* 65 (10), S. 1357–1369. DOI: 10.1016/j.addr.2012.09.039.

Chetty, R.; Gatter, K. (1994): CD3: structure, function, and role of immunostaining in clinical practice. In: *The Journal of pathology* 173 (4), S. 303–307. DOI: 10.1002/path.1711730404.

Feng, Yang; Gong, Rui; Dimitrov, Dimiter S. (2011): Design, expression and characterization of a soluble single-chain functional human neonatal Fc receptor. In: *Protein expression and purification* 79 (1), S. 66–71. DOI: 10.1016/j.pep.2011.03.012.

Hatlem, Daniel; Trunk, Thomas; Linke, Dirk; Leo, Jack C. (2019): Catching a SPY: Using the SpyCatcher-SpyTag and Related Systems for Labeling and Localizing Bacterial Proteins. In: *International journal of molecular sciences* 20 (9). DOI: 10.3390/ijms20092129.

Mack, M.; Riethmüller, G.; Kufer, P. (1995): A small bispecific antibody construct expressed as a functional single-chain molecule with high tumor cell cytotoxicity. In: *Proceedings of the National Academy of Sciences of the United States of America* 92 (15), S. 7021–7025. DOI: 10.1073/pnas.92.15.7021.

Schlegel, Susan; Rujas, Edurne; Ytterberg, Anders Jimmy; Zubarev, Roman A.; Luirink, Joen; Gier, Jan-Willem de (2013): Optimizing heterologous protein production in the periplasm of E. coli by regulating gene expression levels. In: *Microbial cell factories* 12, S. 24. DOI: 10.1186/1475-2859-12-24.

Singh, Pranveer; Sharma, Likhesh; Kulothungan, S. Rajendra; Adkar, Bharat V.; Prajapati, Ravindra Singh; Ali, P. Shaik Syed et al. (2013): Effect of signal peptide on stability and folding of Escherichia coli thioredoxin. In: *PloS* one 8 (5), e63442. DOI: 10.1371/journal.pone.0063442.