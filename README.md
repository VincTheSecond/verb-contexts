# verb-contexts
Select best verb contexts to maximize word2vec verb similarities.

## VERBS/DER

 - cat exp_en_verbs_cinkova/dep.contexts.der | cut -f 2 -d ' ' | cut -f 1 -d '_' | sort | uniq -c | sort -rn > verbs.der
 - python split_contexts.py --contexts ../data/exp_en_verbs_cinkova/dep.contexts.der --output_dir ../data/exp_en_verbs_cinkova/
 - for i in `cat context_bags.verbs.der`; do mkdir exp_en_verbs_cinkova_der_$i; done
 - for i in `cat context_bags.verbs.der`; do mv exp_en_verbs_cinkova/$i.contexts exp_en_verbs_cinkova_der_$i/; done
 - for i in `cat context_bags.verbs.der`; do mv exp_en_verbs_cinkova_der_$i/$i.contexts exp_en_verbs_cinkova_der_$i/dep.contexts; done
 - for i in `cat context_bags.verbs.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_$i" > ../verb-contexts/lrc_verbs_der_$i.sh; done
 - for i in lrc_verbs_der*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.der`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 1 (ALL - X):
 - for i in `cat context_bags.verbs.der`; do mkdir exp_en_verbs_cinkova_der_all_$i; done
 - for i in `cat context_bags.verbs.der`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_verbs_cinkova/dep.contexts.der --output ../data/exp_en_verbs_cinkova_der_all_$i/dep.contexts" > ../verb-contexts/lrc_verbs_der_all_preprocessing_$i.sh; done
 - for i in lrc_verbs_der_all_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_der_all_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_all_$i" > ../verb-contexts/lrc_verbs_der_all_experiment_$i.sh; done
 - for i in lrc_verbs_der_all_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.der`; do echo -en "ALL - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_all_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 2 (ALL - enVerbs001a - X):
 - for i in `cat context_bags.verbs.der`; do mkdir exp_en_verbs_cinkova_der_all_enVerbs001a_$i; done
 - for i in `cat context_bags.verbs.der`; do echo "python remove_contexts.py --remove $i,enVerbs001a --input ../data/exp_en_verbs_cinkova/dep.contexts.der --output ../data/exp_en_verbs_cinkova_der_all_enVerbs001a_$i/dep.contexts" > ../verb-contexts/lrc_verbs_der_all_enVerbs001a_preprocessing_$i.sh; done
 - for i in lrc_verbs_der_all_enVerbs001a_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_der_all_enVerbs001a_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_all_enVerbs001a_$i" > ../verb-contexts/lrc_verbs_der_all_enVerbs001a_experiment_$i.sh; done
 - for i in lrc_verbs_der_all_enVerbs001a_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.der`; do echo -en "ALL - enVerbs001a - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_all_enVerbs001a_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done


## VERBS/DER (MERGED) ===========================================================================================================

 - Vsetky context bags (ALL):
 - for i in `cat context_bags.verbs.merged.der`; do cat exp_en_verbs_cinkova_der_merged_all_$i/dep.contexts >> exp_en_verbs_cinkova_der_merged_all/dep.contexts; done
 - echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_merged_all" > ../verb-contexts/lrc_verbs_der_merged_all.sh
 - qsub -cwd -j y -S /bin/bash lrc_verbs_der_merged_all.sh
 - python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_merged_all/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'

 - Individualne context bags:
 - python split_contexts.py --contexts ../data/exp_en_verbs_cinkova/dep.contexts.der --output_dir ../data/exp_en_verbs_cinkova/ --merge_inverse_relations True
 - for i in `cat context_bags.verbs.merged.der`; do mkdir exp_en_verbs_cinkova_der_merged_$i; done
 - for i in `cat context_bags.verbs.merged.der`; do mv exp_en_verbs_cinkova/$i.contexts exp_en_verbs_cinkova_der_merged_$i/; done
 - for i in `cat context_bags.verbs.merged.der`; do mv exp_en_verbs_cinkova_der_merged_$i/$i.contexts exp_en_verbs_cinkova_der_merged_$i/dep.contexts; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_merged_$i" > ../verb-contexts/lrc_verbs_der_merged_$i.sh; done
 - for i in lrc_verbs_der_merged*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_merged_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - Cyklus 1 (ALL - X):
 - for i in `cat context_bags.verbs.merged.der`; do mkdir exp_en_verbs_cinkova_der_merged_all_$i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_verbs_cinkova/dep.contexts.der --output ../data/exp_en_verbs_cinkova_der_merged_all_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_verbs_der_merged_all_preprocessing_$i.sh; done
 - for i in lrc_verbs_der_merged_all_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_der_merged_all_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_merged_all_$i" > ../verb-contexts/lrc_verbs_der_merged_all_experiment_$i.sh; done
 - for i in lrc_verbs_der_merged_all_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo -en "ALL - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_merged_all_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 2 (ALL - enVerbs001a - X):
 - for i in `cat context_bags.verbs.merged.der`; do mkdir exp_en_verbs_cinkova_der_merged_all_enVerbs001a_$i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "python remove_contexts.py --remove $i,enVerbs001a --input ../data/exp_en_verbs_cinkova/dep.contexts.der --output ../data/exp_en_verbs_cinkova_der_merged_all_enVerbs001a_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_verbs_der_merged_all_enVerbs001a_preprocessing_$i.sh; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_merged_all_enVerbs001a_$i" > ../verb-contexts/lrc_verbs_der_merged_all_enVerbs001a_experiment_$i.sh; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo -en "ALL - enVerbs001a - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_merged_all_enVerbs001a_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 3 (ALL - enVerbs001a - enVerbs004b - X):
 - for i in `cat context_bags.verbs.merged.der`; do mkdir exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_$i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "python remove_contexts.py --remove $i,enVerbs001a,enVerbs004b --input ../data/exp_en_verbs_cinkova/dep.contexts.der --output ../data/exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_preprocessing_$i.sh; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_$i" > ../verb-contexts/lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_experiment_$i.sh; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo -en "ALL - enVerbs001a - enVerbs004b - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 4 (ALL - enVerbs001a - enVerbs004b - enVerbs003a - X):
 - for i in `cat context_bags.verbs.merged.der`; do mkdir exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_$i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "python remove_contexts.py --remove $i,enVerbs001a,enVerbs004b,enVerbs003a --input ../data/exp_en_verbs_cinkova/dep.contexts.der --output ../data/exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_preprocessing_$i.sh; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_$i" > ../verb-contexts/lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_experiment_$i.sh; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo -en "ALL - enVerbs001a - enVerbs004b - enVerbs003a - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 5 (ALL - enVerbs001a - enVerbs004b - enVerbs003a - obj - X):
 - for i in `cat context_bags.verbs.merged.der`; do mkdir exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_$i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "python remove_contexts.py --remove $i,enVerbs001a,enVerbs004b,enVerbs003a,obj --input ../data/exp_en_verbs_cinkova/dep.contexts.der --output ../data/exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_preprocessing_$i.sh; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_$i" > ../verb-contexts/lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_experiment_$i.sh; done
 - for i in lrc_verbs_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.der`; do echo -en "ALL - enVerbs001a - enVerbs004b - enVerbs003a - obj - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_der_merged_all_enVerbs001a_enVerbs004b_enVerbs003a_obj_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done



## VERBS/HAL ===========================================================================================================

 - cat exp_en_verbs_cinkova/dep.contexts.hal | cut -f 2 -d ' ' | cut -f 1 -d '_' | sort | uniq -c | sort -rn > verbs.hal
 - python split_contexts.py --contexts ../data/exp_en_verbs_cinkova/dep.contexts.hal --output_dir ../data/exp_en_verbs_cinkova/
 - for i in `cat context_bags.verbs.hal`; do mkdir exp_en_verbs_cinkova_hal_$i; done
 - for i in `cat context_bags.verbs.hal`; do mv exp_en_verbs_cinkova/$i.contexts exp_en_verbs_cinkova_hal_$i/; done
 - for i in `cat context_bags.verbs.hal`; do mv exp_en_verbs_cinkova_hal_$i/$i.contexts exp_en_verbs_cinkova_hal_$i/dep.contexts; done
 - for i in `cat context_bags.verbs.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_$i" > ../verb-contexts/lrc_verbs_hal_$i.sh; done
 - for i in lrc_verbs_hal*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.hal`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 1:
 - for i in `cat context_bags.verbs.hal`; do mkdir exp_en_verbs_cinkova_hal_all_$i; done
 - for i in `cat context_bags.verbs.hal`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_verbs_cinkova/dep.contexts.hal --output ../data/exp_en_verbs_cinkova_hal_all_$i/dep.contexts" > ../verb-contexts/lrc_verbs_hal_all_preprocessing_$i.sh; done
 - for i in lrc_verbs_hal_all_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_hal_all_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_all_$i" > ../verb-contexts/lrc_verbs_hal_all_experiment_$i.sh; done
 - for i in lrc_verbs_hal_all_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.hal`; do echo -en "ALL - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_all_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 2 (ALL - nmod - X):
 - for i in `cat context_bags.verbs.hal`; do mkdir exp_en_verbs_cinkova_hal_all_nmod_$i; done
 - for i in `cat context_bags.verbs.hal`; do echo "python remove_contexts.py --remove $i,nmod --input ../data/exp_en_verbs_cinkova/dep.contexts.hal --output ../data/exp_en_verbs_cinkova_hal_all_nmod_$i/dep.contexts" > ../verb-contexts/lrc_verbs_hal_all_nmod_preprocessing_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_hal_all_nmod_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_all_nmod_$i" > ../verb-contexts/lrc_verbs_hal_all_nmod_experiment_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.hal`; do echo -en "ALL - nmod - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_all_nmod_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 3 (ALL - nmod - dep - X):
 - for i in `cat context_bags.verbs.hal`; do mkdir exp_en_verbs_cinkova_hal_all_nmod_dep_$i; done
 - for i in `cat context_bags.verbs.hal`; do echo "python remove_contexts.py --remove $i,nmod,dep --input ../data/exp_en_verbs_cinkova/dep.contexts.hal --output ../data/exp_en_verbs_cinkova_hal_all_nmod_dep_$i/dep.contexts" > ../verb-contexts/lrc_verbs_hal_all_nmod_dep_preprocessing_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_dep_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_hal_all_nmod_dep_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_all_nmod_dep_$i" > ../verb-contexts/lrc_verbs_hal_all_nmod_dep_experiment_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_dep_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.hal`; do echo -en "ALL - nmod - dep - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_all_nmod_dep_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 4 (ALL - nmod - dep - derinetVerb - X):
 - for i in `cat context_bags.verbs.hal`; do mkdir exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_$i; done
 - for i in `cat context_bags.verbs.hal`; do echo "python remove_contexts.py --remove $i,nmod,dep,derinetVerb --input ../data/exp_en_verbs_cinkova/dep.contexts.hal --output ../data/exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_$i/dep.contexts" > ../verb-contexts/lrc_verbs_hal_all_nmod_dep_derinetVerb_preprocessing_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_$i" > ../verb-contexts/lrc_verbs_hal_all_nmod_dep_derinetVerb_experiment_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.hal`; do echo -en "ALL - nmod - dep - derinetVerb - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 5 (ALL - nmod - dep - derinetVerb - derinetNoun):
 - for i in `cat context_bags.verbs.hal`; do mkdir exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_derinetNoun_$i; done
 - for i in `cat context_bags.verbs.hal`; do echo "python remove_contexts.py --remove $i,nmod,dep,derinetVerb,derinetNoun --input ../data/exp_en_verbs_cinkova/dep.contexts.hal --output ../data/exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_derinetNoun_$i/dep.contexts" > ../verb-contexts/lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_preprocessing_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_derinetNoun_$i" > ../verb-contexts/lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_experiment_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.hal`; do echo -en "ALL - nmod - dep - derinetVerb - derinetNoun - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_derinetNoun_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 6 (ALL - nmod - dep - derinetVerb - derinetNoun - adv):
 - for i in `cat context_bags.verbs.hal`; do mkdir exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_$i; done
 - for i in `cat context_bags.verbs.hal`; do echo "python remove_contexts.py --remove $i,nmod,dep,derinetVerb,derinetNoun,adv --input ../data/exp_en_verbs_cinkova/dep.contexts.hal --output ../data/exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_$i/dep.contexts" > ../verb-contexts/lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_preprocessing_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_$i" > ../verb-contexts/lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_experiment_$i.sh; done
 - for i in lrc_verbs_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.hal`; do echo -en "ALL - nmod - dep - derinetVerb - derinetNoun - adv - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_all_nmod_dep_derinetVerb_derinetNoun_adv_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done


## VERBS/HAL (MERGED) ===========================================================================================================

Vsetky context bags (ALL):

 - for i in `cat context_bags.verbs.merged.hal`; do cat exp_en_verbs_cinkova_hal_merged_all_$i/dep.contexts >> exp_en_verbs_cinkova_hal_merged_all/dep.contexts; done
 - echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_merged_all" > ../verb-contexts/lrc_verbs_hal_merged_all.sh
 - qsub -cwd -j y -S /bin/bash lrc_verbs_hal_merged_all.sh
 - python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_merged_all/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'


Individualne context bags:

 - python split_contexts.py --contexts ../data/exp_en_verbs_cinkova/dep.contexts.hal --output_dir ../data/exp_en_verbs_cinkova/ --merge_inverse_relations True
 - for i in `cat context_bags.verbs.merged.hal`; do mkdir exp_en_verbs_cinkova_hal_merged_$i; done
 - for i in `cat context_bags.verbs.merged.hal`; do mv exp_en_verbs_cinkova/$i.contexts exp_en_verbs_cinkova_hal_merged_$i/; done
 - for i in `cat context_bags.verbs.merged.hal`; do mv exp_en_verbs_cinkova_hal_merged_$i/$i.contexts exp_en_verbs_cinkova_hal_merged_$i/dep.contexts; done
 - for i in `cat context_bags.verbs.merged.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_merged_$i" > ../verb-contexts/lrc_verbs_hal_merged_$i.sh; done
 - for i in lrc_verbs_hal_merged*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.hal`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_merged_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 1:
 - for i in `cat context_bags.verbs.merged.hal`; do mkdir exp_en_verbs_cinkova_hal_merged_all_$i; done
 - for i in `cat context_bags.verbs.merged.hal`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_verbs_cinkova/dep.contexts.hal --output ../data/exp_en_verbs_cinkova_hal_merged_all_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_verbs_hal_merged_all_preprocessing_$i.sh; done
 - for i in lrc_verbs_hal_merged_all_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_hal_merged_all_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.merged.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_merged_all_$i" > ../verb-contexts/lrc_verbs_hal_merged_all_experiment_$i.sh; done
 - for i in lrc_verbs_hal_merged_all_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.hal`; do echo -en "ALL - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_all_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 2 (ALL - nmod - X):
 - for i in `cat context_bags.verbs.merged.hal`; do mkdir exp_en_verbs_cinkova_hal_merged_all_nmod_$i; done
 - for i in `cat context_bags.verbs.merged.hal`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_verbs_cinkova/dep.contexts.hal --output ../data/exp_en_verbs_cinkova_hal_merged_all_nmod_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_verbs_hal_merged_all_nmod_preprocessing_$i.sh; done
 - for i in lrc_verbs_hal_merged_all_nmod_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_verbs_hal_merged_all_nmod_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.verbs.merged.hal`; do echo "./do_en_experiment.sh exp_en_verbs_cinkova_hal_merged_all_nmod_$i" > ../verb-contexts/lrc_verbs_hal_merged_all_nmod_experiment_$i.sh; done
 - for i in lrc_verbs_hal_merged_all_nmod_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.verbs.merged.hal`; do echo -en "ALL - nmod - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_verbs_cinkova_hal_merged_all_nmod_$i/dim300vecs --dataset=eval_en_verbs/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done


## NOUNS/DER ===========================================================================================================

 - cat exp_en_nouns_cinkova/dep.contexts.der | cut -f 2 -d ' ' | cut -f 1 -d '_' | sort | uniq -c | sort -rn > nouns.der
 - python split_contexts.py --contexts ../data/exp_en_nouns_cinkova/dep.contexts.der --output_dir ../data/exp_en_nouns_cinkova/
 - for i in `cat context_bags.nouns.der`; do mkdir exp_en_nouns_cinkova_der_$i; done
 - for i in `cat context_bags.nouns.der`; do mv exp_en_nouns_cinkova/$i.contexts exp_en_nouns_cinkova_der_$i/; done
 - for i in `cat context_bags.nouns.der`; do mv exp_en_nouns_cinkova_der_$i/$i.contexts exp_en_nouns_cinkova_der_$i/dep.contexts; done
 - for i in `cat context_bags.nouns.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_$i" > ../verb-contexts/lrc_nouns_der_$i.sh; done
 - for i in lrc_nouns_der*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.der`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 1 (ALL - X):
 - for i in `cat context_bags.nouns.der`; do mkdir exp_en_nouns_cinkova_der_all_$i; done
 - for i in `cat context_bags.nouns.der`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_all_$i/dep.contexts" > ../verb-contexts/lrc_nouns_der_all_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_all_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_all_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_all_$i" > ../verb-contexts/lrc_nouns_der_all_experiment_$i.sh; done
 - for i in lrc_nouns_der_all_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.der`; do echo -en "ALL - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_all_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 2 (ALL - nmod - X):
 - for i in `cat context_bags.nouns.der`; do mkdir exp_en_nouns_cinkova_der_all_nmod_$i; done
 - for i in `cat context_bags.nouns.der`; do echo "python remove_contexts.py --remove $i,nmod --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_all_nmod_$i/dep.contexts" > ../verb-contexts/lrc_nouns_der_all_nmod_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_all_nmod_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_all_nmod_$i" > ../verb-contexts/lrc_nouns_der_all_nmod_experiment_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.der`; do echo -en "ALL - nmod - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_all_nmod_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

- cyklus 3 (ALL - nmod - enNouns004a -X):
 - for i in `cat context_bags.nouns.der`; do mkdir exp_en_nouns_cinkova_der_all_nmod_enNouns004a_$i; done
 - for i in `cat context_bags.nouns.der`; do echo "python remove_contexts.py --remove $i,nmod,enNouns004a --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_all_nmod_enNouns004a_$i/dep.contexts" > ../verb-contexts/lrc_nouns_der_all_nmod_enNouns004a_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_all_nmod_enNouns004a_$i" > ../verb-contexts/lrc_nouns_der_all_nmod_enNouns004a_experiment_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.der`; do echo -en "ALL - nmod - enNouns004a - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_all_nmod_enNouns004a_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

- cyklus 4 (ALL - nmod - enNouns004a - enNouns002a - X):
 - for i in `cat context_bags.nouns.der`; do mkdir exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_$i; done
 - for i in `cat context_bags.nouns.der`; do echo "python remove_contexts.py --remove $i,nmod,enNouns004a,enNouns002a --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_$i/dep.contexts" > ../verb-contexts/lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - pocita sa
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_$i" > ../verb-contexts/lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_experiment_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.der`; do echo -en "ALL - nmod - enNouns004a - enNouns002a - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

- cyklus 5 (ALL - nmod - enNouns004a - enNouns002a - prep - X):
 - for i in `cat context_bags.nouns.der`; do mkdir exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_prep_$i; done
 - for i in `cat context_bags.nouns.der`; do echo "python remove_contexts.py --remove $i,nmod,enNouns004a,enNouns002a,prep --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_prep_$i/dep.contexts" > ../verb-contexts/lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_prep_$i" > ../verb-contexts/lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_experiment_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.der`; do echo -en "ALL - nmod - enNouns004a - enNouns002a - prep - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_prep_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

- cyklus 6 (ALL - nmod - enNouns004a - enNouns002a - prep - appos - X):
 - for i in `cat context_bags.nouns.der`; do mkdir exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_prep_appos_$i; done
 - for i in `cat context_bags.nouns.der`; do echo "python remove_contexts.py --remove $i,nmod,enNouns004a,enNouns002a,prep,appos --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_prep_appos_$i/dep.contexts" > ../verb-contexts/lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_appos_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_appos_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_appos_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_prep_appos_$i" > ../verb-contexts/lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_appos_experiment_$i.sh; done
 - for i in lrc_nouns_der_all_nmod_enNouns004a_enNouns002a_prep_appos_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.der`; do echo -en "ALL - nmod - enNouns004a - enNouns002a - prep - appos - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_all_nmod_enNouns004a_enNouns002a_prep_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

## NOUNS/DER (MERGED)

 - Vsetky context bags (ALL):
 - mkdir exp_en_nouns_cinkova_der_merged_all
 - for i in `cat context_bags.nouns.merged.der`; do cat exp_en_nouns_cinkova_der_merged_all_$i/dep.contexts >> exp_en_nouns_cinkova_der_merged_all/dep.contexts; done
 - echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all" > ../verb-contexts/lrc_nouns_der_merged_all.sh
 - qsub -cwd -j y -S /bin/bash lrc_nouns_der_merged_all.sh
 - python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'

 - python split_contexts.py --contexts ../data/exp_en_nouns_cinkova/dep.contexts.der --output_dir ../data/exp_en_nouns_cinkova/ --merge_inverse_relations True
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do mv exp_en_nouns_cinkova/$i.contexts exp_en_nouns_cinkova_der_merged_$i/; done
 - for i in `cat context_bags.nouns.merged.der`; do mv exp_en_nouns_cinkova_der_merged_$i/$i.contexts exp_en_nouns_cinkova_der_merged_$i/dep.contexts; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_$i" > ../verb-contexts/lrc_nouns_der_merged_$i.sh; done
 - for i in lrc_nouns_der_merged*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 1 (ALL - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_merged_all_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_$i" > ../verb-contexts/lrc_nouns_der_merged_all_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 2 (ALL - enNouns004a - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,$i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 3 (ALL - enNouns004a - nmod - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,$i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 4 (ALL - enNouns004a - nmod - enNouns001b - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,$i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 5 (ALL - enNouns004a - nmod - enNouns001b - prep - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,$i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 6 (ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,enNouns002a,$i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a -$i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 7 (ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,enNouns002a,compound,$i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 8 (ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,enNouns002a,compound,conj,$i --input ../data/exp_en_nouns_cinkova/dep.contexts.der --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 9 (ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,enNouns002a,compound,conj,derinetAdj,$i --input ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj/dep.contexts --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 10 (ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - enNouns003b - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,enNouns002a,compound,conj,derinetAdj,enNouns003b,$i --input ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b/dep.contexts --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - enNouns003b - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 11 (ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - enNouns003b - subj - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,enNouns002a,compound,conj,derinetAdj,enNouns003b,subj,$i --input ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj/dep.contexts --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - enNouns003b - subj - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 12 (ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - enNouns003b - subj - derinetNoun - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,enNouns002a,compound,conj,derinetAdj,enNouns003b,subj,derinetNoun,$i --input ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun/dep.contexts --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - enNouns003b - subj - derinetNoun - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 13 (ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - enNouns003b - subj - derinetNoun - enNouns005 - X):
 - for i in `cat context_bags.nouns.merged.der`; do mkdir exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_$i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "python remove_contexts.py --remove enNouns004a,nmod,enNouns001b,prep,enNouns002a,compound,conj,derinetAdj,enNouns003b,subj,derinetNoun,enNouns005,$i --input ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005/dep.contexts --output ../data/exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_preprocessing_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_$i" > ../verb-contexts/lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_experiment_$i.sh; done
 - for i in lrc_nouns_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.der`; do echo -en "ALL - enNouns004a - nmod - enNouns001b - prep - enNouns002a - compound - conj - derinetAdj - enNouns003b - subj - derinetNoun - enNouns005 - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_der_merged_all_enNouns004a_nmod_enNouns001b_prep_enNouns002a_compound_conj_derinetAdj_enNouns003b_subj_derinetNoun_enNouns005_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done


## NOUNS/HAL ===========================================================================================================

 - cat exp_en_nouns_cinkova/dep.contexts.hal | cut -f 2 -d ' ' | cut -f 1 -d '_' | sort | uniq -c | sort -rn > nouns.hal
 - python split_contexts.py --contexts ../data/exp_en_nouns_cinkova/dep.contexts.hal --output_dir ../data/exp_en_nouns_cinkova/
 - for i in `cat context_bags.nouns.hal`; do mkdir exp_en_nouns_cinkova_hal_$i; done
 - for i in `cat context_bags.nouns.hal`; do mv exp_en_nouns_cinkova/$i.contexts exp_en_nouns_cinkova_hal_$i/; done
 - for i in `cat context_bags.nouns.hal`; do mv exp_en_nouns_cinkova_hal_$i/$i.contexts exp_en_nouns_cinkova_hal_$i/dep.contexts; done
 - for i in `cat context_bags.nouns.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_$i" > ../verb-contexts/lrc_nouns_hal_$i.sh; done
 - for i in lrc_nouns_hal*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.hal`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 1:
 - for i in `cat context_bags.nouns.hal`; do mkdir exp_en_nouns_cinkova_hal_all_$i; done
 - for i in `cat context_bags.nouns.hal`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_all_$i/dep.contexts" > ../verb-contexts/lrc_nouns_hal_all_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_all_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_all_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_all_$i" > ../verb-contexts/lrc_nouns_hal_all_experiment_$i.sh; done
 - for i in lrc_nouns_hal_all_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.hal`; do echo -en "ALL - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_all_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 2 (ALL - nmod - X):
 - for i in `cat context_bags.nouns.hal`; do mkdir exp_en_nouns_cinkova_hal_all_nmod_$i; done
 - for i in `cat context_bags.nouns.hal`; do echo "python remove_contexts.py --remove $i,nmod --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_all_nmod_$i/dep.contexts" > ../verb-contexts/lrc_nouns_hal_all_nmod_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_all_nmod_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_all_nmod_$i" > ../verb-contexts/lrc_nouns_hal_all_nmod_experiment_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.hal`; do echo -en "ALL - nmod - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_all_nmod_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 3 (ALL - nmod - compound - X):
 - for i in `cat context_bags.nouns.hal`; do mkdir exp_en_nouns_cinkova_hal_all_nmod_compound_$i; done
 - for i in `cat context_bags.nouns.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_all_nmod_compound_$i/dep.contexts" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_all_nmod_compound_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_all_nmod_compound_$i" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_experiment_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.hal`; do echo -en "ALL - nmod - compound - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_all_nmod_compound_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 4 (ALL - nmod - compound - prep - X):
 - for i in `cat context_bags.nouns.hal`; do mkdir exp_en_nouns_cinkova_hal_all_nmod_compound_prep_$i; done
 - for i in `cat context_bags.nouns.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound,prep --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_all_nmod_compound_prep_$i/dep.contexts" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_prep_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_all_nmod_compound_prep_$i" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_prep_experiment_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.hal`; do echo -en "ALL - nmod - compound - prep - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_all_nmod_compound_prep_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 5 (ALL - nmod - compound - prep - objI - X):
 - for i in `cat context_bags.nouns.hal`; do mkdir exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_$i; done
 - for i in `cat context_bags.nouns.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound,prep,objI --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_$i/dep.contexts" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_prep_objI_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_$i" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_prep_objI_experiment_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.hal`; do echo -en "ALL - nmod - compound - prep - objI - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 6 (ALL - nmod - compound - prep - objI - conj - X):
 - for i in `cat context_bags.nouns.hal`; do mkdir exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_conj_$i; done
 - for i in `cat context_bags.nouns.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound,prep,objI,conj --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_conj_$i/dep.contexts" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_prep_objI_conj_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_conj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_conj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_conj_$i" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_prep_objI_conj_experiment_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_conj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.hal`; do echo -en "ALL - nmod - compound - prep - objI - conj - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_conj_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 7 (ALL - nmod - compound - prep - objI - conj - derinetAdj - X):
 - for i in `cat context_bags.nouns.hal`; do mkdir exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_conj_derinetAdj_$i; done
 - for i in `cat context_bags.nouns.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound,prep,objI,conj,derinetAdj --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_conj_derinetAdj_$i/dep.contexts" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_prep_objI_conj_derinetAdj_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_conj_derinetAdj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_conj_derinetAdj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_conj_derinetAdj_$i" > ../verb-contexts/lrc_nouns_hal_all_nmod_compound_prep_objI_conj_derinetAdj_experiment_$i.sh; done
 - for i in lrc_nouns_hal_all_nmod_compound_prep_objI_conj_derinetAdj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.hal`; do echo -en "ALL - nmod - compound - prep - objI - conj - derinetAdj - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_all_nmod_compound_prep_objI_conj_derinetAdj_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

## NOUNS/HAL (MERGED)

 - Vsetky context bags (ALL):
 - mkdir exp_en_nouns_cinkova_hal_merged_all
 - for i in `cat context_bags.nouns.merged.hal`; do cat exp_en_nouns_cinkova_hal_merged_all_$i/dep.contexts >> exp_en_nouns_cinkova_hal_merged_all/dep.contexts; done
 - echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_all" > ../verb-contexts/lrc_nouns_hal_merged_all.sh
 - qsub -cwd -j y -S /bin/bash lrc_nouns_hal_merged_all.sh
 - python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_merged_all/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'

 - python split_contexts.py --contexts ../data/exp_en_nouns_cinkova/dep.contexts.hal --output_dir ../data/exp_en_nouns_cinkova/ --merge_inverse_relations True
 - for i in `cat context_bags.nouns.merged.hal`; do mkdir exp_en_nouns_cinkova_hal_merged_$i; done
 - for i in `cat context_bags.nouns.merged.hal`; do mv exp_en_nouns_cinkova/$i.contexts exp_en_nouns_cinkova_hal_merged_$i/; done
 - for i in `cat context_bags.nouns.merged.hal`; do mv exp_en_nouns_cinkova_hal_merged_$i/$i.contexts exp_en_nouns_cinkova_hal_merged_$i/dep.contexts; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_$i" > ../verb-contexts/lrc_nouns_hal_merged_$i.sh; done
 - for i in lrc_nouns_hal_merged*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo -en "$i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_merged_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 1:
 - for i in `cat context_bags.nouns.merged.hal`; do mkdir exp_en_nouns_cinkova_hal_merged_all_$i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_merged_all_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_hal_merged_all_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_merged_all_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_all_$i" > ../verb-contexts/lrc_nouns_hal_merged_all_experiment_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo -en "ALL - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_merged_all_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 2 (ALL - nmod - X):
 - for i in `cat context_bags.nouns.merged.hal`; do mkdir exp_en_nouns_cinkova_hal_merged_all_nmod_$i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "python remove_contexts.py --remove $i --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_merged_all_nmod_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_merged_all_nmod_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_all_nmod_$i" > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_experiment_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo -en "ALL - nmod - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_all_nmod_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 3 (ALL - nmod - compound - X):
 - for i in `cat context_bags.nouns.merged.hal`; do mkdir exp_en_nouns_cinkova_hal_merged_all_nmod_compound_$i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_merged_all_nmod_compound_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_all_nmod_compound_$i" > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_experiment_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo -en "ALL - nmod - compound - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_merged_all_nmod_compound_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 4 (ALL - nmod - compound - prep - X):
 - for i in `cat context_bags.nouns.merged.hal`; do mkdir exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_$i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound,prep --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_prep_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_$i" > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_prep_experiment_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo -en "ALL - nmod - compound - prep - $i\t"; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 5 (ALL - nmod - compound - prep - conj - X):
 - for i in `cat context_bags.nouns.merged.hal`; do mkdir exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_$i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound,prep,conj --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_prep_conj_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_$i" > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_prep_conj_experiment_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo -en "ALL - nmod - compound - prep - conj - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 6 (ALL - nmod - compound - prep - conj - subj - X):
 - for i in `cat context_bags.nouns.merged.hal`; do mkdir exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_subj_$i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound,prep,conj,subj --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_subj_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_subj_$i" > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_experiment_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo -en "ALL - nmod - compound - prep - conj - subj - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_subj_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done

 - cyklus 7 (ALL - nmod - compound - prep - conj - subj - derinetAdj - X):
 - for i in `cat context_bags.nouns.merged.hal`; do mkdir exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_$i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "python remove_contexts.py --remove $i,nmod,compound,prep,conj,subj,derinetAdj --input ../data/exp_en_nouns_cinkova/dep.contexts.hal --output ../data/exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_$i/dep.contexts" --merge_inverse_relations True > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_preprocessing_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_preprocessing_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_preprocessing*; do tail -n 1 $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo "./do_en_experiment.sh exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_$i" > ../verb-contexts/lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_experiment_$i.sh; done
 - for i in lrc_nouns_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_experiment_*; do qsub -cwd -j y -S /bin/bash $i; done
 - for i in `cat context_bags.nouns.merged.hal`; do echo -en "ALL - nmod - compound - prep - conj - subj - derinetAdj - $i # "; python ../verb-contexts/evaluation.py --vectors=exp_en_nouns_cinkova_hal_merged_all_nmod_compound_prep_conj_subj_derinetAdj_$i/dim300vecs --dataset=eval_en_nouns/simlex --reflexive_verbs asis --folds=2 2>&1 | grep Spearman | sed -e 's/.*: //'; done
