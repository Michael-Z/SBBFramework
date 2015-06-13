import unittest
from pSBB.SBB.config import Config
from pSBB.SBB.sbb import SBB

TEST_CONFIG = {
    'task': 'reinforcement',
    'reinforcement_parameters': { # only used if 'task' is 'reinforcement'
        'environment': 'tictactoe', # edit _initialize_environment() in SBB and RESTRICTIONS['environment_types'] to add new environments (they must implement DefaultEnvironment)
        'validation_population': 20, # at a validated generation, all the teams with be tested against this population, the best one is the champion
        'champion_population': 30, # at a validated generation, these are the points the champion team will play against to obtain the metrics
        'opponents_pool': 'only_coded_opponents',
        'hall_of_fame': {
            'enabled': False,
            'use_genotype_diversity': False,
        },
        'print_matches': False, # use this option to debug
    },
    'training_parameters': {
        'runs_total': 2,
        'generations_total': 30,
        'validate_after_each_generation': 30,
        'populations': {
            'teams': 12,
            'points': 12,
        },
        'replacement_rate': {
            'teams': 0.5,
            'points': 0.2,
        },
        'mutation': {
            'team': {
                'remove_program': 0.7,
                'add_program': 0.8,
                'mutate_program': 0.2,
            },
            'program': {
                'remove_instruction': 0.7,
                'add_instruction': 0.8,
                'change_instruction': 0.8,
                'swap_instructions': 0.8,
                'change_action': 0.1,
            },
        },
        'team_size': { # the min size is the total number of actions
            'min': 2,
            'max': 12,
        },
        'program_size': {
            'min': 2,
            'max': 12,
        },
    },

    'advanced_training_parameters': {
        'seed': 1, # default = None
        'use_pareto_for_team_population_selection': False, # if False, will select solutions by best fitness
        'use_pareto_for_point_population_selection': False, # if False, will select points using uniform probability
        'use_operations': ['+', '-', '*', '/', 'ln', 'exp', 'cos', 'if_lesser_than', 'if_equal_or_higher_than'],
        'extra_registers': 1,
        'diversity': {
            'genotype_fitness_maintanance': False,
            'fitness_sharing': False,
        },
        'diversity_configs': { # p_value is with how much strenght this diversity metric will be applied to the fitness
            'genotype_fitness_maintanance': {
                'p_value': 0.1,
                'k': 8,
            },
            'fitness_sharing': {
                'p_value': 0.1,
            },       
        },
        'run_initialization_step2': True,
    },
}

class ClassificationTests(unittest.TestCase):
    def setUp(self):
        Config.RESTRICTIONS['write_output_files'] = False

    # def test_reinforcement_for_ttt_without_pareto_and_without_diversity_maintenance_for_only_coded_opponents_for_two_runs(self):
    #     """ Checking if everything for classification is still working and producing the same result. """
    #     config = dict(TEST_CONFIG)
    #     config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = False
    #     config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
    #     config['advanced_training_parameters']['diversity']['genotype_fitness_maintanance'] = False
    #     config['advanced_training_parameters']['diversity']['fitness_sharing'] = False
    #     config['reinforcement_parameters']['opponents_pool'] = 'only_coded'
    #     config['reinforcement_parameters']['hall_of_fame']['enabled'] = False
    #     config['reinforcement_parameters']['hall_of_fame']['use_genotype_diversity'] = False
    #     config['training_parameters']['runs_total'] = 2
    #     Config.USER = config
    #     sbb = SBB()
    #     sbb.run()
    #     result = len(sbb.best_scores_per_runs_)
    #     expected = 2
    #     self.assertEqual(expected, result)

    # def test_reinforcement_for_ttt_without_pareto_and_without_diversity_maintenance_for_only_coded_opponents(self):
    #     """ Checking if everything for classification is still working and producing the same result. """
    #     config = dict(TEST_CONFIG)
    #     config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = False
    #     config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
    #     config['advanced_training_parameters']['diversity']['genotype_fitness_maintanance'] = False
    #     config['advanced_training_parameters']['diversity']['fitness_sharing'] = False
    #     config['reinforcement_parameters']['opponents_pool'] = 'only_coded'
    #     config['reinforcement_parameters']['hall_of_fame']['enabled'] = False
    #     config['reinforcement_parameters']['hall_of_fame']['use_genotype_diversity'] = False
    #     config['training_parameters']['runs_total'] = 1
    #     Config.USER = config
    #     sbb = SBB()
    #     sbb.run()
    #     result = sbb.best_scores_per_runs_
    #     expected = [0.525]
    #     self.assertEqual(expected, result)

    # def test_reinforcement_for_ttt_without_pareto_and_without_diversity_maintenance_for_hybrid_opponents(self):
    #     """ Checking if everything for classification is still working and producing the same result. """
    #     config = dict(TEST_CONFIG)
    #     config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = False
    #     config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
    #     config['advanced_training_parameters']['diversity']['genotype_fitness_maintanance'] = False
    #     config['advanced_training_parameters']['diversity']['fitness_sharing'] = False
    #     config['reinforcement_parameters']['opponents_pool'] = 'hybrid'
    #     config['reinforcement_parameters']['hall_of_fame']['enabled'] = False
    #     config['reinforcement_parameters']['hall_of_fame']['use_genotype_diversity'] = False
    #     config['training_parameters']['runs_total'] = 1
    #     Config.USER = config
    #     sbb = SBB()
    #     sbb.run()
    #     result = sbb.best_scores_per_runs_
    #     expected = [0.475]
    #     self.assertEqual(expected, result)

    # def test_reinforcement_for_ttt_without_pareto_and_without_diversity_maintenance_for_only_sbb_opponents(self):
    #     """ Checking if everything for classification is still working and producing the same result. """
    #     config = dict(TEST_CONFIG)
    #     config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = False
    #     config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
    #     config['advanced_training_parameters']['diversity']['genotype_fitness_maintanance'] = False
    #     config['advanced_training_parameters']['diversity']['fitness_sharing'] = False
    #     config['reinforcement_parameters']['opponents_pool'] = 'only_sbb'
    #     config['reinforcement_parameters']['hall_of_fame']['enabled'] = False
    #     config['reinforcement_parameters']['hall_of_fame']['use_genotype_diversity'] = False
    #     config['training_parameters']['runs_total'] = 1
    #     Config.USER = config
    #     sbb = SBB()
    #     sbb.run()
    #     result = sbb.best_scores_per_runs_
    #     expected = [0.35833]
    #     self.assertEqual(expected, result)

    # def test_reinforcement_for_ttt_without_pareto_and_with_diversity_maintenance(self):
    #     """ Checking if everything for classification is still working and producing the same result. """
    #     config = dict(TEST_CONFIG)
    #     config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = False
    #     config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
    #     config['advanced_training_parameters']['diversity']['genotype_fitness_maintanance'] = True
    #     config['advanced_training_parameters']['diversity']['fitness_sharing'] = True
    #     config['reinforcement_parameters']['opponents_pool'] = 'hybrid'
    #     config['reinforcement_parameters']['hall_of_fame']['enabled'] = False
    #     config['reinforcement_parameters']['hall_of_fame']['use_genotype_diversity'] = False
    #     config['training_parameters']['runs_total'] = 1
    #     Config.USER = config
    #     sbb = SBB()
    #     sbb.run()
    #     result = sbb.best_scores_per_runs_
    #     expected = [0.36666]
    #     self.assertEqual(expected, result)

    # def test_reinforcement_for_ttt_with_pareto_and_without_diversity_maintenance(self):
    #     """ Checking if everything for classification is still working and producing the same result. """
    #     config = dict(TEST_CONFIG)
    #     config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = True
    #     config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = True
    #     config['advanced_training_parameters']['diversity']['genotype_fitness_maintanance'] = False
    #     config['advanced_training_parameters']['diversity']['fitness_sharing'] = False
    #     config['reinforcement_parameters']['opponents_pool'] = 'hybrid'
    #     config['reinforcement_parameters']['hall_of_fame']['enabled'] = False
    #     config['reinforcement_parameters']['hall_of_fame']['use_genotype_diversity'] = False
    #     config['training_parameters']['runs_total'] = 1
    #     Config.USER = config
    #     sbb = SBB()
    #     sbb.run()
    #     result = sbb.best_scores_per_runs_
    #     expected = [0.375]
    #     self.assertEqual(expected, result)

    # def test_reinforcement_for_ttt_without_pareto_and_without_diversity_maintenance_for_only_coded_opponents_with_hall_of_fame(self):
    #     """ Checking if everything for classification is still working and producing the same result. """
    #     config = dict(TEST_CONFIG)
    #     config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = False
    #     config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
    #     config['advanced_training_parameters']['diversity']['genotype_fitness_maintanance'] = False
    #     config['advanced_training_parameters']['diversity']['fitness_sharing'] = False
    #     config['reinforcement_parameters']['opponents_pool'] = 'only_coded'
    #     config['reinforcement_parameters']['hall_of_fame']['enabled'] = True
    #     config['reinforcement_parameters']['hall_of_fame']['use_genotype_diversity'] = False
    #     config['training_parameters']['runs_total'] = 1
    #     Config.USER = config
    #     sbb = SBB()
    #     sbb.run()
    #     result = sbb.best_scores_per_runs_
    #     expected = [0.49166]
    #     self.assertEqual(expected, result)

    # def test_reinforcement_for_ttt_without_pareto_and_without_diversity_maintenance_for_only_coded_opponents_with_hall_of_fame_with_diversity(self):
    #     """ Checking if everything for classification is still working and producing the same result. """
    #     config = dict(TEST_CONFIG)
    #     config['advanced_training_parameters']['use_pareto_for_team_population_selection'] = False
    #     config['advanced_training_parameters']['use_pareto_for_point_population_selection'] = False
    #     config['advanced_training_parameters']['diversity']['genotype_fitness_maintanance'] = False
    #     config['advanced_training_parameters']['diversity']['fitness_sharing'] = False
    #     config['reinforcement_parameters']['opponents_pool'] = 'only_coded'
    #     config['reinforcement_parameters']['hall_of_fame']['enabled'] = True
    #     config['reinforcement_parameters']['hall_of_fame']['use_genotype_diversity'] = True
    #     config['training_parameters']['runs_total'] = 1
    #     Config.USER = config
    #     sbb = SBB()
    #     sbb.run()
    #     result = sbb.best_scores_per_runs_
    #     expected = [0.49166]
    #     self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()