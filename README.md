# KML-Heading-Removal
A 2014 script I wrote to write an integer of 0 to the `<heading>` tag of KML documents created by ArcMap.

Sometimes ArcMap at the time I wrote this script would produce heading values in a KML file that were unwanted, so this script will open a KML file and set all of the `<heading>` tags to a node value of `0`

**Usage**
`python kmlRemoveHeading.py -f {filename}.kml`
