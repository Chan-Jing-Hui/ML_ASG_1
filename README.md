### python-app.yml
Located in .github/workflows folder. On push or pull request, run the quality_control job that downloads dependencies from requirements.txt needed to run the test_model.py, then runs test_model.py
### test_model.py 
Located in tests folder. Checks that the new model's rmse (Root Mean Squared Error) is less than 90% of the baseline model's, otherwise, error code is produced and check fails
### test_data.csv
Located in data folder. Contains the testing data used to evaluate models  
### model.pkl
Final version of registered model, determined to be the most suitable model  
### requirements.txt
Contains the libraries needed to run the test_model.py script

The current model in model.pkl is checked whenever a push or pull request is made. For new models to be checked, they must be exported and saved in the exact same format 'model.pkl'  
To run test_model.py locally, ensure that test_model.py, data/test_data.csv, and model.pkl are in the same directory

The test_model.py script produces an output stating the passing or failing status of the model. The test RMSE of the model is shown if the model passes, and both the test RMSE of the model and of the baseline model is shown if the model fails.
