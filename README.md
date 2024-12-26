# CodeBERT Siamese Network for Code Clone Detection

## Overview
This repository contains the implementation of a Siamese neural network using CodeBERT for semantic code clone detection. The model was trained and evaluated on the GPTCloneBench dataset, achieving an AUC-ROC score of 96.2%.

## 😄 A Note About Code Clones
Yes, you're seeing multiple nearly identical Jupyter notebooks in this repository. The irony of creating code clones while developing a code clone detection tool is not lost on me! This was done intentionally to preserve different experimental results, as Jupyter notebooks override cell outputs when rerun. Consider it a practical demonstration of why we need code clone detection tools 😉

## Dataset
To replicate our results:
1. Download the original GPTCloneBench dataset from [[link](https://github.com/srlabUsask/GPTCloneBench)]
2. Place the data in the `GPTCloneBench/` directory
3. Follow the data preparation for each programming language ('c', 'cs', 'py', 'java') by running 'extract_functions.py' for the true_semantic_clones and the false_semantic_clones (you will find the directory of the false semantic clones commented inside the script) 
4. modify and run contrastive_learning_csv_build.py for each programming language


## important note:
the dataset for the C language is different, since it was originally geneated for Triplet loss function training.



## Acknowledgments
- The authors of CodeBERT and GPTCloneBench
