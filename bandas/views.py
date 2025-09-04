from django.shortcuts import render

# Estructura simple: 5 bandas, 5 álbumes cada una, 3 canciones cada álbum
BANDAS_DATA = {
    'acdc': {
        'nombre': 'AC/DC',
        'imagen': 'acdc.jpg',
        'albumes': {
            'back_in_black': {
                'nombre': 'Back in Black',
                'imagen': 'acdc_album1.jpg',
                'canciones': [
                    {'nombre': 'Hells Bells', 'duracion': '5:12'},
                    {'nombre': 'Back in Black', 'duracion': '4:15'},
                    {'nombre': 'You Shook Me All Night Long', 'duracion': '3:30'}
                ]
            },
            'highway_to_hell': {
                'nombre': 'Highway to Hell',
                'imagen': 'acdc_album2.jpg',
                'canciones': [
                    {'nombre': 'Highway to Hell', 'duracion': '3:28'},
                    {'nombre': 'Girls Got Rhythm', 'duracion': '3:23'},
                    {'nombre': 'Walk All Over You', 'duracion': '5:10'}
                ]
            },
            'thunderstruck': {
                'nombre': 'The Razors Edge',
                'imagen': 'acdc_album3.jpg',
                'canciones': [
                    {'nombre': 'Thunderstruck', 'duracion': '4:52'},
                    {'nombre': 'Fire Your Guns', 'duracion': '2:53'},
                    {'nombre': 'Moneytalks', 'duracion': '3:45'}
                ]
            },
            'rock_or_bust': {
                'nombre': 'Rock or Bust',
                'imagen': 'acdc_album4.jpg',
                'canciones': [
                    {'nombre': 'Rock or Bust', 'duracion': '3:04'},
                    {'nombre': 'Play Ball', 'duracion': '2:47'},
                    {'nombre': 'Rock the Blues Away', 'duracion': '3:24'}
                ]
            },
            'for_those': {
                'nombre': 'For Those About to Rock',
                'imagen': 'acdc_album5.jpg',
                'canciones': [
                    {'nombre': 'For Those About to Rock', 'duracion': '5:44'},
                    {'nombre': 'I Put the Finger on You', 'duracion': '3:25'},
                    {'nombre': 'Lets Get It Up', 'duracion': '4:15'}
                ]
            }
        }
    },
    'gunsnroses': {
        'nombre': 'Guns N\' Roses',
        'imagen': 'gunsnroses.jpg',
        'albumes': {
            'appetite': {
                'nombre': 'Appetite for Destruction',
                'imagen': 'gunsnroses_album1.jpg',
                'canciones': [
                    {'nombre': 'Sweet Child O\' Mine', 'duracion': '5:56'},
                    {'nombre': 'Welcome to the Jungle', 'duracion': '4:34'},
                    {'nombre': 'Paradise City', 'duracion': '6:46'}
                ]
            },
            'use_your_illusion': {
                'nombre': 'Use Your Illusion I',
                'imagen': 'gunsnroses_album2.jpg',
                'canciones': [
                    {'nombre': 'November Rain', 'duracion': '8:57'},
                    {'nombre': 'Don\'t Cry', 'duracion': '4:45'},
                    {'nombre': 'Live and Let Die', 'duracion': '3:04'}
                ]
            },
            'lies': {
                'nombre': 'G N\' R Lies',
                'imagen': 'gunsnroses_album3.jpg',
                'canciones': [
                    {'nombre': 'Patience', 'duracion': '5:56'},
                    {'nombre': 'Used to Love Her', 'duracion': '3:13'},
                    {'nombre': 'You\'re Crazy', 'duracion': '3:17'}
                ]
            },
            'chinese_democracy': {
                'nombre': 'Chinese Democracy',
                'imagen': 'gunsnroses_album4.jpg',
                'canciones': [
                    {'nombre': 'Chinese Democracy', 'duracion': '4:43'},
                    {'nombre': 'Shackler\'s Revenge', 'duracion': '3:37'},
                    {'nombre': 'Better', 'duracion': '4:59'}
                ]
            },
            'spaghetti': {
                'nombre': 'The Spaghetti Incident?',
                'imagen': 'gunsnroses_album5.jpg',
                'canciones': [
                    {'nombre': 'Since I Don\'t Have You', 'duracion': '4:20'},
                    {'nombre': 'New Rose', 'duracion': '2:38'},
                    {'nombre': 'Down on the Farm', 'duracion': '3:28'}
                ]
            }
        }
    },
    'coldplay': {
        'nombre': 'Coldplay',
        'imagen': 'coldplay.jpg',
        'albumes': {
            'parachutes': {
                'nombre': 'Parachutes',
                'imagen': 'coldplay_album1.jpg',
                'canciones': [
                    {'nombre': 'Yellow', 'duracion': '4:29'},
                    {'nombre': 'Trouble', 'duracion': '4:31'},
                    {'nombre': 'Don\'t Panic', 'duracion': '2:17'}
                ]
            },
            'rush_of_blood': {
                'nombre': 'A Rush of Blood to the Head',
                'imagen': 'coldplay_album2.jpg',
                'canciones': [
                    {'nombre': 'In My Place', 'duracion': '3:48'},
                    {'nombre': 'Clocks', 'duracion': '5:07'},
                    {'nombre': 'The Scientist', 'duracion': '5:09'}
                ]
            },
            'x_y': {
                'nombre': 'X&Y',
                'imagen': 'coldplay_album3.jpg',
                'canciones': [
                    {'nombre': 'Speed of Sound', 'duracion': '4:48'},
                    {'nombre': 'Fix You', 'duracion': '4:55'},
                    {'nombre': 'Talk', 'duracion': '5:11'}
                ]
            },
            'viva_la_vida': {
                'nombre': 'Viva la Vida',
                'imagen': 'coldplay_album4.jpg',
                'canciones': [
                    {'nombre': 'Viva la Vida', 'duracion': '4:02'},
                    {'nombre': 'Violet Hill', 'duracion': '3:42'},
                    {'nombre': 'Lovers in Japan', 'duracion': '3:57'}
                ]
            },
            'mylo_xyloto': {
                'nombre': 'Mylo Xyloto',
                'imagen': 'coldplay_album5.jpg',
                'canciones': [
                    {'nombre': 'Paradise', 'duracion': '4:39'},
                    {'nombre': 'Every Teardrop Is a Waterfall', 'duracion': '4:01'},
                    {'nombre': 'Charlie Brown', 'duracion': '4:45'}
                ]
            }
        }
    },
    'twentyonepilots': {
        'nombre': 'Twenty One Pilots',
        'imagen': 'twentyonepilots.jpg',
        'albumes': {
            'blurryface': {
                'nombre': 'Blurryface',
                'imagen': 'twentyonepilots_album1.jpg',
                'canciones': [
                    {'nombre': 'Stressed Out', 'duracion': '3:22'},
                    {'nombre': 'Ride', 'duracion': '3:34'},
                    {'nombre': 'Heathens', 'duracion': '3:15'}
                ]
            },
            'trench': {
                'nombre': 'Trench',
                'imagen': 'twentyonepilots_album2.jpg',
                'canciones': [
                    {'nombre': 'Jumpsuit', 'duracion': '3:58'},
                    {'nombre': 'Levitate', 'duracion': '2:25'},
                    {'nombre': 'Morph', 'duracion': '4:19'}
                ]
            },
            'scaled_and_icy': {
                'nombre': 'Scaled and Icy',
                'imagen': 'twentyonepilots_album3.jpg',
                'canciones': [
                    {'nombre': 'Shy Away', 'duracion': '2:55'},
                    {'nombre': 'Choker', 'duracion': '3:31'},
                    {'nombre': 'The Outside', 'duracion': '3:32'}
                ]
            },
            'vessel': {
                'nombre': 'Vessel',
                'imagen': 'twentyonepilots_album4.jpg',
                'canciones': [
                    {'nombre': 'Ode to Sleep', 'duracion': '5:09'},
                    {'nombre': 'Holding on to You', 'duracion': '3:56'},
                    {'nombre': 'Migraine', 'duracion': '3:59'}
                ]
            },
            'regional_at_best': {
                'nombre': 'Regional at Best',
                'imagen': 'twentyonepilots_album5.jpg',
                'canciones': [
                    {'nombre': 'Guns for Hands', 'duracion': '4:18'},
                    {'nombre': 'Lovely', 'duracion': '4:17'},
                    {'nombre': 'Ruby', 'duracion': '3:42'}
                ]
            }
        }
    },
    'linkinpark': {
        'nombre': 'Linkin Park',
        'imagen': 'linkinpark.jpg',
        'albumes': {
            'hybrid_theory': {
                'nombre': 'Hybrid Theory',
                'imagen': 'linkinpark_album1.jpg',
                'canciones': [
                    {'nombre': 'In the End', 'duracion': '3:36'},
                    {'nombre': 'One Step Closer', 'duracion': '2:36'},
                    {'nombre': 'Crawling', 'duracion': '3:29'}
                ]
            },
            'meteora': {
                'nombre': 'Meteora',
                'imagen': 'linkinpark_album2.jpg',
                'canciones': [
                    {'nombre': 'Numb', 'duracion': '3:07'},
                    {'nombre': 'Somewhere I Belong', 'duracion': '3:33'},
                    {'nombre': 'Breaking the Habit', 'duracion': '3:16'}
                ]
            },
            'minutes_to_midnight': {
                'nombre': 'Minutes to Midnight',
                'imagen': 'linkinpark_album3.jpg',
                'canciones': [
                    {'nombre': 'What I\'ve Done', 'duracion': '3:25'},
                    {'nombre': 'Bleed It Out', 'duracion': '2:44'},
                    {'nombre': 'Shadow of the Day', 'duracion': '4:49'}
                ]
            },
            'living_things': {
                'nombre': 'Living Things',
                'imagen': 'linkinpark_album4.jpg',
                'canciones': [
                    {'nombre': 'Burn It Down', 'duracion': '3:50'},
                    {'nombre': 'Lost in the Echo', 'duracion': '3:25'},
                    {'nombre': 'Castle of Glass', 'duracion': '3:25'}
                ]
            },
            'one_more_light': {
                'nombre': 'One More Light',
                'imagen': 'linkinpark_album5.jpg',
                'canciones': [
                    {'nombre': 'Heavy', 'duracion': '2:49'},
                    {'nombre': 'Battle Symphony', 'duracion': '3:36'},
                    {'nombre': 'One More Light', 'duracion': '4:15'}
                ]
            }
        }
    },
        'green_day': {
        'nombre': 'Green Day',
        'imagen': 'green_day.jpg',
        'albumes': {
            'dookie': {
                'nombre': 'Dookie',
                'imagen': 'green_day_album1.jpg',
                'canciones': [
                    {'nombre': 'Basket Case', 'duracion': '3:03'},
                    {'nombre': 'When I Come Around', 'duracion': '2:58'},
                    {'nombre': 'Longview', 'duracion': '3:59'}
                ]
            },
            'american_idiot': {
                'nombre': 'American Idiot',
                'imagen': 'green_day_album2.jpg',
                'canciones': [
                    {'nombre': 'American Idiot', 'duracion': '2:54'},
                    {'nombre': 'Boulevard of Broken Dreams', 'duracion': '4:20'},
                    {'nombre': 'Holiday', 'duracion': '3:52'}
                ]
            },
            '21st_century_breakdown': {
                'nombre': '21st Century Breakdown',
                'imagen': 'green_day_album3.jpg',
                'canciones': [
                    {'nombre': '21st Century Breakdown', 'duracion': '5:09'},
                    {'nombre': 'Know Your Enemy', 'duracion': '3:11'},
                    {'nombre': '21 Guns', 'duracion': '5:21'}
                ]
            },
            'nimrod': {
                'nombre': 'Nimrod',
                'imagen': 'green_day_album4.jpg',
                'canciones': [
                    {'nombre': 'Hitchin’ a Ride', 'duracion': '2:51'},
                    {'nombre': 'Nice Guys Finish Last', 'duracion': '2:49'},
                    {'nombre': 'Good Riddance (Time of Your Life)', 'duracion': '2:34'}
                ]
            },
            'insomniac': {
                'nombre': 'Insomniac',
                'imagen': 'green_day_album5.jpg',
                'canciones': [
                    {'nombre': 'Geek Stink Breath', 'duracion': '2:15'},
                    {'nombre': 'Brain Stew', 'duracion': '3:13'},
                    {'nombre': 'Jaded', 'duracion': '1:30'}
                ]
            }
        }
    }
}

# Vistas simples
def lista_bandas(request):
    return render(request, 'bandas/bandas.html', {'bandas': BANDAS_DATA})

def lista_albumes(request, banda_id):
    banda = BANDAS_DATA.get(banda_id)
    if not banda:
        return render(request, 'bandas/error.html', {'mensaje': 'Banda no encontrada'})
    return render(request, 'bandas/albumes.html', {'banda_id': banda_id, 'banda': banda})

def lista_canciones(request, banda_id, album_id):
    banda = BANDAS_DATA.get(banda_id)
    if not banda:
        return render(request, 'bandas/error.html', {'mensaje': 'Banda no encontrada'})
    album = banda['albumes'].get(album_id)
    if not album:
        return render(request, 'bandas/error.html', {'mensaje': 'Álbum no encontrado'})
    return render(request, 'bandas/canciones.html', {
        'banda_id': banda_id, 
        'album_id': album_id, 
        'banda': banda, 
        'album': album
    })
