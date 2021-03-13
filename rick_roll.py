from aiohttp import web


routes = web.RouteTableDef()

@routes.get("/{path:.*}")
async def hello(request):
    if request.match_info['path'] == "bait.png":
        return web.FileResponse("bait.png")
    else:
        return web.FileResponse("rick_roll.html")


app = web.Application()
app.add_routes(routes)
web.run_app(app, port = 4100)