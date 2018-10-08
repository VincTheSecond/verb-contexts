#!/bin/bash

CONFIG=${1:-"exp_en_nouns_cinkova_der_merged"}

CELEX=/net/work/people/kriz/udapi/data/D_celex/dictionary.txt
DATA=/net/cluster/TMP/kriz/UDAPI/data
mkdir ../celex
mkdir ../data
mkdir ../simlex

lang=`echo $CONFIG | cut -d"_" -f2`
pos=`echo $CONFIG | cut -d"_" -f3`
name=`echo $CONFIG | cut -d"_" -f4`
type1=`echo $CONFIG | cut -d"_" -f5 `
merged=`echo $CONFIG | cut -d"_" -f6`

merge_flag=""
if [ $merged == ]; then
    merge_flag="--merge_inverse_relations True"
fi

exp=${CONFIG}
echo Preparing ${exp}
mkdir ../data/$exp

echo Removing Contexts
python remove_contexts.py --remove "" --input $DATA/exp_${lang}_${pos}_${name}/dep.contexts.$type1 --output ../data/$exp/dep.contexts $merge_flag

echo Training Embeddings
./do_${lang}_experiment.sh $exp

echo Evaluating Celex
python evaluation_celex.py --celex $CELEX --vectors ../data/$exp/dim300vecs --report ../celex/$exp.csv

echo Evaluating Simlex
./evaluation.py --vectors=../data/$exp/dim300vecs --dataset=$DATA/eval_${lang}_${pos}/simlex --reflexive_verbs asis --folds=2 2>&1 | tee ../simlex/$exp.out
