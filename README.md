## fractfact
pair of brute force scripts written out of interest in finding minimal length rational factorizations of integers, *k*, st.: <br/>
<div align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=k,&space;i&space;\in&space;\mathbb{Z}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k,&space;i&space;\in&space;\mathbb{Z}" title="k, i \in \mathbb{Z}" /></a> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=s_i&space;\in&space;\{-1,1\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_i&space;\in&space;\{-1,1\}" title="s_i \in \{-1,1\}" /></a> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=\prod_{i=&space;k&space;&plus;&space;1}^{j}&space;(\frac{i}{i&plus;1})^{s_i}&space;=&space;k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\prod_{i=&space;k&space;&plus;&space;1}^{j}&space;(\frac{i}{i&plus;1})^{s_i}&space;=&space;k" title="\prod_{i= k + 1}^{j} (\frac{i}{i+1})^{s_i} = k" /></a>
</div>

ie. a factorization of a given integer *k* presented as a product of flip signed rationals with both numerator and denominator increasing by 1 starting at *k+1*. <br/>
ex. 
<div align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=2&space;=&space;(\frac{4}{3})(\frac{5}{4})(\frac{6}{5})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?2&space;=&space;(\frac{4}{3})(\frac{5}{4})(\frac{6}{5})" title="2 = (\frac{4}{3})(\frac{5}{4})(\frac{6}{5})" /></a>
  </div>
  
### results
due to the fact that a reduced solution of any length yields the prime factorization of a given *k* the problem is NP complete and therefore (especially a brute force solution such as this script) finding such *k*'s takes quite a bit of time... 

### ex. output (fraction-factor-iter.py):
-----GOAL:1-----

range=2 to 24
8388608
ahh!
['1.0', '0 0 0 0 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0', '(3/2) (4/3) (5/4) (6/5) (6/7) (7/8) (8/9) (9/10) (10/11) (11/12) (12/13) (13/14) (14/15) (15/16) (16/17) (17/18)  = 1.0, epsilon=0.000009032', 'multiple count=16']
ahh!
['1.0', '0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', '(3/2) (4/3) (4/5) (5/6) (6/7) (7/8)  = 1.0, epsilon=0.000000000', 'multiple count=6']
8388608
-----GOAL:2-----

range=3 to 24
8388608
ahh!
['2.0', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', '(4/3) (5/4) (6/5)  = 2.0, epsilon=0.333333333', 'multiple count=3']
8388608
-----GOAL:3-----

range=4 to 24
8388608
ahh!
['3.0', '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0', '(5/4) (6/5) (7/6) (8/7) (9/8) (10/9) (11/10) (12/11)  = 3.0, epsilon=0.250000000', 'multiple count=8']
8388608
-----GOAL:4-----

