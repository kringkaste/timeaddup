> [!CAUTION]
> This repository is not maintained anymore. If you are using Albert, there is a new [repository](https://github.com/kringkaste/albert-time-addup).

# Add up time ranges

This script is for [Alfred](https://www.alfredapp.com/) or [Albert](https://albertlauncher.github.io/) to add up multiple time ranges. The result is a floating-point number of hours.

## Query format

All times are in 24h format. The time ranges consists of pairs of time strings separated by spaces. The first time sting of the pair is the start time and the second is the end time. E.g.:

`t 12:00 12:15 13:30 14:00`

The query above starts with the trigger `t ` followed by two pairs of time ranges which will be calculated and added up: `12:00` to `12:15` and `13:30` to `14:00`.

You can modify the result by a number of minutes. Just add the string `+10m` to add 10 minutes or `-12m` to subtract 12 minutes from the result. 

## Install for Alfred on macOS

If you want to use the script in Alfred, you first have to copy the `timecalc` module to your site-packages folder:

```shell
# Install the module
cp -r timecalc ~/Library/Python/3.8/lib/python/site-packages
```

Then you can copy the `timeaddup.py` somewhere in your system. The path in the included `timeaddup.alfredworkflow` file expects the script in `/usr/local/bin`. You can change it later in the imported workflow if you use an other folder.

```shell
sudo cp timeaddup.py /usr/local/bin
```

Then import the workflow by double click the `timeaddup.alfredworkflow` in the Finder.

## Install for Albert on Linux

Clone this repo into the Albert extension folder:

```shell
git clone git@github.com:kringkaste/timeaddup.git ~/.local/share/albert/org.albert.extension.python/modules/timeaddup
```

Then copy the `timecalc` module to your site-packages folder:

```shell
cp -r ~/.local/share/albert/org.albert.extension.python/modules/timeaddup/timecalc ~/.local/lib/python3.9/site-packages
```

Restart Albert and go to the extension tab in the settings and activate the extension.
