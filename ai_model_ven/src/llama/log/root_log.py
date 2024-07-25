import logging
import logging.config
import yaml
import os

def setup_logging(config_file='logging_config.yaml'):
    file_path = os.path.join(os.getcwd(), "llama", "config", config_file)
    with open(file_path, 'r') as f:
        config = yaml.safe_load(f)
        logging.config.dictConfig(config)

# Call setup_logging() at the start of your application
setup_logging()

# Now you can use logging in your modules
logger = logging.getLogger(__name__)
logger.info("Logger initialized.")
