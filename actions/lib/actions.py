from st2common.runners.base_action import Action
import pysnow as sn


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.client = self._get_client()

    def _get_client(self):
        instance_name = self.config['instance_name']
        username = self.config['username']
        password = self.config['password']
        use_ssl = self.config['use_ssl']

        client = sn.Client(instance=instance_name, user=username, password=password, use_ssl=use_ssl)

        if 'custom_params' in self.config and isinstance(self.config['custom_params'], dict):
            client.parameters.add_custom(self.config['custom_params'])

        return client
