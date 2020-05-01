import argparse

import numpy as np

from utils.data import load_data
from utils.model import train_model, load_model
from utils.plot import plot_pca,plot_data


def parse_args():
    def str2bool(v):
        if isinstance(v, bool):
            return v
        if v.lower() in ('yes', 'true', 't', 'y', '1'):
            return True
        elif v.lower() in ('no', 'false', 'f', 'n', '0'):
            return False
        else:
            raise argparse.ArgumentTypeError('Boolean value expected')

    parser = argparse.ArgumentParser()

    parser.add_argument('--load', type=str2bool, default=False,
                        help='True: Load trained model  False: Train model default: True')

    parser.add_argument('--gs', type=str2bool, default=False,
                        help='Find optimal parameters with 10-Fold GridSearchCV')

    parser.print_help()

    return parser.parse_args()


if __name__ == '__main__':
    np.random.seed(1)

    args = parse_args()
    features, labels = load_data('data/credit_data.csv', 'default', ('income', 'age', 'loan'))
    plot_pca(features.to_numpy(), labels.to_numpy())
    plot_data(features,labels)
    if args.load:
        model = load_model()
        income, age, loan = 27845.8008938469, 55.4968525394797, 10871.1867897838
        print(model.predict([list((income, age, loan))])[0])
    else:
        model = train_model(features, labels, args)
        income, age, loan = 27845.8008938469, 55.4968525394797, 10871.1867897838
        print(model.predict([list((income, age, loan))])[0])
