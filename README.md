## fractfact
pair of brute force scripts written out of interest in finding minimal length rational factorizations of integers, *k*, st.: <br/>
<div align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=k,&space;i&space;\in&space;\mathbb{Z}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?k,&space;i&space;\in&space;\mathbb{Z}" title="k, i \in \mathbb{Z}" /></a> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=s_i&space;\in&space;\{-1,1\}" target="_blank"><img src="https://latex.codecogs.com/gif.latex?s_i&space;\in&space;\{-1,1\}" title="s_i \in \{-1,1\}" /></a> <br/>
<a href="https://www.codecogs.com/eqnedit.php?latex=\prod_{i=&space;k&space;&plus;&space;1}^{j}&space;(\frac{i}{i&plus;1})^{s_i}&space;=&space;k" target="_blank"><img src="https://latex.codecogs.com/gif.latex?\prod_{i=&space;k&space;&plus;&space;1}^{j}&space;(\frac{i}{i&plus;1})^{s_i}&space;=&space;k" title="\prod_{i= k + 1}^{j} (\frac{i}{i+1})^{s_i} = k" /></a>
</div>

ie. a factorization of a given integer *k* presented as a product of "flipped" signed rationals with both numerator and denominator increasing by 1 starting at *k+1*. <br/>
ex. 
<div align="center">
<a href="https://www.codecogs.com/eqnedit.php?latex=2&space;=&space;(\frac{4}{3})(\frac{5}{4})(\frac{6}{5})" target="_blank"><img src="https://latex.codecogs.com/gif.latex?2&space;=&space;(\frac{4}{3})(\frac{5}{4})(\frac{6}{5})" title="2 = (\frac{4}{3})(\frac{5}{4})(\frac{6}{5})" /></a>
  </div>
  
### results
due to the fact that a reduced solution of any length yields the prime factorization of a given *k* the problem is NP complete and therefore (especially a brute force solution such as this script) finding such *k*'s takes quite a bit of time... <br/> <br/>

sample program output in *resultsfract.txt*

