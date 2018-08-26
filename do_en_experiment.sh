#!/usr/bin/env bash

mkdir -p ../data/$1
cd ../data/$1

# Baseline:
# udapy read.Conllu filename=/net/data/UD_English/udapipe_tp.bz2 zellig_harris.Baseline $2 > dep.contexts 2> log

# Scenar EnVerbs
#udapy read.Conllu filename=/net/data/UD_English/udapipe_tp.bz2 zellig_harris.EnVerbs > dep.contexts 2> log

# Trenovanie word2vec
../../word2vecf/count_and_filter -train dep.contexts -cvocab cv -wvocab wv -min-count 100 2>> log
../../word2vecf/word2vecf -train dep.contexts -wvocab wv -cvocab cv -output dim300vecs -size 300 -negative 15 -threads 10 -sample 1e-4 -iters 15 2>> log

# Evaluacia
python ../../verb-contexts/evaluation.py --vectors=dim300vecs --dataset=../../data/eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>> log
