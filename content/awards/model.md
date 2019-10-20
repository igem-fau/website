---
title: Model Your Project
color: red
---



# allerGEM

There are many obstacles in drug development. In fact around for around 37% the development process is terminated
already in the preclinical stage, and this even rapidly increases to 52% during the clinical phase I (Cook et al., 2014).
One of the many reasons are toxic side-effects and allergenic reactions. 

Since it was clear that during the course of this iGEM project we will not reach a clinical phase, we tried to deal with the 
question for allergenity pro-actively. Recognizing solely from the protein sequence if it allergenic or not could offer many
possibilites to detect potential problems of our construct design early-on in the development process.

Given the complexity of this task, it seems the perfect occasion to resort to deep learning and neural networks. In the last
years there were many astonishing examples, like Google's AlphaFold for protein folding, **TODO: 2 more examples** that
show the power of machine learning in science.

## Dataset

**TODO: Insert text here**

## Architecture

Based on the sequential nature of our input data, as well as the promising results of convolutional neural networks on protein sequences, we tailored a residual neural network for the task of predicting the allergencity of proteins. 

The first stage is an embedding that maps the protein sequences into a sequence in a higher dimensional space. This allows to already extract a large number of different features from the sequence before summarizing the information at last in a final assessment. This is possible since the protein distribution comprises a dense manifold within the incredibly complex space of possible sequences. 

The following steps are a concatenation of building blocks of similar topology with the task to summarize the information from the previous stages. For this, we first separate the input from the previous layers into two separate pathways: the first one leaves the input as is. But in the second one we manipulate the signal with three subsequent convolution kernels and a ReLU activation, two with a filter size of 3 in order to take into account the information of adjacent amino acids, and one of filter size 1. The result of both paths is then added together and pooled by pairs, only keeping the output of the neuron with the largest activation. Effectively this cuts the sequence into half with each residual building block.

What seems like an unnecessary complication has mere practical implications: by adding the output of the manipulated to the original one, the network focuses on small deviations. This allows to speed up the learning process. In effect this means that information is not discarded too early in the chain but is kept. This allows to draw better conclusions in total.

After several steps of these building blocks we finally take the information into account for the final prediction: this is obtained by a single neuron that is fully connected to all neurons from the preceding layer and uses a sigmoid activation to keep the output within a range between 0 and 1. 

![Architecture of our neural network](/awards/images/neural-network-architecture.svg)

In total this leaves us with a model with 128,000 trainable parameters. The model is built with the help of the popular TensorFlow library and trained on NVidia Kepler K80 GPUs offered at Google Colaboratory for free.

## How good is good?

In the end it is essential to make sure to quantify the success rate of our model. One metric that may come to mind is the *accuracy* of the model: from our test sequences, how many are classified correctly?
Already in the first tests we obtained promising accuracies of around 98-99%. However, there is a problem with judging the quality based on accuracy.

The reason for this is that much more sequences from non-allergens are known — and available to us in our dataset — than allergens. In fact, we have approximately 10 times more non-allergen protein sequences in the dataset than allergens. This makes the dataset highly unbalanced. 
As a result a completely lazy classifier that classifies every sequence as non-allergen will get an accuracy of over 90%. Clearly, this casts some doubt if this is a metric that is well-suited for judging the quality.

As a result we choose to look at *precision* and *recall* that are described in the following figure. They both have the advantage of being mostly insensitive to the unbalance in datasets.

{{< rawhtml >}}
<img class="w-2/3 mx-auto my-6" src="/awards/images/statistics-overview.svg" />
{{< /rawhtml >}}

Since our neural network outputs a decimal number in the range of 0 and 1 it is required to decide on some threshold. For all outputs that are smaller than this threshold we classify the sequence as non-allergenic, for all larger (or equal) outputs as an allergen. Since the definition *precision* and *recall* then implicitely depend on the chosen threshold -- for the true/false positives/negatives changes with the chosen value -- it is natural to check multiple values and compare them.

This is the idea of the *receiver operator curve* and *precision recall curve* that is shown in the following figures. In the former, we plot the recall, i.e. the percentage of the allergens that were found of our neural network, against the *false positive rate*. The main objective is, obviously, to maximize the recall while minimizing the number of false positives. 

The effectiveness of this can be summarized by calculating the area under the curve (AUC). The two baselines we can compare with are a random classifier that would obtain an AUC of 0.5 and the perfect classifier that obtains an AUC of 1. In our case we have an area of 0.985, which is generally considered a quite successful model in the industry.

{{< rawhtml >}}
<div class="flex justify-between">
<img class="w-1/2 h-auto my-6" src="/awards/images/roc-final.png" />
<img class="w-1/2 h-auto my-6" src="/awards/images/pr-final.png" />
</div>
{{< /rawhtml >}}

In addition, we collaborated with the german company imbus that specializes on software quality. They presented us a guideline
for best practices for machine learning projects and together we made sure that those are implemented within our neural network.
**TODO update**

## Use allerGEM

Thanks to tensorflowjs, *allerGEM* can also be run in the browser directly, which is why we make it available to everyone
directly on our wiki page. In the following box you can check your protein sequences for allergenicity. 

{{< floating-box id="allerGEM" title="allerGEM" >}}

<textarea id="sequence" onchange="resetStatus()" onkeyup="resetStatus()" class="bg-gray-100 font-mono outline-none border-transparent w-full p-4 rounded-lg my-2 h-56"></textarea>

<button class="outline-none fancy-btn-blue px-6 py-2 text-white" onclick="makePrediction()">Predict</button>

{{< /floating-box >}}

## The Biobrick Parts registry

The Biobrick parts registry constains many sequences, including many from the therapeutics track. Having our tool
at hand, we decided that it is useful to run the neural network against the registry. For this we employed the
FASTA collection provided by iGEM and offer a quick access to the results in the following box. 
It suffices to enter the id of the part to obtain the results from our neural network.

{{< floating-box id="parts-library" title="Parts Library" >}}

<h2 class="mb-4">Check the parts library</h2>

<input id="part" placeholder="BBA_" class="bg-gray-100 font-mono outline-none border-transparent w-full p-4 rounded-lg my-2" />

<button class="outline-none fancy-btn-blue px-6 py-2 text-white" onclick="makePrediction()">Show prediction</button>

<p class="text-xs my-4 text-gray-700">
The complete FASTA file of the parts library provided by iGEM is unfortunately not updated regularly, as a result 
not all the parts are contained in our file. For any missing part you can, however, use our network itself on the
protein sequence.
</p>

{{< /floating-box >}}

## Conclusion

Altogether, *allerGEM* shows the strength of deep learning and promising results. It was able to outperform existing models like,
XXX, XXX and XXX. Due to its generality, it is moreover quite simply to train the network on further properties, besides allergenity.
The required steps are to collect the corresponding data and retrain the model. With the help of transfer learning it may even be possible
to speed up the learning process by employing what was already learned by our existing model about protein sequences.

But keep in mind, in the end this is only a prediction based on the existing data and does not replace a 
clinical trial, it simply gives indications early-on in the development process.
