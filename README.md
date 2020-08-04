# CMSC6950_Traffic
CMSC6950 Project
#INSTALLATION and DEPENDENCIES
Cartopy and shapely have strong dependencies to dynamic libraries which may not be available on your system by default. If possible, install Anaconda, then:
conda install cartopy shapely
Then either with pip or from sources install the package as follows:
pip install traffic
python setup.py install
If you don't have Anaconda installed, you may install the package using command:
pip install traffic
However, due to strong dependencies mentioned before, you might get an error like: "Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output."
If so, run the command:
!apt-get -qq install python-cartopy python3-cartopy
and then,
pip install traffic
