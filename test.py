import pandas  as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from matplotlib import style
import matplotlib.dates as mdates
from matplotlib.ticker import MaxNLocator
# We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
sns.set(style="white", color_codes=True)
#import plotly.offline
import cufflinks as cf # requires pip install cufflinks
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)

df = pd.read_csv(r'C:/Users/Famubukky/Workspace.famubukky/pytest/Stroke.csv')
print(df)

df.info()

df.columns

df.isnull().sum()