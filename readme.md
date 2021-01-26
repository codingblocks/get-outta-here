# Get Outta Here!

![Screenshot of Get Outta Here game](https://raw.githubusercontent.com/codingblocks/gotta-get-out/main/main.png)

- [Available on itch.io](https://thejoezack.itch.io/get-outta-here)
- [Game Design + Playthrough on YouTube](https://www.youtube.com/watch?v=xTM3GeMiz54)

## Game Description

This game was created for the first Coding Blocks Game Jam #cbjam. The theme was "Everything is Broken". The idea was to
create a game focused around a broken down ship, where you had to slowly "wake" personnel and bring systems online in
order to fix up the ship before you were overtaken by Space Pirates. There isn't much inside the game to tell you this,
because I ran short on time, but I hope you get the gist!
You are the captain of a broken down spaceship. Your goal is to fix the ship to get out of dangerous space while fending
waves of space pirates.

## Mechanics

This is a deck/engine-building game, where you accumulate cards in order increase your increase your fuel enough to "get
outta here". Fuel slowly decreases over time, but there are cards you can play to increase your "energy" in order to
ultimately buy more fuel. Be careful though, if you don't build a balanced deck it can be real hard to "get outta here"
before the pirates arrive!

## Special Thanks to:

This game was fully developed on Twitch for a [game jam](https://itch.io/jam/coding-blocks-2021). Huge thank you to
everybody that helped me through my various self-induced problems. Special shout out to the following, who were
incredibly patient with me:

- columferry
- dsqrt4

## About building this project...

I didn't include the assets for this project, but you can find/buy them using the links below. If you drop them into
an "assets" folder than everything should (wink) "just work". Ping me if you have any trouble with that and I can help
you!

## How to play the Game

### Get it from itch.io (Windows only)

You can download the bundled executable from itch.io (link above). It comes with an exe and **all Game Assets included**
, no further tweaking required. You will however need to ignore a nasty **Security Warning** from Windows. (not
recommended)

### Running from Source with Python (any OS)

This is the preferred approach if you care security.

#### Set it up

If you have ever had written a single line of python, you probably know what to do already and skip this section.

- make sure you have [Python3](https://www.python.org/) installed
- clone this repository and change into the newly created directory
- create a python virtual environment (_optional_)
    - execute `python3 -m venv game_environment`
    - activate via `game_environment/bin/activate.ps1` (Windows PowerShell), or `source game_environment/bin/activate` (
      Bash)
- install the game's requirements
    - execute `pip install -r requirements.txt`

#### Add the missing assets

I didn't include the assets for this project for licensing reasons, but you can find/buy them using the links below. If
you drop them into an `assets` folder than everything should (wink) "just work". Ping me if you have any trouble with
that and I can help you!

- https://www.oryxdesignlab.com/products/16-bit-sci-fi-tileset
- https://kodiakgraphics.itch.io/futuristic-cards
- https://fonts.google.com/specimen/Press+Start+2P

#### Start the Game

Assuming you've got all the assets in place and still have your virtual environment activated, you can start the game
simply by executing:

```sh
python3 main.py
```

That's all, have fun!

## Publishing

- `python publish.py py2exe`
- `butler push dist thejoezack/get-outta-here:windows-beta`

**NOTE:** packaging this app into an exe requires you to `pip install -r requirements/publishing.txt`

