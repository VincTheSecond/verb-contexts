# verb-contexts
Select best verb contextes to maximase word2vec verb similarities.

## VERBS/DER

 - python split_contexts.py --contexts ../data/exp_en_verbs_cinkova/dep.contexts.der --output_dir ../data/exp_en_verbs_cinkova/
 - for i in `cat verbs.der | sed -E 's/^\s*[0-9]+ //'`; do mkdir exp_en_verbs_cinkova_der_$i; done
 - for i in `cat verbs.der | sed -E 's/^\s*[0-9]+ //'`; do mv exp_en_verbs_cinkova/$i.contexts exp_en_verbs_cinkova_der_$i/; done
 - for i in `cat verbs.der | sed -E 's/^\s*[0-9]+ //'`; do mv exp_en_verbs_cinkova_der_$i/$i.contexts exp_en_verbs_cinkova_der_$i/dep.contexts; done
 - for i in `cat verbs.der | sed -E 's/^\s*[0-9]+ //'`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_$i" > ../verb-contexts/lrc_verbs_der_$i.sh; done
 - for i in lrc_verbs_der*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat verbs.der | sed -E 's/^\s*[0-9]+ //'`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

## VERBS/HAL

 - python split_contexts.py --contexts ../data/exp_en_verbs_cinkova/dep.contexts.hal --output_dir ../data/exp_en_verbs_cinkova/
 - for i in `cat verbs.hal | sed -E 's/^\s*[0-9]+ //'`; do mkdir exp_en_verbs_cinkova_hal_$i; done
 - for i in `cat verbs.hal | sed -E 's/^\s*[0-9]+ //'`; do mv exp_en_verbs_cinkova/$i.contexts exp_en_verbs_cinkova_hal_$i/; done
 - for i in `cat verbs.hal | sed -E 's/^\s*[0-9]+ //'`; do mv exp_en_verbs_cinkova_hal_$i/$i.contexts exp_en_verbs_cinkova_hal_$i/dep.contexts; done
 - for i in `cat verbs.hal | sed -E 's/^\s*[0-9]+ //'`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_$i" > ../verb-contexts/lrc_verbs_hal_$i.sh; done
 - for i in lrc_verbs_hal*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat verbs.hal | sed -E 's/^\s*[0-9]+ //'`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

## NOUNS/DER

 - python split_contexts.py --contexts ../data/exp_en_nouns_cinkova/dep.contexts.der --output_dir ../data/exp_en_nouns_cinkova/
 - for i in `cat nouns.der | sed -E 's/^\s*[0-9]+ //'`; do mkdir exp_en_nouns_cinkova_der_$i; done
 - for i in `cat nouns.der | sed -E 's/^\s*[0-9]+ //'`; do mv exp_en_nouns_cinkova/$i.contexts exp_en_nouns_cinkova_der_$i/; done
 - for i in `cat nouns.der | sed -E 's/^\s*[0-9]+ //'`; do mv exp_en_nouns_cinkova_der_$i/$i.contexts exp_en_nouns_cinkova_der_$i/dep.contexts; done
 - for i in `cat nouns.der | sed -E 's/^\s*[0-9]+ //'`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_$i" > ../verb-contexts/lrc_nouns_der_$i.sh; done
 - for i in lrc_nouns_der*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat nouns.der | sed -E 's/^\s*[0-9]+ //'`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

## NOUNS/HAL

 - python split_contexts.py --contexts ../data/exp_en_nouns_cinkova/dep.contexts.hal --output_dir ../data/exp_en_nouns_cinkova/
 - for i in `cat nouns.hal | sed -E 's/^\s*[0-9]+ //'`; do mkdir exp_en_nouns_cinkova_hal_$i; done
 - for i in `cat nouns.hal | sed -E 's/^\s*[0-9]+ //'`; do mv exp_en_nouns_cinkova/$i.contexts exp_en_nouns_cinkova_hal_$i/; done
 - for i in `cat nouns.hal | sed -E 's/^\s*[0-9]+ //'`; do mv exp_en_nouns_cinkova_hal_$i/$i.contexts exp_en_nouns_cinkova_hal_$i/dep.contexts; done
 - for i in `cat nouns.hal | sed -E 's/^\s*[0-9]+ //'`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_$i" > ../verb-contexts/lrc_nouns_hal_$i.sh; done
 - for i in lrc_nouns_hal*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat nouns.hal | sed -E 's/^\s*[0-9]+ //'`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done
