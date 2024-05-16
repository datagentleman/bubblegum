<div align="center">
             _     _      _           _       
  __ _  ___ | | __| | ___| |__   __ _(_)_ __  
 / _` |/ _ \| |/ _` |/ __| '_ \ / _` | | '_ \ 
| (_| | (_) | | (_| | (__| | | | (_| | | | | |
 \__, |\___/|_|\__,_|\___|_| |_|\__,_|_|_| |_|
 |___/        
<pre>


⭐⭐⭐ Distributed KeyVal ⭐⭐⭐
</pre>

</div>


## What will goldchain ?

Distributed KeyValue database tailored for blockchain data. The goal is to store the entire
Ethereum blockchain (around 9TB) on single server - and make basic operations fast.


## Starting small

Initially, I will work with a 2TB dataset, and upon successful implementation, 
I will invest in nvme storage to accommodate the full 9TB blockchain, along with additional storage for backups.

The entire implementation will be done in python and cython (with some simple cpp code).
In the end I want to optimize python code to get maximum performance out of it.
