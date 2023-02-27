import numpy as np
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def get_test(dataset, pred_target, percents_to_test=0.2):
    x = dataset.drop(pred_target, axis=1)
    y = dataset[pred_target]

    x_train, x_test, y_train, y_test = train_test_split(x, y,
                                                        test_size=percents_to_test,
                                                        random_state=0)
    return x_train, x_test, y_train, y_test


def print_stats(model_name, mse, rmse, score):
    print(model_name)
    print(f"MSE on test set: {mse:.2f}")
    print(f"RMSE on test set: {rmse:.2f}")
    print(f"Prediction accuracy on test set: {score:.2f}")
    print("-----------------------------------------------")


def test_model(model_name, model, x_test, y_test):
    y_pred = model.predict(x_test)
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    score = model.score(x_test, y_test)

    print_stats(model_name, mse, rmse, score)


def histograms(dataset, dataset_columns):
    fig, axs = plt.subplots(2, 3, figsize=(15, 8))
    axs[0, 0].hist(dataset[dataset_columns.TOTAL_ROOMS])
    axs[0, 0].set_title('Total Rooms')
    axs[0, 1].hist(dataset[dataset_columns.TOTAL_BEDROOMS])
    axs[0, 1].set_title('Total Bedrooms')
    axs[0, 2].hist(dataset[dataset_columns.COMPLEX_INHABITANTS])
    axs[0, 2].set_title('Complex Inhabitants')
    axs[1, 0].hist(dataset[dataset_columns.APARTMENTS_NR])
    axs[1, 0].set_title('Apartments Nr')
    axs[1, 1].hist(dataset[dataset_columns.COMPLEX_AGE])
    axs[1, 1].set_title('Complex Age Value')
    axs[1, 2].hist(dataset[dataset_columns.MEDIAN_COMPLEX_VALUE])
    axs[1, 2].set_title('Median Complex Value')

    plt.show()


def scatter(dataset, dataset_columns):
    fig, axs = plt.subplots(2, 3, figsize=(15, 8))
    axs[0, 0].scatter(dataset[dataset_columns.MEDIAN_COMPLEX_VALUE],
                      dataset[dataset_columns.TOTAL_ROOMS])
    axs[0, 0].set_title('Median Complex Value vs Total Rooms')
    axs[0, 1].scatter(dataset[dataset_columns.MEDIAN_COMPLEX_VALUE],
                      dataset[dataset_columns.TOTAL_BEDROOMS])
    axs[0, 1].set_title('Median Complex Value vs Total Bedrooms')
    axs[0, 2].scatter(dataset[dataset_columns.MEDIAN_COMPLEX_VALUE],
                      dataset[dataset_columns.COMPLEX_INHABITANTS])
    axs[0, 2].set_title('Median Complex Value vs Complex Inhabitants')
    axs[1, 0].scatter(dataset[dataset_columns.MEDIAN_COMPLEX_VALUE],
                      dataset[dataset_columns.APARTMENTS_NR])
    axs[1, 0].set_title('Median Complex Value vs Apartments Nr')
    axs[1, 1].scatter(dataset[dataset_columns.MEDIAN_COMPLEX_VALUE],
                      dataset[dataset_columns.COMPLEX_AGE])
    axs[1, 1].set_title('Median Complex Value vs Complex Age')
    plt.show()


def correlation(dataset, dataset_columns):
    corr_matrix = dataset.corr()
    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(corr_matrix, cmap='coolwarm')

    ax.set_xticks(range(len(dataset_columns)))
    ax.set_yticks(range(len(dataset_columns)))
    ax.set_xticklabels(dataset_columns)
    ax.set_yticklabels(dataset_columns)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    for i in range(len(dataset_columns)):
        for j in range(len(dataset_columns)):
            ax.text(j, i, '{:.2f}'.format(corr_matrix.iloc[i, j]),
                    ha="center", va="center", color="w")

    ax.set_title("Correlation Matrix")
    fig.colorbar(im)
    plt.show()
