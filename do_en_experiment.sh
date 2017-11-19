#!/usr/bin/env bash

mkdir -p ../data/$1

# Baseline:
# udapy read.Conllu filename=/net/data/UD_English/udapipe_tp.bz2 zellig_harris.Baseline $2 > ../data/$1/dep.contexts 2> ../data/$1/log

# Scenar EnVerbs
#udapy read.Conllu filename=/net/data/UD_English/udapipe_tp.bz2 zellig_harris.EnVerbs > ../data/$1/dep.contexts 2> ../data/$1/log

# Trenovanie word2vec
../word2vecf/count_and_filter -train ../data/$1/dep.contexts -cvocab ../data/$1/cv -wvocab ../data/$1/wv -min-count 100 2>> ../data/$1/log
../word2vecf/word2vecf -train ../data/$1/dep.contexts -wvocab ../data/$1/wv -cvocab ../data/$1/cv -output ../data/$1/dim300vecs -size 300 -negative 15 -threads 10 -sample 1e-4 -iters 15 2>> ../data/$1/log

# Evaluacia
python evaluation.py --vectors=../data/$1/dim300vecs --dataset=../data/eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>> ../data/$1/log
