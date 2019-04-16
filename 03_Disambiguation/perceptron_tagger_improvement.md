# Improving Perceptron Tagger

I added the following code to the _get_features function:

add('i-2 tag+i word', prev2, context[i])

This made the tagger's performance improve from 96.28% to 96.64%.