from django.shortcuts import render

# Diccionario de bandas, álbumes y canciones
BANDAS = {
	'acdc': {
		'nombre': 'AC/DC',
		'imagen': 'bandas/acdc.jpg',
		'albumes': [
			{'id': 'high_voltage', 'nombre': 'High Voltage', 'imagen': 'albumes/high_voltage.jpg', 'canciones': ["It's a Long Way to the Top", "T.N.T.", "High Voltage"]},
			{'id': 'highway_to_hell', 'nombre': 'Highway to Hell', 'imagen': 'albumes/highway_to_hell.jpg', 'canciones': ["Highway to Hell", "Girls Got Rhythm", "Touch Too Much"]},
			{'id': 'back_in_black', 'nombre': 'Back in Black', 'imagen': 'albumes/back_in_black.jpg', 'canciones': ["Hells Bells", "Shoot to Thrill", "Back in Black"]},
			{'id': 'for_those_about', 'nombre': 'For Those About to Rock', 'imagen': 'albumes/for_those_about.jpg', 'canciones': ["For Those About to Rock", "Let's Get It Up", "Evil Walks"]},
			{'id': 'black_ice', 'nombre': 'Black Ice', 'imagen': 'albumes/black_ice.jpg', 'canciones': ["Rock 'n' Roll Train", "Big Jack", "Anything Goes"]},
		]
	},
	'gnr': {
		'nombre': "Guns N' Roses",
		'imagen': 'bandas/gnr.jpg',
		'albumes': [
			{'id': 'appetite', 'nombre': 'Appetite for Destruction', 'imagen': 'albumes/appetite.jpg', 'canciones': ["Welcome to the Jungle", "Sweet Child o' Mine", "Paradise City"]},
			{'id': 'lies', 'nombre': "G N' R Lies", 'imagen': 'albumes/lies.jpg', 'canciones': ["Patience", "Used to Love Her", "One in a Million"]},
			{'id': 'illusion1', 'nombre': 'Use Your Illusion I', 'imagen': 'albumes/illusion1.jpg', 'canciones': ["November Rain", "Don't Cry", "Live and Let Die"]},
			{'id': 'illusion2', 'nombre': 'Use Your Illusion II', 'imagen': 'albumes/illusion2.jpg', 'canciones': ["Civil War", "Knockin' on Heaven's Door", "Yesterdays"]},
			{'id': 'chinese', 'nombre': 'Chinese Democracy', 'imagen': 'albumes/chinese.jpg', 'canciones': ["Chinese Democracy", "Better", "Street of Dreams"]},
		]
	},
	'coldplay': {
		'nombre': 'Coldplay',
		'imagen': 'bandas/coldplay.jpg',
		'albumes': [
			{'id': 'parachutes', 'nombre': 'Parachutes', 'imagen': 'albumes/parachutes.jpg', 'canciones': ["Yellow", "Shiver", "Trouble"]},
			{'id': 'rush', 'nombre': 'A Rush of Blood to the Head', 'imagen': 'albumes/rush.jpg', 'canciones': ["Clocks", "The Scientist", "In My Place"]},
			{'id': 'xy', 'nombre': 'X&Y', 'imagen': 'albumes/xy.jpg', 'canciones': ["Fix You", "Speed of Sound", "Talk"]},
			{'id': 'viva', 'nombre': 'Viva la Vida or Death and All His Friends', 'imagen': 'albumes/viva.jpg', 'canciones': ["Viva la Vida", "Violet Hill", "Lost!"]},
			{'id': 'mylo', 'nombre': 'Mylo Xyloto', 'imagen': 'albumes/mylo.jpg', 'canciones': ["Paradise", "Every Teardrop Is a Waterfall", "Charlie Brown"]},
		]
	},
	'21pilots': {
		'nombre': 'Twenty One Pilots',
		'imagen': 'bandas/21pilots.jpg',
		'albumes': [
			{'id': 'vessel', 'nombre': 'Vessel', 'imagen': 'albumes/vessel.jpg', 'canciones': ["Holding on to You", "Car Radio", "House of Gold"]},
			{'id': 'blurryface', 'nombre': 'Blurryface', 'imagen': 'albumes/blurryface.jpg', 'canciones': ["Stressed Out", "Ride", "Tear in My Heart"]},
			{'id': 'trench', 'nombre': 'Trench', 'imagen': 'albumes/trench.jpg', 'canciones': ["Jumpsuit", "Nico and the Niners", "My Blood"]},
			{'id': 'scaled', 'nombre': 'Scaled and Icy', 'imagen': 'albumes/scaled.jpg', 'canciones': ["Shy Away", "Choker", "Saturday"]},
			{'id': 'selftitled', 'nombre': 'Twenty One Pilots', 'imagen': 'albumes/selftitled.jpg', 'canciones': ["Implicit Demand for Proof", "Fall Away", "Johnny Boy"]},
		]
	},
	'linkinpark': {
		'nombre': 'Linkin Park',
		'imagen': 'bandas/linkinpark.jpg',
		'albumes': [
			{'id': 'hybrid', 'nombre': 'Hybrid Theory', 'imagen': 'albumes/hybrid.jpg', 'canciones': ["In the End", "Crawling", "One Step Closer"]},
			{'id': 'meteora', 'nombre': 'Meteora', 'imagen': 'albumes/meteora.jpg', 'canciones': ["Numb", "Somewhere I Belong", "Faint"]},
			{'id': 'minutes', 'nombre': 'Minutes to Midnight', 'imagen': 'albumes/minutes.jpg', 'canciones': ["What I've Done", "Bleed It Out", "Shadow of the Day"]},
			{'id': 'thousand', 'nombre': 'A Thousand Suns', 'imagen': 'albumes/thousand.jpg', 'canciones': ["The Catalyst", "Waiting for the End", "Burning in the Skies"]},
			{'id': 'living', 'nombre': 'Living Things', 'imagen': 'albumes/living.jpg', 'canciones': ["Burn It Down", "Lost in the Echo", "Castle of Glass"]},
		]
	},
}

def bandas(request):
	return render(request, 'catalogo/bandas.html', {'bandas': BANDAS})

def albumes(request, banda_id):
	banda = BANDAS.get(banda_id)
	if not banda:
		return render(request, 'catalogo/error.html', {'mensaje': 'Banda no encontrada'})
	return render(request, 'catalogo/albumes.html', {'banda_id': banda_id, 'banda': banda})

def canciones(request, banda_id, album_id):
	banda = BANDAS.get(banda_id)
	if not banda:
		return render(request, 'catalogo/error.html', {'mensaje': 'Banda no encontrada'})
	album = next((a for a in banda['albumes'] if a['id'] == album_id), None)
	if not album:
		return render(request, 'catalogo/error.html', {'mensaje': 'Álbum no encontrado'})
	return render(request, 'catalogo/canciones.html', {'banda_id': banda_id, 'album': album})
COLDPLAY_DATA = {
	'tipos': {
		'albumes_estudio': {
			'nombre': 'Álbumes de Estudio',
			'albumes': [
				{
					'id': 'parachutes',
					'nombre': 'Parachutes',
					'caratula': 'parachutes.jpg',
					'temas': [
						{'nombre': "Don't Panic", 'duracion': '2:17'},
						{'nombre': 'Shiver', 'duracion': '5:00'},
						{'nombre': 'Spies', 'duracion': '5:18'},
					]
				},
				{
					'id': 'arushofblood',
					'nombre': 'A Rush of Blood to the Head',
					'caratula': 'arushofblood.jpg',
					'temas': [
						{'nombre': 'Politik', 'duracion': '5:18'},
						{'nombre': 'In My Place', 'duracion': '3:48'},
						{'nombre': 'Clocks', 'duracion': '5:07'},
					]
				},
				{
					'id': 'x&y',
					'nombre': 'X&Y',
					'caratula': 'x&y.jpg',
					'temas': [
						{'nombre': 'Square One', 'duracion': '6:25'},
						{'nombre': 'What If', 'duracion': '4:57'},
						{'nombre': 'Fix You', 'duracion': '4:55'},
					]
				},
				{
					'id': 'viva',
					'nombre': 'Viva la Vida',
					'caratula': 'viva.jpg',
					'temas': [
						{'nombre': 'Life in Technicolor', 'duracion': '2:29'},
						{'nombre': 'Cemeteries of London', 'duracion': '3:21'},
						{'nombre': 'Viva la Vida', 'duracion': '4:02'},
					]
				},
				{
					'id': 'everyday',
					'nombre': 'Everyday Life',
					'caratula': 'everyday.jpg',
					'temas': [
						{'nombre': 'Sunrise', 'duracion': '2:31'},
						{'nombre': 'Church', 'duracion': '3:50'},
						{'nombre': 'Trouble in Town', 'duracion': '4:38'},
					]
				},
			]
		},
		'eps': {
			'nombre': 'EPs',
			'albumes': [
				{'id': 'safety', 'nombre': 'Safety EP', 'caratula': 'safety.jpg', 'temas': [
					{'nombre': 'Bigger Stronger', 'duracion': '4:49'},
					{'nombre': 'No More Keeping My Feet on the Ground', 'duracion': '4:31'},
					{'nombre': 'Such a Rush', 'duracion': '4:57'},
				]},
				{'id': 'prospekt', 'nombre': "Prospekt's March", 'caratula': 'prospekt.jpg', 'temas': [
					{'nombre': 'Life in Technicolor II', 'duracion': '4:06'},
					{'nombre': 'Postcards from Far Away', 'duracion': '0:48'},
					{'nombre': 'Glass of Water', 'duracion': '4:44'},
				]},
				{'id': 'theblue', 'nombre': 'The Blue Room', 'caratula': 'theblue.jpg', 'temas': [
					{'nombre': 'Bigger Stronger', 'duracion': '4:49'},
					{'nombre': "Don't Panic", 'duracion': '2:17'},
					{'nombre': 'See You Soon', 'duracion': '2:51'},
				]},
				{'id': 'mince', 'nombre': 'Mince Spies', 'caratula': 'mince.jpg', 'temas': [
					{'nombre': 'Brothers & Sisters', 'duracion': '4:05'},
					{'nombre': 'Only Superstition', 'duracion': '4:10'},
					{'nombre': 'Easy to Please', 'duracion': '3:02'},
				]},
				{'id': 'leftright', 'nombre': 'LeftRightLeftRightLeft', 'caratula': 'leftright.jpg', 'temas': [
					{'nombre': 'Glass of Water', 'duracion': '4:43'},
					{'nombre': '42', 'duracion': '3:57'},
					{'nombre': 'Clocks', 'duracion': '5:07'},
				]},
			]
		},
		'singles': {
			'nombre': 'Singles',
			'albumes': [
				{'id': 'yellow', 'nombre': 'Yellow', 'caratula': 'yellow.jpg', 'temas': [
					{'nombre': 'Yellow', 'duracion': '4:29'},
					{'nombre': 'Help Is Round the Corner', 'duracion': '2:38'},
					{'nombre': 'No More Keeping My Feet on the Ground', 'duracion': '4:31'},
				]},
				{'id': 'clocks', 'nombre': 'Clocks', 'caratula': 'clocks.jpg', 'temas': [
					{'nombre': 'Clocks', 'duracion': '5:07'},
					{'nombre': 'Crests of Waves', 'duracion': '3:39'},
					{'nombre': 'Animals', 'duracion': '5:16'},
				]},
				{'id': 'fixyou', 'nombre': 'Fix You', 'caratula': 'fixyou.jpg', 'temas': [
					{'nombre': 'Fix You', 'duracion': '4:55'},
					{'nombre': 'The World Turned', 'duracion': '3:32'},
					{'nombre': 'Pour Me', 'duracion': '5:14'},
				]},
				{'id': 'viva', 'nombre': 'Viva la Vida', 'caratula': 'viva.jpg', 'temas': [
					{'nombre': 'Viva la Vida', 'duracion': '4:02'},
					{'nombre': 'Death Will Never Conquer', 'duracion': '1:17'},
					{'nombre': 'Lost?', 'duracion': '3:55'},
				]},
				{'id': 'adventure', 'nombre': 'Adventure of a Lifetime', 'caratula': 'adventure.jpg', 'temas': [
					{'nombre': 'Adventure of a Lifetime', 'duracion': '4:23'},
					{'nombre': 'Everglow', 'duracion': '4:42'},
					{'nombre': 'Miracles', 'duracion': '3:55'},
				]},
			]
		},
		'colaboraciones': {
			'nombre': 'Colaboraciones',
			'albumes': [
				{'id': 'something', 'nombre': 'Something Just Like This', 'caratula': 'something.jpg', 'temas': [
					{'nombre': 'Something Just Like This', 'duracion': '4:07'},
					{'nombre': 'Something Just Like This (Tokyo Remix)', 'duracion': '4:08'},
					{'nombre': 'Something Just Like This (Alesso Remix)', 'duracion': '4:08'},
				]},
				{'id': 'letssing', 'nombre': "Let's Sing", 'caratula': 'letssing.jpg', 'temas': [
					{'nombre': "Let's Sing", 'duracion': '3:45'},
					{'nombre': "Let's Sing (Remix)", 'duracion': '4:00'},
					{'nombre': "Let's Sing (Acoustic)", 'duracion': '3:50'},
				]},
				{'id': 'beautiful', 'nombre': 'Beautiful', 'caratula': 'beautiful.jpg', 'temas': [
					{'nombre': 'Beautiful', 'duracion': '3:29'},
					{'nombre': 'Beautiful (Remix)', 'duracion': '3:50'},
					{'nombre': 'Beautiful (Acoustic)', 'duracion': '3:40'},
				]},
				{'id': 'orphan', 'nombre': 'Orphans', 'caratula': 'orphan.jpg', 'temas': [
					{'nombre': 'Orphans', 'duracion': '3:17'},
					{'nombre': 'Arabesque', 'duracion': '5:40'},
					{'nombre': 'Guns', 'duracion': '1:55'},
				]},
				{'id': 'hymn', 'nombre': 'Hymn for the Weekend', 'caratula': 'hymn.jpg', 'temas': [
					{'nombre': 'Hymn for the Weekend', 'duracion': '4:18'},
					{'nombre': 'Hymn for the Weekend (Remix)', 'duracion': '3:32'},
					{'nombre': 'Hymn for the Weekend (Acoustic)', 'duracion': '3:45'},
				]},
			]
		},
	}
}

def catalogo_principal(request):
	tipos = COLDPLAY_DATA['tipos']
	return render(request, 'catalogo/catalogo_principal.html', {'tipos': tipos})

def albumes_tipo(request, tipo_id):
	tipo = COLDPLAY_DATA['tipos'].get(tipo_id)
	if not tipo:
		return render(request, 'catalogo/error.html', {'mensaje': 'Tipo no encontrado'})
	return render(request, 'catalogo/albumes_tipo.html', {'tipo_id': tipo_id, 'tipo': tipo})

def temas_album(request, tipo_id, album_id):
	tipo = COLDPLAY_DATA['tipos'].get(tipo_id)
	if not tipo:
		return render(request, 'catalogo/error.html', {'mensaje': 'Tipo no encontrado'})
	album = next((a for a in tipo['albumes'] if a['id'] == album_id), None)
	if not album:
		return render(request, 'catalogo/error.html', {'mensaje': 'Álbum no encontrado'})
	return render(request, 'catalogo/temas_album.html', {'tipo_id': tipo_id, 'album': album})

def detalle_album(request, tipo_id, album_id):
	tipo = COLDPLAY_DATA['tipos'].get(tipo_id)
	if not tipo:
		return render(request, 'catalogo/error.html', {'mensaje': 'Tipo no encontrado'})
	album = next((a for a in tipo['albumes'] if a['id'] == album_id), None)
	if not album:
		return render(request, 'catalogo/error.html', {'mensaje': 'Álbum no encontrado'})
	return render(request, 'catalogo/detalle_album.html', {'album': album})
