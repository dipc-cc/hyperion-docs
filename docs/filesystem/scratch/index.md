# scratch filesystem

`/scratch` is a shared high performance storage that system provides access to large amounts of disk. It meant to be used as the work space for jobs.

!!! Tip
    You should use it only to submit jobs from and to redirect all your I/O.

## Check your scratch usage

The storage offered by the `/scratch` filesystem is limited for each user. In case you want to check your your occupation, you can do it by running the following command:

```
beegfs-ctl --cfgFile=/etc/beegfs/beegfs-client-scratch.conf --getquota --uid $USER
```

!!! note "Storage increase"
    Although the storage capacity of `/scratch` should be large enough, if more is needed, contact us and we will assess the storage increase. 



