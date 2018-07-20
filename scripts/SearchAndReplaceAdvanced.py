# Copyright (c) 2017 Ruben Dulek
# The PostProcessingPlugin is released under the terms of the AGPLv3 or higher.
# 
# Modified 2018 by Maximilian Bügler ( http://www.maxbuegler.eu/ )
#

import re #To perform the search and replace.

from ..Script import Script

##  Performs a search-and-replace on all g-code starting at a specific layer.
#
#   Due to technical limitations, the search can't cross the border between
#   layers.
class SearchAndReplaceAdvanced(Script):
    def getSettingDataString(self):
        return """{
            "name": "Search and Replace Advanced",
            "key": "SearchAndReplaceAdvanced",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "search":
                {
                    "label": "Search",
                    "description": "All occurrences of this text will get replaced by the replacement text.",
                    "type": "str",
                    "default_value": ""
                },
                "replace":
                {
                    "label": "Replace",
                    "description": "The search text will get replaced by this text.",
                    "type": "str",
                    "default_value": ""
                },
                "is_regex":
                {
                    "label": "Use Regular Expressions",
                    "description": "When enabled, the search text will be interpreted as a regular expression.",
                    "type": "bool",
                    "default_value": false
                },
                "first_layer":
                {
                    "label": "First layer",
                    "description": "Layer to start at",
                    "type": "int",
                    "default_value": 0
                }
            }
        }"""

    def execute(self, data):
        search_string = self.getSettingValueByKey("search")
        if not self.getSettingValueByKey("is_regex"):
            search_string = re.escape(search_string) #Need to search for the actual string, not as a regex.
        search_regex = re.compile(search_string)

        replace_string = self.getSettingValueByKey("replace")

        first_layer = self.getSettingValueByKey("first_layer")

        for layer_number, layer in enumerate(data):
            if layer_number > first_layer:
                data[layer_number] = re.sub(search_regex, replace_string, layer) #Replace all.
        
        return data
