Using the EU DOES data set as the training set, as it is freely available and contains the various categories of scrap at least in the EU. I also deleted the Background label from both data sets, as the test data had no images in the folder. Also moved the TEST folder out of the DOES folder

Link for the data here: https://zenodo.org/records/8219163

With the current structure on the test set, I am only achieving an accuracy of 67%, while the train accuracy is 98% and flatlined, so it's likely overfitting. I will try to combat that.

Structure has been updated to include more color bands and now has a 74% accuracy a 7% improvement. Will consider more options.
