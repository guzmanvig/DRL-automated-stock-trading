from model.models import *

file_name = config.AMZN_DATA_FILE
use_turbulence = False
stock_dimension = 1

# file_name = config.DOW30_DATA_FILE
# use_turbulence = True
# stock_dimension = 30



def run_model() -> None:
    """Train the model."""

    # read and preprocess data
    data = preprocess_data(file_name)
    if use_turbulence:
        data = add_turbulence(data)

    # 2015/10/01 is the date that validation starts
    # 2016/01/01 is the date that real trading starts
    # unique_trade_date needs to start from 2015/10/01 for validation purpose
    unique_trade_date = data[(data.datadate > 20151001)&(data.datadate <= 20200707)].datadate.unique()

    # rebalance_window is the number of months to retrain the model
    # validation_window is the number of months to validation the model and select for trading
    rebalance_window = 63
    validation_window = 63
    
    ## Ensemble Strategy
    run_ensemble_strategy(df=data, 
                          unique_trade_date= unique_trade_date,
                          rebalance_window = rebalance_window,
                          validation_window=validation_window,
                          use_turbulence=use_turbulence,
                          stock_dimension=stock_dimension)

    #_logger.info(f"saving model version: {_version}")

if __name__ == "__main__":
    run_model()
