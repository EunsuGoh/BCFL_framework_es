config=\
  {
    'TRAINING_ITERATIONS':2,
    'TRAINING_HYPERPARAMS':{
    'final_round_num': 3, # sould be same with 'TRAINING_ITERATIONS'
    'batch_size': 64,
    'epochs': 1,
    'learning_rate': 0.001,
    },
    'NUMBER_OF_TRAINERS':3, 
    #  Available evaluation methods : 'loo','shapley'
    'EVAL_METHOD':'step',
    'ROUND_DURATION':20000, # seconds
    # Available client selection methods : 'all', 'random', 'fcfs', "score_order"
    'SELECTION_METHOD':'all'
  }
