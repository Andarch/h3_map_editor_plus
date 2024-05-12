# Disclaimer
This is a fork of the original project by Shakajiub (https://github.com/Shakajiub/h3_map_editor) with some enhancements.

# Change log
	- Added help/h/help command to show available commands and scripts
	- Added swap_layers script
	- Added missing value of 255 (Random) to the Town class.

# Usage

## Launch

```
./h3_map_editor_plus.py
```
-or-
```
./h3_map_editor_plus.py [filename]
```

## Commands

```
> help/h/hlp
```
Shows you a list of available commands and scripts.

```
> open [filename]
```
Can be used to open a map while the editor is running.

```
> save [filename]
```
To write your changes into a new map file. You can omit the ".h3m" extension here as well, the editor will add it if necessary. If you do not specify the filename, the map will be saved as "output.h3m".

```
> print/show [key]
```
Shows you the parsed data for a specific key (e.g. "general"). See [h3_map_editor_plus.py](h3_map_editor_plus.py) (map_data) for a list of all the keys.

```
> quit/q/exit
```
To exit the editor.


## Scripts

To actually make changes in the map file, you will need to use custom scripts. All scripts should be implemented in [src/scripts.py](src/scripts.py).

```
> swap_layers [> swap_layers]
```
Swaps the layers in a map, including terrain, objects, and settings such as main towns and win/loss conditions.

```
count_objects [> count]
```
Is a simple example that goes through all the objects placed in the map and prints out how many copies of each object can be found.

```
generate_guards [> guards]
```
Is a more complex example. The script goes through specific objects (Pandora's Boxes, Artifacts, Resources, etc.) and checks if the last line in the object's message box is "-guards XXX". Whenever it finds that, it generates guards for the object with a total AI value of XXX, then replaces the text with a "Guarded by XYZ" description. See the script itself for a more detailed explanation.
