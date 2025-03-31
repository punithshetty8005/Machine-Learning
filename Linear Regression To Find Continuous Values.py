{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8264f9e9-1b39-49cc-98c8-874ab9f530be",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter the size of the house in sqft:  1600\n",
      "Enter the number of bedrooms:  3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Predicted price for a house with size 1600.0 sqft and 3 bedrooms: Rs.418163.93\n"
     ]
    }
   ],
   "source": [
    "import numpy as np \n",
    "from sklearn.linear_model import LinearRegression \n",
    "\n",
    "X = np.array([[1000, 2], [1500, 3], [1200, 2], [1800, 4], [900, 2], [2000, 3]]) \n",
    "y = np.array([300000, 400000, 350000, 500000, 280000, 450000]) \n",
    "\n",
    "model = LinearRegression() \n",
    "\n",
    "model.fit(X, y) \n",
    "\n",
    "size = float(input(\"Enter the size of the house in sqft: \")) \n",
    "bedrooms = int(input(\"Enter the number of bedrooms: \")) \n",
    "new_data = np.array([[size, bedrooms]]) \n",
    "\n",
    "predicted_price = model.predict(new_data) \n",
    "\n",
    "print(\"Predicted price for a house with size {} sqft and {} bedrooms: Rs.{:.2f}\".\n",
    "      format(size, bedrooms, predicted_price[0])) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2f5308a5-90c3-4937-abc6-720009d5b455",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
