{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from pygeocoder import Geocoder\n",
    "file = pd.read_csv(\"test_address.csv\",names = [\"Address\"])\n",
    "file[\"Address\"].str.strip()\n",
    "file\n",
    "for i in range(0,len(file.index)):\n",
    "    try:\n",
    "        geocoded = Geocoder.geocode(file.iloc[i])\n",
    "        file['Best_Predicted'][i]=geocoded.formatted_address\n",
    "        file['House_Street_No'][i]=geocoded.premise\n",
    "        file['Locality_Colony'][i]=geocoded.neighborhood\n",
    "        file['Area_Ward'][i]=geocoded.sublocality\n",
    "        file['City'][i]=geocoded.administrative_area_level_1\n",
    "        file['Pincode'][i]=geocoded.postal_code\n",
    "    except:\n",
    "        file['Best_Predicted'][i]=None\n",
    "        file['House_Street_No'][i]=None\n",
    "        file['Locality_Colony'][i]=None\n",
    "        file['Area_Ward'][i]=None\n",
    "        file['City'][i]=None\n",
    "        file['Pincode'][i]=None\n",
    "        \n",
    "file.to_csv('predicted_address.csv')\n",
    "\n",
    "# pygeocoder Usage Reference: https://bitbucket.org/xster/pygeocoder/wiki/Home"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
