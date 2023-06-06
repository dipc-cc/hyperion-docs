# Getting started

!!! success "About this page" This document will guide you through the basics of using Hyperion.

## Connecting to Hyperion

### Linux

Most Linux distributions come with an SSH client pre-installed. The default SSH client is the OpenSSH client.

Open a Terminal to establish a connection with the login node of any of out HPC systems:

```
$ ssh username@hyperion-login-01.sw.ehu.es
$ ssh username@hyperion-login-02.sw.ehu.es
```

You will need to replace `username` with the username you were assigned.

### MacOS

MacOS also comes with a command-line SSH client installed by default. The usage of this client is identical to the usage described in the previous section for GNU/Linux.

If you are using macOS and want to be able to run graphical applications on the clusters then you need to install the latest version of the XQuartz X Windows server.

### Windows
Windows users can use the built-in OpenSSH client starting from Windows 10 build 1809 or later. To enable the OpenSSH client, follow these steps:

- Open ``Settings`` and navigate to ``Apps > Optional Features``.
- Click ``Add a feature`` and search for ``OpenSSH Client``.
- Select ``Install``.

Once installed, you can use the command prompt or PowerShell to connect to a remote server.

Alternatively, you can download and install third-party SSH clients like [PuTTY](https://www.putty.org/) or [MobaXterm](https://mobaxterm.mobatek.net).

## Software

Hyperion supply a rich set of compilers, HPC utilities, programming libraries, development tools, debuggers/profilers, data and visualization tools. 

We provide a list of application specific documentation that are built by DIPC staff. 

Software can be accessed via `module` command. Go to [Software](/path/to/software) secttion to read in depth about it.

!!! question "Something missing?" 
    If there is something missing that you would like to have on our systems, please [submit a request](/path/to/request/submission) and we will evaluate it for appropriateness, cost, effort, and benefit to the community.


