# Predicting Academic Performance #                   

### Deployment on Heroku ###
https://final-project-heroku-2.herokuapp.com/

## INTRODUCTION ##

Education is a key factor for achieving long term economic progress. Our project intends to approach student achievement in secondary education using Machine Learning modeling techniques. 

Should we care about Student Performance models? 
YES

One approach is to utilize machine learning to build predictive models of student performance. Through the ethical collection of student data, via academic records and surveys, a model can be created to anticipate where resources can be focused to boost student performance. This targeted application of resources can be more efficient and proactive than traditional models, with the ability to help students before warning signs appear.

For example, through predictive modeling, a tutor can be assigned before a student falls behind; or, programs can more actively provide resources to students who might be disadvantaged for various socio-economic factors.

## DATA ##

Source: https://archive.ics.uci.edu/ml/datasets/student+performance

The Math and Portuguese data csv files were loaded and merged.

Checked for nulls and renamed the columns for better understanding.

Created final grade column for letter grades A+:18-20 A:16-17 B:14-15 C:10-13 & F<10.

## ANALYSIS AND VISUALIZATIONS ##

Once the data was cleaned and merged, we created our initial Model. We used Random Forest Classifier. We used the students final grade as label, and sorted the rest of factors based on their weight. Then we analyzed the main and interesting factors and created visualizations. We used Python Pandas Matplotlib and Seaborn library for data analysis and statistical data visualizations. These are the seven questions we analyzed.

Does parent’s education level affect the kid’s performance?

Is there a gap in performance between rural and urban students?

Is alcohol consumption associated with poor academic performance?

Should the students be allowed to go out with friends frequently?

How important is attendance in academic performance?

How does students Quarter-1 and Quarter-2 scores impact Final grade?

Are aspirations for higher education important?

## FURTHER RESEARCH ##

We also have a further research page, where we have listed the interesting reads about the studies and research done in the field of higher education and predictive analytics. Pointers for anyone intrested in the doing further research.

## MODEL ##

Before constructing a model, the data had to be processed for optimal learning. This included converting all columns with text values into integers. For the columns with only two different values, a list comprehension was used to binary-encode the data. Columns with multiple text values ('mother_job', 'father_job', 'reason') were split up into multiple binary-encoded columns using the pandas.get_dummies() function. Finally, the 'Pass_Fail' column was one-hot-encoded.

Neural Network- Got an accuracy 77.39%

Our first attempt was a neural network with 41 input features, 41 neurons in the first hidden layer, 20 neurons in the second hidden layer, and 2 outputs: Pass or Fail. The sklearn preprocessing StandardScaler() function was used to condense the X data around 0, thus decreasing the model's bias.

Randon Forest Network- Got an accuracy 81.22%

With a baseline score from the neural network, we began to explore other classifiers to maximize the accuracy of our predictions. Our next model was a Random Forest Classifier made up of 200 individual decision trees that each give a class prediction, and the class with the most 'votes' is chosen as the model's prediction.

Logistic Regression- Got an accuracy 84.67%

The last basic model was a Logistic Regression, a model that uses the sigmoid function to sort datapoints into two classes. Since this model produced the best results out of the three we had tested so far, we decided to do additional research into Logistic Regressions to see what optimizations could be made, and how far we could push the accuracy.

Optimized Logistic Regression- Got an accuracy 92.03%

We were able to implement to modules that drastically improved the performance of the model: over sampling and recursive feature elemination. The imblearn (imbalanced learn) SMOTE() function takes the testing portion of a dataset and synthesizes new X and y pairs such that each class (in this case "Pass" and "Fail") has the same amount of samples. Note that because these samples are only added to the training data, the accuracy of the model on the testing data is not falsely skewed. Recursive feature elemination iterates through a succession of models, assigning weights to each 'feature' (columns in the X dataset) and removing the least impactful feature with each iteration until the specified number of features is reached. Thus, our model is only trained on the features that have the highest correlation, and becomes more accurate. With these two optimizations, our final logistic regression is able to predict whether a student will pass or fail an upcoming class based on eight simple survey questions (see Predict page), with 92% accuracy.

We saved our final model to Test_Score_LR_v2.pkl pickle file.

## PREDICT ##

We used python flask. For the predict page we used GET method to load the page and POST method when the form is submitted. Which run the model to display the predictions based on the input parameters. And displayed the final predictions "This Student is Likely to Pass" or "This Student is at Risk of Failing".

## CONCLUSION ##

We hope our prediction tool can be used to help schools and parents improve the students overall school performance. As a direct outcome of this project, more efficient student prediction tools can be developed, improving the quality of education and enhancing school resource management. The results show that a good predictive accuracy can be achieved, provided that we have access to socio-economic data from various school districts.

October-November 2020
