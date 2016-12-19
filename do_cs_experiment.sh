#!/usr/bin/env bash

#mkdir -p ../data/$1
#udapy read.ReducedConllu filename=../data/UD_English/data.bz2 bundles_per_document=100000 cc4cswr.Vulic $2 > ../data/$1/dep.contexts 2> ../data/$1/log
../word2vecf/count_and_filter -train ../data/$1/dep.contexts.$2 -cvocab ../data/$1/cv.$2 -wvocab ../data/$1/wv.$2 -min-count 1 2>> ../data/$1/log.$2
../word2vecf/word2vecf -train ../data/$1/dep.contexts.$2 -wvocab ../data/$1/wv.$2 -cvocab ../data/$1/cv.$2 -output ../data/$1/dim300vecs.$2 -size 300 -negative 15 -threads 10 -sample 1e-4 -iters 15 2>> ../data/$1/log.$2

