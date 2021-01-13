### Command Line Arguments 

#### Command line arguments
parameters that are given to a program or script, so it is important to
cope up with it. In OpenCV, images and different types of files are usually passed as parameters.
So to handle command line arguments, python uses sys.argv.
*  It sets all the parameters in the sys.argv.
*  First element of sys.argv[0] will be the path to the script or script name (it depends upon
the OS)
*  From second element i.e sys.argv[1] it will be the list of parameters.

#### Argparse command-line option
If our programs have very complicated parameters or multiple file names, we should use python
library “argparse” as it handles in a more systematic way.

* First program will determine what arguments it requires.
* Then argparse will parse these into sys.arg
* Also, argparse help and usage message, issues error when invalid arguments are provided.

-------------------------------------------------------------------

### Code
```javascript
 import argparse
 parser = argparse.ArgumentParser()
 parser.add_argument(“first_argument”, help=”this is the string with the first argument”)
 args = parser.parse_args()
 ```
