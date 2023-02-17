# Mac Changer with Python 3
This code is a mac changer for Kali Linux computer. It is a code created using modules `subprocess`, `re` and `optparse`.

## Usage

#### Interface selection

| Parameter | Description                |
| :-------- | :------------------------- |
| `-i` or `--interface` | Interface where you want to change your mac address |

#### Mac address changer

| Parameter | Description                     |
| :-------- | :-------------------------------- |
| `-m` or `--mac` | The mac address you want to change |

#### Example:

```
python mac_address_changer.py -i eth0 -m 00:11:22:33:44:55
```
