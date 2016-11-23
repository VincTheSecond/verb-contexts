mkdir -p ../data/$1
udapy read.ReducedConllu filename=../data/UD_English/data.bz2 bundles_per_document=100000 cc4cswr.Vulic $2 > ../data/$1/dep.contexts 2> ../data/$1/log
../word2vecf/count_and_filter -train ../data/$1/dep.contexts -cvocab ../data/$1/cv -wvocab ../data/$1/wv -min-count 100 2>> ../data/$1/log
../word2vecf/word2vecf -train ../data/$1/dep.contexts -wvocab ../data/$1/wv -cvocab ../data/$1/cv -output ../data/$1/dim300vecs -size 300 -negative 15 -threads 10 -sample 1e-4 -iters 15 2>> ../data/$1/log
python evaluation.py --vectors=../data/$1/dim200vecs --dataset=../data/D_simlex/SimLex-222.txt 2>> ../data/$1/log
