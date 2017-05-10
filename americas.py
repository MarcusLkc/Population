from pygal.maps.world import World
rom pygal.maps.world import World


wm = World()
wm.force_uri_protocol = 'http'
wm.title = 'North, Central, and South America'

wm.add('Nort America', ['ca','mx','us'])
wm.add('Central America',['bz','cr','gt','hn','ni','pa','sv'])
wm.add('South America', ['ar','bo','br','cl','co','ec','gf','gy','pe','sr','uy','ve'])
wm.render_to_file('americas.svg')