---
title: Project Inspiration and Description
color: green
---

# How it came about: Our fascination for Antibody Engineering and Modularity

{{< rawhtml >}}
<div class="mx-auto w-1/2 my-20">
    <img class="shadow-lg rounded-lg" src="/project/images/PHOTO-2019-01-13-18-18-30.jpg">
    <div class="text-center mt-4">Our kick-off weekend</div>
</div>
{{< /rawhtml >}}

In order to find a project idea, our student leaders organised a kickstart week-end. It didn’t take long for the students of the special masters course in? Integrated immunology to excite the other students to face the challenges and potential immunology has to offer synthetic biologists. The Bispecific T-cell engager (BiTE) caught our fascination as a modular construct and served as inspiration for creating a similar Bispecific Antibody (BsAb). Removed of problematic components for prokaryotic expression, such as the glycolysation, it seemed ideal to be expressed in parts or as a whole .

# BsAb structure and function

The BsAb, short for Bispecific Antibody, is a fusion protein composed of two antigen binding fragments coupled together via a linker. Although the sequence derives from a somatic antibody, an antigen binding fragment is a single peptide chain, called single chain variable Fragment (scFv). Thus, it is not solely connected through disulfide-bridges, as is the case with somatic antibodies (Sedykh et al. 2018). One antigen binding fragment is specific to T-cell surface structures by recruiting T-cells. Whilst the other antigen binding Fragment on the other end is specific to unwanted cells, such as cancer cells. In turn it brings T-cells bound on the other end of the BsAb in direct vicinity. In this manner BsAbs can be used to target aberrant tissues very locally, in contrast to the broad effect of chemotherapy, especially in the phase of metastasizing cancer cells.

{{% figure id="1" title="BsAbs with different linkers" src="/project/images/Bispecific antibodies.svg" %}}

We set out designing our modular BsAbs. The diagram above depicts a construct linking SpyTag and SpyCatcher. The components SpyTag and SpyCatcher are separate peptide sequences, each fusioned respectively to a scFv (single chain variable fragment) containing only one antigen binding site and forming half a BsAb each. Such subunits can be expressed in co-cultures, later linked irreversibly by an in-vitro isopeptide reaction of SpyTag with SpyCatcher. This seemed very promising for modularity.

Firstly a set of different effector subunits could be expressed with varying affinities or functions, i.e. different antigen specificities or enzymatic activity.

Secondly subunits are linked in vitro, configured to the BsAb most suited to the treatment situation.

Furthermore different expression systems could be used, with the BsAb broken down into short length sequences ideal for DNA vectors. Thereby the possible problem of producing a large, complex protein that could result in the formation of insoluble aggregates can be avoided. We therefore focused on the SpyTag/SpyCatcher linked BsAb.

Our wet-lab team decided to test three different designs inspired by the BsAb, which differ in their linker:

{{< rawhtml >}}
<ol style="list-style: decimal !important; margin-left: 20px;">
<li class="my-4" style="padding-left: 10px;">SpyTag/SpyCatcher system linking two scFvs (single chain variable fragment)</li>
<li class="my-4" style="padding-left: 10px;">Chemical ligation of four fragments</li>
<li class="my-4" style="padding-left: 10px;">BsAb expressed as a whole unit and as standard of comparison</li>
</ol>
{{< /rawhtml>}}
    

For the details and further literature of our design see the design page.

In the process of explaining the details of bispecific antibodies to other team members a section of our team devoted to informatics, chemistry, and computational biology saw their opportunity to implement molecular dynamic simulations and neural networks for antibody engineering. Having defined parts of the therapeutic agent it turned out that the linking component would be key to proper functioning, as it determines not only the modular potential but also stability and binding affinity of the BsAb on the whole.

# Setting our project

We chose the setting of colorectal cancer to apply our ideas and achieve a comprehensive approach to fight the disease. Colorectal cancer is still the second-largest cause of cancer-related death. The major hurdles of traditional treatments are the negative side effects of the treatment and the problem of targeting and eliminating secondary tumours (Kuipers et al. 2015; Steeg 2016 and Noone A. M. et al. 2018). Bispecific antibodies, such as the Bispecific T-cell Engager (BiTE) are a promising approach to overcome these hurdles, enabling immune-cells to target colorectal cancer cells specifically (Graber K. 2014).

{{% figure id="2" title="Non recognition of tumor cells vs.  BsAB in action" src="/project/images/BsAB_cancer cells.svg" %}}

Our BsAb is geared against CD3 on T-lymphocytes and GPA33. GPA33 can be found on 95% of all colorectal cancer cells, thereby allowing them to be specifically targeted (Heath et al. 1997). By also binding CD3, the BsAb can bring cytotoxic T-lymphocytes (CTLs) into direct contact with the cancer cells, which activates the CTLs to release their cytotoxic granules and kill the malignant cell (Osada et al. 2010; Gruber et al. 1994).

# Wet lab and Proof of Concept

Since the application of bispecific antibodies is a relatively new approach, current protocols for their production are not yet standardized. In most cases mammalian cells are used for the expression of these proteins. However, this expression system is associated with very high costs and proves to be very time-consuming. The use of the bacterial host Escherichia coli poses an alternative for the expression of recombinant protein. It is well published and provides many advantages over the expression in mammalian cells. The cultivation is far cheaper due to the higher proliferation rate and faster protein production. Despite these benefits, producing proteins of mammalian origin in E. coli has shown to be difficult since post-translational modifications are often vital to protein folding and function and cannot be replicated in these bacterial systems. Especially for complex proteins like antibodies, misfolding is often detrimental for their solubility and performance (Spadiut et al. 2014; Liu und Huang 2018; Lee und Jeong 2015). A solution however would be the periplasmic expression of recombinant protein, as this offers an oxidizing environment that is beneficial for correct protein folding, as well as a reduced number of proteases that may degrade our protein (Liu und Huang 2018; Thie et al. 2008). For this reason, we plan to use a PelB leader sequence to transport our constructs to the periplasm of E. coli for synthesis.

By using a variety of expression systems, we can determine the most efficient one for our purposes. We are going to use a pET27b plasmid with a T7 promoter and lacZ control, as well as a pACYC184 plasmid with a ptac promoter in the E. coli strains BL21, BL21 Star and Tuner. For eukaryotic expression we will use the HEK cell line.

**Our intermediate steps to reach our ultimate goal of producing one modular Tag and Catcher BsAb are:**

{{< rawhtml >}}
<ol style="list-style: decimal !important; margin-left: 20px;">
<li class="my-4" style="padding-left: 10px;">Designing the sequences</li>
<li class="my-4" style="padding-left: 10px;">Transfection and Transformation of our different constructs in different prokaryotic and eukaryotic stems</li>
<li class="my-4" style="padding-left: 10px;">Expression, yield and purification</li>
<li class="my-4" style="padding-left: 10px;">First test: Western blot</li>
<li class="my-4" style="padding-left: 10px;">Linking</li>
<li class="my-4" style="padding-left: 10px;">Second test and proof of concept: cytotoxic killing essays</li>
</ol>
{{< /rawhtml>}}

Due to difficulties with ethical regulations we decided to use the professional network of FAU and cooperated with Prof. Dr. Matthias Peipp to get help with the Cytotoxic Killing Assays. See Documentation on Experiments page.

With MD-simulations (molecular dynamics) of our linker sequences the stability and binding affinity of the product can be analysed. Furthermore, the use of neural networks should allow us to predict allergenicity of bispecific antibody prototypes, thus reducing costly stalemate wet-lab endeavours and thereby integrating different disciplines and rounding off our comprehensive approach.

{{< rawhtml >}}
<div class="mx-auto w-2/3 my-20">
    <img class="rounded-lg" src="/project/images/BsAb_Workflow.svg">
</div>
{{< /rawhtml >}}

## References

1.  Sedykh, Sergey E.; Prinz, Victor V.; Buneva, Valentina N.; Nevinsky, Georgy A. (2018): Bispecific antibodies: design, therapy, perspectives. In: Drug design, development and therapy 12, S. 195–208. DOI: 10.2147/DDDT.S151282.
    
2.  Kuipers, Ernst J.; Grady, William M.; Lieberman, David; Seufferlein, Thomas; Sung, Joseph J.; Boelens, Petra G. et al. (2015): Colorectal cancer. In: Nature reviews. Disease primers 1, S. 15065. DOI: 10.1038/nrdp.2015.65.
    
3.  Noone A. M., et al.: SEER Cancer Statistics Review, 1975-2015, National Cancer Institute. National Cancer Institute. Bethesda, MD 2018.
    
4.  Garber K.: Bispecific antibodies rise again. Nature Reviews Drug Discovery 2014:13, 799–801
    
5.  Heath, J. K.; White, S. J.; Johnstone, C. N.; Catimel, B.; Simpson, R. J.; Moritz, R. L. et al. (1997): The human A33 antigen is a transmembrane glycoprotein and a novel member of the immunoglobulin superfamily. In: Proceedings of the National Academy of Sciences of the United States of America 94 (2), S. 469–474. DOI: 10.1073/pnas.94.2.469.
    
6.  Osada, T.; Hsu, D.; Hammond, S.; Hobeika, A.; Devi, G.; Clay, T. M. et al. (2010): Metastatic colorectal cancer cells from patients previously treated with chemotherapy are sensitive to T-cell killing mediated by CEA/CD3-bispecific T-cell-engaging BsAb antibody. In: British journal of cancer 102 (1), S. 124–133. DOI: 10.1038/sj.bjc.6605364.
    
7.  Spadiut, Oliver; Capone, Simona; Krainer, Florian; Glieder, Anton; Herwig, Christoph (2014): Microbials for the production of monoclonal antibodies and antibody fragments. In: Trends in biotechnology 32 (1), S. 54–60. DOI: 10.1016/j.tibtech.2013.10.002.
    
8.  Liu, Yongkang; Huang, He (2018): Expression of single-domain antibody in different systems. In: Applied microbiology and biotechnology 102 (2), S. 539–551. DOI: 10.1007/s00253-017-8644-3.
    
9.  Lee, Yong Jae; Jeong, Ki Jun (2015): Challenges to production of antibodies in bacteria and yeast. In: Journal of bioscience and bioengineering 120 (5), S. 483–490. DOI: 10.1016/j.jbiosc.2015.03.009.

