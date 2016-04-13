#!/usr/bin/env python3

"""
Main script

Use python 3
"""

import os, sys
import numpy as np
import params
import utils
import vocabulary

# Parametters
nbEpoch = 150
learningRate = 0.1 # TODO: Replace by AdaGrad !!
regularisationTerm = 0.01 # Lambda

def main():
    print("Welcome into RNTN implementation 0.1")
    
    print("Parsing dataset, creating dictionary...")
    # Dictionary initialisation
    vocabulary.initVocab()
    
    # Loading dataset
    trainingSet = utils.loadDataset("trees/train.txt");
    testingSet = utils.loadDataset("trees/test.txt");
    #validationSet = loadDataset("trees/dev.txt");
    
    vocabulary.vocab.sort();
    
    print("Datasets loaded !")
    
    # Datatransform (normalisation, remove outliers,...) ??
    
    # Creating the model
    # TODO: Possibility of loading from file (default initialize randomly)
    # TODO: What is the best possible initialisation
    V  = np.random.rand(params.wordVectSpace, 2*params.wordVectSpace, 2*params.wordVectSpace) * params.randInitMaxValueNN # Tensor of the RNTN layer
    W  = np.random.rand(params.wordVectSpace, 2*params.wordVectSpace)                         * params.randInitMaxValueNN # Regular term of the RNTN layer
    Ws = np.random.rand(params.nbClass, params.wordVectSpace)                                 * params.randInitMaxValueNN # Softmax classifier
    #L = # Vocabulary (List of N words on vector, representation) << Contained in the vocab variable
    
    # TODO: Include the training in the cross-validation loop (tune parametters)
    # Main loop
    for i in range(nbEpoch):
        print("Epoch: ", i)
        
        # Randomly shuffle the dataset
        # trainingSet.shuffle()
        
        # Loop over the training samples
        for trainingSample in trainingSet: # Select next the training sample
            # Forward pass
            rntnOutput = trainingSample.computeRntn(V, W) # Evaluate the model recursivelly
            finalOutput = utils.softmax(np.dot(Ws, rntnOutput)) # Use softmax classifier to get the final prediction
            
            # Backward pass (Compute the gradients)
            gradientWs = np.dot(np.multiply(trainingSample.labelVect(), (np.ones(params.nbClass) - utils.softmax(np.dot(Ws, rntnOutput)))), np.transpose(rntnOutput))
            gradientWs += regularisationTerm * Ws
            
            # Update the weights
            Ws -= learningRate * gradientWs # Step in the oposite of the gradient
        
        # Compute new testing error
        
        # Saving the model (every X epoch)


if __name__ == "__main__":
    main()
