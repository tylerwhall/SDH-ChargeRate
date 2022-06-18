# Charge Rate Limit

This is a plugin for the [SteamOS Plugin Loader](https://github.com/SteamDeckHomebrew/PluginLoader).

## Motivation

Limiting the charge rate can be helpful for:

1. Reduced waste heat (and thus power) when running on an external battery
2. Long-term battery health when primarily powered from AC.

## Usage

1. `git clone` the repo into the `/home/deck/homebrew/plugins` folder on your Steam Deck
2. Opening the plugin will initialize the limit to the minimum of 250mA.
3. Set a higher limit if desired.
4. Firmware will reset the limit on suspend or power off, so set the limit after plugging in.

## License

This is licensed under GNU GPLv3.
