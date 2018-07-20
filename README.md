# CuraPostProcessingPlugins
Post Processing Plugins for Cura

# M109TOM104Fix.py
Replaces all M109 (Set temp and wait) with M104 (Set temp and continue) After intial heatup. 
Only use this if your standby temperature is set equal to your printing temperature. 
Only makes sense if both extruders are used at pretty much every layer.

# SearchAndReplaceAdvanced.py
Replaces a string same as the stock script, but only starts at a specific layer
