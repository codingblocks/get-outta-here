# Gotta Get Outta Here!

[https://thejoezack.itch.io/get-outta-here](Available on itch.io)

## Game Description

You are the captain of a broken down spaceship. Your goal is to fix the ship to get out of dangerous space while fending waves of space pirates. 

You do this by accumulating resources and waking up passengers from cryosleep. 

## Special Thanks to:

This game was fully developed on Twitch for a [game jam](https://itch.io/jam/coding-blocks-2021). Huge thank you to everybody that helped me through my various self-induced problems. Special shout out to the following, who were incredibly patient with me:

- absolution1383
- columferry
- dsqrt4

## Definitely do
- 15m Submitting
- 15m Publish on Github (minus assets)
- 1hr Update itch.io page
  - Make a video
  - Windows only
  - Github
  - Special Thanks

### Maybe...
- Animations
  - Personnel 
  - Particularly around card choice, discarding, drawing

### Yeah right...
- Sounds
- Show warning if resource gets low
- Show message when resources are looking good (for 500 fuel, "Halfway there!")
- Hiding alert messages :P
- Say which resource is preventing the buy
- Card choice should be a modal
- Better cards
  - More cards
  - Percentage cards

### Start Conditions
- plus Currency per Round
- x Cards per Round

## Mechanics
- Ship Combat
- Environmental Effects (Asteroids)

* Buying New Cards
* Selling New Cards
* Single Currency

## 
- Flying Boar for Top Boss (named Colum)
- dsqrt green

## Inspiration

- Slay the Spire
- Monster Train
- Ratopolis
- Hearthstone
- Engine-Building Games
  - Dominion
  - Star Realms
  - Small World

## Cards

### Card

Represent an action the player may take. They cost resoruces and can have immediate affects, spawn critters, or have other affects on the game.

#### Card Categories
- Personnel (Permanent Upgrades)
  - +10 Currency / round
  - +1 Room Defense
- Engineering Cards (Actions)
  - Re-Route Power to Engineering: +50 Currency / 3 rounds
- Cantina
- Library
- Waste disposal
- Plumbing/Custodial
- Armory
- Ship Weapons
- Cargo
- Vehicle / Flight Bay
- Prison
- Upgrades 

### CardLibrary

All cards available in the game

### Player
  
Has cards that represent their abailities. Only the abilities in their "hand" are available at any given moment.

The player also has a stock and discard pile that represent their potential and spent abilities that will eventually cycle through.

### Hand

All of the cards currently available for the player to play, right now!

#### Card Ideas

- Door Upgrades
  - # of Uses
  - (Note the ship could get nicer looking)
- Player Characters
  - Unique Characters
  - Generic
  
## Assets
- https://www.oryxdesignlab.com/products/16-bit-sci-fi-tileset
- https://kodiakgraphics.itch.io/futuristic-cards
- https://fonts.google.com/specimen/Press+Start+2P

## TODO

- Dim the card light on discard and/or draw pile when empty
- Brighten the light on hover


## Economy

- Energy: (used to play cards)
- Shields: (used for defense)
- Fuel: (beat the game when you get to x)
- Cards to Draw
- Time to Draw
- Time till next wave
- Strength of next wave

## Publishing
- `python publish.py py2exe`
- `butler push dist thejoezack/get-outta-here:windows-beta`

