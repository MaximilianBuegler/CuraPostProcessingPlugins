# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.
# 
# Modified 2018 by Maximilian Bügler ( http://www.maxbuegler.eu/ )
#

import re #To perform the search and replace.

from ..Script import Script

##  Replaces all M109s by M104s after initial heatup, in order to remove waiting times between layers. Only makes sense if standby temperature equals printint temperature
class M109TOM104Fix(Script):
    def getSettingDataString(self):
        return """{
            "name": "M109 To M104 Fix",
            "key": "M109TOM104Fix",
            "metadata": {},
            "version": 2,
            "settings":{}
        }"""

    def execute(self, data):
        search_string = "M109"
        search_string = re.escape(search_string) #Need to search for the actual string, not as a regex.
        search_regex = re.compile(search_string)
        replace_string = "M104"
        first_layer = 1

        for layer_number, layer in enumerate(data):
            if layer_number > first_layer:
                data[layer_number] = re.sub(search_regex, replace_string, layer) #Replace all.
        
        return data
