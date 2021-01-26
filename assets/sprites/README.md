# Sprites Directory
This is where sprites for the game are stored.

Refer to [config.py](../../src/config.py) to learn which files are expected to be here,
or to modify it to use your own sprite sheets.

The general structure assumed to be found here is:
```text
.
├── set1
│   ├── sprite_a.png
│   └── sprite_b.png
└── set2
    ├── sprite_a.png
    └── sprite_b.png
```

Using your own sprites might be tricky though, because the game
makes certain assumptions about the provided sprite sheets.

**ATTENTION:** You _must_ provide the [16-Bit SciFi sprites from Oryx Design Lab](https://www.oryxdesignlab.com/products/16-bit-sci-fi-tileset)
(or appropriate sprites of the same size) in a directory named `Oryx-SciFi` to keep the TMX maps working! 

The files contained in there during the build are: 
- cancel_button.png
- oryx_16bit_scifi_creatures_extra_trans.png
- oryx_16bit_scifi_creatures_trans.png
- oryx_16bit_scifi_FX_lg_trans.png
- oryx_16bit_scifi_FX_sm_trans.png
- oryx_16bit_scifi_interface_trans.png
- oryx_16bit_scifi_items_trans.png
- oryx_16bit_scifi_vehicles_trans.png
- oryx_16bit_scifi_world_decals_trans.png
- oryx_16bit_scifi_world_extra_trans.png
- oryx_16bit_scifi_world_trans.png
