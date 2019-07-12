# explorer-from-wsl
call explorer.exe from wsl shell by unix-style path

## install

```bash
$ python3 -m pip install ExplorerFromWSL
```

## uninstall

```bash
$ python3 -m pip uninstall ExplorerFromWSL
```

## usage

### wsl shell command

#### open current directory

```bash
$ explorer .
```

or, simply

```bash
$ explorer
```

#### open drvfs ( windows drive C:\\\\, D:\\\\ )

```bash
$ explorer /mnt/c/Users/${wINDOWS_USER}/path/to/dir
```

```bash
$ explorer /mnt/d/path/to/dir
```

#### open wslfs ( wsl filesystem under / )

__CAUTION__ need "Windows 10 May 2019 Update (version 1903)" or later.  
This update enable to open wsl directory as network directory.

home directory

```bash
$ explorer ~
```

```bash
$ explorer $HOME
```

any unix style path available

```bash
$ explorer ~/path/to/dir
```