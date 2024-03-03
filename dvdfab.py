"""
DVDFab ExtendDownload v1.0.0

This script is designed to facilitate the downloading of specific versions of software products from DVDFab and other related products by utilizing their public APIs to fetch download links for specific versions.

Author: hyugogirubato
Date: 2024-03-03
Contact: https://github.com/hyugogirubato/DVDFabExtendDownload/issues
Repository: https://github.com/hyugogirubato/DVDFabExtendDownload

Note: This script is provided 'as is', with no warranty expressed or implied. The author or contributors are not responsible for any damages that may arise from its use.
"""
from enum import Enum

import requests
from pick import pick


class Products(Enum):
    DVDFab = {
        'eds_pid': 20021,
        'software': {
            'win': {
                'DVDFab x86': [22, 42, 57, 66],
                'DVDFab x64': [26, 44, 58, 67]
            },
            'mac': {
                'DVDFab for Intel Chip': [41, 56, 65],
                'DVDFab for Apple Chip': [60, 68]
            }
        }
    }
    StreamFab = {
        'eds_pid': 20022,
        'software': {
            'win': {
                'StreamFab x86': [48],
                'StreamFab x64': [49]
            },
            'mac': {
                'StreamFab for Intel Chip': [50],
                'StreamFab for Apple Chip': [59]
            }
        }
    }
    MusicFab = {
        'eds_pid': 20300,
        'software': {
            'win': {
                'MusicFab x86': [69],
                'MusicFab x64': [70]
            },
            'mac': {
                'MusicFab for Intel Chip': [71],
                'MusicFab for Apple Chip': [72]
            }
        }
    }
    PlayerFab = {
        'eds_pid': 20024,
        'software': {
            'win': {
                'PlayerFab x86': [31],
                'PlayerFab x64': [12],
                'Player 6 x86': ['player6_31'],
                'Player 6 x64': ['player6_12']
            },
            'mac': {
                'Player 6': [32],
                'Player 5': [28],
            }
        }
    }
    UniFab = {
        'eds_pid': 20023,
        'software': {
            'win': {
                'UniFab x86': [98],
                'UniFab x64': [99],
                'Toolkit': [202],
                'Video Converter Pro': [93],
                'VideoCruise': [1051]
            }
        }
    }
    Passkey = {
        'eds_pid': 20025,
        'software': {
            'win': {
                'Passkey': [20]
            }
        }
    }
    PhotoEnhancerAI = {
        'eds_pid': 20026,
        'software': {
            'win': {
                'Photo Enhancer AI': [90]
            }
        }
    }
    VideoEnhancerAI = {
        'eds_pid': 20027,
        'software': {
            'win': {
                'Video Enhancer AI': [92]
            }
        }
    }
    MediaRecover = {
        'eds_pid': 20028,
        'software': {
            'win': {
                'Media Recover': [91]
            }
        }
    }
    Geekit = {
        'eds_pid': 20029,
        'software': {
            'win': {
                'Geekit': [25]
            }
        }
    }
    ExplorerFab = {
        'eds_pid': None,
        'software': {
            'win': {
                'ExplorerFab x86': [203],
                'ExplorerFab x64': [204]
            }
        }
    }


if __name__ == '__main__':
    print('[I] DVDFab ExtendDownload v1.0.0')
    name, _ = pick([p.name for p in Products], 'Product')
    print(f'[I] Product: {name}')
    product = Products[name].value

    platform, _ = pick(list(product['software'].keys()), 'Platform')
    print(f'[I] Platform: {platform}')
    software, _ = pick(list(product['software'][platform].keys()), 'Software')
    print(f'[I] Software: {software}')

    versions = requests.request(
        method='GET',
        url='https://backend.streamfab.com/change_log/extend_download',
        params={'lang': 'en', 'software': ','.join(map(str, product['software'][platform][software]))}
    ).json()['data']

    _, index = pick([v['version'] for v in versions], 'Version')
    source = versions[index]['extend_download']
    print(f'[I] Download: {source}')
