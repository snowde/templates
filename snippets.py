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
  
touch ~/.bash_profile; open ~/.bash_profile

what I have:

# Setting PATH for Python 3.5
# The original version is saved in .bash_profile.pysave
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH

# added by Anaconda2 4.1.0 installer
export PATH="/Users/dereksnow/anaconda/bin:$PATH"
export PATH=$PATH:/Applications/Postgres.app/Contents/Versions/latest/bin   

  I don't think I should use pip install, I think I should use conda install. 
  
  If you are using python 3, you might want to use pip3 to install to conda otherwise it might install 2.
  
  sudo pip3 install requests
