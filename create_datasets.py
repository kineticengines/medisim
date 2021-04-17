# Copyright 2020 Babylon Partners. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Create a collection of binary medical term similarity datasets."""

import os
import sys
import yaml

from dataset_creation.positive_instances_from_labels import positive_instances_from_labels
from dataset_creation.positive_instances_from_substitutions import positive_instances_from_substitutions
from dataset_creation.negative_sampling_from_positive_instances import negative_instances

config_path="config.yaml"

with open(config_path , 'r') as config_file:
    config = yaml.safe_load(config_file)
    
print('*** Starting creation of positive instances from concept labels ***\n')
positive_instances_from_labels(easy_hard_split=config['easy_hard_split'],
                               split_distance=config['split_distance'] ,
                               snomed_description_path=config['snomed_description_path'],
                               dataset_path=config['dataset_path'],
                               snomed_concept_path=config['snomed_concept_path'])

print('*** Starting creation of positive instances from concept substitutions ***\n')
positive_instances_from_substitutions(easy_hard_split=config['easy_hard_split'],
                                      split_distance=config['split_distance'] ,
                                      snomed_description_path=config['snomed_description_path'],
                                      dataset_path=config['dataset_path'],
                                      snomed_association_refset_path=config['snomed_association_refset_path'])

print('*** Starting creation of negative instances ***\n')
negative_instances(dataset_path=config['dataset_path'],
                   strategies=config['neg_sampling_strategies'])
