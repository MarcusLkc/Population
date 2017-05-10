from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'Populations pf Cpimtroes in North America'
wm.add('North America', {'ca': 34126000, 'us': 30934900, 'mx': 113423000})
wm.render_to_file('na_populations.svg')