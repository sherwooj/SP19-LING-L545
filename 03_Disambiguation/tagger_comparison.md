# Comparison of POS Taggers

I ran 3 part of speech taggers on the UD_Finnish-TDT treebank:

  - UDPipe
  - Perceptron-based tagger
  - hunpos trigram HMM tagger


UDPipe had an accuracy of 94.64%, the perceptron-based tagger had 90.42% accuracy, and hunpos 
got 100% accuracy.

Hunpos got the best score, but I had to do more preprocessing of the data in order to evaluate 
it than I did for the other two taggers. It added two extra tabs to each line, which caused the 
evaluation program to fail because it handled the extra whitespace as two more features. I had to 
get rid of the white space before I could properly run the evaluator.