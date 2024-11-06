#

# Install

```bash
virtualenv -p python3 venv3 ;
source venv3/bin/activate &&

pip install argparse requests matplotlib scipy pandas
```

# Use

```bash
python3 measure/main.py -r 10 -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
python3 analysis/main.py -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
```
