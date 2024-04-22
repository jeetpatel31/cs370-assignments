Name of the assignment : Milestone 3

================================================

Date of submission : 04/21/2024

================================================

Instructions on how to run the code :

The key steps involved are:

Load the image data and corresponding masks into NumPy arrays.
Split large images into smaller patches of a desired size for training.
Create a PyTorch dataset from the image patches and masks.
Define a custom PyTorch dataset class to handle bounding box prompts for SAM.
Set up the SAM model, optimizer, and loss function for fine-tuning.
Train the model on the custom dataset for a specified number of epochs.
Save the fine-tuned model's state dictionary.
Load the fine-tuned model for inference on new images.
Provide prompts (bounding boxes or point grids) to the model for segmentation.
Visualize the segmentation results on test images.



================================================

Instructions on how to run any tests (if applicable):

As for running tests, the code does not explicitly include any test cases. However, you can validate the performance of the fine-tuned model by running inference on a separate set of test images and evaluating the segmentation results qualitatively or quantitatively 

================================================

Instructions on how to run any notebook (if applicable) :

You can run this in any env. Just choose GPU. This speeds things up significantly.

The notebook is laid out step-by-step. Just run each cell in order, from installing packages to visualizing the segmentation results. If there are instructions or comments in the notebook, they'll guide you through what each part does. And that's pretty much it!