---
title: 'Booting from grub'
date: 2018-02-16
permalink: /posts/2018/02/Booting from grub/
mathjax: true
tags:
  - Grub
  - Linux
---
## The Problem
I have a dual system window10/Ubuntu16.04 installed in my laptop. Today I can not access window files from Ubuntu and tried one
command line from youtube which seems to mess things up :< The system did not boot like before but entering into the grub prompt instead.
It seems that system does not know where/what to boot now and may need a manual configuration.

## The solution
I spent some time googling and found these two posts quite useful for me. [Here](https://www.linux.com/learn/how-rescue-non-booting-grub-2-Linux) and [Here](https://ubuntuforums.org/showthread.php?t=2140115)

First, I changed the booting priority in bios so that linux will boot first. I have an Asus laptop. To enter into BIOS, hold `F2`
when starting your machine.

### Find the root system
When in grub prompt, type `ls` to check files in the system. You will see things like `(hd0)`,`(hd0,gpt1)`, ...
`ls` each one to find where the root system is (you can omit the gpt label). For me, it is `(hd0,gpt9)`. 
`ls (hd0,9)/` outputs things like:
```
lost+found/ bin/ ... vmlinuz ... initrd.img ...
```
If you have many linuxes installed, double check if it is the right system by command `cat (hd0,9)/etc/issue`.

### Boot the system
Now, it is time let GRUB know the system you want to boot by typing commend:
```
grub> set root (hd0,9)
grub> Linux /vmlinuz root=/dev/sta5
grub> initrd /initrd.img
grub> boot
```

*If you do not know where your root device is, you can use `UUID` for specifying the path.
type `cat /etc/fstab` and check the output. The `UUID` for the root device is located in the entry where `\` is in the `<mount on>`
column. Then you can replace `root=/dev/sta5` by `root=UUID=[UUID you found]`.

* If you want to specify the kernel version of your linux, you can check available ones by typing `ls (hd0,9)/boot/`. To
suppress the output, you can do `set pager=1`. Now you can boot the system you want by
```
grub> set root (hd0,9)
grub> Linux /boot/vmlinuz-[version] root=/dev/sta5
grub> initrd /boot/initrd.img-[version]
grub> boot
```
The version has to be the same in the second and thrid command line or you will get a kernel panic.

Hurrah, the system now boots correctly.
To fix it permantly, after you boot succesfully. Type these in the shell:

```
$ update-grub
$ grub-install /dev/sda
```

Hopefully, I did not mess up with linux again...
