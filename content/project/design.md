---
title: Design
color: green
---

The aim of the project was to create different variants of bispecific antibodies. 
For this in total seven different constructs were designed and modified to fit into different vectors and expressions systems. 
In order to get a better hold of which of these constructs belongs to one another in order to create a functional bispecific antibody the names go as follows:

{{% rawhtml %}}<div style="padding-top: 50px;"></div>{{% /rawhtml %}}

**Construct 1 (K1)**: Codes for a whole bispecific T cell engager. 
Parts:  BBa\_K3117029[K1 eucaryotes](http://parts.igem.org/Part:BBa_K3117029) (eucaryotes) and BBa\_K3117046 [K1 E.coli](http://parts.igem.org/Part:BBa_K3117046) (*E. coli*)

**Construct 2 (K2a/K2b)**: Bispecific antibody realized in two subconstructs with SpyTag/SpyCatcher as a connectivity module between CD3 and GPA33 binding heads. 
Parts eucaryotes: BBa\_K3117026 [K2a eucaryotes](http://parts.igem.org/Part:BBa_K3117026) (K2a) 
and BBa\_K3117030[K2b eucaryotes](http://parts.igem.org/Part:BBa_K3117030) (K2b)
Parts *E.coli*: BBa\_K3117047 [K2a E. coli](http://parts.igem.org/Part:BBa_K3117047) (K2a) 
and BBa\_K3117048 [K2b E. coli](http://parts.igem.org/Part:BBa_K3117048) (K2b)

**Construct 3 (K3a/K3b)**: CD3 antigen binding fragment (Fab) split in two subconstructs coding for either the light or heavy chain. 

**Construct 4 (K4a/K4b)**: GPA33 Fab split in two subconstructs coding for either the light or heavy chain. 

{{% rawhtml %}}<div style="padding-top: 50px;"></div>{{% /rawhtml %}}

This design allows us to create three differently linked bispecific antibody types. 
In K1 the antigen binding regions are connected by a flexible Glycine-Serine Linker (BBa\_K3117004) [GS Linker](http://parts.igem.org/Part:BBa_K3117004)), commonly used in fusion proteins (Trinh et al. 2004). 
Whereas K2 relies on SpyTag/SpyCatcher, a system introduced by Mark Howarth. This allows to create fusion proteins by adding the SpyTag to one protein and the SpyCatcher to another. 
Once those proteins get into close contact a spontaneous binding, between Asparagin and Lysin residue in the protein segments, occurs forming a covalent bond (Hatlem et al., 2019). 

In our project this allows to create a bispecific antibody with the potential to not only create one antibody, but a whole toolbox of bispecific antibodies. 
This provides the possibility to screen a wide variety of bispecific antibody combinations for their efficacy in less time and with less effort.

{{% figure id="1" title="Visualization of a bispecific antibody, linked with the SpyTag/SpyCatcher system." src="/project/images/TagCatchercells.svg" %}}

The constructs were prepared for expression in mammalian and prokaryotic cells with special adjustments for several expression vectors. 
While Gibson assembly was the method of choice for cloning, construct design still wanted to give as much flexibility as possible. 
For this reason, the overhangs needed for Gibson assembly were not already synthesized with the constructs but added later via PCR.



## Overview of all-important protein domains

**GPA33**: The variable regions of the heavy and light chain of an antibody against GPA33 are linked with a [G4S]4 linker. GPA33 is a surface marker of colorectal cancer cells. 
Under healthy conditions GPA33 is just expressed on gastric cells. (Kataoka Shiro, 2007 EP 1 801 208 A1)

**CD3**: The variable regions of the heavy and light chain of an antibody against CD3 are connected via a [G4S]3 linker. 
CD3 is co-expressed with the T cell receptor on T cells. Binding leads to downstream signaling cascades and activation of the T cell. 

**Igk leader**: Is a signal peptide leading to protein secretion into the supernatant. The Igk leader is cleaved of during this process. 
Adding of this Leader allows easy protein gathering from supernatant without having to lyse the cells.

**HisTag**: Six His residues form a His-Tag which is commonly used for protein purification and detection is added to each construct. 
Detection in a western blot and purification with HisTrap columns is performed with produced proteins.

**StrepTag**: This tag consisting out of eight amino acids (Trp-Ser-His-Pro-Gln-Phe-Glu-Lys) is a short affinity tag commonly used in protein purification and detection assays. 
Detection of Strep-Tag can be performed with Streptavidin or Strep-Tactin, which has a much higher affinity.

**SpyTag**: The SpyTag segment is designed to bind its partner SpyCatcher. 
In addition to a His-Tag in the sequence, the protein can be detected with an anti-SUMO antibody in a western blot. 

**SpyCatcher**: The SpyCatcher segment is the binding partner of SpyTag. 
ErlangenTag: The Erlangen Tag is added to many constructs to diversify the 5' sequence, as the sequence 3' of the stop codons is highly repetitive due to the His Tag. 
Thus, the Erlangen Tag allows us to create better conditions for primer binding and serves as a special trademark for our teams, constructs.

**Kappa-Light chain**: Human Kappa-Light chain was used in K3b and K4b to create Fab fragments. 
Ig1 Ch1: Human Ig1 Ch1 domain was used to create functional Fab fragments together with the Kappa-Light chain.


## Overview of Construct Assembly for cloning

K1, K2a and K2b were prepared for expression in *E. coli* and mammalian cells. 
The leader depicted in the figures below is therefore dependent on whether the construct is modified for expression in prokaryotic or eukaryotic cells.

{{% figure id="2" title="Overview of all created constructs (K1, K2a, K2b, K3a, K3b, K4a, K4b). The later constructs (K3a, K3b, K4a, K4b) were not modified for expression in mammalian cells and thus were designed with the peIB secretion leader sequence. K1, K2a and K2a were designed for expression in pro- and eukaryotic cells. For this reason, the secretion leader sequence was either peIB for prokaryotic expression or the IgKappa-leader. Lac operator was only present in constructs designed for prokaryotic cells." src="/project/images/All_constructs_overview.svg" %}}


## *E. coli* expression

### pACYC184

For the *E. coli* expression pACYC184 was chosen as it is a relatively small vector making cloning easier. 
The Vector carries two antibiotic resistances against Chloramphenicol and Tetracyclin. 
Both resistances are superior to Ampicillin resistance in securing successful cloning, as they are facilitating actual death of prokaryotic cells with out the resistance instead of just hindering the growth (Kehrenberg et al., 2005). 
Every construct designed for this vector carried its own promotor, ribosomal binding site and peIB leader and a 3' His Tag. 
In order to compensate the highly repetitive region at the 3' region which makes binding primers a difficult task the ERLANGEN Tag was introduced to create a larger variety and better conditions for primer binding. 
Each construct was prepared for Gibson assembly and classical restriction cloning. Primers and PCR Layout was performed according to the layout in figure 3. 

{{% rawhtml %}}
<div>
    <img class="w-2/3 mx-auto" src="/project/images/PCR_Layout_K3,4.png" />
    <div class="block w-2/3 mx-auto my-12 text-center">
    <p class="inline-block font-bold">Figure 3</p>: PCR Layout for K3 and K4. The depicted layout shows the process of Gibson overhang generation and subsequent fusion of the subconstructs. Step 0 shows the first amplification step, preparing the constructs for the actual overhang generation. Within this step large parts of the Erlangen Tag are lost and only a small rudiment remains. Step 1 is dedicated to overhang generation for Gibson assembly prolonging the constructs on either side. The subconstruct with the suffix a (K3a, K4a) receive a 5' overhang for the pACYC184 vector and a 3' overhang fitting the respective construct with suffix b (K3b, K4b). The b constructs do not receive a 5' overhang but a 3' overhang fitting to the pACYC184 vector.  This layout assured directional cloning with polycistronically expressed constructs, yielding functional Fab fragments
    </div>
</div>
{{% /rawhtml %}}

## Used Vector

### pSEC/tag2/Hygro/C/-/OK

This vector, kindly provided by Prof. Matthias Peipp, carries a Hygromycin resistance and is suited for protein expression in mammalian cell systems (Makrides et al., 1999). 
Its CMV promotor allows constitutive high yield protein expression. Besides the Resistance the vector carries a large variety of restriction sites, 
a T7 promotor 3' of the CMV promotor for easy PCR amplification, an IgKappa Leader for protein export into the supernatant and a Myc Epitop and His-Tag for purification steps. 
The way this vector was used it was cut with NheI and EcoRV, cleaving the IgKappa Leader and large parts of the multiple cloning site. NheI creates a 5' vector overhang, whereas EcoRV is a blunt cutting enzyme. 
The decision to excise this part was taken in order to set the desired protein sequence directly adjacent to the leader sequence, avoiding any additional undesired amino acids. 
Other features of the vector such as the Myc-Epitope or the His-Tag were not used as the constructs already possess at least one His-Tag.

## References

Trinh, R., Gurbaxani, B., Morrison, S. L., & Seyfzadeh, M. (2004). Optimization of codon pair use within the (GGGGS) 3 linker sequence results in enhanced protein expression. Molecular immunology, 40(10), 717-722.

Hatlem, D., Trunk, T., Linke, D., & Leo, J. C. (2019). Catching a SPY: Using the SpyCatcher-SpyTag and Related Systems for Labeling and Localizing Bacterial Proteins. International journal of molecular sciences, 20(9), 2129.
	
Kehrenberg, C., Schwarz, S., Jacobsen, L., Hansen, L. H., & Vester, B. (2005). A new mechanism for chloramphenicol, florfenicol and clindamycin resistance: methylation of 23S ribosomal RNA at A2503. Molecular microbiology, 57(4), 1064-1073.

Makrides, S. C. (1999). Components of vectors for gene transfer and expression in mammalian cells. Protein expression and purification, 17(2), 183-202.