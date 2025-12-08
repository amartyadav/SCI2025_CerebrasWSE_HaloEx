### 1. Install Lima and QEMU using Homebrew
Make sure you have [Homebrew](https://brew.sh/) installed on your Apple Silicon Mac. Then, open a terminal and run the following commands to install Lima and QEMU:
```bash
brew install lima qemu
```
### 2. Set up an x86 VM with Lima
The following config.yml is provided as an example, with your Mac’s home directory and /tmp/lima mounted as writeable directories:
```yaml
vmType: "qemu"

images:
- location: "https://cloud-images.ubuntu.com/releases/22.04/release-20231130/ubuntu-22.04-server-cloudimg-amd64.img"
  arch: "x86_64"
  digest: "sha256:7edc2eccf1e34df23d9561b721b6fed381c3b6e8c916c91c71bbce7b8488b496"

arch: "x86_64"

# max/base mean the maximum/minimum features supported by the host system
cpuType:
  x86_64: "max"

ssh:
  loadDotSSHPubKeys: false

mounts:
- location: "~"
  writable: true
- location: "/tmp/lima"
  writable: true

containerd:
  system: false
  user: false


provision:
- mode: system
  script: |
    #!/bin/bash
    set -eux -o pipefail
    export DEBIAN_FRONTEND=noninteractive
    apt-get update -y && apt install -y squashfs-tools-ng
    wget https://github.com/sylabs/singularity/releases/download/v4.0.2/singularity-ce_4.0.2-jammy_amd64.deb
    apt install -y ./singularity-ce_4.0.2-jammy_amd64.deb

probes:
- script: |
    #!/bin/bash
    set -eux -o pipefail
    if ! timeout 30s bash -c "until command -v singularity >/dev/null 2>&1; do sleep 3; done"; then
      echo >&2 "singularity is not installed yet"
      exit 1
    fi
  hint: See "/var/log/cloud-init-output.log" in the guest

message: |
  To run `singularity` inside your lima VM:
    $ limactl shell {{.Name}} singularity run library://alpine
```

Save this configuration to a file named `config.yml`.

### 3. Create and start the Lima VM
Run the following command to create and start the Lima VM using the configuration file you just created:
```bash
# Create a VM named cs_sdk
$ limactl start ./config.yml --name cs_sdk
```

### 4. Untar and add to PATH
Now, untar the Cerebras SDK tarball at any location under your Mac’s home directory. We can now start a shell inside the VM, add the SDK to the PATH, and run:
```bash
# Start shell inside VM
$ limactl shell cs_sdk

# Add absolute path under Mac home directory containing SDK to PATH
# This MUST be absolute path; homedir on VM and Mac are not the same
$ export PATH=/User/path/to/sdk:$PATH
```

From this point, you can run the SDK examples within the VM. Lima VMs automatically port forward, so if you launch the SDK GUI within the VM, you can view it in your Mac’s browser at 127.0.0.1:8000/sdk-gui.