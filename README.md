# kddcup98
Experiment with [KDD Cup 1998 data](http://kdd.ics.uci.edu/databases/kddcup98/kddcup98.html)

Convert it to a contextual bandit problem (see http://www.cs.columbia.edu/~jebara/6998/BanditsPaper.pdf)


## Steps
1. [download-data.pv](./data-preparation/download-data.py)
2. [run-csv2vw.sh](./data-preparation/run-csv2vw.sh)
3. Run vw as cb
4. Off-policy evaluation
