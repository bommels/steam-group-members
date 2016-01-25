from SteamGroup import steamgroup

steamids = steamgroup.get_steam_ids()

# Print SteamID's fetched
for id in steamids:
	print('[ID64] ' + str(id))