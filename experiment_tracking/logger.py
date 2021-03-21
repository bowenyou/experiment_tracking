import os
import json
import datetime

class Experiment:

    def __init__(
        self,
        params,
        metric,
        optimizer,
        scheduler=None,
        file_dir=None,
        name='default',
        debug=False,
        version=None,
        description=None
    ):

        self.params = params
        self.metric = metric
        self.optimizer = optimizer
        self.scheduler = scheduler
        self.file_dir = file_dir
        self.name = name
        self.debug = debug
        self.version = version
        self.description = description

    def start_experiment(self):

        directory_name = f'file_dir/{self.name}_{self.version}'
        self.directory_name = directory_name
        self.start_time = datetime.datetime.now()
        try:
            os.makedirs(directory_name)
        except FileExistsError:
            pass

        self.loss = []
        self.epoch = 1

    def log(self, loss):

        self.loss.append({'epoch': self.epoch, 'loss': loss})
        self.epoch += 1

    def end_experiment(self):

        self.end_time = datetime.datetime.now()

        output_json = {
            'name': self.name,
            'version': self.version,
            'date': self.experiment_time,
            'duration': self.end_time - self.start_time,
            'description': self.description,
            'params': self.params,
            'metric': self.metric,
            'optimizer': self.optimizer,
            'scheduler': self.scheduler,
            'training_loss': self.loss
        }

        with open(f'{self.directory_name}/log.json', 'w') as out:
            json.dump(output_json, out)
