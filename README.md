# Sequence-Alignment-Problem

## Results

| M+N    | Time in MS (Basic) | Time in MS (Efficient) | Memory in KB (Basic) | Memory in KB (Efficient) |
| -------- | ------- | ------- | ------- | ------- |
| 16 | 0.0567436 | 0.1542568 | 12016 | 12176 |
| 64 | 0.6198883 | 1.2979507 | 12080 | 12192 |
| 128 | 2.2640228 | 4.4877529 | 12192 | 12192 |
| 256 | 8.6152553 | 16.4060592 | 12768 | 12208 |
| 384 | 19.7138786 | 36.0031127 | 13616 | 12224 |
| 512 | 35.2869033 | 64.7828578 | 14096 | 12240 |
| 768 | 80.6217193 | 142.6899433 | 14320 | 12256 |
| 1024 | 149.4488716 | 239.3960952 | 15840 | 12304 |
| 1280 | 232.5308322 | 374.4950294 | 16592 | 12320 |
| 1536 | 334.7339630 | 526.1707305 | 19008 | 12352 |
| 2048 | 613.6848926 | 968.3861732 | 22992 | 12400 |
| 2560 | 952.9838562 | 1508.7149143 | 29440 | 12432 |
| 3072 | 1396.4669704 | 2142.9791450 | 41408 | 12512 |
| 3584 | 1870.6498146 | 2952.8899192 | 45696 | 12576 |
| 3968 | 2304.8110008 | 3666.4571762 | 54384 | 12608 |

## Memory vs Problem Size (M+N)
<img width="628" alt="image" src="https://github.com/ayushiiamin/Sequence-Alignment-Problem/assets/77382840/c09c6f68-6629-4723-b292-60cb587a6942">
<br />
- Basic: Polynomial O(m*n)
- Efficient: Linear O(min(m,n))

## Time vs Problem Size (M+N)
<img width="628" alt="image" src="https://github.com/ayushiiamin/Sequence-Alignment-Problem/assets/77382840/c452686b-b1a7-4b4b-93c0-fd5341bb722c">\
- Basic: Polynomial O(m*n)
- Efficient: Polynomial O(m*n)

### Contributers:
- Ayushi Amin <i>(ayushima@usc.edu)</i>
- Ankita Samanta <i>(ankitasa@usc.edu)</i>
- Aditya Srivastava <i>(adityasr@usc.edu)</i>
