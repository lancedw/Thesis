import numpy as np
import pandas as pd
from notebooks.data_loaders.utils import Utilities

class SequenceGenerator():

    @staticmethod
    # function to create sequences with one target column
    def create_single_step_sequences(
            input_data: pd.DataFrame, 
            output_feature_columns,
            input_sequence_length, 
            output_sequence_length, 
            episode_length, 
            n_episodes
        ):
        sequences= []

        # make sequences per episode, one sequence can only hold data of one and the same episode!
        for n in range(n_episodes):
            print(f"sequencing episode {n}...", end='\r')
            for l in range(episode_length-output_sequence_length-input_sequence_length+1):

                i = l+(n*episode_length)

                # sequence = input_data.iloc[i:i+input_sequence_length][input_feature_columns]
                sequence = input_data.iloc[i:i+input_sequence_length]

                target_position = i + input_sequence_length
                # target = input_data.iloc[target_position:target_position+output_sequence_length][output_feature_columns]
                target = input_data.iloc[target_position:target_position+output_sequence_length][output_feature_columns]
                
                sequences.append((sequence, target))

        return sequences

    @staticmethod
    # function to create sequences with PR inputs to PR outputs
    def create_PR_to_PR_sequences(
            input_data: pd.DataFrame, 
            input_sequence_length, 
            output_sequence_length, 
            episode_length, 
            n_episodes
        ):
        sequences= []

        # make sequences per episode, one sequence can only hold data of one and the same episode!
        for n in range(n_episodes):
            print(f"sequencing episode {n}...", end='\r')
            for l in range(episode_length-output_sequence_length-input_sequence_length+1):

                i = l+(n*episode_length)

                # sequence = input_data.iloc[i:i+input_sequence_length][input_feature_columns]
                sequence = input_data.iloc[i:i+input_sequence_length].transpose()

                target_position = i + input_sequence_length
                # target = input_data.iloc[target_position:target_position+output_sequence_length][output_feature_columns]
                target = input_data.iloc[target_position:target_position+output_sequence_length].transpose()

                sequences.append((sequence, target))

        return sequences

    @staticmethod
    # function to create sequences with image inputs to PR outputs
    def create_img_to_PR_sequences(
            input_data: pd.DataFrame, 
            input_images,
            input_sequence_length, 
            output_sequence_length,  
            episode_length, 
            n_episodes
        ):
        sequences= []

        # make sequences per episode, one sequence can only hold data of one and the same episode!
        for n in range(n_episodes):
            print(f"sequencing episode {n}...", end='\r')
            for l in range(episode_length-output_sequence_length-input_sequence_length+1):
                
                i = l+(n*episode_length)

                # grab image input tensors from list with img_tensors
                sequence = input_images[i:i+input_sequence_length]

                # grab pr output sequence from dataframe
                target_position = i + input_sequence_length
                target = input_data.iloc[target_position:target_position+output_sequence_length].transpose()

                sequences.append((sequence, target))

        return sequences

    @staticmethod
    # function to create sequences with image and PR inputs to PR outputs
    def create_ImgPR_to_PR_sequences(
            input_data: pd.DataFrame, 
            input_images,
            input_sequence_length, 
            output_sequence_length,  
            episode_length, 
            n_episodes
        ):

        sequences= []

        # make sequences per episode, one sequence can only hold data of one and the same episode!
        for n in range(n_episodes):
            print(f"sequencing episode {n}...", end='\r')
            for l in range(episode_length-output_sequence_length-input_sequence_length+1):
                
                i = l+(n*episode_length)

                # grab image input tensors from list with img_tensors
                img_sequence = input_images[i:i+input_sequence_length]
                pr_sequence = input_data[i:i+input_sequence_length]

                # grab pr output sequence from dataframe
                target_position = i + input_sequence_length
                target = input_data.iloc[target_position:target_position+output_sequence_length].transpose()

                sequences.append(((img_sequence, pr_sequence), target))

        return sequences