BOT_NAME = 'uoc_spider'
LOG_LEVEL = 'ERROR'
SPIDER_MODULES = ['spiders']

DEFAULT_REQUEST_HEADERS = {
        'authority': 'api.pisos.com',
        'sec-ch-ua': '"Chromium";v="92", " Not A;Brand";v="99", "Google Chrome";v="92"',
        'accept': 'application/json, text/plain, */*',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        'origin': 'https://www.pisos.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pisos.com/mapa/venta/pisos-isla_de_mallorca/',
        'accept-language': 'en-GB,en;q=0.9,es-ES;q=0.8,es;q=0.7,en-US;q=0.6,ca;q=0.5,lt;q=0.4',
        'cookie': 'CustomSessionId=de17e0b9d09440bb8497047ebeeef65f; NombreOrigenSesion=Indeterminado; NombreOrigenMarketing=Indeterminado; _gid=GA1.2.1268439225.1630168158; AMCVS_9854C13E58403FEB0A495D53@AdobeOrg=1; s_ecid=MCMID|63987960052095364043921952337018889833; s_cc=true; AMCV_9854C13E58403FEB0A495D53@AdobeOrg=-1124106680|MCIDTS|18868|MCMID|63987960052095364043921952337018889833|MCAAMLH-1630772957|6|MCAAMB-1630772957|RKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y|MCOPTOUT-1630175358s|NONE|MCAID|NONE|vVersion|5.2.0; didomi_token=eyJ1c2VyX2lkIjoiMTdiOGQ5ODAtZTM1MC02NTk5LWE2YjItNjY2NmM4MzNmNDQyIiwiY3JlYXRlZCI6IjIwMjEtMDgtMjhUMTY6Mjk6MjUuOTE0WiIsInVwZGF0ZWQiOiIyMDIxLTA4LTI4VDE2OjI5OjI1LjkxNFoiLCJ2ZW5kb3JzIjp7ImVuYWJsZWQiOlsidHdpdHRlciIsImdvb2dsZSIsImM6YWRvYmUtdGFnbWFuYWdlciIsImM6c2VudHJ5IiwiYzpxdWFsaWZpby1XQTdXbkhCaSIsImM6c2FsZXNmb3JjZS1FNmhRblpCMiIsImM6ZG9ndHJhY2stZWNwbXBwMk0iLCJjOmhvdGphciIsImM6aW5zdGFncmFtIiwiYzpvbW5pdHVyZS1hZG9iZS1hbmFseXRpY3MiLCJjOmNoYXJ0YmVhdCIsImM6bmV3LXJlbGljIiwiYzpnaWd5YS1jb3VudGVyIiwiYzpnaWd5YSIsImM6bHVja3ktb3JhbmdlIiwiYzppbmRpZ2l0YWxsLVAzRjRpZlc0IiwiYzprZWVzaW5nLThmVEhyVUFnIiwiYzp2aWx5bngtTjNZSjlaSlgiLCJjOmJsdWVrbm93LThkZ0NHNktKIiwiYzpjb25uZWN0aWYtN2dKYUNHdzIiLCJjOjR3LW1hcmtldHBsYWNlIl19LCJwdXJwb3NlcyI6eyJlbmFibGVkIjpbImRhdGFfc2hhcmluZyIsImdlb2xvY2F0aW9uX2RhdGEiLCJkZXZpY2VfY2hhcmFjdGVyaXN0aWNzIl19LCJ2ZW5kb3JzX2xpIjp7ImVuYWJsZWQiOlsiZ29vZ2xlIl19LCJ2ZXJzaW9uIjoyLCJhYyI6IkFGbUFDQUZrLkFBQUEifQ==; euconsent-v2=CPLp-v7PLp-v7AHABBENBoCsAP_AAH_AAAAAHkNf_X9fb2vj-_59d_t0eY1P9_63t-wzjheNs-8NyZ_X_J8X42MyvB34pqYKmR4EunLBAQdlHGHcTQgAwIkVqTPsYk2MjzNKJ7JEmlMbO2dYGH9vn8XTuZKY70-8___zv3-v_v__7qAAAAAgBAAAAAgAAIABAAAAAAAEDiwCTDUvIAGxLHAk2jSqFECMKwkKgFABRQDC0TWEBI4KdkcBHqCBAAhMQEIEQIMQUQMAgAEAgCQiIAQA4EAiAIgEAAIARICEABEgCCwAsDAIABQDQsAIoAhAkIMDgqOUwICJFooJ5AAAAAAQAgAAAAAAAEAA.f_gAD_gAAAAA; UltimoEspecialista=176138; __gads=ID=638b2de19fab49b6:T=1630168174:S=ALNI_MakfbSMMMtQkDkEwE4SxXQhHMU23w; _hjid=f41b80d0-07e2-4699-8326-0442b0154ccf; UltimaUrlParrilla=https://www.pisos.com/busqueda/0.1000.F002.C00000000000201.0.0X0.0.0.0X0.0.0X0X0.1.0.0X0.0X0.0/; _hjAbsoluteSessionInProgress=0; cto_bundle=QQyxkV9NRmNrcHRidUI1cmkzUDlObmE5OG52cXNON25kMiUyRjBHJTJCbTA4cGZreU9Ea0NCZ3JlZWRkSnNmN21DZCUyQjJmTVJ5THVadVMxR004SEs0NDZOSUp3YlpQRElTdzMybzJkVzdudTVYcHlaZExFemZTcE9BcDklMkJ4Z3Z4MGVacGk4N1RvMSUyQmVGZVZjNVBzVzVwU0RmRlhlWUpnJTNEJTNE; s_nr=1630175464703-Repeat; s_ppn=busqueda:0-1000-f002-c00000000000201-0-0x0-0-0-0x0-0-0x0x0-1-0-0x0-0x0-0:pisos-en-isla-de-mallorca-islas-baleares-illes-balears-pisos-com; _gat_UA-2057447-4=1; s_ppvl=busqueda%3A0-1000-f002-c00000000000201-0-0x0-0-0-0x0-0-0x0x0-1-0-0x0-0x0-0%3Apisos-en-isla-de-mallorca-islas-baleares-illes-balears-pisos-com,4,4,396,1280,396,1280,800,2,P; s_ppv=comprar%3Acasa-sestanyol-de-migjorn-15042766476-100100%3Acasa-en-venta-en-sestanyol-de-migjorn-en-sestanyol-de-migjorn-por-397-000-%u20AC,15,15,664,1280,664,1280,800,2,P; cookieNavegacionPortal=https://~/mapa/$vn/pisos-isla_de_mallorca/*https://~/mapa/$vn/pisos-isla_de_mallorca/*https://~/mapa/$vn/pisos-isla_de_mallorca/*https://~/mapa/$vn/pisos-isla_de_mallorca/*https://~/$cr/casa-sestanyol_de_migjorn-15042766476_100100/; _gat=1; _ga_7N4KR6VRNY=GS1.1.1630175465.3.1.1630175469.0; _ga=GA1.1.1542726223.1630168158'
    }

MONGODB_SERVER = "mongo_uoc"
MONGODB_PORT = 27017
MONGODB_DB = "uoc"
MONGODB_COLLECTION = "real_states"

DOWNLOAD_DELAY = 5
CONCURRENT_REQUESTS_PER_DOMAIN = 5
