import os
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

class MtcarsModel(object):
    """
    Mtcars Model

    Model_method: LinearRegression
    Default_data: Mtcars.csv


    """
    def __init__(self, test_size = 0.2,random_state=42):
        self._data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'Data', 'mtcars.csv')
        self._test_size = test_size
        self._random_state = random_state
        self._model = LinearRegression()
        self._y_pred = None
        self._r_squared = None
        self._features = None
        self._rmse = None
        self._r2 = None
        self._sample_size = None
        self._dataframe = None
        self._is_trained = False

        
    def _load_data(self, path=None):
        """
        load csv files to dataframe
        """
        try:
            if path is None:
                path = self._data_path
            self._dataframe = pd.read_csv(path, index_col=0)

            # save all other features exclude the [label == mpg]
            self._features = [col for col in self._dataframe.columns if col != 'mpg']
            return self._dataframe
        
        except Exception as e:
            raise ValueError(f"Cannot load the csv file into Pandas dataframe: {e}")

    def _fit(self):
        """
        Perform linear regression using scikit-learn
        https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
        """
        results = {}
        if self._dataframe is None:
            self._load_data()

        # Features= X
        # target= y
        X = self._dataframe[self._features]
        y = self._dataframe['mpg']

        # test train split
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=self._test_size, random_state=self._random_state
        )

        # Train model
        self._model.fit(X_train, y_train)
 
        # Calculate metrics
        self._y_pred = self._model.predict(X_test)
        
        # Calculate R-squared and RMSE
        self._r_squared = r2_score(y_test, self._y_pred)
        self._rmse = mean_squared_error(y_test, self._y_pred, squared=False)
        self._sample_size = len(X_train)

        # return model training metrics as results 
        results = {
            'model': self._model,
            'predictions': self._y_pred,
            'rmse': self._rmse,
            'r2': self._r_squared,
            'coefficients': self._model.coef_,
            'intercept': self._model.intercept_
        }
        self._is_trained = True

        return results
    
    def _predict(self, X):
        """
        Make prediction using model
        """
        if not self._is_trained:
            raise ValueError("Model is not trained yet!! please _fit() first")
        # Make sure features matched
        X = X[self._features]

        return self._model.predict(X)

# def main():
#     M = MtcarsModel(test_size=0.2, random_state=42)
#     df = M._load_data()  # First load the data
#     M._fit()  # Train the model
    
#     # Make predictions on the same data
#     predictions = M._predict(df)
    
#     # Print some results
#     print("Predictions:", predictions)
#     print("R-squared:", M._r_squared)
#     print("RMSE:", M._rmse)


# if __name__ == "__main__":
#     main()
