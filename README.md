# Steam Group Members
Fetches SteamID64s of Steam group members. You can specify your own Steam Group URL. API key not required.

### Usage
SteamGroup is written in Python 3.4.2.

### Requirements
- Python 3+
- The `requests` package. Use `pip install requests` to install.
- Your Steam Group URL.

### Running
- Specify your URL in `SteamGroup.py`
- `from SteamGroup import steamgroup`
- Use `steamgroup.get_steam_ids()` to get returned ids.


### Example
View `example.py` for code example.

```python
from SteamGroup import steamgroup
steamid = steamgroup.get_steam_ids()
```
Output:
```
[200] http://steamcommunity.com/groups/SteamLadder/memberslistxml?xml=1&p=1
[200] http://steamcommunity.com/groups/SteamLadder/memberslistxml?xml=1&p=2
[OK!] Fetched 1980 SteamIDs
```
Result:

`steamids` now contains an array of SteamID64s fetched with SteamGroup.

