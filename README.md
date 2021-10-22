# PokeZukan API

- [Project Overview](#-Project-Overview)
- [API Documentation](#-API-Documentation)
- [Disclaimer](#-Disclaimer)


## Project Overview

PokeZukan API has been created to be used in PokeZukan Mobile App and other future Projects.  
We need to have access to an API not connected to a online database, for this reason I have scraped [pokémondb.net](https://pokemondb.net) website and gathered information from [PokeAPI](https://pokeapi.co/) which then saved the needed info of all Pokémons in a JSON file.

## API Documentation

### Contents

- abilities
- data
- images
- moves

### Abilities
**GET** ```https://cdn.jsdelivr.net/gh/glennkok1501/PokeZukanAPI@main/abilities/all.json```
```json
{
    "count": 327,
    "abilities": [
        {
            "name": "stench",
            "link": "abilities/stench.json"
        },
        {
            "name": "drizzle",
            "link": "abilities/drizzle.json"
        },
        {
            "name": "speed boost",
            "link": "abilities/speed-boost.json"
        },
```

**GET** ```https://cdn.jsdelivr.net/gh/glennkok1501/PokeZukanAPI@main/abilities/static.json```
```json
{
    "name": "static",
    "effect": "whenever a move makes contact with this pok\u00e9mon, the move's user has a 30% chance of being paralyzed.  pok\u00e9mon that are immune to electric-type moves can still be paralyzed by this ability.  overworld: if the lead pok\u00e9mon has this ability, there is a 50% chance that encounters will be with an electric pok\u00e9mon, if applicable.",
    "description": "the pok\u00e9mon is charged with static electricity, so contact with it may cause paralysis."
}
```

### Data
- pokemon
- location
- moves


#### Pokemon
Information of Pokemon.  
**GET** ```https://cdn.jsdelivr.net/gh/glennkok1501/PokeZukanAPI@main/data/pokemon/all.json```
```json
{
    "count": 1035,
    "pokemon": [
        {
            "id": 1,
            "name": "bulbasaur",
            "sprite": "images/pokemon/bulbasaur.png",
            "link": "data/pokemon/bulbasaur.json"
        },
        {
            "id": 2,
            "name": "ivysaur",
            "sprite": "images/pokemon/ivysaur.png",
            "link": "data/pokemon/ivysaur.json"
        },
        {
            "id": 3,
            "name": "venusaur",
            "sprite": "images/pokemon/venusaur.png",
            "link": "data/pokemon/venusaur.json"
        },
```
**GET** ```https://cdn.jsdelivr.net/gh/glennkok1501/PokeZukanAPI@main/data/pokemon/pikachu.json```
```json
{
    "name": "pikachu",
    "id": 25,
    "info": {
        "species": "mouse pok\u00e9mon",
        "abilities": [
            {
                "name": "static",
                "is_hidden": false
            },
            {
                "name": "lightning-rod",
                "is_hidden": true
            }
        ],
        "types": [
            "electric"
        ],
        "height": 0.4,
        "weight": 6.0
    },
    "sprites": {
        "home": "images/pokemon/pikachu.png",
        "artwork": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/25.png"
    },
    "moves": "data/moves/pikachu.json",
    "location": "data/location/pikachu.json",
    "base_stats": {
        "hp": 35,
        "attack": 55,
        "defense": 40,
        "sp. atk": 50,
        "sp. def": 50,
        "speed": 90
    },
    "entry": "when it smashes its opponents with its bolt- shaped tail, it delivers a surge of electricity equivalent to a lightning strike.",
    "training": {
        "base_exp": 112,
        "capture_rate": 190,
        "growth_rate": "medium",
        "ev_yield": [
            {
                "stat": "speed",
                "effort": 2
            }
        ]
    },
    "breeding": {
        "base_happiness": 70,
        "egg_group": [
            "ground",
            "fairy"
        ],
        "gender": {
            "male": 50.0,
            "female": 50.0
        },
        "egg_cycle": {
            "hatch_counter": 10,
            "steps": 2805
        }
    }
}
```

#### Location
Which games and areas the Pokemon can be found.  
**GET** ```https://cdn.jsdelivr.net/gh/glennkok1501/PokeZukanAPI@main/data/location/pikachu.json```
```json
{
    "location": [
        {
            "game": [
                "diamond",
                "pearl",
                "platinum"
            ],
            "area": [
                "trophy-garden-area"
            ]
        },
        {
            "game": [
                "yellow"
            ],
            "area": [
                "pallet-town-area"
            ]
        },
...
```

#### Moves
Moveset of the Pokemon includes levelup, tutor, machine.  
**GET** ```https://cdn.jsdelivr.net/gh/glennkok1501/PokeZukanAPI@main/data/moves/pikachu.json```
```json
{
    "moves": [
        {
            "name": "mega-punch",
            "method": "tutor",
            "level": 0
        },
        {
            "name": "pay-day",
            "method": "machine",
            "level": 0
        },
        {
            "name": "thunder-punch",
            "method": "tutor",
            "level": 0
        },
...
```

### Images
- moves
- pokemon
- type

#### Moves
Artwork of Pokemon move category.  
**GET** ```https://raw.githubusercontent.com/glennkok1501/PokeZukanAPI/main/images/moves/physical.png```  
![](https://raw.githubusercontent.com/glennkok1501/PokeZukanAPI/main/images/moves/physical.png)

> Credits
> Move Category Icons
> physical: https://img.pokemondb.net/images/icons/move-physical.png
> special: https://img.pokemondb.net/images/icons/move-special.png
> status: https://img.pokemondb.net/images/icons/move-status.png

#### Pokemon
Sprites of Pokemon Artwork.  
**GET** ```https://raw.githubusercontent.com/glennkok1501/PokeZukanAPI/main/images/pokemon/pikachu.png```  
![](https://raw.githubusercontent.com/glennkok1501/PokeZukanAPI/main/images/pokemon/pikachu.png)

> Credits
> Sprites created by theSLAYER from The Project Pokémon
> https://projectpokemon.org/home/docs/spriteindex_148/
> HOME Sprites: Gen 1: https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-1-r128/
> HOME Sprites: Gen 2: https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-2-r129/
> HOME Sprites: Gen 3: https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-3-r130/
> HOME Sprites: Gen 4: https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-4-r131/
> HOME Sprites: Gen 5: https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-5-r132/
> HOME Sprites: Gen 6: https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-6-r133/
> HOME Sprites: Gen 7: https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-7-r134/
> HOME Sprites: Gen 8: https://projectpokemon.org/home/docs/spriteindex_148/home-sprites-gen-8-r135/

#### Type
Pokemon Type Icons.  
**GET** ```https://raw.githubusercontent.com/glennkok1501/PokeZukanAPI/main/images/types/ic_electric.png```  
![](https://raw.githubusercontent.com/glennkok1501/PokeZukanAPI/main/images/types/ic_electric.png)

> Credits
> Pokemon Types Icons
> https://commons.wikimedia.org/wiki/Category:Pok%C3%A9mon_types_icons

### Moves
**GET** ```https://cdn.jsdelivr.net/gh/glennkok1501/PokeZukanAPI@main/moves/all.json```
```json
{
    "count": 844,
    "moves": [
        {
            "name": "pound",
            "type": "normal",
            "link": "moves/pound.json"
        },
        {
            "name": "karate chop",
            "type": "fighting",
            "link": "moves/karate-chop.json"
        },
        {
            "name": "double slap",
            "type": "normal",
            "link": "moves/double-slap.json"
        },
        {
            "name": "comet punch",
            "type": "normal",
            "link": "moves/comet-punch.json"
        },
        {
            "name": "mega punch",
            "type": "normal",
            "link": "moves/mega-punch.json"
        },
...
```

**GET** ```https://cdn.jsdelivr.net/gh/glennkok1501/PokeZukanAPI@main/moves/thunderbolt.json```
```json
{
    "name": "thunderbolt",
    "type": "electric",
    "category": "special",
    "power": 90,
    "accuracy": 100,
    "pp": 15,
    "contest": "cool",
    "effect": "has a 10% chance to paralyze the target.",
    "description": "a strong electric blast crashes down on the target. this may also leave the target with paralysis."
}
```

## Disclaimer

PokeZukanAPI is an unofficial, free fan made API service and is not affiliated, endorsed or supported by Nintendo, GAME FREAK or The Pokémon Company in any way. Some images used in this app are copyrighted and are supported under fair use. Arts, visuals, names, Pokémon and Pokémon names are properties of the companies mentioned previously.
No copyright or trademark infringement is intended.
© 2021 Pokémon.
© 1995–2021 Nintendo/Creatures Inc./GAME FREAK inc.