---
title: Model Your Project
color: red
---

Modern computational methods provide invaluable tools for biological research. In this year's iGEM project we focused on
two powerful methods to aid us in the whole process of designing our constructs. On one hand, we conducted molecular simulations 
of peptide linkers for improved protein characteristics, while on the other hand establishing an artificial neural network to 
pro-actively detect potential allergenic protein sequences.

# Molecular dynamics simulations

## Why we simulated

Over the last decades biological research has revealed more and more complex features of living systems. But now we are at a point, where purely laboratory work cannot embrace all of life’s intriguing facettes, either because the dimensions are often too small to be observed directly or because molecular interactions are too complicated and fast to be seen directly.
To facilitate the investigation of such systems and the construction of novel biological systems, like designer drugs or nanomaterials, numerous applications have been developed. One such tool are molecular dynamics simulations. We took advantage of such a system rationally design our bispecific antibody.

{{% accordion id="MD-sims" title="What are MD-simulations" %}}
The basic principle of molecular dynamics (MD-) simulations is to define a virtual composition of solvent molecules on your machine, embed the molecules of interest and tell the machine the physical rules to apply to all molecules. Subsequently, you let the computer calculate the position and momentum of every molecule at every time point, being limited in resolution and simulation time almost only by the computational resources at hand.
{{% /accordion  %}}

## What and how we simulated

For our project, we used the free version "AmberTools18" in order to simulate potential peptide linkers to facilitate rational decision making concerning the actual implemented linker for the synthesized bispecific antibody.

### Simulated molecules

For specifying the exact sequence of our peptide linker we simulated two types of proteins, commonly used in fusion proteins, in an all-atomistic (AA) fashion. One is the _(G4S)n_ linker, where _G4S_ is the abbreviation for _Gly-Gly-Gly-Gly-Ser_, and n stands for the number of repeats of this motif within the linker. This linker is known to establish a flexible conformation, as can be seen in the video above  when applied to connect parts of a fusion protein \[Huston et al. 2018\]. Moreover, the combination of flexible and hydrophobic residues reduces the likelihood of interactions between the linker and the functional domains of the fusion protein \[Marqusee 1987\]. This linker type was simulated before the wet-lab started with the aim of finding the motif repeat of choice for yielding most probably a functional protein. The other simulated linker has the sequence motif _(EA3K)n_, where _EA3K_ is short for _Glu-Ala-Ala-Ala-Lys_, and _n_ stands again for the number of motif repeats within the linker. This linker is known to adapt a helical conformation \[Różycki et al. 2017\] (see video below) and was simulated simultaneously to the synthesis of our bispecific antibody in order to optimize the linker composition of following constructs. Motif repeats were _n = {2, 3, 4, 6, 8}_ for both linkers. 

{{% figure id="1a" title="(G4S)4 conformations" src="/awards/images/g4s4_5fps_EDIT.gif" %}}
{{% figure id="1b" title="(EA3K)4 conformations" src="/awards/images/EA3K_5fps_EDIT.gif" %}}

### Simulation specifications

Both linkers were simulated under the same conditions. First, the sequences and their necessary files for simulations were generated using tLEaP. This includes coordinate files and topology files.

Subsequently, energy minimization was performed for 1000 cycles to allow the generated structures to relax, before the actual simulation.

Then, the system was equilibrated, meaning that the volume was warmed from 100 K to 310 K over 200 ps.
Finally, the linker was simulated in implicit solvent for 400 ns with a time step of 2 fs and by using the ff14SB force field.

The lengths of the peptides were determined by measuring the direct distance between the {{% rawhtml %}}&alpha;{{% /rawhtml %}}-C atoms of the first and the last amino acid within the particular linker. The coordinates during the simulations were saved in 100 ps time steps.

## Rational Linker Choice

### Results

The images below show the distribution of conformation lengths for each linker with vertical dashed lines indicating its average end-to-end distance, respectively.

{{% figure id="2a" title="Length distribution of the (G4S)n linker" src="/awards/images/g4s_hist.png" %}}

{{% figure id="2b" title="Length distribution of the (EA3K)n linker" src="/awards/images/eak_hist.png" %}}

Furthermore, it appears that the length of a linker is linearly dependent on the number of amino acids of which it is made of and only the slope of this linear function depends on the conformation of the linker.

{{% figure id="3" title="Average length against number of amino acids" src="/awards/images/l_vs_n.png" %}}

This also shows that the (EA3K)n linker possesses a longer average length, when compared with the (G4S)n linker, for any number of motif repeats within our simulations. This results are consistent with a recent study published by Różycki et al. \[Różycki et al. 2016\]. 

### Why we favoured _(G4S)4_

According to Klein et al., the diameter of an scFv is about 35 Å \[Klein et al. 2009\]. Our own distance calculations of the scFv fragment from the pdb entry 3h3b using pymol resulted in an average diameter of about 42 Å. We calculated the distance between the C-terminal {{% rawhtml %}}&alpha;{{% /rawhtml %}}-C atom of the V<sub>H</sub> region (where the linker to the complement scFv is attached) and {{% rawhtml %}}&alpha;{{% /rawhtml %}}-C atoms of residues lying at the outer border of the protein. This can be seen in the video below. The V<sub>H</sub> and V<sub>L</sub> regions are colored in red and green, respectively. The linker would be attached at the yellow marked atom. The aforementioned {{% rawhtml %}}&alpha;{{% /rawhtml %}}-C atoms are presented as spheres.

![<scFv domain>](/awards/images/lscFv.gif)

Former studies have shown that a short linker can impair the functional properties of domains within fusion proteins. In general, too close distances between protein domains may destabilize the whole protein conformation, thus impairing its functionality \[Vazana et al. 2013, Arai et al. 2001, Arai et al. 2004\]. Additionally, simulations by Robinson-Mosher et al. \[Robinson-Mosher et al., 2013\] came to the conclusion that the actual distance between domains of linker-tethered proteins was multiple times closer than the attachment points of the linker connecting the domains. So, in order to maintain protein flexibility while still securing a certain distance between the scFv regions, our chosen linker should possess approx. half the diameter of the attached domain. Thus, we excluded the linkers (G4S)2 and (G4S)3, which adapted average end-to-end distances of 14.7 Å and 18.6 Å, respectively. On the other hand, we did not want to include more motif repeats than necessary for successful expression, because with the number of homologous repeats within a sequence rises the probability of deletion of sequence parts during cloning experiments, thereby diminishing the control over the final protein sequence and conformation.

### A potential alternative

While expressing the designed antibody in the wet-lab, we investigated the aforementioned _(EA3K)n_ linker in-silico. The underlying rationale is that  the peptides helical conformation keeps the two domains of the protein distant from each other and preventing potential interaction between them \[Arai et al. 2001\]. The formation of a relatively stiff helix can be deduced from the comparison between the _(G4S)n_ and the _(EA3K)n_linkers, where for each number of repeats the _(EA3K)n_ linker has on average a bigger physical length than the more flexible _(G4S)n_ linker. This can also be seen in the video showing the _(EA3K)4_ linker conformations. Another reason for implementing a stiffer linker lies within the nature of the T-cell receptor (TCR). Previous studies have shown that mechanical forces acting on the T-cell receptor initiate TCR signalling \[Li et al. 2010\].

Since the expression of our bispecific antibody was successful using the _(G4S)4_ linker, which established an average length of 21.4 Å in our simulations, we advice to also express the antibody using the _(EA3K)3_, which showed an average length of 20.5 Å. Due to the stiffness and length of the _(EA3K)3_ linker, we assume that upon binding of such an antibody to both, the T-cell as well as the target cell, an amplified activation of the T-cell due to sher forces may occur.

## Computational limitations

Due to limited computational resources, we only simulated our linkers without attached domains at both ends. However, for flexibe linkers up to a length of 15 amino acids, no significant difference was observed when performing AA MD-simulations whether with spheres up to a radius of 28 Å attached to both linker ends or without any additional residue  \[Różycki et al. 2016\]. These results strengthen our confidence that our results are valid approximations of the attributes of such linkers within the actual engineered protein and worthy to be considered for rational decisions regarding the design of the protein of interest.

Albeit widely used in experimental research and being standard parts for linking protein parts together, the utilized linker types and peptide linkers in general show only scarse computational investigation regarding their actual physical length and their conformations in an all-atomistic fashion and when applied to antibody fusion proteins within the literature. Our study aims to present a step to close this gap and to engage further research in this area in order to predict the effect of different linker compositions and lengths on the engineered fusion protein and to anticipate potential problems before they even occur in the wet-lab.

# Deep Learning 

There are many obstacles in drug development. In fact, for around 37% of all drugs under development the process is terminated already in the preclinical stage, and this even rapidly increases to 52% during the clinical phase I \[Cook et al. 2014\]. One of the many reasons are toxic side-effects and allergic reactions.

Since it was clear that during the course of this iGEM project we will not reach a clinical phase, we tried to deal with the question for allergenicity pro-actively. Recognizing potential allergenicity solely from the protein sequence would offer many possibilities to detect implicit problems of our construct design early-on in the development process.

Given the complexity of this task, it seems the perfect occasion to resort to deep learning and neural networks. In the last years emerged many astonishing examples concerning protein features, like Google’s AlphaFold for predicting protein tertiary structures \[Evans et al. 2018\], the DEEPred for predicting a protein’s function \[Rifaioglu et al. 2019\], or the task to predict protein interactions \[Zhang et al. 2019\]. These examples  show the power of machine learning in biological disciplines. 

## Dataset

To train our network we gathered data from various peer reviewed databases which have been categorizing allergens for the past 10 to 15 years \[Goodman 2016, Mari 2004, Ivanciuc 2003, Fiers 2004\]. The collected data contains a ratio of 90% non-allergens to 10% allergens and was randomly split into training-, validation- and test-data, while maintaining the allergen to non-allergen ratio in each of the splits. The training set, which amounts for 60% of data points, is used to provide examples for the neural network to fit the internal parameters, whereas the validation data is used for monitoring the progress of the training process on unseen data points. Ultimately, the training is concluded with the test set, where the final performance can be quantified and potential overfitting can be detected. Validation- and test-sets each amount for 20% of data entries.

For statistical evaluation of our model, we split our data using a k-fold cross validation approach. Therefore, we split our data into 5 equally sized groups and used every possible arrangement of these groups as training-, validation-, and test data. Using this approach, one can observe whether the performance of the resulting model is consistent between the different data splits, implying independence from the used data. Additionally, by providing these splits, the model becomes highly reproducible.

## Architecture

Based on the sequential nature of our input data, as well as the promising results of convolutional neural networks on protein sequences, we tailored a residual neural network for the task of predicting the allergenicity of proteins. \[Wang, Sheng 2017\]

The first stage is an embedding that maps the protein sequences into a sequence in a higher dimensional space. This already allows to extract a large number of different features from the sequence before summarizing the information at last in a final assessment. This is possible since the protein distribution comprises a dense manifold within the incredibly complex space of possible sequences. 

The following steps are a concatenation of building blocks of similar topology with the task to summarize the information from the previous stages. For this, we first separate the input from the previous layers into two separate pathways: the first one leaves the input as is. But in the second one we manipulate the signal with three subsequent convolution kernels and a ReLU activation, two with a filter size of 3 in order to take into account the information of adjacent amino acids, and one of filter size 1. The result of both paths is then added together and pooled by pairs, only keeping the output of the neuron with the largest activation. Effectively this cuts the sequence into half with each residual building block.

What seems like an unnecessary complication has mere practical implications: by adding the output of the manipulated to the original one, the network focuses on small deviations. This allows to speed up the learning process. In effect this means that information is not discarded too early in the chain but is kept. This allows to draw better conclusions in total. \[He, Kaiming 2016\]

After several steps of these building blocks we finally take the information into account for the final prediction: this is obtained by a single neuron that is fully connected to all neurons from the preceding layer and uses a sigmoid activation to keep the output within a range between 0 and 1. 

{{% figure id="4" title="Architecture of our neural network" src="/awards/images/neural-network-architecture.svg" %}}

In total this leaves us with a model with 128,000 trainable parameters. The model is built with the help of the popular TensorFlow library and trained on NVidia Kepler K80 GPUs offered at Google Colaboratory for free.

## How good is good?

In the end it is essential to make sure to quantify the success rate of our model. One metric that may come to mind is the accuracy of the model: from our test sequences, how many are classified correctly?
Already in the first tests we obtained promising accuracies of around 98-99%. However, there is a problem with judging the quality based on accuracy.

The reason for this is that much more sequences from non-allergens are known — and available to us in our dataset — than allergens. In fact, we have approximately 10 times more non-allergen protein sequences in the dataset than allergens. This makes the dataset highly unbalanced. 
As a result a completely lazy classifier that classifies every sequence as non-allergen will get an accuracy of over 90%. Clearly, this casts some doubt if this is a metric that is well-suited for judging the quality.

As a consequence we choose to look at precision and recall that are described in the following figure. They both have the advantage of being mostly insensitive to the unbalance in datasets.

{{% figure id="5" title="Precision and recall" src="/awards/images/statistics-overview.svg" %}}

Since our neural network outputs a decimal number in the range of 0 and 1, it is required to decide on some threshold. For all outputs that are smaller than this threshold we classify the sequence as non-allergenic, for all larger (or equal) outputs as an allergen. Since the definition precision and recall then implicitly depend on the chosen threshold -- for the true/false positives/negatives changes with the chosen value -- it is natural to check multiple values and compare them.

This is the idea of the receiver operator curve (ROC) and precision recall curve (PRC) that is shown in the following figures. In the former, we plot the recall, i.e. the percentage of the allergens that were found of our neural network, against the false positive rate. The main objective is, obviously, to maximize the recall while minimizing the number of false positives. 

The effectiveness of this can be summarized by calculating the area under the curve (AUC). The two baselines we can compare with are a random classifier that would obtain an AUC of 0.5 and the perfect classifier that obtains an AUC of 1. In our case we have an area of 0.985, which is generally considered a quite successful model in the industry.

{{< rawhtml >}}
<div class="flex justify-between">
<img class="w-1/2 h-auto my-6" src="/awards/images/roc-final.png" />
<img class="w-1/2 h-auto my-6" src="/awards/images/pr-final.png" />
</div>
{{< /rawhtml >}}

Those results could be consistently reproduced, independent of the chosen data split, which further indicates that our neural network is able to extract proper features to predict the allergenicity of proteins.

## Network Conclusion

Altogether, allerGEM shows the strength of deep learning and promising results. It was able to outperform existing models, like \[Kuo-Bin 2004\] and \[Mohabatkar, 2013\]. Due to its generality, it is moreover quite simply to train the network on further properties, besides allergenicity.
The required steps are to collect the corresponding data and retrain the model. With the help of transfer learning it may even be possible to speed up the learning process by employing what was already learned by our existing model about protein sequences.

But keep in mind, in the end this is only a prediction based on the existing data and does not replace a clinical trial, it simply gives indications early-on in the development process.

## Use allerGEM

Thanks to tensorflows, allerGEM can also be run in the browser directly, which is why we make it available to everyone directly on our wiki page. In the following box you can check your protein sequences for allergenicity. The sources of our neural network, together with the trained model can be found on our [github repository](https://github.com/igem-fau/allerGEM).

{{< allerGEM model="https://raw.githubusercontent.com/igem-fau/allerGEM/master/final/model.json" >}}

## The Biobrick Parts registry

The Biobrick parts registry contains many sequences, including many from the therapeutics track. Having our tool at hand, we decided that it is useful to run the neural network against the registry. For this we employed the FASTA collection provided by iGEM and offer a quick access to the results in the following box. It suffices to enter the id of the part to obtain the results from our neural network.

{{< predict-parts-registry url="https://raw.githubusercontent.com/igem-fau/allerGEM/master/final/parts_registry.json" >}}

## References

Arai R., et al., "Conformations of variable linked chimeric proteins evaluated by synchroton X-ray small-angle scattering", _Proteins_, 2004:57, 829-838

Arai R., et al., "Design of the linkers which effectively separate domains of a bifunctional fusion protein", _Protein Eng._, 2001:14, 529-532

Evans R., et al.  "De novo structure prediction with deep-learning based scoring" _In Thirteenth Critical Assessment of Techniques for Protein Structure Prediction (Abstracts)_, 1-4 December 2018

Fiers, M. W., et al., "Allermatch™, a webtool for the prediction of potential allergenicity according to current FAO/WHO Codex alimentarius guidelines.", _BMC bioinformatics_, 2004:5(1), 133

Goodman, R. E., et al., "AllergenOnline: a peer‐reviewed, curated allergen database to assess novel food proteins for potential cross‐reactivity." _Molecular nutrition & food research_, 2016:60(5), 1183-1198

He, K., et al., "Deep residual learning for image recognition.", _In Proceedings of the IEEE conference on computer vision and pattern recognition_, 2016, 770-778

Huston, J. S., et al., "Protein engineering of antibody binding sites: recovery of specific activity in an anti-digoxin single-chain Fv analogue produced in Escherichia coli.", _Proceedings of the National Academy of Sciences_, 2018:85, 5879-5883

Ivanciuc, O., et al., "Detecting potential IgE-reactive sites on food proteins using a sequence and structure database, SDAP-food.", _Journal of agricultural and food chemistry_, 2003:51(16), 4830-4837

Klein, Joshua S., et al. "Examination of the contributions of size and avidity to the neutralization mechanisms of the anti-HIV antibodies b12 and 4E10." _Proceedings of the National Academy of Sciences_, 2009:106.18, 7385-7390.

Li K., Issac P., and Krishnan, A. "Predicting allergenic proteins using wavelet transform." _Bioinformatics_, 2004:20.16, 2572-2578.

Li K., Ya-Chen, et al. "Cutting Edge: mechanical forces acting on T cells immobilized via the TCR complex can trigger TCR signaling.", _The Journal of Immunology_, 2010:184.11, 5959-5963.

Mari, A., & Riccioli, D., "The Allergome Web Site-a database of allergenic molecules. Aim, structure, and data of a web-based resource.", _Journal of Allergy and Clinical Immunology_, 2004:113(2), 301

Marqusee S., Baldwin R.L., "Helix stabilisation by Glu-...Lys+ salt bridges in short peptides of de novo design", _Proc. Natl. Acad. Sci. U.S.A._, 1987:84, 8898-8902

Mohabatkar, H., et al. "Prediction of allergenic proteins by means of the concept of Chou's pseudo amino acid composition and a machine learning approach.", _Medicinal Chemistry_ 2013:9.1, 133-137.

Rifaioglu, A. S., et al. "DEEPred: Automated Protein Function Prediction with Multi-task Feed-forward Deep Neural Networks." _Scientific reports_, 2019:9.1, 7344

Robinson-Mosher A. et al., "Dynamics simulations for engineering macromolecular interactions", _Chaos: An Interdisciplinary Journal of Nonlinear Science_, 2013:23.2, 025110

Różycki B., and Cieplak M., "Stiffness of the C-terminal disordered linker affects the geometry of the active site in endoglucanase Cel8A.", _Molecular BioSystems_, 2016:12, 3589-3599

Różycki B., et al., "The length but not the sequence of peptide linker modules exerts the primary influence on the conformations of protein domains in cellulosome multi-enzyme complexes", _Physical Chemistry Chemical Physics_, 2017:19, 21414-21425

Van Rosmalen M., Krom M., Merkx M, "Tuning the Flexibility of Glycine-Serine Linkers To Allow Rational Design of Multidomain Proteins", _Biochemistry_ 2017:56(50), 6565-6574

Vazana Y. et al., "A synthetic biology approach for evaluating the functional contribution of designer cellulosome components to deconstruction of cellulosic substrates", _Biotechnology for Biofuels_, 2013:6, 1822+

Wang, S., et al., "Accurate de novo prediction of protein contact map by ultra-deep learning model.", _PLoS computational biology_, 2017:13(1), e1005324.

Zhang, L., et al., "Protein–protein interactions prediction based on ensemble deep neural networks.", _Neurocomputing_, 2019:324, 10-19