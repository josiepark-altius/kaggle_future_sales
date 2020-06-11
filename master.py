import src.preprocess.preprocess as preprocess
from src.utils.load_save_data import load_environment, load_static_files
import config_load

from dotenv import load_dotenv

def main():
    '''
    '''
    print('Starting Program')
    print('=================')
    # load data
    static_files = load_static_files()

    # preprocess training data
    train = preprocess.main()
    

    # run model

    # save model

    # evaluate model



    return None


if __name__ == "__main__":
    main()