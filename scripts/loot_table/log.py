import os
import json

folders = [
    "JAT;mEE-DP",
    "data",
    "minecraft",
    "loot_table",
    "blocks"
]

entries = [
    "acacia_log",
    "birch_log",
    "cherry_log",
    "dark_oak_log",
    "jungle_log",
    "mangrove_log",
    "oak_log",
    "spruce_log",
    "stripped_acacia_log",
    "stripped_birch_log",
    "stripped_cherry_log",
    "stripped_dark_oak_log",
    "stripped_jungle_log",
    "stripped_mangrove_log",
    "stripped_oak_log",
    "stripped_spruce_log"
]

main = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(main, "..", "..")
for _ in folders:
    path = os.path.join(path, _)

for _ in entries:
    file_path = os.path.join(path, f"{_}.json")
    
    content = {
        "type": "minecraft:block",
        "pools": [
            {
                "rolls": 1,
                "bonus_rolls": 0,
                "entries": [
                    {
                        "type": "minecraft:item",
                        "name": f"minecraft:{_}",
                        "conditions": [
                            {
                                "condition": "minecraft:match_tool",
                                "predicate": {
                                    "items": "#jmee:tool/log"
                                }
                            }
                        ]
                    }
                ]
            }
        ],
        "random_sequence": f"minecraft:blocks/{_}"
    }
    
    with open(file_path, 'w') as json_file:
        json.dump(content, json_file, indent=4)
