'''@file deepclustering_loss.py
contains the DeepclusteringLoss'''

import tensorflow as tf
import loss_computer
from nabu.neuralnetworks.components import ops

class DeepclusteringLoss(loss_computer.LossComputer):
    '''A loss computer that calculates the loss'''

    def __call__(self, targets, logits, seq_length):
        '''
        Compute the loss

        Creates the operation to compute the deep clustering loss

        Args:
            targets: a dictionary of [batch_size x time x ...] tensor containing
                the targets
            logits: a dictionary of [batch_size x time x ...] tensor containing
                the logits
            seq_length: a dictionary of [batch_size] vectors containing
                the sequence lengths

        Returns:
            a scalar value containing the loss
        '''
                   
	outputs = logits['outputs']         
	binary_target=targets['binary_targets']            
	usedbins = targets['usedbins']
	seq_length = seq_length['features']
		    
	loss = ops.deepclustering_loss(binary_target, outputs, usedbins, 
					seq_length,self.batch_size)
            
        return loss
