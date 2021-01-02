# schiphol-runway
Custom component for Home Assistant to show active runways for Amsterdam Airport Schiphol

Creates two sensors:

- Landing runway: main landing runway in use at Schiphol (shown as runway number (e.g. 36R)
- Take-off runway: main landing runway in use at Schiphol (shown as 

(shown as runway number (e.g. 36R))

To install:

1) in the Home Assistant directory (where configuration.xml lives), create a folder *'custom_components'* (if not already present).
2) In *'custom_components'*, create a folder *'schiphol_runway'*.
3) Copy files in this repository to this folder. 
4) Add the following to *configuration.yaml*:
'''
sensor:
  - platform: schiphol_runway
'''
5) Restart HA and wait for the sensors to update (can take up to a minute).
