# Supress unnecessary warnings so that presentation looks clean
import warnings
warnings.filterwarnings('ignore')

import pandas #provides data structures to quickly analyze data
#Since this code runs on Kaggle server, data can be accessed directly in the 'input' folder'

#Save the id's for submission file
ID = dataset_test['id']

# iloc creates a way for reading in a dataframe based on columns and rows.

PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH

Honestly I would scratch all this and install python, pip and virtualenv using homebrew so everything is in /usr/local/bin/

Editing Bash:
  
  Honestly I would scratch all this and install python, pip and virtualenv using homebrew so everything is in /usr/local/bin/
