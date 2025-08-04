# Install Guide
Please install vosk [API](https://repology.org/project/vosk-api/versions) and python for your distro. Before anything else.

```
git clone https://github.com/Tahosol/wakeup-for-freyja
cd wakeup-for-freyja
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

After this You will need to go into the python script to change the directory of model for vosk and path to freyja. Then you can make the script run on system boot by running
```
python /path/to/the/python/wakeup.py
```
