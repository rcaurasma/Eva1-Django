from django.db import models

# Datos de las bandas organizados como diccionarios
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
            'high_voltage': {
                'nombre': 'High Voltage',
                'imagen': 'acdc_album4.jpg',
                'canciones': [
                    {'nombre': 'T.N.T.', 'duracion': '3:35'},
                    {'nombre': 'High Voltage', 'duracion': '3:48'},
                    {'nombre': 'Live Wire', 'duracion': '5:50'}
                ]
            },
            'for_those_about_to_rock': {
                'nombre': 'For Those About to Rock',
                'imagen': 'acdc_album5.jpg',
                'canciones': [
                    {'nombre': 'For Those About to Rock', 'duracion': '5:44'},
                    {'nombre': 'I Put the Finger on You', 'duracion': '3:25'},
                    {'nombre': 'Lets Get It Up', 'duracion': '4:14'}
                ]
            }
        }
    },
    'gunsnroses': {
        'nombre': 'Guns N\' Roses',
        'imagen': 'gunsnroses.jpg',
        'albumes': {
            'appetite_for_destruction': {
                'nombre': 'Appetite for Destruction',
                'imagen': 'gunsnroses_album1.jpg',
                'canciones': [
                    {'nombre': 'Welcome to the Jungle', 'duracion': '4:31'},
                    {'nombre': 'It\'s So Easy', 'duracion': '3:21'},
                    {'nombre': 'Nightrain', 'duracion': '4:26'}
                ]
            },
            'use_your_illusion_i': {
                'nombre': 'Use Your Illusion I',
                'imagen': 'gunsnroses_album2.jpg',
                'canciones': [
                    {'nombre': 'Right Next Door to Hell', 'duracion': '3:02'},
                    {'nombre': 'Dust N\' Bones', 'duracion': '4:58'},
                    {'nombre': 'Live and Let Die', 'duracion': '3:04'}
                ]
            },
            'use_your_illusion_ii': {
                'nombre': 'Use Your Illusion II',
                'imagen': 'gunsnroses_album3.jpg',
                'canciones': [
                    {'nombre': 'Civil War', 'duracion': '7:42'},
                    {'nombre': '14 Years', 'duracion': '4:21'},
                    {'nombre': 'Yesterdays', 'duracion': '3:16'}
                ]
            },
            'chinese_democracy': {
                'nombre': 'Chinese Democracy',
                'imagen': 'gunsnroses_album4.jpg',
                'canciones': [
                    {'nombre': 'Chinese Democracy', 'duracion': '4:43'},
                    {'nombre': 'Shackler\'s Revenge', 'duracion': '3:36'},
                    {'nombre': 'Better', 'duracion': '4:58'}
                ]
            },
            'gnr_lies': {
                'nombre': 'G N\' R Lies',
                'imagen': 'gunsnroses_album5.jpg',
                'canciones': [
                    {'nombre': 'Reckless Life', 'duracion': '3:20'},
                    {'nombre': 'Nice Boys', 'duracion': '3:01'},
                    {'nombre': 'Move to the City', 'duracion': '4:45'}
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
                    {'nombre': 'Don\'t Panic', 'duracion': '2:17'},
                    {'nombre': 'Shiver', 'duracion': '5:00'},
                    {'nombre': 'Spies', 'duracion': '5:18'}
                ]
            },
            'a_rush_of_blood': {
                'nombre': 'A Rush of Blood to the Head',
                'imagen': 'coldplay_album2.jpg',
                'canciones': [
                    {'nombre': 'Politik', 'duracion': '5:18'},
                    {'nombre': 'In My Place', 'duracion': '3:48'},
                    {'nombre': 'God Put a Smile upon Your Face', 'duracion': '4:57'}
                ]
            },
            'x_and_y': {
                'nombre': 'X&Y',
                'imagen': 'coldplay_album3.jpg',
                'canciones': [
                    {'nombre': 'Square One', 'duracion': '4:47'},
                    {'nombre': 'What If', 'duracion': '4:57'},
                    {'nombre': 'White Shadows', 'duracion': '5:28'}
                ]
            },
            'viva_la_vida': {
                'nombre': 'Viva la Vida or Death and All His Friends',
                'imagen': 'coldplay_album4.jpg',
                'canciones': [
                    {'nombre': 'Life in Technicolor', 'duracion': '2:29'},
                    {'nombre': 'Cemeteries of London', 'duracion': '3:21'},
                    {'nombre': 'Lost!', 'duracion': '3:55'}
                ]
            },
            'mylo_xyloto': {
                'nombre': 'Mylo Xyloto',
                'imagen': 'coldplay_album5.jpg',
                'canciones': [
                    {'nombre': 'Mylo Xyloto', 'duracion': '0:42'},
                    {'nombre': 'Hurts Like Heaven', 'duracion': '4:02'},
                    {'nombre': 'Paradise', 'duracion': '4:38'}
                ]
            }
        }
    },
    'twentyonepilots': {
        'nombre': 'Twenty One Pilots',
        'imagen': 'twentyonepilots.jpg',
        'albumes': {
            'vessel': {
                'nombre': 'Vessel',
                'imagen': 'twentyonepilots_album1.jpg',
                'canciones': [
                    {'nombre': 'Ode to Sleep', 'duracion': '5:09'},
                    {'nombre': 'Holding on to You', 'duracion': '3:54'},
                    {'nombre': 'Migraine', 'duracion': '3:59'}
                ]
            },
            'blurryface': {
                'nombre': 'Blurryface',
                'imagen': 'twentyonepilots_album2.jpg',
                'canciones': [
                    {'nombre': 'Heavydirtysoul', 'duracion': '3:54'},
                    {'nombre': 'Stressed Out', 'duracion': '3:22'},
                    {'nombre': 'Ride', 'duracion': '3:34'}
                ]
            },
            'trench': {
                'nombre': 'Trench',
                'imagen': 'twentyonepilots_album3.jpg',
                'canciones': [
                    {'nombre': 'Jumpsuit', 'duracion': '3:58'},
                    {'nombre': 'Levitate', 'duracion': '2:25'},
                    {'nombre': 'Morph', 'duracion': '4:19'}
                ]
            },
            'scaled_and_icy': {
                'nombre': 'Scaled and Icy',
                'imagen': 'twentyonepilots_album4.jpg',
                'canciones': [
                    {'nombre': 'Good 4 U', 'duracion': '2:58'},
                    {'nombre': 'Choker', 'duracion': '3:26'},
                    {'nombre': 'Shy Away', 'duracion': '2:55'}
                ]
            },
            'self_titled': {
                'nombre': 'Twenty One Pilots',
                'imagen': 'twentyonepilots_album5.jpg',
                'canciones': [
                    {'nombre': 'Implicit Demand for Proof', 'duracion': '5:05'},
                    {'nombre': 'Fall Away', 'duracion': '3:16'},
                    {'nombre': 'The Pantaloon', 'duracion': '3:58'}
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
                    {'nombre': 'Papercut', 'duracion': '3:05'},
                    {'nombre': 'One Step Closer', 'duracion': '2:36'},
                    {'nombre': 'With You', 'duracion': '3:23'}
                ]
            },
            'meteora': {
                'nombre': 'Meteora',
                'imagen': 'linkinpark_album2.jpg',
                'canciones': [
                    {'nombre': 'Foreword', 'duracion': '0:13'},
                    {'nombre': 'Don\'t Stay', 'duracion': '3:07'},
                    {'nombre': 'Somewhere I Belong', 'duracion': '3:33'}
                ]
            },
            'minutes_to_midnight': {
                'nombre': 'Minutes to Midnight',
                'imagen': 'linkinpark_album3.jpg',
                'canciones': [
                    {'nombre': 'Wake', 'duracion': '1:40'},
                    {'nombre': 'Given Up', 'duracion': '3:09'},
                    {'nombre': 'Leave Out All the Rest', 'duracion': '3:29'}
                ]
            },
            'a_thousand_suns': {
                'nombre': 'A Thousand Suns',
                'imagen': 'linkinpark_album4.jpg',
                'canciones': [
                    {'nombre': 'The Requiem', 'duracion': '2:01'},
                    {'nombre': 'The Radiance', 'duracion': '0:57'},
                    {'nombre': 'Burning in the Skies', 'duracion': '4:13'}
                ]
            },
            'living_things': {
                'nombre': 'Living Things',
                'imagen': 'linkinpark_album5.jpg',
                'canciones': [
                    {'nombre': 'Lost in the Echo', 'duracion': '3:25'},
                    {'nombre': 'In My Remains', 'duracion': '3:20'},
                    {'nombre': 'Burn It Down', 'duracion': '3:50'}
                ]
            }
        }
    }
}
