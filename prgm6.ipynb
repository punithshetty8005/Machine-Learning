{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "419aa8ba-349c-4df4-8975-b7d554b53fa4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Data after handling missing values:\n",
      "    Age  Gender   Income\n",
      "0  25.0  Female  50000.0\n",
      "1  30.0    Male  60000.0\n",
      "2  29.5    Male  45000.0\n",
      "3  28.0  Female  56250.0\n",
      "4  35.0    Male  70000.0\n",
      "\n",
      "Data after categorical encoding:\n",
      "   Gender_Female  Gender_Male\n",
      "0            1.0          0.0\n",
      "1            0.0          1.0\n",
      "2            0.0          1.0\n",
      "3            1.0          0.0\n",
      "4            0.0          1.0\n",
      "\n",
      "Data after feature scaling:\n",
      "   Scaled Age  Scaled Income\n",
      "0   -1.382164      -0.727778\n",
      "1    0.153574       0.436667\n",
      "2    0.000000      -1.310001\n",
      "3   -0.460721       0.000000\n",
      "4    1.689312       1.601112\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.impute import SimpleImputer\n",
    "from sklearn.preprocessing import OneHotEncoder, StandardScaler\n",
    "data = {\n",
    "    'Age': [25, 30, None, 28, 35],\n",
    "    'Gender': ['Female', 'Male', 'Male', 'Female', 'Male'], \n",
    "    'Income': [50000, 60000, 45000, None, 70000]\n",
    "}\n",
    "  \n",
    "df = pd.DataFrame(data) \n",
    "\n",
    "imputer = SimpleImputer(strategy='mean') \n",
    "df[['Age', 'Income']] = imputer.fit_transform(df[['Age', 'Income']]) \n",
    "\n",
    "print(\"Data after handling missing values:\") \n",
    "print(df) \n",
    "\n",
    "encoder = OneHotEncoder() \n",
    "encoded_data = encoder.fit_transform(df[['Gender']]).toarray() \n",
    "\n",
    "encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Gender'])) \n",
    "\n",
    "print(\"\\nData after categorical encoding:\") \n",
    "print(encoded_df) \n",
    "\n",
    "scaler = StandardScaler() \n",
    "\n",
    "scaled_data = scaler.fit_transform(df[['Age', 'Income']]) \n",
    " \n",
    "scaled_df = pd.DataFrame (scaled_data, columns=['Scaled Age', 'Scaled Income']) \n",
    "print(\"\\nData after feature scaling:\") \n",
    "print(scaled_df) \n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37966c6f-52c6-42ba-905b-5e55dc28957d",
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
