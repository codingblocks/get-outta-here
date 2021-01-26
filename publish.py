import glob
from distutils.core import setup

opts = {
    "py2exe": {
        # if you import .py files from subfolders of your project, then those are
        # submodules.  You'll want to declare those in the "includes"
        'includes': [],
    }
}

setup(

    # this is the file that is run when you start the game from the command line.
    windows=['main.py'],

    # options as defined above
    options=opts,

    # data files - these are the non-python files, like images and sounds
    # the glob module comes in handy here.
    data_files=[
        (r"assets\fonts\Press_Start_2P", glob.glob(r"assets\fonts\Press_Start_2P\*")),
        (r"assets\sprites\Oryx-SciFi", glob.glob(r"assets\sprites\Oryx-SciFi\*.png")),
        (r"assets\sprites\futuristic-cards-alpha", glob.glob(r"assets\sprites\futuristic_cards-alpha\*")),
        (r"assets\sprites\futuristic-cards-delta", glob.glob(r"assets\sprites\futuristic_cards-delta\*")),
        (r"assets\sprites\futuristic-cards-epsilon", glob.glob(r"assets\sprites\futuristic_cards-epsilon\*")),
        (r"data", glob.glob(r"data\cards.json")),
        (r"maps", glob.glob(r"maps\*")),
    ],

    # this will pack up a zipfile instead of having a glut of files sitting
    # in a folder.
    zipfile="lib/shared.zip"
)
# C:\Users\me\Projects\games\pygame\everything-is-broken\assets
