import json

import requests
from pathlib import Path

from dvdfab import EDS_PRODUCTS


def update(obj1: dict, obj2: dict) -> dict:
    for k2, v2 in obj2.items():
        v1 = obj1.get(k2)
        if v1:
            assert type(v2) == type(v1), 'Type mismatch'
            if isinstance(v2, dict):
                obj1[k2] = update(v1, v2)
            elif isinstance(v2, list):
                for i2 in v2[::-1]:
                    if i2 not in v1:
                        v1.insert(0, i2)
                obj1[k2] = v1
            else:
                obj1[k2] = v2
        else:
            obj1[k2] = v2

    return obj1


if __name__ == '__main__':
    laravel = 'YOUR_LARAVEL_TOKEN'

    links = {}
    for product, pvalue in EDS_PRODUCTS.items():
        print(product)
        for system, svalue in pvalue['software'].items():
            print(system)
            for arch, avalue in svalue.items():
                print(arch)
                r = requests.request(
                    method='GET',
                    url='https://web-backend-us.dvdfab.cn/change_log/extend_download',
                    params={
                        'lang': 'en',
                        'software': avalue,
                        'laravel_session': laravel,
                        'product_line': product.lower().replace(' ', '_')
                    },
                    headers={
                        'Accept': 'application/json',
                        'Accept-Encoding': 'gzip, deflate, br, zstd',
                        'Accept-Language': 'en-US,en;q=0.9',
                        'Connection': 'keep-alive',
                        'Host': 'web-backend-us.dvdfab.cn',
                        'Origin': 'https://www.dvdfab.cn',
                        'Referer': 'https://www.dvdfab.cn/',
                        'sec-ch-ua': '"Not)A;Brand";v="99", "Microsoft Edge";v="127", "Chromium";v="127"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Sec-Fetch-Dest': 'empty',
                        'Sec-Fetch-Mode': 'cors',
                        'Sec-Fetch-Site': 'same-site',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
                    }
                )
                r.raise_for_status()
                versions = r.json()['data']
                links.setdefault(product, {}).setdefault(system, {})[arch] = versions

    backup: dict = json.loads(Path('backup.json').read_bytes())
    current = update(backup, links)

    Path('backup.json').write_text(json.dumps(current, indent=4))
