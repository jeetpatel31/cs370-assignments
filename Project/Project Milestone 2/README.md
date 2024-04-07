Name of the assignment : Milestone 2

================================================

Date of submission : 04/07/2024

================================================

Instructions on how to run the code : 

You'll want to install some packages to get everything up and running. Mainly, leafmap and samgeo.

Creating a Map: We start by creating an interactive map using Leaf Map. This map lets us visualize satellite imagery and the segmentation results later on. You can center the map around a specific location and even choose the kind of satellite base map you want to see.

Downloading Images: The next step involves drawing a rectangle on the map to select the area you're interested in. This area's satellite image is then downloaded as a GeoTIFF file, which is just a fancy way of saying it's a high-quality image with geographic information attached.

Running the Segmentation: With our image downloaded, we then run the segmentation model. This part is cool because it's where the magic happens. The model segments the image, differentiating between various objects or features within it.

Visualizing the Result: After the segmentation, we can see the results right on the map. We can also compare the original satellite image with the segmented one, side by side, to see how well our model worked.

================================================

Instructions on how to run any tests (if applicable): 

This project doesn't specifically mention tests, but generally speaking, you'd want to check for a few things:

Make sure the environment is set up correctly and all dependencies are installed.

Test downloading images to see if the selected area is correctly captured.

Run the segmentation on different areas to ensure the model is consistently performing well.

================================================

Instructions on how to run any notebook (if applicable) :

You can run this in any env. Just choose GPU. This speeds things up significantly.

The notebook is laid out step-by-step. Just run each cell in order, from installing packages to visualizing the segmentation results. If there are instructions or comments in the notebook, they'll guide you through what each part does. And that's pretty much it!