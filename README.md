<div align="center">

# Kheremara

</div>

> [!WARNING]
> At the moment, Kheremara doesn't actually work yet. That's why you don't see any install instructions or anything of the sort.

_Exaroton_ has a neat little feature where it turns off your server when it's not running, and when a player wants to join while it's off--the server starts for them. This saves money and electricity.

_Kheremara_ is my own implementation of the whole idea for [Endstone](https://endstone.dev/stable). With Kheremara, your servers with nobody in it don't have to stay fully online, saving on your resources.

## How Kheremara Works

Kheremara's autostart/autostop is planned to work like the following: if the server has no players for a set amount of time, stop it and run an extremely lightweight [Pumpkin](https://pumpkinmc.org/) server that acts as a buffer in place of it. Afterwards, if a player joins the buffer server, the buffer server tells the _actual_ server to wake up, and when it's ready, it transports all players from the buffer server directly to the actual server, and shuts down the buffer server entirely.