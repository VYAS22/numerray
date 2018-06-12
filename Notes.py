NoteName = ('C','C#/Db','D','D#/Eb','E','F','F#/Gb','G','G#/Ab','A','A#/Bb','B')
Scale = ('0','1','2','3','4','5','6','7','8')
NotePitch = ( 16.3500,
17.3200,
18.3500, 
19.4500,
20.6000,
21.8300,
23.1200,
24.5000,
25.9600,
27.5000,
29.1353,
30.8677,
32.7032,
34.6479,
36.7081,
38.8909,
41.2035,
43.6536,
46.2493,
48.9995,
51.9130,
55.0000,
58.2705,
61.7354,
65.4064,
69.2957,
73.4162,
77.7817,
82.4069,
87.3071,
92.4986,
97.9989,
103.826,
110.000,
116.541,
123.471,
130.813,
138.591,
146.832,
155.563,
164.814,
174.614,
184.997,
195.998,
207.652,
220.000,
233.082,
246.942,
261.626,
277.183,
293.665,
311.127,
329.628,
349.228,
369.994,
391.995,
415.305,
440.000,
466.164,
493.883,
523.251,
554.365,
587.330,
622.254,
659.255,
698.456,
739.989,
783.991,
830.609,
880.000,
932.328,
987.767,
1046.50,
1108.73,
1174.66,
1244.51,
1318.51,
1396.91,
1479.98,
1567.98,
1661.22,
1760.00,
1864.66,
1975.53,
2093.00,
2217.46,
2349.32,
2489.02,
2637.02,
2793.83,
2959.96,
3135.96,
3322.44,
3520.00,
3729.31,
3951.07,
4186.01,
4434.92,
4698.63,
4978.03,
5274.04,
5587.65,
5919.91,
6271.93,
6644.88,
7040.00,
7458.62,
7902.13 )
k = 0
Note = ["" for x in range(108)]
for i in range(0,9):
    for j in range(0,12):
        k = i*12 + j
        Note[k] = (NoteName[j] + Scale[i])
print ('NOTE___PITCH')
for k in range(0,108):
    print ( str(NotePitch[k]) + '  ' + Note[k])
    print ()