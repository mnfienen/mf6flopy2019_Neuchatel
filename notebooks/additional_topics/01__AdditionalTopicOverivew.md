Additional Topics Overview
-----------------------------------------------

### jupyter Notebook Examples

We've added a few topics we weren't able to cover in the class this week. Please feel free to browse these.

##### ***In this folder***

+ An overview of grid intersection which can be used to identify model grid cells that intersect features from shapefiles. This example updates a model with a realistic strem.  *03-Intersection-Capabilities-completed.ipynb* 

+ A particle tracking example using MODPATH 7 along with MODFLOW 6 is provided in the notebook *06_modpath-completed.ipynb*

+ A class project building a model from datasets is in the notebook *ClassModel-completed.ipynb*

+ One application of automating model runs is to set up a model, observe the simulated flow in a stream, and then stress the model with wells in all model cells. This can return a map of depletion potential (e.g. how much baseflow is reduced due to pumping at each area of the model). This is a metric of vulnerability. The notebook *Automating-Model-Runs-completed.ipynb* is a demonstration of how to set this up. Note that this setup indicates how other types of automation could work like evaluating a suite of realizations of hydraulic conductivity, for example.

##### ***In the DataAnalysisUsingPandas folder***
There are three notebooks using `pandas` for data analysis (these are not related to MODFLOW)

+ An example using input from an Excel file to explore weather patterns is in *Pandas\_weather\_timeseries\_Wunderground.ipynb*. This explores various time-series manipulation and some cool plotting with Rose plots.

+ The notebook *Pandas\_ColoradoRiver.ipynb* uses `pandas` to explore flow in the Colorado River near the Grand Canyon. 

+ The notebook *Pandas_ColoradoRiver-FFT.ipynb* applied Fourier analysis to the Colorado River time series to explore characteristic frequency of the signal before and after the Glen Canyon dam was built and filled in 1963.
