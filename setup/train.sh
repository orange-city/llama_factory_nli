CUDA_VISIBLE_DEVICES=4,5,6,7 llamafactory-cli train \
    --stage sft \
    --do_train true \
    --model_name_or_path /sunhao/LLM/Meta-Llama-3-8B-Instruct \
    --dataset MSciNLI_train \
    --dataset_dir ./data \
    --template llama3 \
    --finetuning_type lora \
    --output_dir ./saves/LLaMA3-8B/lora/sft \
    --overwrite_cache true \
    --overwrite_output_dir true \
    --cutoff_len 2048 \
    --preprocessing_num_workers 16 \
    --per_device_train_batch_size 2 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 8 \
    --lr_scheduler_type cosine \
    --logging_steps 50 \
    --warmup_steps 20 \
    --save_steps 100 \
    --eval_steps 50 \
    --evaluation_strategy steps \
    --load_best_model_at_end true \
    --learning_rate 5e-5 \
    --num_train_epochs 5.0 \
    --val_size 0.1 \
    --plot_loss true \
    --fp16 true



CUDA_VISIBLE_DEVICES=4,5,6,7 llamafactory-cli train \
    --stage sft \
    --do_train true \
    --model_name_or_path /sunhao/LLM/Meta-Llama-3-8B-Instruct \
    --dataset MSciNLI_train2 \
    --dataset_dir ./data \
    --template llama3 \
    --finetuning_type full \
    --output_dir ./saves/LLaMA3-8B/full/sft \
    --overwrite_cache true \
    --overwrite_output_dir False \
    --cutoff_len 1024 \
    --preprocessing_num_workers 16 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --lr_scheduler_type cosine \
    --logging_steps 50 \
    --warmup_steps 20 \
    --deepspeed examples/deepspeed/ds_z3_config.json \
    --save_steps 1000000 \
    --eval_steps 100 \
    --evaluation_strategy steps \
    --load_best_model_at_end true \
    --learning_rate 5e-5 \
    --num_train_epochs 5.0 \
    --val_size 0.1 \
    --plot_loss true \
    --bf16 true

CUDA_VISIBLE_DEVICES=0,1,2,3 llamafactory-cli train \
    --stage sft \
    --do_train true \
    --model_name_or_path /sunhao/LLM/Meta-Llama-3-8B-Instruct \
    --dataset MSciNLI_train \
    --dataset_dir ./data \
    --template llama3 \
    --finetuning_type full \
    --output_dir ./saves/LLaMA3-8B/full/sft_input \
    --overwrite_cache true \
    --overwrite_output_dir False \
    --cutoff_len 1024 \
    --preprocessing_num_workers 16 \
    --per_device_train_batch_size 1 \
    --per_device_eval_batch_size 1 \
    --gradient_accumulation_steps 2 \
    --lr_scheduler_type cosine \
    --logging_steps 50 \
    --warmup_steps 20 \
    --deepspeed examples/deepspeed/ds_z3_config.json \
    --save_steps 1000000 \
    --eval_steps 100 \
    --evaluation_strategy steps \
    --load_best_model_at_end true \
    --learning_rate 5e-5 \
    --num_train_epochs 5.0 \
    --val_size 0.1 \
    --plot_loss true \
    --bf16 true



CUDA_VISIBLE_DEVICES=4,5,6,7 llamafactory-cli train \
    --model_name_or_path /sunhao/LLM/Meta-Llama-3-8B-Instruct \
    --dataset nli \
    --stage sft \
    --finetuning_type full \
    --per_device_train_batch_size 1 \
    --learning_rate 5e-5 \
    --num_train_epochs 2 \
    --per_device_eval_batch_size 20 \
    --eval_steps 10000000000 \
    --save_steps 100 \
    --logging_steps 10 \
    --output_dir /data/zhenrong/LLaMA-Factory/saves/LLaMA3-8B/full/sft \
    --do_train true \
    --template llama3 \
    --cutoff_len 1024 \
    --max_samples 100000000 \
    --overwrite_cache true \
    --preprocessing_num_workers 16 \
    --gradient_accumulation_steps 2 \
    --lr_scheduler_type cosine \
    --warmup_ratio 0.1 \
    --report_to wandb \
    --bf16 true \
    --ddp_timeout 180000000 \
    --val_size 0.1 \
    --eval_strategy steps \
    --plot_loss true \
    --overwrite_output_dir False



CUDA_VISIBLE_DEVICES=4,5,6,7 /home/sunhao/miniconda3/envs/dpo/bin/python \
/home/sunhao/miniconda3/envs/dpo/bin/torchrun \
  --nnodes 1 \
  --node_rank 0 \
  --nproc_per_node 4 \
  --master_addr 127.0.0.1 \
  --master_port 20628 \
  /data/sunhao/code/LLaMA-Factory/src/llamafactory/launcher.py \
  --model_name_or_path /sunhao/LLM/Meta-Llama-3-8B-Instruct \
  --dataset nli \
  --stage sft \
  --finetuning_type full \
  --per_device_train_batch_size 4 \
  --learning_rate 1.0e-6 \
  --num_train_epochs 10.0 \
  --per_device_eval_batch_size 20 \
  --eval_steps 10000000000 \
  --save_steps 400 \
  --logging_steps 10 \
  --output_dir /data/zhenrong/LLaMA-Factory/saves/LLaMA3-8B/full/sft \
  --do_train true \
  --deepspeed examples/deepspeed/ds_z3_config.json \
  --template llama3 \
  --cutoff_len 1024 \
  --max_samples 100000000 \
  --overwrite_cache true \
  --preprocessing_num_workers 16 \
  --report_to wandb \
  --gradient_accumulation_steps 2 \
  --lr_scheduler_type cosine \
  --warmup_ratio 0.1 \
  --bf16 true \
  --ddp_timeout 180000000 \
  --val_size 0.1 \
  --eval_strategy steps \
  --plot_loss true \
  --overwrite_output_dir False