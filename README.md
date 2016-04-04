# Commitwatch

Commitwatch is an OSX tray applet that displays your Github contributions today.
With commitwatch you can avoid forgetting about your contribution streak, and 
keep track of how active you've been each day!

## Installation

You can get the latest version of commitwatch from the [releases page][1]. 


Simply download the file titled `trayapp.zip`, extract it, and copy the OSX
application to your Applications directory.

## Development

To start developing commitwatch, clone the repository locally. Commitwatch has
no external dependencies, and you should run it outside of any virtualenvs so
that you ensure you're using OSX's main Python distribution.

```bash
> python trayapp.py # Run the app
```

To generate a build release of commitwatch, you will need a virtualenv. Install 
py2app and all of the application's OSX dependencies within that virtualenv, 
then build the application from within it as well.

```bash
env> python setup.py py2app # Build the app
```

OSX's Python has odd behaviours that will likely cause the application to not
start if ran from within a virtualenv, and not build if built outside of a 
virtualenv... Your mileage may vary!

[1]:https://github.com/chrisfosterelli/commitwatch/releases
