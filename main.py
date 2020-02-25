from bitmex_websocket import BitMEXWebsocket
ws = BitMEXWebsocket(endpoint="https://testnet.bitmex.com/api/v1", symbol="XBTUSD", api_key=None, api_secret=None)
print(ws.market_depth())
