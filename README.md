Using the EU DOES data set as the training set, as it is freely available and contains the various categories of scrap at least in the EU. I also deleted the Background label from both data sets, as the test data had no images in the folder. Also moved the TEST folder out of the DOES folder

Link for the data here: https://zenodo.org/records/8219163

With the current structure on the test set, I am only achieving an accuracy of 67%, while the train accuracy is 98% and flatlined, so it's likely overfitting. I will try to combat that.

Structure has been updated to include more color bands and now has a 74% accuracy a 7% improvement. Will consider more options.

May 12, 2026
Made wepage you can run locally that will use your camera to capture a video feed and the once clicked will begin identifying if something is a piece of scrap metal and what type when put in frame. If it is not it will respond undefined. I don't have scrap metal but when passed test images it accurately classifies them. Will update the model if I reach higher accuracies. 
